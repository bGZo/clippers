---
created: 2024-12-28T10:25:47
source: "https://www.cnblogs.com/thisiswhy/p/17965123"
type: "archive-web"
modified: 2025-01-15T11:38:15
---

你好呀，我是歪歪。

Spring 的事件监听机制，不知道你有没有用过，实际开发过程中用来进行代码解耦简直不要太爽。

但是我最近碰到了一个涉及到泛型的场景，常规套路下，在这个场景中使用该机制看起来会很傻，但是最终了解到 Spring 有一个优雅的解决方案，然后去了解了一下，感觉有点意思。

和你一起盘一盘。

## Demo

首先，第一步啥也别说，先搞一个 Demo 出来。

需求也很简单，假设我们有一个 Person 表，每当 Person 表新增或者修改一条数据的时候，给指定服务同步一下。

伪代码非常的简单：

```java
boolean success = addPerson(person)
if(success){
    //发送person，add代表新增
    sendToServer(person,"add");
}
```

这代码能用，完全没有任何问题。

但是，你仔细想，“发给指定服务同步一下”这样的动作按理来说，不应该和用户新增和更新的行为“耦合”在一起，他们应该是两个独立的逻辑。

所以从优雅实现的角度出发，我们可以用 Spring 的事件机制进行解耦。

比如改成这样：

```mipsasm
boolean success = addPerson(person)
if(success){
    publicAddPersonEvent(person,"add");
}
```

addPerson 成功之后，直接发布一个事件出去，然后“发给指定服务同步一下”这件事情就可以放在事件监听器去做。

对应的代码也很简单，新建一个 SpringBoot 工程。

首先我们先搞一个 Person 对象：

```typescript
@Data
public class Person {
    private String name;

    public Person(String name) {
        this.name = name;
    }
}
```

由于我们还要告知是新增还是修改，所以还需要搞个对象封装一层：

```kotlin
@Data
public class PersonEvent {

    private Person person;

    private String addOrUpdate;

    public PersonEvent(Person person, String addOrUpdate) {
        this.person = person;
        this.addOrUpdate = addOrUpdate;
    }
}
```

然后搞一个事件发布器：

```less
@Slf4j
@RestController
public class TestController {

    @Resource
    private ApplicationContext applicationContext;

    @GetMapping("/publishEvent")
    public void publishEvent() {
        applicationContext.publishEvent(new PersonEvent(new Person("why"), "add"));
    }
}
```

最后来一个监听器：

```less
@Slf4j
@Component
public class EventListenerService {

    @EventListener
    public void handlePersonEvent(PersonEvent personEvent) {
        log.info("监听到PersonEvent: {}", personEvent);
    }

}
```

Demo 就算是齐活了，你把代码粘过去，也用不了一分钟吧。

启动服务跑一把：

![](https://why-image-1300252878.cos.ap-chengdu.myqcloud.com/img/20220716/20240113213419.png)

看起来没有任何毛病，在监听器里面直接就监听到了。

这个时候假设，我还有一个对象，叫做 Order，每当 Order 表新增或者修改一条数据的时候，也要给指定服务同步一下。

怎么办？

这还不简单？

照葫芦画瓢呗。

![](https://why-image-1300252878.cos.ap-chengdu.myqcloud.com/img/20220716/20240115000331.png)

先来一个 Order 对象：

```typescript
@Data
public class Order {
    private String orderName;

    public Order(String orderName) {
        this.orderName = orderName;
    }
}
```

再来一个 OrderEvent 封装一层：

```mipsasm
@Data
public class OrderEvent {
    
    private Order order;

    private String addOrUpdate;

    public OrderEvent(Order order, String addOrUpdate) {
        this.order = order;
        this.addOrUpdate = addOrUpdate;
    }
}
```

然后再发布一个对应的事件：

![](https://why-image-1300252878.cos.ap-chengdu.myqcloud.com/img/20220716/20240113213613.png)

新增一个对应的事件监听：

![](https://why-image-1300252878.cos.ap-chengdu.myqcloud.com/img/20220716/20240113213637.png)

发起调用：

![](https://why-image-1300252878.cos.ap-chengdu.myqcloud.com/img/20220716/20240113213658.png)

完美，两个事件都监听到了。

那么问题又来了，假设我还有一个对象，叫做 Account，每当 Account 表新增或者修改一条数据的时候，也要给指定服务同步一下。

或者说，我有几十张表，对应几十个对象，都要做类似的同步。

请问阁下又该如何应对？

你当然可以按照前面处理 Order 的方式，继续依葫芦画瓢。

但是这样势必会来带的一个问题是对象的膨胀，你想啊，毕竟每一个对象都需要一个对应的 xxxxEvent 封装对象。

这样的代码过于冗余，丑，不优雅。

![](https://why-image-1300252878.cos.ap-chengdu.myqcloud.com/img/20220716/20240115000437.png)

怎么办？

自然而然的我们能想到泛型，毕竟人家干这个事儿是专业的，放一个通配符，管你多少个对象，通通都是“T”，也就是这样的：

```kotlin
@Data
class BaseEvent<T> {
    private T data;
    private String addOrUpdate;

    public BaseEvent(T data, String addOrUpdate) {
        this.data = data;
        this.addOrUpdate = addOrUpdate;
    }
    
}
```

对应的事件发布的地方也可以用 BaseEvent 来代替：

![](https://why-image-1300252878.cos.ap-chengdu.myqcloud.com/img/20220716/20240113213748.png)

这样用一个 BaseEvent 就能代替无数的 xxxEvent，做到通用，这是它的好处。

同时对应的监听器也需要修改：

![](https://why-image-1300252878.cos.ap-chengdu.myqcloud.com/img/20220716/20240113213955.png)

启动服务，跑一把。

发起调用之后你会发现控制台正常输出：

![](https://why-image-1300252878.cos.ap-chengdu.myqcloud.com/img/20220716/20240113214110.png)

但是，注意我要说但是了。

但是监听这一坨代码我感觉不爽，全部都写在一个方法里面了，需要用非常多的 if 分支去做判断。

而且，假设某些对象在同步之前，还有一些个性化的加工需求，那么都会体现在这一坨代码中，不够优雅。

怎么办呢？

很简单，拆开监听：

![](https://why-image-1300252878.cos.ap-chengdu.myqcloud.com/img/20220716/20240113214202.png)

但是再次重启服务，发起调用你会发现：控制台没有输出了？怎么回事，怎么监听不到了呢？

![](https://why-image-1300252878.cos.ap-chengdu.myqcloud.com/img/20220716/20240113210919.png)

## 官网怎么说？

在 Spring 的官方文档中，关于泛型类型的事件通知只有寥寥数语，但是提到了两个解决方案：

> https://docs.spring.io/spring-framework/reference/core/beans/context-introduction.html#context-functionality-events-generics

![](https://why-image-1300252878.cos.ap-chengdu.myqcloud.com/img/20220716/20240113211419.png)

首先官网给出了这样的一个泛型对象：EntityCreatedEvent

然后说比如我们要监听 Person 这个对象创建时的事件，那么对应的监听器代码就是这样的：

```typescript
@EventListener
public void onPersonCreated(EntityCreatedEvent<Person> event) {
 // ...
}
```

和我们 Demo 里面的代码结构是一样的。

那么怎么才能触发这个监听呢？

第一种方式是：

```csharp
class PersonCreatedEvent extends EntityCreatedEvent<Person> { … }).
```

也就是给这个对象创造一个对应的 xxxCreatedEvent，然后去监听这个 xxxCreatedEvent。

和我们前面提到的 xxxxEvent 封装对象是一回事。

为什么我们必须要这样做呢？

官网上提到了这几个词：

> Due to type erasure

![](https://why-image-1300252878.cos.ap-chengdu.myqcloud.com/img/20220716/20240113214728.png)

type erasure，泛型擦除。

因为泛型擦除，所以导致直接监听 EntityCreatedEvent 事件是不生效的，因为在泛型擦除之后，EntityCreatedEvent 变成了 EntityCreatedEvent<?>。

封装一个对象继承泛型对象，通过他们之间一一对应的关系从而绕开泛型擦除这个问题，这个方案确实是可以解决问题。

但是，前面说了，不够优雅。

官网也觉得这个事情很傻：

![](https://why-image-1300252878.cos.ap-chengdu.myqcloud.com/img/20220716/20240113215609.png)

它怎么说的呢？

> In certain circumstances, this may become quite tedious if all events follow the same structure.
> 在某些情况下，如果所有事件都遵循相同的结构，这可能会变得相当 tedious。

好，那么 tedious，是什么意思？哪个同学举手回答一下？

![](https://why-image-1300252878.cos.ap-chengdu.myqcloud.com/img/20220716/20240115000710.png)

这是个四级词汇，得认识，以后考试的时候要考：

![](https://why-image-1300252878.cos.ap-chengdu.myqcloud.com/img/20220716/20240113215406.png)

quite tedious，相当啰嗦。

我们都不希望自己的程序看起来是 tedious 的。

所以，官方给出了另外一个解决方案：ResolvableTypeProvider。

![](https://why-image-1300252878.cos.ap-chengdu.myqcloud.com/img/20220716/20240113215635.png)

我也不知道这是在干什么，反正我拿到了代码样例，那我们就白嫖一下嘛：

```kotlin
@Data
class BaseEvent<T> implements ResolvableTypeProvider {
    private T data;
    private String addOrUpdate;

    public BaseEvent(T data, String addOrUpdate) {
        this.data = data;
        this.addOrUpdate = addOrUpdate;
    }

    @Override
    public ResolvableType getResolvableType() {
        return ResolvableType.forClassWithGenerics(getClass(), ResolvableType.forInstance(getData()));
    }
}
```

再次启动服务，你会发现，监听器又好使了：

![](https://why-image-1300252878.cos.ap-chengdu.myqcloud.com/img/20220716/20240113222058.png)

那么问题又来了。

这是为什么呢？

![](https://why-image-1300252878.cos.ap-chengdu.myqcloud.com/img/20220716/20240115000802.png)

## 为什么？

我也不知道为什么，但是我知道源码之下无秘密。

所以，先打上断点再说。

关于 @EventListener 注解的原理和源码解析，我之前写过一篇相关的文章：[《扯下@EventListener这个注解的神秘面纱。》](https://mp.weixin.qq.com/s/RSgd_bWH_oPQUDU3IsJEOQ)

有兴趣的可以看看这篇文章，然后再试着按照文章中的方式去找对应的源码。

我这篇文章就不去抽丝剥茧的一点点找源码了，直接就是一个大力出奇迹。

因为我们已知是 ResolvableTypeProvider 这个接口在搞事情，所以我只需要看看这个接口在代码中被使用的地方有哪些：

![](https://why-image-1300252878.cos.ap-chengdu.myqcloud.com/img/20220716/1705156620567.png)

除去一些注释和包导入的地方，整个项目中只有 ResolvableType 和 MultipartHttpMessageWriter 这个两个中用到了。

直觉告诉我，应该是在 ResolvableType 用到的地方打断点，因为另外一个类看起来是 Http 相关的，和我的 Demo 没啥关系。

所以我直接在这里打上断点，然后发起调用，程序果然就停在了断点处：

> org.springframework.core.ResolvableType#forInstance

![](https://why-image-1300252878.cos.ap-chengdu.myqcloud.com/img/20220716/1705156836477.png)

我们观察一下，发现这几行代码核心就干一个事儿：判断 instance 是不是 ResolvableTypeProvider 的子类。

如果是则返回一个 type，如果不是则返回 forClass(instance.getClass())。

通过 Debug 我们发现 instance 是 BaseEvent：

![](https://why-image-1300252878.cos.ap-chengdu.myqcloud.com/img/20220716/20240113224602.png)

巧了，这就是 ResolvableTypeProvider 的子类，所以返回的 type 是这样式儿的：

> com.example.elasticjobtest.BaseEvent<com.example.elasticjobtest.Person>

![](https://why-image-1300252878.cos.ap-chengdu.myqcloud.com/img/20220716/20240113224728.png)

是带具体的类型的，而这个类型就是通过 getResolvableType 方法拿到的。

前面我们在实现 ResolvableTypeProvider 的时候，就重写了 getResolvableType 方法，调用了 ResolvableType.forClassWithGenerics，然后用 data 对应的真正的 T 对象实例的类型，作为返回值，这样泛型对应的真正的对象类型，就在运行期被动态的获取到了，从而解决了编译阶段泛型擦除的问题。

如果没有实现 ResolvableTypeProvider 接口，那么这个方法返回的就是 BaseEvent<?>：

> com.example.elasticjobtest.BaseEvent<?>

![](https://why-image-1300252878.cos.ap-chengdu.myqcloud.com/img/20220716/20240113225044.png)

看到这里你也就猜到个七七八八了。

都已经拿到具体的泛型对象了，后面再发起对应的事件监听，那不是顺理成章的事情吗？

好，现在你在第一个断点处就收获到了一个这么关键的信息，接下来怎么办呢？

接着断点处往下调试，然后把整个链路都梳理清楚呗。

再往下走，你会来到这个地方：

> org.springframework.context.event.AbstractApplicationEventMulticaster#getApplicationListeners

![](https://why-image-1300252878.cos.ap-chengdu.myqcloud.com/img/20220716/20240114224039.png)

从 cache 里面获取到了一个 null。

因为这个缓存里面放的就是在项目启动过程中已经触发过的框架自带的 listener 对象：

![](https://why-image-1300252878.cos.ap-chengdu.myqcloud.com/img/20220716/20240114224243.png)

调用的时候，如果能从缓存中拿到对应的 listener，则直接返回。而我们 Demo 中的自定义 listener 是第一次触发，所以肯定是没有的。

因此关键逻辑就这个方法的最后一行：retrieveApplicationListeners 方法里面

> org.springframework.context.event.AbstractApplicationEventMulticaster#retrieveApplicationListeners

![](https://why-image-1300252878.cos.ap-chengdu.myqcloud.com/img/20220716/20240114224336.png)

这个地方再往下写，就是我前面我提到的这篇文章中我写过的内容了 [《扯下@EventListener这个注解的神秘面纱。》](https://mp.weixin.qq.com/s/RSgd_bWH_oPQUDU3IsJEOQ)。

和泛型擦除的关系已经不大了，我就不再写一次了。

只是给大家看一下这个方法在我们的 Demo 中，最终返回的 allListeners 就是我们自定义的这个事件监听器：

> com.example.elasticjobtest.EventListenerService#handlePersonEvent

![](https://why-image-1300252878.cos.ap-chengdu.myqcloud.com/img/20220716/1705247506848.png)

为什么是这个？

因为我当前发布的事件的主角就是 Person 对象：

![](https://why-image-1300252878.cos.ap-chengdu.myqcloud.com/img/20220716/20240114235236.png)

同理，当 Order 对象的事件过来的时候，这里肯定就是对应的 handleOrderEvent 方法：

![](https://why-image-1300252878.cos.ap-chengdu.myqcloud.com/img/20220716/20240114235453.png)

如果我们把 BaseEvent 的 ResolvableTypeProvider 接口拿掉，那么你再看对应的 allListeners，你就会发现找不到我们对应的自定义 Listener 了：

![](https://why-image-1300252878.cos.ap-chengdu.myqcloud.com/img/20220716/20240114233342.png)

为什么？

因为当前事件对应的 ResolvableType 是这样的：

> org.springframework.context.PayloadApplicationEvent<com.example.elasticjobtest.BaseEvent<?>>

![](https://why-image-1300252878.cos.ap-chengdu.myqcloud.com/img/20220716/20240114233524.png)

而我们并没有自定义一个这样的 Listener：

```typescript
@EventListener
public void handleAllEvent(BaseEvent<?> orderEvent) {
    log.info("监听到Event: {}", orderEvent);
}
```

所以，这个事件发布了，但是没有对应的消费。

大概就是这么个意思。

核心逻辑就在 ResolvableTypeProvider 接口里面，重写了 getResolvableType 方法，在运行期动态的获取泛型对应的真正的对象类型，从而解决了编译阶段泛型擦除的问题。

很好，现在摸清楚了，是个很简单的思路，之前是 Spring 的，现在它是我的了。

![](https://why-image-1300252878.cos.ap-chengdu.myqcloud.com/img/20220716/20240115001248.png)

## 为什么需要发布订阅模式 ?

既然写到 Spring 的事件通知机制了，那么就顺便聊聊这个发布订阅模式。

也许在看的过程中，你会冒出这样一个问题：为什么要搞这么麻烦？把这些事件监听的业务逻辑直接写在对应的数据库操作语句之后不行么？

要回答这个问题，我们可以先总结一下事件通知机制的使用场景。

1. 数据变化之后同步清除缓存，这是一种简单可靠的缓存更新方式。只有在清除失败，或者数据库主从同步间隙被脏读才有可能出现缓存脏数据，概率比较小，一般业务上也是可以接受的。
2. 通过某种方式告诉下游系统数据变化，比如往消息队列里面扔消息。
3. 数据的统计、监控、异步触发等场景。当然这动作似乎用 AOP 也可以做，但是实际上在某些业务场景下，做切面统计，反而没有通过发布订阅机制来得直接，灵活度也更好。

除了上面这些外，肯定还有一些其他的场景，但是这些场景都有一个共同点：与核心业务关系不大，但是又具备一定的普适性。

比如完成用户注册之后给用户发一个短信，或者发个邮件啥的。这个事情用发布订阅机制来做是再合适不过的了。

编码过程中牢记单一职责原则，要知道一个类该干什么不该干什么，这是面向对象编程 的关键点之一。

当你一个类中注入了大量的 Service 的时候，你就要考虑考虑，是不是有什么做的不合适的地方了，是不是有些 Service 其实不应该注入进来的。

是不是该用用发布订阅了？

另外，当你的项目中真的出现了文章最开始说的，各种各样的 xxxEvent 事件对应的封装的时候，任何一个来开发的人都觉得这样写是不是有点冗余的时候，你就应该考虑一下是不是有更加优雅的解决方案。

假设这个方案由于某些原因不能使用或者不敢使用是一回事。

但是知不知道这个方案，是另一回事。

![](https://why-image-1300252878.cos.ap-chengdu.myqcloud.com/img/20220716/20240115000222.png)
