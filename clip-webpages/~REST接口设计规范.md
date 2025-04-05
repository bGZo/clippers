---
title: "REST接口设计规范"
created: 2025-04-05T15:50:56
modified: 2025-04-05T15:50:56
source: https://wangwei.info/about-rest-api/
tags:
tags-link:
type: archive-web
---

REST接口设计规范

[ 随遇而安 ](https://wangwei.info/)

  * [Code](https://wangwei.info/tag/code/)
  * [Geek](https://wangwei.info/tag/geek/)
  * [闲聊](https://wangwei.info/tag/other/)
  * [About](https://wangwei.info/about/)
  * [我的微博](https://weibo.com/hummerking)
  * [我的500PX](https://500px.com/hummerking)



[](https://www.facebook.com/linkibot "Facebook") [](https://twitter.com/david_ixi "Twitter")

Subscribe

[Code](https://wangwei.info/tag/code/)

# REST接口设计规范

  * [ ![David Wang](data:image/jpeg;base64,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) ](https://wangwei.info/author/david/)



#### [David Wang](https://wangwei.info/author/david/)

2015年11月10日 • 17 min read

## URI格式规范

  * URI(Uniform Resource Identifiers) 统一资源标示符
  * URL(Uniform Resource Locator) 统一资源定位符



URI的格式定义如下：  
`URI = scheme "://" authority "/" path [ "?" query ] [ "#" fragment ]`

URL是URI的一个子集(一种具体实现)，对于REST API来说一个资源一般对应一个唯一的URI(URL)。在URI的设计中，我们会遵循一些规则，使接口看起透明易读，方便使用者调用。

  * **关于分隔符“/”的使用**



"/"分隔符一般用来对资源层级的划分，例如  
`http://api.canvas.restapi.org/shapes/polygons/quadrilaterals/squares`

对于REST API来说，"/"只是一个分隔符，并无其他含义。为了避免混淆，"/"不应该出现在URL的末尾。例如以下两个地址实际表示的都是同一个资源：  
`http://api.canvas.restapi.org/shapes/`  
`http://api.canvas.restapi.org/shapes`

REST API对URI资源的定义具有唯一性，一个资源对应一个唯一的地址。为了使接口保持清晰干净，如果访问到末尾包含 "/" 的地址，服务端应该301到没有 "/"的地址上。当然这个规则也仅限于REST API接口的访问，对于传统的WEB页面服务来说，并不一定适用这个规则。

  * **URI中尽量使用连字符"-"代替下划线"_"的使用**



连字符"-"一般用来分割URI中出现的字符串(单词)，来提高URI的可读性，例如：  
<http://api.example.restapi.org/blogs/mark-masse/entries/this-is-my-first-post>

使用下划线"_"来分割字符串(单词)可能会和链接的样式冲突重叠，而影响阅读性。但实际上，"-"和"_ "对URL中字符串的分割语意上还是有些差异的："-"分割的字符串(单词)一般各自都具有独立的含义，可参见上面的例子。而"_"一般用于对一个整体含义的字符串做了层级的分割，方便阅读，例如你想在URL中体现一个ip地址的信息：210_110_25_88 .

  * **URI中统一使用小写字母**



根据RFC3986定义，URI是对大小写敏感的，所以为了避免歧义，我们尽量用小写字符。但主机名(Host)和scheme（协议名称:http/ftp/...）对大小写是不敏感的。

  * **URI中不要包含文件(脚本)的扩展名**



例如 .php .json 之内的就不要出现了，对于接口来说没有任何实际的意义。如果是想对返回的数据内容格式标示的话，通过HTTP Header中的Content-Type字段更好一些。

### 资源的原型

  * **文档(Document)**



文档是资源的单一表现形式，可以理解为一个对象，或者数据库中的一条记录。在请求文档时，要么返回文档对应的数据，要么会返回一个指向另外一个资源(文档)的链接。以下是几个基于文档定义的URI例子：  
`http://api.soccer.restapi.org/leagues/seattle` `http://api.soccer.restapi.org/leagues/seattle/teams/trebuchet` `http://api.soccer.restapi.org/leagues/seattle/teams/trebuchet/players/mike`

  * **集合(Collection)**



集合可以理解为是资源的一个容器(目录)，我们可以向里面添加资源(文档)。例如：  
`http://api.soccer.restapi.org/leagues` `http://api.soccer.restapi.org/leagues/seattle/teams` `http://api.soccer.restapi.org/leagues/seattle/teams/trebuchet/players`

  * **仓库(Store)**



仓库是客户端来管理的一个资源库，客户端可以向仓库中新增资源或者删除资源。客户端也可以批量获取到某个仓库下的所有资源。仓库中的资源对外的访问不会提供单独URI的，客户端在创建资源时候的URI除外。例如：  
`PUT /users/1234/favorites/alonso`  
上面的例子我们可以理解为，我们向一个id是1234的用户的仓库(收藏夹)中，添加了一个名为alonso的资源。通俗点儿说：就是用户收藏了一个自己喜爱的球员阿隆索。

  * **控制器(Controller)**



控制器资源模型，可以执行一个方法，支持参数输入，结果返回。 是为了除了标准操作:增删改查(CRUD)以外的一些逻辑操作。控制器(方法)一般定义子URI中末尾，并且不会有子资源(控制器)。例如我们向用户重发ID为245743的消息：  
`POST /alerts/245743/resend`

### URI命名规范

  * 文档(Document)类型的资源用**名词(短语)单数** 命名
  * 集合(Collection)类型的资源用**名词(短语)复数** 命名
  * 仓库(Store)类型的资源用**名词(短语)复数** 命名
  * 控制器(Controller)类型的资源用**动词(短语)**命名
  * URI中有些字段可以是变量，在实际使用中可以按需替换



例如一个资源URI可以这样定义：  
`http://api.soccer.restapi.org/leagues/{leagueId}/teams/{teamId}/players/{playerId}`  
其中：leagueId,teamId,playerId 是变量(数字，字符串都类型都可以)。

  * **CRUD** 的操作不要体现在URI中，HTTP协议中的操作符已经对CRUD做了映射。



CRUD是创建，读取，更新，删除这四个经典操作的简称  
例如删除的操作用REST规范执行的话，应该是这个样子：  
`DELETE /users/1234`

以下是几个错误的示例：  
`GET /deleteUser?id=1234`  
`GET /deleteUser/1234`  
`DELETE /deleteUser/1234`  
`POST /users/1234/delete`

### URI的query字段

`http://api.college.restapi.org/students/morgan/send-sms`  
`http://api.college.restapi.org/students/morgan/send-sms?text=hello`

以上的两个URI看起来很像，但实际的含义是有差别的。第一个URI是一个发送消息的Controller类型的API，第二个URI是发送一个text的内容是hello的消息。

在REST中,query字段一般作为查询的参数补充，也可以帮助标示一个唯一的资源。但需要注意的是，作为一个提供查询功能的URI，无论是否有query条件，我们都应该保证结果的唯一性，一个URI对应的返回数据是不应该被改变的(在资源没有修改的情况下)。HTTP中的缓存也可能缓存查询结果，这个也是我们需要知道的。

  * Query参数可以作为Collection或Store类型资源的过滤条件来使用



例如：  
`GET /users //返回所有用户列表`  
`GET /users?role=admin //返回权限为admin的用户列表`

  * Query参数可以作为Collection或Store资源列表分页标示使用



如果是一个简单的列表操作，可以这样设计：  
`GET /users?pageSize=25&pageStartIndex=50`  
如果是一个复杂的列表或查询操作的话，我们可以为资源设计一个Collection，因为复杂查询可能会涉及比较多的参数，建议使用Post的方式传入，例如这样：  
`POST /users/search`

## HTTP交互设计

### HTTP请求方法的使用

  * **GET** 方法用来获取资源
  * **PUT** 方法可用来新增/更新Store类型的资源
  * **PUT** 方法可用来更新一个资源
  * **POST** 方法可用来创建一个资源
  * **POST** 方法可用来触发执行一个Controller类型资源
  * **DELETE** 方法用于删除资源



一旦资源被删除，GET/HEAD方法访问被删除的资源时，要返回404  
DELETE是一个比较纯粹的方法，我们不能对其做任何的重构或者定义，不可附加其它状态条件，如果我们希望"软"删除一个资源，则这种需求应该由Controller类资源来实现。

### HTTP响应状态码的使用

  * **200 (“OK”)** 用于一般性的成功返回，不可用于请求错误返回
  * **201 (“Created”)** 资源被创建
  * **202 (“Accepted”)** 用于Controller控制类资源异步处理的返回，仅表示请求已经收到。对于耗时比较久的处理，一般用异步处理来完成
  * **204 (“No Content”)** 此状态可能会出现在PUT、POST、DELETE的请求中，一般表示资源存在，但消息体中不会返回任何资源相关的状态或信息。
  * **301 (“Moved Permanently”)** 资源的URI被转移，需要使用新的URI访问
  * **302 (“Found”)** 不推荐使用，此代码在HTTP1.1协议中被303/307替代。我们目前对302的使用和最初HTTP1.0定义的语意是有出入的，应该只有在GET/HEAD方法下，客户端才能根据Location执行自动跳转，而我们目前的客户端基本上是不会判断原请求方法的，无条件的执行临时重定向
  * **303 (“See Other”)** 返回一个资源地址URI的引用，但不强制要求客户端获取该地址的状态(访问该地址)
  * **304 (“Not Modified”)** 有一些类似于204状态，服务器端的资源与客户端最近访问的资源版本一致，并无修改，不返回资源消息体。可以用来降低服务端的压力
  * **307 (“Temporary Redirect”)** 目前URI不能提供当前请求的服务，临时性重定向到另外一个URI。在HTTP1.1中307是用来替代早期HTTP1.0中使用不当的302
  * **400 (“Bad Request”)** 用于客户端一般性错误返回, 在其它4xx错误以外的错误，也可以使用400，具体错误信息可以放在body中
  * **401 (“Unauthorized”)** 在访问一个需要验证的资源时，验证错误
  * **403 (“Forbidden”)** 一般用于非验证性资源访问被禁止，例如对于某些客户端只开放部分API的访问权限，而另外一些API可能无法访问时，可以给予403状态
  * **404 (“Not Found”)** 找不到URI对应的资源
  * **405 (“Method Not Allowed”)** HTTP的方法不支持，例如某些只读资源，可能不支持POST/DELETE。但405的响应header中必须声明该URI所支持的方法
  * **406 (“Not Acceptable”)** 客户端所请求的资源数据格式类型不被支持，例如客户端请求数据格式为application/xml，但服务器端只支持application/json
  * **409 (“Conflict”)** 资源状态冲突，例如客户端尝试删除一个非空的Store资源
  * **412 (“Precondition Failed”)** 用于有条件的操作不被满足时
  * **415 (“Unsupported Media Type”)** 客户所支持的数据类型，服务端无法满足
  * **500 (“Internal Server Error”)** 服务器端的接口错误，此错误于客户端无关



## 原数据设计

### HTTP Headers

  * **Content-Type** 标示body的数据格式
  * **Content-Length** body 数据体的大小，客户端可以根据此标示检验读取到的数据是否完整，也可以通过Header判断是否需要下载可能较大的数据体
  * **Last-Modified** 用于服务器端的响应，是一个资源最后被修改的时间戳，客户端(缓存)可以根据此信息判断是否需要重新获取该资源
  * **ETag** 服务器端资源版本的标示，客户端(缓存)可以根据此信息判断是否需要重新获取该资源，需要注意的是，ETag如果通过服务器随机生成，可能会存在多个主机对同一个资源产生不同ETag的问题
  * Store类型的资源要支持有条件的PUT请求



假设有两个客户端client#1/#2都向一个Store资源提交PUT请求，服务端是无法清楚的判断是要insert还是要update的，所以我们要在header中加入条件标示if-Match，If-Unmodified-Since 来明确是本次调用API的意图。例如：

client#1第一次向服务端发起一个请求 PUT /objects/2113 此时2113资源还不存在，那服务端会认为本次请求是一个insert操作，完成后，会返回 201 (“Created”)

client#2再一次向服务端发起同一个请求 PUT /objects/2113 时，因2113资源已存在，服务端会返回 409 (“Conflict”)

为了能让client#2的请求成功，或者说我们要清楚的表明本次操作是一次update操作，我们必须在header中加入一些条件标示，例如 if-Match。我们需要给出资源的ETag(if-Match:Etag)，来表明我们希望更新资源的版本，如果服务端版本一致，会返回200 (“OK”) 或者 204 (“No Content”)。如果服务端发现指定的版本与当前资源版本不一致，会返回 412 (“Precondition Failed”)

  * **Location** 在响应header中使用，一般为客户端感兴趣的资源URI,例如在成功创建一个资源后，我们可以把新的资源URI放在Location中，如果是一个异步创建资源的请求，接口在响应202 (“Accepted”)的同时可以给予客户端一个异步状态查询的地址

  * **Cache-Control, Expires, Date** 通过缓存机制提升接口响应性能,同时根据实际需要也可以禁止客户端对接口请求做缓存。对于REST接口来说，如果某些接口实时性要求不高的情况下，我们可以使用**max-age** 来指定一个小的缓存时间，这样对客户端和服务器端双方都是有利的。一般来说只对GET方法且返回200的情况下使用缓存，在某些情况下我们也可以对返回3xx或者4xx的情况下做缓存，可以防范错误访问带来的负载。

  * 我们可以自定义一些头信息，作为客户端和服务器间的通信使用，但不能改变HTTP方法的性质。自定义头尽量简单明了，不要用body中的信息对其作补充说明。




### 数据媒体类型(Media Type)

定义如下：
    
    
    Content-Type: type "/" subtype *( ";" parameter )
    两个实例：
    Content-type: text/html; charset=ISO-8859-4
    Content-type: text/plain; charset="us-ascii"
    

type 主类型一般为：application, audio, image, message, model, multipart, text, video。REST接口的主类型一般使用**application**

### 数据媒体类型(Media Type)设计

  * 设计上来说，服务器端可以支持多种媒体类型
  * 可以通过URI的查询字段来指定客户端希望的数据类型


    
    
    GET /bookmarks/mikemassedotcom?accept=application/xml
    

## 数据媒体格式的设计

### body的媒体格式

  * json是一种流行且轻便友好的格式，json是一种无序的键值对的集合，其中key是需要用双引号引起来的，value如果是数字可以不用双引号，如果是非数字的格式需要使用双引号。


    
    
    这是一个json格式的例子：
    {
    "firstName" : "Osvaldo",
    "lastName" : "Alonso", "firstNamePronunciation" : "ahs-VAHL-doe", "number" : 6,
    "birthDate" : "1985-11-11"
    }
    

  * json是允许大小写混用命名的，但要避免使用特殊符号
  * 除了json我们也可以使用其他常用的格式，例如xml,html等
  * body本身只应包含资源相关的信息，不要附加其它传输状态的信息



### 错误响应描述

  * 错误信息的格式应该保持一致，例如用以下方式(json格式):


    
    
    {
      "id" : Text,  //错误唯一标示id
      "description" : Text  //错误具体描述
    }
    
    如果有多个错误，可以用json数组来描述：
    {
      "elements" : [
        {
          "id" : "Update Failed",
          "description" : "Failed to update /users/1234"
        }
      ]
    }
    

  * 错误类型需要保持统一



## 客户端关注的问题

### 接口版本管理

  * 一个资源，只用一种单一的URI来标示，资源的版本不应该体现在URI中
  * 资源的版本是可以由客户端来指定的，并且提供向后兼容
  * ETag可以用来管理资源的版本，有助于客户端缓存的应用



### 接口的安全

  * 使用OAuth认证，对敏感资源保护
  * 使用API管理策略，或管理平台（Apigee, Mashery）



### 接口数据响应的结构

  * 客户端可以指定接口返回需要的资源字段，或者指定不希望返回的字段，这样有助于提升接口交互的效率，较少带宽的浪费


    
    
    只获许部分字段：
    GET /students/morgan?fields=(firstName, birthDate)
    
    不希望获取某些字段：
    GET /students/morgan?fields=!(address,schedule!(wednesday, friday))
    

  * 资源数据中可以包含嵌入式链接，用来描述查询资源的子集，我们也可以传入相关参数，要求服务端替换链接为实际的数据


    
    
    {
      "firstName" : "Morgan", 
      "birthDate" : "1992-07-31",
      # Other fields...
      "links" : {
        "self" : {
          "href" : "http://api.college.restapi.org/students/morgan",
          "rel" : "http://api.relations.wrml.org/common/self" 
        },
        "favoriteClass" : {
          "href" : "http://api.college.restapi.org/classes/japn-301",    
          "rel" : "http://api.relations.wrml.org/college/favoriteClass"
        },
        # Other links... 
      }
    }
    
    如果我们传入embed=(favoriteClass)的参数，返回的数据中将用实际的内容替换links里的对应的潜入资源：
    # Request
    GET /students/morgan?embed=(favoriteClass)
    
    # Response
    {
      "firstName" : "Morgan",
      "birthDate" : "1992-07-31", 
      "favoriteClass" : { //需要返回的嵌入数据
        "id" : "japn-301",
        "name" : "Third-Year Japanese", 
        "links" : {
          "self" : {
            "href" : "http://api.college.restapi.org/classes/japn-301",     
            "rel" : "http://api.relations.wrml.org/common/self"
          } 
        }
    }
    
    # Other fields...
      "links" : { 
        "self" : {
          "href" : "http://api.college.restapi.org/students/morgan",
          "rel" : "http://api.relations.wrml.org/common/self" 
        },
        # 之前的嵌入式链接favoriteClass,已被替换为实体数据
        # Other links... 
      }
    }
    
    
    #其中嵌入式链接信息中的 rel ,一般是对 href 资源如何交互的描述，例如是通过 GET 还是 POST 方法，可以是以下的结构:
    {
      "name": "morgan",
      "method": "GET", 
      ... #其它描述字段
    }
    
    

### JavaScript客户端

目前主流的浏览器对JavaScript的支持越来越完善，因此对于WEB应用来说，我们完全可以把客户单看成一个JavaScript客户端。

  * 一般浏览器对于跨域的操作都有一定的安全策略，通常我们可以使用JSONP来解决跨域接口访问的限制
  * 通过CORS(Cross-Origin Resource Sharing)来解决跨域访问，此方法与JSONP相比，支持更多的方法，JSONP只能用于GET请求, 一般现代的浏览器会支持CORS的方式



> 本文内容参考/引用于:  
>  Mark.Masse《REST.API.Design.Rulebook》

## Sign up for more like this.

Enter your email Subscribe

## [ Ghost开启Https后重复重定向无法访问的问题  Ghost开启Https支持，除了Nginx的配置外，还需要修改 config.production.json 配置文件中 url 的配置项。 重启Ghost后出现了访问页面会重复重定向301的问题，造成页面无法访问。经查，和以下的Nginx配置有关，需要额外添加一条 proxy_set_header X-Forwarded-Proto $scheme 的配置，即可解决。相关配置如下： location / { proxy_pass http://127.0.0.1:3001; proxy_set_header Host $host:443; proxy_set_header X-Real-IP $remote_addr; proxy_set_header X-Forwarded-For $proxy_add_x_ ](https://wangwei.info/ghost-https-repeat-redirect-issue-fixed/) 2022年10月31日 — 1 min read

## [ 如何安装免费SSL证书 Let's Encrypt  SSL证书选择有很多，其中有很多免费的方案可供选择，免费SSL证书中普遍认为Let's Encrypt做的还不错，下面大概简单介绍一下Let's Encrypt的安装和使用，安装环境为自有主机权限，系统为CentOS Stream release 8 Let's Encrypt简介 Let's Encrypt 是一家免费、开放、自动化的证书颁发机构（CA），为公众的利益而运行。 它是一项由 Internet Security Research Group (ISRG) 提供的服务。 Let’s Encrypt的关键原则为： * 免费： 任何拥有域名的人都可以使用 Let’s Encrypt 免费获取受信的证书。 * 自动化： 运行于服务器上的软件可以与 Let’s Encrypt 直接交互，以便轻松获取证书，安全地配置它，并自动进行续期。 * 安全： Let’s Encrypt 将成为一个推动 ](https://wangwei.info/how-to-install-lets-encrypt/) 2022年10月31日 — 5 min read

## [ 如何保持SSH客户端的连接不被关闭  SSH客户端连接服务器的时候，会有因客户端不活跃而被服务器主动关闭链接的情况。这种情况我们一般可以修改服务器端SSHD的配置文来解决。 1.修改服务器端SSHD的配置文件 sudo vim /etc/ssh/sshd_config 2.修改ClientAlive相关配置 ClientAliveInterval 60 ClientAliveCountMax 3 一般默认ClientAlive的两行配置是被关闭（默认会被#注释掉的） * ClientAliveInterval 多久（秒）检测一次客户端是否存活，默认是0不检测，一般修改为60（s）即可 * ClientAliveCountMax 最多检测多少次，默认3次即可，如上设置，如果3x60s=180秒内如果客户端无存活应答，服务器端会主动关闭连接 按如上设置，可以防止客户端在不活跃的时候被服务器主动关闭连接 3.修改完配置后，需要重新加载SSHD配置生效 sudo service sshd reload ](https://wangwei.info/how-to-keep-ssh-connection-is-not-closed/) 2020年6月26日 — 1 min read

[随遇而安](https://wangwei.info/) © 2022

[Powered by Ghost](https://ghost.org/)
