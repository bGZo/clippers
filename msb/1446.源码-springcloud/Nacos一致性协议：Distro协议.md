# Nacos一致性协议：Distro协议

## 简介

Distro协议是Nacos社区自研的一种AP分布式协议，是面向临时实例设计的一种分布式协议，其保证在某些Nacos节点宕机后，整个临时实例处理系统依旧可以正常工作。作为一种有状态的中间件应用内嵌协议，Distro保证了各个Nacos节点对于注册请求的统一协调和储存。

## 设计思想

Distro协议的主要设计思想如下：

- Nacos 每个节点是平等的都可以处理写请求，同时把新数据同步到其他节点。
- 每个节点只负责部分数据，定时发送自己负责数据的校验值到其他节点来保持数据一致性。
- 每个节点独立处理读请求，及时从本地发出响应。

## Nacos为什么需要一致性协议

- Nacos 在开源支持就定下了⼀个目标，尽可能的减少用户部署以及运维成本，做到用户只需要⼀个程序包，就可以快速以单机模式启动 Nacos 或者以集群模式启动 Nacos。而Nacos 是⼀个需要存储数据的⼀个组件，因此，为了实现这个目标，就需要在 Nacos 内部实现数据存储。单机下其实问题不大，简单的内嵌关系型数据库即可；但是集群模式下，就需要考虑如何保障各个节点之间的数据⼀致性以及数据同步，而要解决这个问题，就不得不引入共识算法，通过算法来保障各个节点之间的数据的⼀致性。
- Distro 协议是阿里巴巴自研的⼀个最终⼀致性协议，而最终⼀致性协议有很多，比如Gossip（流行病协议）、Eureka 内的数据同步算法。而 Distro 算法是集 Gossip 以及 Eureka 协议的优点并加以优化而出来的，对于原生的 Gossip，由于随机选取发送消息的节点，也就不可避免的存在消息重复发送给同⼀节点的情况，增加了网络的传输的压力，也给消息节点带来额外的处理负载，而Distro算法引入了权威 Server 的概念，每个节点负责⼀部分数据以及将自己的数据同步给其他节点，有效的降低了消息冗余的问题。

## 数据初始化

新加入的 Distro 节点会进行全量数据拉取。具体操作是轮询所有的 Distro 节点，通过向其他的机器发送请求拉取全量数据。

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1396/1653478305025/6bf7c9a52cb14b2ab51c6318f351323c.png)

在全量拉取操作完成之后，Nacos 的每台机器上都维护了当前的所有注册上来的非持久化实例数据。

## 数据校验

在 Distro 集群启动之后，各台机器之间会定期的发送心跳。心跳信息主要为各个机器上的所有数据的元信息（之所以使用元信息，是因为需要保证网络中数据传输的量级维持在⼀个较低水平）。这种数据校验会以心跳的形式进行，即每台机器在固定时间间隔会向其他机器发起⼀次数据校验请求。

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1396/1653478305025/f6d934c238a049e2811392569b1c4c8b.png)

⼀旦在数据校验过程中，某台机器发现其他机器上的数据与本地数据不⼀致，则会发起⼀次全量拉取请求，将数据补齐。

## 写操作

对于⼀个已经启动完成的 Distro 集群，在⼀次客户端发起写操作的流程中，当注册非持久化的实例的写请求打到某台 Nacos 服务器时，Distro 集群处理的流程图如下。

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1396/1653478305025/bfcc7ef9bfd0453b840ec6eaa6f729aa.png)

整个步骤包括几个部分（图中从上到下顺序）：

1. 前置的 Filter 拦截请求，并根据请求中包含的 IP 和 port 信息计算其所属的Distro 责任节点，并将该请求转发到所属的 Distro 责任节点上。
2. 责任节点上的 Controller 将写请求进行解析。
3. Distro 协议定期执行 Sync 任务，将本机所负责的所有的实例信息同步到其他节点上。

## 读操作：

由于每台机器上都存放了全量数据，因此在每⼀次读操作中，Distro 机器会直接从本地拉取数据。快速响应。

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1396/1653478305025/317c7deef5a54f2389ec244ceb33aa38.png)

这种机制保证了 Distro 协议可以作为⼀种 AP 协议，对于读操作都进行及时的响应。在网络分区的情况下，对于所有的读操作也能够正常返回；当网络恢复时，各个 Distro 节点会把各数据分片的数据进行合并恢复。

## 总结：

Distro 协议是 Nacos 对于临时实例数据开发的⼀致性协议。其数据存储在缓存中，并且会在启动时进行全量数据同步，并定期进行数据校验。

在 Distro 协议的设计思想下，每个 Distro 节点都可以接收到读写请求。所有的Distro协议的请求场景主要分为三种情况：

1. 当该节点接收到属于该节点负责的实例的写请求时，直接写入。
2. 当该节点接收到不属于该节点负责的实例的写请求时，将在集群内部路由，转发给对应的节点，从而完成读写。
3. 当该节点接收到任何读请求时，都直接在本机查询并返回（因为所有实例都被同步到了每台机器上）。

Distro 协议作为 Nacos 的内嵌临时实例⼀致性协议，保证了在分布式环境下每个节点上面的服务信息的状态都能够及时地通知其他节点，可以维持数十万量级服务实例的存储和⼀致性。

# AP模式集群数据同步源码分析

#### 全量数据同步

首先我们需要先找到DistroProtocol类型，它就是Distro协议的实现，然后在它的构造方法中，启动了一个startDistroTask()任务，其中包括了初始化同步任务 startLoadTask()

```java
private void startDistroTask() {
    if (EnvUtil.getStandaloneMode()) {
        isInitialized = true;
        return;
    }
    startVerifyTask();
    // 初始化同步任务
    startLoadTask();
}
```

startLoadTask()数据加载任务创建了一个DistroLoadDataTask任务，并传入了一个修改当前节点Distro协议完成状态的回调函数。

```java
private void startLoadTask() {
    DistroCallback loadCallback = new DistroCallback() {
        @Override
        public void onSuccess() {
            isInitialized = true;
        }

        @Override
        public void onFailed(Throwable throwable) {
            isInitialized = false;
        }
    };
    //传入了一个修改当前节点Distro协议完成状态的回调函数。
    GlobalExecutor.submitLoadDataTask(
        new DistroLoadDataTask(memberManager, distroComponentHolder, DistroConfig.getInstance(), loadCallback));
}
```

接下来我们需要查看load方法，这里判断了几种情况，其中loadAllDataSnapshotFromRemote（读取所有远程的数据快照）

```java
private void load() throws Exception {
    // 若除了自身之外没有其他节点，则休眠一秒，可以其他节点未启动
    while (memberManager.allMembersWithoutSelf().isEmpty()) {
        Loggers.DISTRO.info("[DISTRO-INIT] waiting server list init...");
        TimeUnit.SECONDS.sleep(1);
    }
    // 若数据类型为空，说明distroComponentHolder的组件注册器还未初始化完毕
    while (distroComponentHolder.getDataStorageTypes().isEmpty()) {
        Loggers.DISTRO.info("[DISTRO-INIT] waiting distro data storage register...");
        TimeUnit.SECONDS.sleep(1);
    }
    // 加载每个类型的数据
    for (String each : distroComponentHolder.getDataStorageTypes()) {
        if (!loadCompletedMap.containsKey(each) || !loadCompletedMap.get(each)) {
            // 调用加载方法，并标记已处理
            loadCompletedMap.put(each, loadAllDataSnapshotFromRemote(each));
        }
    }
}
```

调用loadAllDataSnapshotFromRemote(each)方法获取同步数据，从其他节点获取同步数据，使用DistroTransportAgent获取数据，使用DistroDataProcessor来处理数据。

```java
private boolean loadAllDataSnapshotFromRemote(String resourceType) {
    // 获取数据传输对象
    DistroTransportAgent transportAgent = distroComponentHolder.findTransportAgent(resourceType);
    // 获取数据处理器
    DistroDataProcessor dataProcessor = distroComponentHolder.findDataProcessor(resourceType);
    if (null == transportAgent || null == dataProcessor) {
        Loggers.DISTRO.warn("[DISTRO-INIT] Can't find component for type {}, transportAgent: {}, dataProcessor: {}",
                            resourceType, transportAgent, dataProcessor);
        return false;
    }
    // 向每个节点请求数据
    for (Member each : memberManager.allMembersWithoutSelf()) {
        try {
            Loggers.DISTRO.info("[DISTRO-INIT] load snapshot {} from {}", resourceType, each.getAddress());
            // 获取数据
            DistroData distroData = transportAgent.getDatumSnapshot(each.getAddress());
            // 解析数据
            boolean result = dataProcessor.processSnapshot(distroData);
            Loggers.DISTRO
                .info("[DISTRO-INIT] load snapshot {} from {} result: {}", resourceType, each.getAddress(),
                      result);
            // 若解析成功，标记此类型数据已经加载完毕
            if (result) {
                distroComponentHolder.findDataStorage(resourceType).finishInitial();
                return true;
            }
        } catch (Exception e) {
            Loggers.DISTRO.error("[DISTRO-INIT] load snapshot {} from {} failed.", resourceType, each.getAddress(), e);
        }
    }
    return false;
}
```

这里我们要查看一下如何获取的数据，使用DistroTransportAgent获取数据getDatumSnapshot()方法，看完这个方法我们还要看一下如何处理数据。

```java
@Override
public DistroData getDatumSnapshot(String targetServer) {
    // 从节点管理器获取目标节点信息
    Member member = memberManager.find(targetServer);
    // 判断目标服务器是否健康
    if (checkTargetServerStatusUnhealthy(member)) {
        throw new DistroException(
            String.format("[DISTRO] Cancel get snapshot caused by target server %s unhealthy", targetServer));
    }
    // 构建请求参数
    DistroDataRequest request = new DistroDataRequest();
    // 设置请求的操作类型为DataOperation.SNAPSHOT（数据快照）
    request.setDataOperation(DataOperation.SNAPSHOT);
    try {
        Response response = clusterRpcClientProxy.sendRequest(member, request);
        if (checkResponse(response)) {
            return ((DistroDataResponse) response).getDistroData();
        } else {
            throw new DistroException(
                String.format("[DISTRO-FAILED] Get snapshot request to %s failed, code: %d, message: %s",
                              targetServer, response.getErrorCode(), response.getMessage()));
        }
    } catch (NacosException e) {
        throw new DistroException("[DISTRO-FAILED] Get distro snapshot failed! ", e);
    }
}
```

使用DistroDataProcessor来处理数据processSnapshot(distroData)方法

```java
@Override
public boolean processSnapshot(DistroData distroData) {
    // 反序列化获取distroData为ClientSyncDatumSnapshot
    ClientSyncDatumSnapshot snapshot = ApplicationUtils.getBean(Serializer.class)
        .deserialize(distroData.getContent(), ClientSyncDatumSnapshot.class);
    // 处理结果集，这里将返回远程节点负责的所有Client以及所有的service、instance信息
    for (ClientSyncData each : snapshot.getClientSyncDataList()) {
        // 处理每一个client
        handlerClientSyncData(each);
    }
    return true;
}
```

具体处理数据方法handlerClientSyncData()

```java
private void handlerClientSyncData(ClientSyncData clientSyncData) {
    Loggers.DISTRO.info("[Client-Add] Received distro client sync data {}", clientSyncData.getClientId());
    // 因为是同步数据，所以这里缓存数据
    clientManager.syncClientConnected(clientSyncData.getClientId(), clientSyncData.getAttributes());
    Client client = clientManager.getClient(clientSyncData.getClientId());
    // 升级客户端服务信息
    upgradeClient(client, clientSyncData);
}
```

这里的核心点就是upgradeClient方法，此方法的目的就是同步各个节点的数据

```java
private void upgradeClient(Client client, ClientSyncData clientSyncData) {
    List<String> namespaces = clientSyncData.getNamespaces();
    List<String> groupNames = clientSyncData.getGroupNames();
    List<String> serviceNames = clientSyncData.getServiceNames();
    List<InstancePublishInfo> instances = clientSyncData.getInstancePublishInfos();
    // 已同步的服务集合
    Set<Service> syncedService = new HashSet<>();
    for (int i = 0; i < namespaces.size(); i++) {
        //从获取的数据中构建一个Service对象
        Service service = Service.newService(namespaces.get(i), groupNames.get(i), serviceNames.get(i));
        //单例模式
        Service singleton = ServiceManager.getInstance().getSingleton(service);
        // 标记此service已经被处理
        syncedService.add(singleton);
        // 获取当前实例
        InstancePublishInfo instancePublishInfo = instances.get(i);
        // 判断是否包含当前获取的实例
        if (!instancePublishInfo.equals(client.getInstancePublishInfo(singleton))) {
            // 不包含则添加
            client.addServiceInstance(singleton, instancePublishInfo);
            // 当前节点发布服务注册事件
            NotifyCenter.publishEvent(
                new ClientOperationEvent.ClientRegisterServiceEvent(singleton, client.getClientId()));
        }
    }
    // 若当前client内部已发布的service不在本次同步的列表内，说明已经过时了，要删掉
    for (Service each : client.getAllPublishedService()) {
        if (!syncedService.contains(each)) {
            client.removeServiceInstance(each);
            NotifyCenter.publishEvent(
                new ClientOperationEvent.ClientDeregisterServiceEvent(each, client.getClientId()));
        }
    }
}
```

到这里就完成了数据初始化同步，Nacos每台机器上都维护了当前所有注册上来的非持久化实例数据。

但是各位要注意的是，这只是一个新的Nacos节点上线的同步数据操作，那么如果某个注册的客户端节点改变那，那么所有的Nacos节点都是需要数据同步的

#### 增量数据同步

数据完成初始化后，节点的数据发生变化后需要将增量数据同步到其他节点。

这里我们就要关注的重点为：

DistroClientDataProcessor类继承了SmartSubscriber，遵循Subscriber/Notify（订阅发布）模式，当有订阅的事件触发时会进行回调通知。

DistroClientDataProcessor订阅了ClientChangedEvent(服务改变)、ClientDisconnectEvent(服务断开)和ClientVerifyFailedEvent(验证失败)事件。
在subscribeTypes方法中体现

```java
@Override
public List<Class<? extends Event>> subscribeTypes() {
    List<Class<? extends Event>> result = new LinkedList<>();
    result.add(ClientEvent.ClientChangedEvent.class);
    result.add(ClientEvent.ClientDisconnectEvent.class);
    result.add(ClientEvent.ClientVerifyFailedEvent.class);
    return result;
}
```

这里我们重点关注ClientChangedEvent事件，那么当事件触发时，会调用onEvent方法

```java
@Override
public void onEvent(Event event) {
    if (EnvUtil.getStandaloneMode()) {
        return;
    }
    if (!upgradeJudgement.isUseGrpcFeatures()) {
        return;
    }
    if (event instanceof ClientEvent.ClientVerifyFailedEvent) {
        syncToVerifyFailedServer((ClientEvent.ClientVerifyFailedEvent) event);
    } else {
        // 增量同步调用方法
        syncToAllServer((ClientEvent) event);
    }
}
```

查看syncToAllServer()方法

```java
private void syncToAllServer(ClientEvent event) {
    Client client = event.getClient();
    // Only ephemeral data sync by Distro, persist client should sync by raft.
    if (null == client || !client.isEphemeral() || !clientManager.isResponsibleClient(client)) {
        return;
    }
    if (event instanceof ClientEvent.ClientDisconnectEvent) {
        DistroKey distroKey = new DistroKey(client.getClientId(), TYPE);
        distroProtocol.sync(distroKey, DataOperation.DELETE);
        // 节点变更事件，即增量数据同步方法
    } else if (event instanceof ClientEvent.ClientChangedEvent) {
        DistroKey distroKey = new DistroKey(client.getClientId(), TYPE);
        distroProtocol.sync(distroKey, DataOperation.CHANGE);
    }
}
```

查看同步方法sync()向除本节点外的所有节点进行数据同步，对每个节点执行具体的同步逻辑syncToTarget方法。

```java
//通过配置延迟开始同步
//@param distroKey 同步数据的分发密钥
//@param action    数据操作的动作
public void sync(DistroKey distroKey, DataOperation action) {
    sync(distroKey, action, DistroConfig.getInstance().getSyncDelayMillis());
}
```

```java
//开始将数据同步到所有远程服务器。
//@param distroKey 同步数据的分发密钥
//@param action    数据操作的动作
//@param delay     同步延迟时间
public void sync(DistroKey distroKey, DataOperation action, long delay) {
    for (Member each : memberManager.allMembersWithoutSelf()) {
        syncToTarget(distroKey, action, each.getAddress(), delay);
    }
}
```

继续跟踪：syncToTarget(方法)

```java
/**
* 开始同步到目标服务器。
*
* @param distroKey    同步数据的分发密钥
* @param action       数据操作的动作
* @param targetServer 目标服务器
* @param delay        同步延迟时间
*/
public void syncToTarget(DistroKey distroKey, DataOperation action, String targetServer, long delay) {
    DistroKey distroKeyWithTarget = new DistroKey(distroKey.getResourceKey(), distroKey.getResourceType(),
                                                  targetServer);
    DistroDelayTask distroDelayTask = new DistroDelayTask(distroKeyWithTarget, action, delay);
    distroTaskEngineHolder.getDelayTaskExecuteEngine().addTask(distroKeyWithTarget, distroDelayTask);
    if (Loggers.DISTRO.isDebugEnabled()) {
        Loggers.DISTRO.debug("[DISTRO-SCHEDULE] {} to {}", distroKey, targetServer);
    }
}
```

分析到这里就能清楚增量数据同步的信息了，那么其他服务在接受到数据增量更新以后还会调用upgradeClient（客户端升级方法）来进行数据同步这里和全量的过程就一致了。
