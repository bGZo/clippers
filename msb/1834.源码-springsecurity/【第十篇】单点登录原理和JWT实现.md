# 单点登录原理及JWT实现

> 讲师：邓澎波

# 一、单点登录效果

&emsp;&emsp;首先我们看通过一个具体的案例来加深对单点登录的理解。案例地址：https://gitee.com/xuxueli0323/xxl-sso?_from=gitee_search 把案例代码直接导入到IDEA中

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1462/1653026439009/0f96cc2b66a44f8ea80b23d616643d88.png)

&emsp;&emsp;然后分别修改下server和samples中的配置信息

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1462/1653026439009/b64bac2054774f98bc95e542e618a6d5.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1462/1653026439009/b43231ee7ca84ca6b41747d8b1a0d090.png)

在host文件中配置

```txt
127.0.0.1 sso.server.com
127.0.0.1 client1.com
127.0.0.1 client2.com
```

然后分别启动server和两个simple服务。

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1462/1653026439009/8fcc6ee9aed240e69a6eef7994835bdd.png)

访问测试：

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1462/1653026439009/676e3fde71dc4caba0a786a8ce467009.png)

其中一个节点登录成功后其他节点就可以访问了

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1462/1653026439009/37787f3c801f471e85396787399e2166.png)

自行测试。

# 二、单点登录实现

&emsp;&emsp;清楚了单点登录的效果后，我们就可以自己来创建一个单点登录的实现了。来加深下单点登录的理解了。

## 1.创建项目

&emsp;&emsp;通过Maven创建一个聚合工程，然后在工程中创建3个子模块，分别为认证服务和客户端模块。

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1462/1653026439009/ae75301201c94a9ebda0aa92ed3a519f.png)

引入相同的依赖

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1462/1653026439009/fc0afeec609e488383253aca038cea2b.png)

## 2.client1

&emsp;&emsp;我们先在client1中来提供相关的接口。我们提供一个匿名访问的接口和一个需要认证才能访问的接口。

```java
@Controller
public class UserController {

    @ResponseBody
    @GetMapping("/hello")
    public String hello(){
        return "hello";
    }

    @GetMapping("/queryUser")
    public String queryUser(Model model){
        model.addAttribute("list", Arrays.asList("张三","李四","王五"));
        return "user";
    }
}
```

user.html中的代码为：

```html
<!DOCTYPE html>
<html lang="en" xmlns:th="http://www.thymeleaf.org">
<head>
  <meta charset="UTF-8">
  <title>$Title$</title>
</head>
<body>
  <h1>用户管理：</h1>
    <ul>
      <li th:each="user:${list}">
        [[${user}]]
      </li>
    </ul>
</body>
</html>
```

访问测试：

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1462/1653026439009/c5b5280366ae4144a7ffe20212a9a738.png)

没有认证就能访问，所以得加上验证的逻辑。

```java
    @GetMapping("/queryUser")
    public String queryUser(Model model, HttpSession session){
        Object userLogin = session.getAttribute("userLogin");
        if(userLogin != null){
            // 说明登录过了，直接放过
            model.addAttribute("list", Arrays.asList("张三","李四","王五"));
            return "user";
        }
        // 说明没有登录，需要跳转到认证服务器认证  为了能在登录成功后跳回到当前页面，传递参数
        return "redirect:http://sso.server:8080/loginPage?redirect=http://client1.com:8081/queryUser";
    }
```

可以看到当我们访问queryUser请求的时候，因为没有登录所以会重定向到认证服务中的服务，做登录处理。这时就需要进入到server服务中处理

## 3.server服务

&emsp;&emsp;在服务端我们需要提供两个接口，一个调整到登录界面，一个处理认证逻辑以及一个登录页面

```java

@Controller
public class LoginController {

    /**
     * 跳转到登录界面的逻辑
     * @return
     */
    @GetMapping("/loginPage")
    public String loginPage(@RequestParam(value = "redirect" ,required = false) String url, Model model){
        model.addAttribute("url",url);
        return "login";
    }

    /**
     * 处理登录请求
     * @return
     */
    @PostMapping("/ssoLogin")
    public String login(@RequestParam("userName") String userName,
                        @RequestParam("password") String password,
                        @RequestParam(value = "url",required = false) String url){
        if("zhangsan".equals(userName) && "123".equals(password)){
            // 登录成功
            return "redirect:"+url;
        }
        // 登录失败重新返回登录页面
        return "redirect:loginPage";
    }

}
```

登录页面代码逻辑

```html
<!DOCTYPE html>
<html lang="en" xmlns:th="http://www.thymeleaf.org">
<head>
    <meta charset="UTF-8">
    <title>sso-server-login</title>
</head>
<body>
   <h1>Server登录页面</h1>
  <form action="/ssoLogin" method="post" >
      账号:<input type="text" name="userName" ><br/>
      密码:<input type="password" name="password"><br/>
      <input type="hidden" name="url" th:value="${url}">
      <input type="submit" value="提交">
  </form>
</body>
</html>
```

然后当我们在client1中访问需要认证的服务的时候就会跳转到登录界面

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1462/1653026439009/8eaaf39e86814ecbbd6372b2aca23f41.png)

提交登录操作。当我们提交登录成功的情况，应该要重定向会原来的访问地址，但实际情况和我们所想的有点出入：

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1462/1653026439009/b62099f6f4b0479a8e7c2009930853b1.png)

原来的queryUser中的逻辑为：

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1462/1653026439009/d1ef3e79af1541058a441a5c77318e2d.png)

## 4. 认证凭证

&emsp;&emsp;上面的问题是我们在认证服务登录成功了，但是client1中并不知道登录成功了，所以认证成功后需要给client1一个认证成功的凭证。也就是Token信息。

```java
    /**
     * 处理登录请求
     * @return
     */
    @PostMapping("/ssoLogin")
    public String login(@RequestParam("userName") String userName,
                        @RequestParam("password") String password,
                        @RequestParam(value = "url",required = false) String url){
        if("zhangsan".equals(userName) && "123".equals(password)){
            // 通过UUID生成Token信息
            String uuid = UUID.randomUUID().toString().replace("-","");
            // 把生成的信息存储在Redis服务中
            redisTemplate.opsForValue().set(uuid,"zhangsan");
            // 登录成功
            return "redirect:"+url+"?token="+uuid;
        }
        // 登录失败重新返回登录页面
        return "redirect:loginPage";
    }
```

生成的Token同步保存在了Redis中，然后在重定向的地址中携带了token信息。然后在client1中处理

```java
@GetMapping("/queryUser")
    public String queryUser(Model model,
                            HttpSession session,
                            @RequestParam(value = "token",required = false) String token){
        if(token != null){
            // token有值 说明认证了
            // TODO 基于token 去服务器获取用户信息
            session.setAttribute("userLogin","张三");
        }

        Object userLogin = session.getAttribute("userLogin");
        if(userLogin != null){
            // 说明登录过了，直接放过
            model.addAttribute("list", Arrays.asList("张三","李四","王五"));
            return "user";
        }
        // 说明没有登录，需要跳转到认证服务器认证  为了能在登录成功后跳回到当前页面，传递参数
        return "redirect:http://sso.server.com:8080/loginPage?redirect=http://client1.com:8081/queryUser";
    }
```

然后我们就可以来访问client1中的服务了

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1462/1653026439009/080268690481458a8fc8337bb2802a12.png)

## 5. client2

&emsp;&emsp;控制器逻辑：

```java
@Controller
public class OrderController {

    @GetMapping("/order")
    public String getOrder(HttpSession session, Model model){
        Object userLogin = session.getAttribute("userLogin");
        if(userLogin != null){
            // 说明认证了
            model.addAttribute("list", Arrays.asList("order1","order2","order3"));
            return "order";
        }
        return "redirect:http://sso.server.com:8080/loginPage?redirect=http://client2.com:8082/order";
    }
}
```

order.html页面内容：

```html
<!DOCTYPE html>
<html lang="en" xmlns:th="http://www.thymeleaf.org">
<head>
  <meta charset="UTF-8">
  <title>$Title$</title>
</head>
<body>
  <h1>订单管理：</h1>
    <ul>
      <li th:each="order:${list}">
        [[${order}]]
      </li>
    </ul>
</body>
</html>
```

&emsp;&emsp;通过前面的介绍我们可以发现clent1认证后可以访问了，但是client2提交请求的时候还是会跳转到server服务，做认证的处理。

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1462/1653026439009/7f2d428565b34444b65ce4fedcf0fa9e.png)

&emsp;&emsp;造成这个的原因是client1认证成功后在Session中保存了认证信息，但是在client2是获取不到的，这时我们可以在Server服务登录成功后在浏览器的Cookie中存储一个token信息，然后在其他服务跳转到要进入登录页面之前的接口服务中判断Cookie中是否有值，如果有则认为是其他服务登录过的，直接放过。

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1462/1653026439009/769c32ab334b42b88b7790e22183ccea.png)

提交请求的时候校验

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1462/1653026439009/e5897e82cfa54d82895a95915140298f.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1462/1653026439009/f689d4c8e13844df82cc591327cf1c3c.png)

搞定

# 三、JWT实现

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1462/1653026439009/eb26302d12014d61a3f63ae500d2ef51.png)

## 1.JWT介绍

### 1.1 什么是JWT

> 官方：JSON Web Token (JWT) is an open standard ([RFC 7519](https://tools.ietf.org/html/rfc7519)) that defines a compact and self-contained way for securely transmitting information between parties as a JSON object. This information can be verified and trusted because it is digitally signed. JWTs can be signed using a secret (with the **HMAC** algorithm) or a public/private key pair using **RSA** or  **ECDSA** .

&emsp;&emsp;JSON Web 令牌(JWT)是一种开放标准(RFC 7519) ，它定义了一种紧凑和自包含的方式，用于作为 JSON 对象在各方之间安全地传输信息。可以验证和信任此信息，因为它是数字签名的。JWTs 可以使用 secret (使用 HMAC 算法)或使用 RSA 或 ECDSA 的公钥/私钥对进行签名。

&emsp;&emsp;通俗的解释：JWT简称 JSON Web Token，也就是JSON形式作为Web应用中的令牌信息，用于在各方之间安全的将信息作为JSON对象传输，在数据传输过程中可以完成数据加密，签名等操作。

### 1.2 基于Session认证

&emsp;&emsp;我们最先接触到的认证方式就是基于Session的认证方式，每一个会话在服务端都会存储在HttpSession中，相当于一个Map，然后通过Cookie的形式给客户端返回一个jsessionid，然后每次访问的时候都需要从HttpSession中根据jsessionid来获取，通过这个逻辑来判断是否是认证的状态。

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1462/1653026439009/7a38b36f65b24be9bdb84b8b7833a184.png)

存在的问题：

1. 每个用户都需要做一次记录，而Session一般情况下都会存在内存中，增大了服务器的开销
2. 集群环境下Session需要同步，或者分布式Session来处理
3. 因为是基于Cookie来传输的，如果Cookie被解惑，用户容易受到CSRF攻击。
4. 前后端分离项目中会更加的麻烦

### 1.3 基于JWT的认证

&emsp;&emsp;具体流程如下：

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1462/1653026439009/8ebddb973f52472c831f45f25afeb93b.png)

认证的流程：

1. 用户通过表单把账号密码提交到后端服务后，如果认证成功就会生成一个对应的Token信息
2. 之后用户请求资源都会携带这个Token值，后端获取到后校验通过放行，校验不通过拒绝

jwt的优势：

1. 简介：可以通过URL，POST参数或者HTTP header发送，因为数据量小，传输速度快。
2. 自包含：负载中包含了所有用户所需的信息，避免多次查询数据
3. 夸语音：以JSON形式保存在客户端。
4. 不需要服务端保存信息，适合分布式环境。

### 1.4 JWT的结构

令牌的组成：

- 标头(Header)
- 有效载荷(Payload)
- 签名(Signature)

因此JWT的格式为： xxxx.yyyy.zzzz  Header.Payload.Signature

**Header**:

&emsp;&emsp;header通常由两部分组成：令牌的类型【JWT】和所使用的签名算法。例如HMAC、SHA256或者RSA，它会使用 Base64 编码组成 JWT结构的第一部分。注意：Base64是一种编码，是可以被翻译回原来的样子的。

```json
{
   "alg":"HS256",
   "typ":"JWT"
}
```

**Payload**:

&emsp;&emsp;令牌的第二部分是有效负载，其中包含声明，声明是有关实体（通常是用户信息）和其他数据的声明，它会使用Base64来编码，组成JWT结构的第二部分。

```json
{
	"userId":"123",
	"userName":"波波烤鸭",
	"admin":true
}
```

因为会通过Base64编码，所以不要把敏感信息写在Payload中。

**Signature**：

&emsp;&emsp;签名部分，前面两部分都是使用 Base64 进行编码的，即前端可以解开header和payload中的信息，Signature需要使用编码后的 header 和 payload 以及我们提供的一个秘钥，然后使用 header 中指定的前面算法(HS256) 进行签名，签名的作用是保证 JWT 没有被篡改过

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1462/1653026439009/5d13e4452619415e88236592fe3515a7.png)

## 2.JWT实现

### 2.1 JWT基本实现

&emsp;&emsp;生成Token令牌

```java
    /**
     * 生成Token信息
     */
    @Test
    void generatorToke() {
        Map<String,Object> map = new HashMap<>();
        map.put("alg","HS256");
        map.put("typ","JWT");
        Calendar calendar = Calendar.getInstance();
        calendar.add(Calendar.SECOND,60);
        String token = JWT.create()
                .withHeader(map) // 设置header
                .withClaim("userid", 666) // 设置 payload
                // 设置过期时间
                .withExpiresAt(calendar.getTime())
                .withClaim("username", "波波烤鸭") // 设置 payload
                .sign(Algorithm.HMAC256("qwaszx")); // 设置签名  保密
        System.out.println(token);
    }
```

&emsp;&emsp;根据Token来验证是否正确。

```java
   /**
     * 验证Token信息
     */
    @Test
    public void verifier(){
        String token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NTMwNTE5ODUsInVzZXJpZCI6NjY2LCJ1c2VybmFtZSI6IuazouazoueDpOm4rSJ9.0LW5MFihMeYNfRfez0a68ncaKQ13j5pSnVZTB7m1CDw";
        JWTVerifier jwtVerifier = JWT.require(Algorithm.HMAC256("qwaszx")).build();
        DecodedJWT verify = jwtVerifier.verify(token);
        System.out.println(verify.getClaim("userid").asInt());
        System.out.println(verify.getClaim("username").asString());
    }
```

验证中场景的异常信息：

* SignatureVerificationException 签名不一致异常
* TokenExpiredException Token过期异常
* AlgorithmMismatchException 算法不匹配异常
* InvalidClaimException 失效的payload异常

### 2.2 JWT封装

&emsp;&emsp;为了简化操作我们可以对上面的操作进一步封装来简化处理

```java
package com.bobo.jwt.utils;

import com.auth0.jwt.JWT;
import com.auth0.jwt.JWTCreator;
import com.auth0.jwt.algorithms.Algorithm;
import com.auth0.jwt.interfaces.DecodedJWT;

import java.util.Calendar;
import java.util.Map;

/**
 * JWT操作的工具类
 */
public class JWTUtils {
    private static final String SING = "123qwaszx";

    /**
     * 生成Token  header.payload.sing 组成
     * @return
     */
    public static String getToken(Map<String,String> map){
        Calendar instance = Calendar.getInstance();
        instance.add(Calendar.DATE,7); // 默认过期时间 7天
        JWTCreator.Builder builder = JWT.create();
        // payload 设置
        map.forEach((k,v)->{
            builder.withClaim(k,v);
        });
        // 生成Token 并返回
        return builder.withExpiresAt(instance.getTime())
                    .sign(Algorithm.HMAC256(SING));
    }

    /**
     * 验证Token
     * @return
     *     DecodedJWT  可以用来获取用户信息
     */
    public static DecodedJWT verify(String token){
        // 如果不抛出异常说明验证通过，否则验证失败
        return JWT.require(Algorithm.HMAC256(SING)).build().verify(token);
    }
}

```

### 2.3 SpringBoot应用

&emsp;&emsp;首先是在登录方法中，如果登录成功，我们需要生成对应的Token信息，然后将Token信息响应给客户端。

```java
@PostMapping("/login")
    public Map<String,Object> login(User user){
        Map<String,Object> res = new HashMap<>();
        if("zhang".equals(user.getUserName()) && "123".equals(user.getPassword())){
            // 登录成功
            Map<String,String> map = new HashMap<>();
            map.put("userid","1");
            map.put("username","zhang");
            String token = JWTUtils.getToken(map);
            res.put("flag",true);
            res.put("msg","登录成功");
            res.put("token",token);
            return res;
        }
        res.put("flag",false);
        res.put("msg","登录失败");
        return res;
    }
```

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1462/1653026439009/f12ed59c883549b7a35a66376ed22b12.png)

&emsp;&emsp;然后就是用户提交请求的时候需要携带Token信息，然后我们在controller中处理请求之前需要对token做出校验。如果验证通过就继续处理请求，否则就拦截该请求。

```java
    @PostMapping("/queryUser")
    public Map<String,Object> queryUser(@RequestParam("token") String token){
        // 获取用信息之前校验
        Map<String,Object> map = new HashMap<>();
        try{
            DecodedJWT verify = JWTUtils.verify(token);
            map.put("state",true);
            map.put("msg","请求成功");
            return map;
        }catch (SignatureVerificationException e){
            e.printStackTrace();
            map.put("msg","无效签名");
        }catch (TokenExpiredException e){
            e.printStackTrace();
            map.put("msg","Token过期");
        }catch (AlgorithmMismatchException e){
            e.printStackTrace();
            map.put("msg","算法不一致");
        }catch (Exception e){
            e.printStackTrace();
            map.put("msg","Token无效");
        }
        map.put("state",false);
        return map;
    }
```

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1462/1653026439009/15fbca2940e84d649bc20dcf95410723.png)

&emsp;&emsp;但是上面的情况我们看到在controller中添加了大幅度的Token校验的代码，增大的冗余代码，这时我们可以考虑把Token校验的代码放在拦截器中处理。我们创建一个自定义的拦截器.

```java
/**
 * 自定义的拦截器
 *     对特定的情况校验是否携带的有Token信息，如果不携带直接拒绝
 *     然后对Token校验合法性
 */
public class JWTInterceptor implements HandlerInterceptor {

    @Override
    public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object handler) throws Exception {
        String token = request.getParameter("token");
        // 获取用信息之前校验
        Map<String,Object> map = new HashMap<>();
        try{
            DecodedJWT verify = JWTUtils.verify(token);
            return true;
        }catch (SignatureVerificationException e){
            e.printStackTrace();
            map.put("msg","无效签名");
        }catch (TokenExpiredException e){
            e.printStackTrace();
            map.put("msg","Token过期");
        }catch (AlgorithmMismatchException e){
            e.printStackTrace();
            map.put("msg","算法不一致");
        }catch (Exception e){
            e.printStackTrace();
            map.put("msg","Token无效");
        }
        map.put("state",false);
        // 把Map转换为JSON响应
        String json = new ObjectMapper().writeValueAsString(map);
        response.setContentType("application/json;charset=UTF-8");
        response.getWriter().println(json);
        return false;
    }
}
```

要让拦截器生效我们还需要添加对应的配置类。

```java
@Configuration
public class InterceptorConfig implements WebMvcConfigurer {

    @Override
    public void addInterceptors(InterceptorRegistry registry) {
        registry.addInterceptor(new JWTInterceptor())
                .addPathPatterns("/queryUser") // 需要拦截的请求
                .addPathPatterns("/saveUser") // 需要拦截的请求
                .excludePathPatterns("/login"); // 需要排除的请求
    }
}
```

然后添加一个测试的方法 `/saveUser`

```java
    @PostMapping("/saveUser")
    public String saveUser(){
        System.out.println("------------>");
        return "success";
    }
```

测试访问，把过期时间缩短到1分钟

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1462/1653026439009/4edf0ad33b6140ddaba31960c226925d.png)

正常的访问

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1462/1653026439009/954e22c210434ea2b3771e63e8e56916.png)

Token过期后再访问

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1462/1653026439009/e0adfda4b19849f18797886320066485.png)

搞定
