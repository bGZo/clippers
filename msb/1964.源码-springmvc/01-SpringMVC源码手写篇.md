# SpringMVC源码-手写篇

# 一、SpringMVC的基本结构

## 1.MVC简介

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1462/1666674557051/a965e06ac7af4d6db0bd255a6908e44b.png)

以前的纯Servlet的处理方式：

```java
@Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {

        String type = req.getParameter(Constant.REQUEST_PARAMETER_TYPE);

        if(type != null && !"".equals(type)){
            if(Constant.SERVLET_TYPE_SAVE.equals(type)){
                // 添加用户信息
                try {
                    saveOrUpdateUser(req, resp);
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }else if(Constant.SERVLET_TYPE_UPDATE.equals(type)){
                // 更新用户信息
            }else if(Constant.SERVLET_TYPE_DELETE.equals(type)){
                // 删除用户信息
                deleteUserById(req, resp);
            }else if(Constant.SERVLET_TYPE_QUEYR.equals(type)){
                // 查询用户
                queryUser(req, resp);
            }else if(Constant.SERVLET_TYPE_QUERYBYID.equals(type)){
                // 查询单条记录
                String id = req.getParameter("id");
                User user = userService.queryById(Integer.parseInt(id));
                // 跳转到更新的页面同时保存数据到Request作用域中
                req.setAttribute("user",user);
                req.getRequestDispatcher("/user/userUpdate.jsp").forward(req,resp);
            }else if(Constant.SERVLET_TYPE_CHECK.equals(type)){
                // 验证账号是否存在
                String userName = req.getParameter("userName");
                String s = userService.checkUserName(userName);
                resp.getWriter().println(s);
                resp.flushBuffer();
            }
        }else{
            // 查询用户信息
            queryUser(req, resp);
        }
    }
```

为了尽量减少依赖Servlet API，提高程序的可测试性、可复用性而发展出了很多的框架技术：

* Struts1
* Struts2
* SpringMVC

经典面试题：Struts2和SpringMVC的区别

1. 请求映射上的区别。
2. 请求数据绑定上的区别。

## 2.基本结构

&emsp;&emsp;然后我们来看看SpringMVC的基本结构

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1462/1666674557051/4fed1e122eb74d71a2dbabf9fae1b179.png)

从图中我们可以得到的相关信息

1. 有四个非常重要的角色
2. DispatchServlet很重要
3. 谁来负责Controller
4. DispatchServlet根据什么规则分发请求
5. View是什么
6. DispatchServlet负责转发。如何知道怎么转发?
7. MVC是严格的分工协作

# 二、控制器

&emsp;&emsp;接下来我们看看应该要如何来设计我们的Controller。控制器的作用是用来具体的处理用户的请求。我们系统能够通过一个普通的bean对象来作为我们的Controller。但是在Spring中对于Bean的管理都是以IoC容器来管理的。这样可以充分的利用SpringIoC和AOP的功能。

问题思考：

1. 请求如何和Bean对于
2. 请求如何和Bean的方法对应

## 1.实例级别的映射

&emsp;&emsp;也就是通过请求地址和Bean的名称对应。通过这个Bean来处理请求。但是如何知道用这个Bean中的哪个方法来处理呢？这时我们可以定义一个接口@Controller.然后声明对应的方法。让Bean去实现这个接口。

```java
public interface Controller {

	ModelAndView handleRequest(HttpServletRequest request, HttpServletResponse response) throws Exception;
}
```

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1462/1666674557051/566f607c77b245b6abfff64254fe74e4.png)

&emsp;&emsp;接下来我们需要思考：handleRequest这个方法需要返回什么信息？

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1462/1666674557051/6eb8ca151998488ebe25837c8a461809.png)

&emsp;&emsp;也就是控制器需要返回用户需要的数据和对应的View。那么对应的返回数据应该有什么特点呢？站在我们现在这个角度我们是完全不知道应该要返回什么数据的。完全需要基于用户的需要了。也就是数据需要呈现 `多样话`。这时可以通过Map来非常灵活的使用。

&emsp;&emsp;同时对应的View也应该具备对应的 `多样化`的特点。

```
public interface View {
	void render(Map<String, ?> model, HttpServletRequest request, HttpServletResponse response);
}
```

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1462/1666674557051/7cc24e7349974c309b555c97089d4fe1.png)

&emsp;&emsp;这里的数据和View的串联我们可以自定义一个ModelAndView这个实现来处理

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1462/1666674557051/ed9f363f6b5f46358340243d05b16a4c.png)

所以上面的Controller中定义方法的返回值我们就可以定义为ModelAndView了

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1462/1666674557051/5a41854f16ef4bc1a6fee9b3501cf9d1.png)

还有对应Controller对于客户的响应状态我们可以定义一个 `HttpStatus`来统一管理

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1462/1666674557051/8380e0e078ca4754b3f0b899f1c61077.png)

&emsp;&emsp;这种方式我们可以看到一个Bean对象处理请求的话我们还需要在 `handleRequest`方法中来判断处理。或者一个Bean处理一个请求，这种方式是非常不灵活的。

## 2.方法级别的映射

&emsp;&emsp;第二种选择就是具体的请求直接映射到我们对应的方法中。我们定义的普通Bean不需要实现Controller接口了。就作为一个Controller存在。

&emsp;&emsp;那么怎么表示一个Bean是Controller呢？我们需要显示的通过@Controller注解来实现。

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1462/1666674557051/5954198970264430ac07919ffcca1289.png)

&emsp;&emsp;怎么映射请求到具体的方法中呢？我们可以通过@RequestMapping注解来指定

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1462/1666674557051/61462a6893db4a93a0556baf78676aba.png)

然后对应的定义如下：

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1462/1666674557051/8a0a44c7bee640129c77ef38096d8e96.png)

## 3.如何实现多种方式的支持

&emsp;&emsp;上面我们介绍了Controller处理请求的两种方式

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1462/1666674557051/f25c3072320c4e4e9c775d13b012916a.png)

那如何让SpringMVC框架能够支持这两种方式呢？甚至更多的方式

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1462/1666674557051/782e21472bdc47db85509015f73e0d1d.png)

我们来分析下如何来实现这种需求：

1. 各种方式的请求映射是不一样的
2. 各种方式对应的Request Handler 也是不一样的
   1. 方式一：Controller接口的实现对象
   2. @Controller、@RequestMapping注解标识的Bean的方法
3. 如何设计DispatchServlet来灵活的处理呢

不同的方式，映射的规则不相同，请求处理器也不一样。这时我们可以考虑通过 `策略模式`来处理了.对应的接口为 HandlerMapping。

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1462/1666674557051/73f53cd69e9e4a2fa18fb3f5fc23ea8b.png)

然后将对应的接口的实现者设置为Bean。DispatchServlet从ApplicationContext中获取对应的配置

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1462/1666674557051/fa6cef90cea44cc89ee3f7030374c106.png)

&emsp;&emsp;有了对应的handlerMapping然后怎么针对不同的请求来选择对应的实现策略呢，这时我们可以提供对应的适配器来处理。

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1462/1666674557051/9731e8ba8bdd436bae9c2355dcdba6a1.png)

* 每种不同的请求处理器提供它的适配实现，配置为Bean
* DispatchServlet 从ApplicationContext中获取所有配置。面向HandlerAdapter。隔绝了handler的变化影响。

方式一通过Controller接口处理还是很方便的直接只是 handlerRequest方法就可以直接处理了。但是方式二，我们通过@Controller，@RequestMapping注解来映射到对应的方法这块应该要怎么实现呢？

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1462/1666674557051/5d68649d2b4f477fbde9936f0ecab0b7.png)

分析：方式二的Handler是@Controller、@RequestMapping注解标识的Bean和方法，需要定义一个实体类保存BeanName，方法名。@RequestMapping的注解信息。

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1462/1666674557051/402c902794c84138b790953dcc5c3954.png)

定义 `RequestMappingInfo`来存储对应的注解信息。那么这个注解信息该由谁去获取呢？并且在什么时候获取呢？这时我们可以在RequestMappingHandlerMapping的getHandler方法之前处理这个解析就可以了。

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1462/1666674557051/0fbd33982c0f41c8bf22c57bd2624d35.png)

我们实现者两个接口来做这个事情就可以了。

```java
	@Override
	public void afterPropertiesSet() throws Exception {
		// 检测@Controller Bean
		for (String beanName : this.applicationContext.getBeanNamesForType(Object.class)) {
			Class<?> beanType = this.applicationContext.getType(beanName);
			if (isHandlerBean(beanType)) {
				detectHandlerMethod(beanType);
			}
		}
	}
```

还有一个问题。如果存放检测到的RequestMappingInfo信息呢。如下

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1462/1666674557051/911633d164e04e06adcb45cdbbb1558e.png)

## 4. DispatchServlet

&emsp;&emsp;到这我们就把Controller怎么找到的路径讲解清楚了，然后来看下DispatchServlet是如何处理的，我们应该怎么来设计。

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1462/1666674557051/c1980d9f52db4a7eb33106a5265b2f52.png)

我们先来考虑下DispatchServlet要具备哪些功能

1. 创建ApplicationContext容器
2. 要从容器中获取HandlerMapping、HandlerAdapter
3. 完成分发
4. 完成view转发
5. 完成异常处理

然后我们得考虑DispatchServlet要完成这些事情，它应该怎么去实现？

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1462/1666674557051/192295ae14834d3ca09104cc34bcd311.png)

那么对应的操作：

1. 在init方法中完成3个属性的初始化
2. 在service方法中完成handler分发、执行的逻辑
3. 在destory方法中关闭ApplicationContext

对应的DispatcherServlet 应该的结构

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1462/1666674557051/d48a7c6ba70240bb885d9e29f088f3e9.png)

对应的核心代码

```java
	/**
	 * 初始化 MVC相关组件的策略提供者，从applicationContext中获取
	 * 
	 * @param applicationContext
	 */
	private void initStrategies(ApplicationContext applicationContext) {
		// 1、initHandlerMapping
		initHandlerMappings(applicationContext);

		// 2、initHandlerAdapter
		initHandlerAdapters(applicationContext);

	}
```

service方法

```java
	@Override
	protected void service(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
		// 在这里可把一些Dispatcher持有的对象放入到Request中，以被后续处理过程中可能需要使用到
		req.setAttribute(WEB_APPLICATION_CONTEXT_ATTRIBUTE_NAME, webApplicationContext);

		this.doDispatch(req, resp);

	}
```

doDispatch方法

```java
	private void doDispatch(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
		Object handler = null;
		ModelAndView mv = null;
		Exception dispatchException = null;
		try {
			// 1、获取请求对应的handler
			handler = this.getHandler(req);
			// 2、如果没有对应的handler
			if (handler == null) {
				noHandlerFound(req, resp);
				return;
			}
			// 3、如果有对应的handler，获得handler的Adapter

			HandlerAdapter ha = this.getHandlerAdapter(handler);

			// 4、执行adapter
			mv = ha.handle(req, resp, handler);

		} catch (Exception e) {
			dispatchException = e;
		}
		// 5、转发给view
		processDispatchResult(req, resp, handler, mv, dispatchException);
	}
```

# 三、Model&View

&emsp;&emsp;上面介绍请求了怎么分发到Controller来处理请求，接下来我们就需要看看处理完请求后如何响应对应的 `数据`和 `View`。

## 1.View

&emsp;&emsp;我们再回看下前面介绍的HandlerAdapter。

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1462/1666674557051/60bbf96a0cf84b0db76e33117ef752e3.png)

可以看到对应的handle方法统一返回的是ModelAndView对象。我们需要在方法中创建他的实例，提供对应的View对象。这样Controller的方法的职责就不专一了，被污染了。而且不能灵活的替换View层了。不够灵活。这时我们可以重新定义ModelAndView。再其中加入一个视图名称。

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1462/1666674557051/eadcfc6e4421490b9920d1ec88aa002d.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1462/1666674557051/dd2bcd661dc64d058fa12a4e7be3efc1.png)

加入视图名称后，我们在Controller中的方法返回就可以如下的写法了

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1462/1666674557051/1972eec8ce9e45b5a2b0d8dbaea8930e.png)

但是有有了一个新的问题，最终的ModelAndView对象由谁来完成呢？根据前面的讲解我们肯定能想到通过 `HandlerAdapter`来实现了。

```java
	@Override
	public ModelAndView handle(HttpServletRequest request, HttpServletResponse response, Object handler)
			throws Exception {
		// TODO Auto-generated method stub
		RequestMappingInfo mappingInfo = (RequestMappingInfo) handler;
		// ....
		return null;
	}
```

当然这块我们还有一些其他的疑问

1. Model数据怎么获取？--》参数传递
2. 还可以直接返回ModelAndView吗？ --》完全可以
3. 返回的是视图名称。怎么转换为View呢？谁来转换呢？ --》专门设计一个来处理

## 3.ViewResolver

&emsp;&emsp;定义一个ViewResolver完成视图名到视图的转换。刚开始不知道怎么干，直接定义一个接口

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1462/1666674557051/4d341ca0923c429499efe5a4b7d36d43.png)

&emsp;&emsp;不同的视图技术可能有不同的View实现及转换规则。那就实现ViewResolver来提供对应的转换规则。都配置为Bean。DispatcherServlet可以从容器中获取。

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1462/1666674557051/97fbc88241444434be3f38f8adf7113e.png)

需要在DispatcherServlet中完成它的初始化以及对应的视图渲染逻辑。

然后来看看ViewResolver的实现。一个基于URL的转发，重定义的ViewResolver实现

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1462/1666674557051/13cb3ebe17b54950a652ce7a58a2c866.png)

增加其他的ViewResolver实现

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1462/1666674557051/2f1f491cb19e46838fe15f0c202642dc.png)

增加其他的View实现

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1462/1666674557051/210e54bf10ad426c9c7386ea174f22ce.png)

## 2.Model

&emsp;&emsp;数据存储Model的设计，相对就比较简单了。

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1462/1666674557051/2d065e4a66db4602b94658194db1a515.png)

# 四、HandlerInterceptor

&emsp;&emsp;上面介绍了那么多还是有问题没有涵盖到，比如请求参数如何绑定到方法参数？需要对请求进行一些过滤，再交给Handler处理。

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1462/1666674557051/5616e48eb4e54e2fa7bea6a7491f58b2.png)

这些其实都可以交给HandlerInterceptor来处理的。

```java
public interface HandlerInterceptor {
    default boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object handler) throws Exception {
        return true;
    }

    default void postHandle(HttpServletRequest request, HttpServletResponse response, Object handler, @Nullable ModelAndView modelAndView) throws Exception {
    }

    default void afterCompletion(HttpServletRequest request, HttpServletResponse response, Object handler, @Nullable Exception ex) throws Exception {
    }
}
```
