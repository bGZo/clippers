---
title: "Spring 3 MVC Interceptor tutorial. Spring MVC Interceptor example. Interceptor tutorial"
created: 2025-04-05T15:50:58
modified: 2025-04-05T15:50:58
source: https://www.viralpatel.net/spring-mvc-interceptor-example/
tags:
tags-link:
type: archive-web
---

  * [About](https://www.viralpatel.net/about/)
  * [Contact](https://www.viralpatel.net/contact/)
  * [Privacy](https://www.viralpatel.net/privacy/)


[ViralPatel.net](https://www.viralpatel.net/)

  
  
  


  * [Home](https://www.viralpatel.net/)
  * [Android](https://www.viralpatel.net/category/android/)
  * [Java](https://www.viralpatel.net/category/java/)
  * [Spring](https://www.viralpatel.net/category/spring/)
  * Frameworks
  * [Database](https://www.viralpatel.net/category/database/)
  * [JavaScript](https://www.viralpatel.net/category/javascript/)
  * Web
  * More…


# Spring 3 MVC Interceptor tutorial with example

by [Viral Patel](https://www.viralpatel.net/author/viral/ "Posts by Viral Patel") · November 20, 2012

Spring MVC provides a powerful mechanism to intercept an http request. Similar to [Servlet Filter concept](https://www.viralpatel.net/tutorial-java-servlet-filter-example-using-eclipse-apache-tomcat/), Spring MVC provides a way to define special classes called Interceptors that gets called before and after a request is served.

## Quick Overview

Each interceptor you define must implement `org.springframework.web.servlet.HandlerInterceptor` interface. There are three methods that need to be implemented. `preHandle(..)` is called before the actual handler is executed; The preHandle(..) method returns a boolean value. You can use this method to break or continue the processing of the execution chain. When this method returns true, the handler execution chain will continue; when it returns false, the `DispatcherServlet` assumes the interceptor itself has taken care of requests (and, for example, rendered an appropriate view) and does not continue executing the other interceptors and the actual handler in the execution chain. `postHandle(..)` is called after the handler is executed; `afterCompletion(..)` is called after the complete request has finished. These three methods should provide enough flexibility to do all kinds of preprocessing and postprocessing. You can define an interceptor class as follow:
    
    
    import javax.servlet.http.HttpServletRequest;
    import javax.servlet.http.HttpServletResponse;
    
    import org.springframework.web.servlet.HandlerInterceptor;
    import org.springframework.web.servlet.ModelAndView;
    
    public class HelloWorldInterceptor implements HandlerInterceptor  {
    	@Override
    	public boolean preHandle(HttpServletRequest request,
    			HttpServletResponse response, Object handler) throws Exception {
    		
    		System.out.println("Pre-handle");
    		
    		return true;
    	}
    	//override postHandle() and afterCompletion() 
    }
    
    
    Code language: Java (java)

Once the interceptor is defined, you can ask Spring MVC to configure it via `<mvc:interceptors>` tag within spring-servlet.xml file.
    
    
    <mvc:interceptors>
       <bean class="net.viralpatel.spring3.interceptor.HelloWorldInterceptor" />
    </mvc:interceptors>
    
    Code language: HTML, XML (xml)

Let us start with the complete Demo application. We will create a demo Interceptor that logs each request. Tools and technologies:

  1. Java 5 (or above)
  2. Spring MVC 3.0 (or above)
  3. Eclipse 3.2 (or above)


We will need following JAR files in order to execute this project.

![spring-interceptor-jar-files](https://www.viralpatel.net/app/uploads/2012/11/spring-interceptor-jar-files.png)![spring-interceptor-jar-files](data:image/png;base64,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)

If you are using [Apache Maven](https://www.viralpatel.net/introduction-apache-maven-build-framework-build-automation-tool/) as dependency management, add following dependencies to pom.xml.

_pom.xml_
    
    
     <dependencies>
       <dependency>
          <groupId>org.springframework</groupId>
          <artifactId>spring-webmvc</artifactId>
          <version>3.0.1.RELEASE</version>
       </dependency>
       <dependency>
          <groupId>jstl</groupId>
          <artifactId>jstl</artifactId>
          <version>1.2</version>
       </dependency>
    </dependencies>
    
    Code language: HTML, XML (xml)

Let us create a simple Spring MVC Interceptor class that logs each request.

## Step 1: The Controller – Create new Spring MVC Controller

We create a simple Spring MVC controller that displays a plain JSP view. 

_HelloWorldController.java_
    
    
     package net.viralpatel.spring3.controller;
    
    import org.springframework.stereotype.Controller;
    import org.springframework.web.bind.annotation.RequestMapping;
    import org.springframework.web.bind.annotation.RequestMethod;
    
    @Controller
    public class HelloWorldController {
    
    
        @RequestMapping(value = "/hello", method = RequestMethod.GET)
        public String sayHello() {
            return "hello";
        }
    }
    
    Code language: Java (java)

The controller has one method `sayHello()` which is mapped to URL **/hello**  using `@RequestMapping`. This simply paints the hello.jsp view.

## Step 2: The View – Create new JSPs

Create two JSPs, hello.jsp that displays hello message and index.jsp that simply redirects first request to /hello.html. 

_/WEB-INF/jsp/hello.jsp_
    
    
     <html>
    <head>
    	<title>Spring MVC Interceptor example</title>
    </head>
    <body>
    	<h1>Hello!!</h1>
    </body>
    </html>
    
    Code language: HTML, XML (xml)

_WebContent/index.jsp_
    
    
    <jsp:forward page="hello.html"></jsp:forward>
    
    Code language: HTML, XML (xml)

The index.jsp simply redirects to hello.html which calls the HelloWorldController.

## Step 3: The Interceptor – Spring MVC HandlerInterceptor

Let’s create the Spring based Handler Interceptor which will intercept the request and print a message. 

_HelloWorldInterceptor.java_
    
    
     package net.viralpatel.spring3.interceptor;
    
    import javax.servlet.http.HttpServletRequest;
    import javax.servlet.http.HttpServletResponse;
    
    import org.springframework.web.servlet.HandlerInterceptor;
    import org.springframework.web.servlet.ModelAndView;
    
    public class HelloWorldInterceptor implements HandlerInterceptor  {
    	@Override
    	public boolean preHandle(HttpServletRequest request,
    			HttpServletResponse response, Object handler) throws Exception {
    		
    		System.out.println("Pre-handle");
    		
    		return true;
    	}
    	
    	@Override
    	public void postHandle(HttpServletRequest request,
    			HttpServletResponse response, Object handler,
    			ModelAndView modelAndView) throws Exception {
    		System.out.println("Post-handle");
    	}
    	
    	@Override
    	public void afterCompletion(HttpServletRequest request,
    			HttpServletResponse response, Object handler, Exception ex)
    			throws Exception {
    		System.out.println("After completion handle");
    	}
    }
    
    
    Code language: Java (java)

Thus in each of the method preHandle, postHandle and afterCompletion we print a message on console.

## Step 4: Spring Configuration

Now lets glue up the source code and configure Spring. Note how we declared the interceptor in spring-servlet.xml using <mvc:interceptors> tag. 

_spring-servlet.xml_
    
    
     <beans xmlns="http://www.springframework.org/schema/beans"
    	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    	xmlns:context="http://www.springframework.org/schema/context"
    	xmlns:mvc="http://www.springframework.org/schema/mvc"
    	xsi:schemaLocation="http://www.springframework.org/schema/beans	http://www.springframework.org/schema/beans/spring-beans.xsd http://www.springframework.org/schema/context	http://www.springframework.org/schema/context/spring-context.xsd http://www.springframework.org/schema/mvc http://www.springframework.org/schema/mvc/spring-mvc.xsd">
    		
    	<context:annotation-config />
    	<context:component-scan base-package="net.viralpatel.spring3.controller"/>
    	
    	<mvc:interceptors>
          <bean class="net.viralpatel.spring3.interceptor.HelloWorldInterceptor" />
    	</mvc:interceptors> 
    	
      <bean id="jspViewResolver"
    	class="org.springframework.web.servlet.view.InternalResourceViewResolver">
    		<property name="viewClass"
    			value="org.springframework.web.servlet.view.JstlView" />
    		<property name="prefix" value="/WEB-INF/jsp/" />
    		<property name="suffix" value=".jsp" />
      </bean>
    </beans>
    
    
    Code language: HTML, XML (xml)

Also configure the spring’s DispatcherServlet in web.xml file. 

_web.xml_
    
    
     <?xml version="1.0" encoding="UTF-8"?>
    <web-app xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    	xmlns="http://java.sun.com/xml/ns/javaee" 
    	xmlns:web="http://java.sun.com/xml/ns/javaee/web-app_2_5.xsd"
    	xsi:schemaLocation="http://java.sun.com/xml/ns/javaee 
    		http://java.sun.com/xml/ns/javaee/web-app_2_5.xsd" 
    	id="WebApp_ID" version="2.5">
    	
    	<display-name>Spring3MVC-Interceptor example</display-name>
    	<servlet>
    		<servlet-name>spring</servlet-name>
    		<servlet-class>
    			org.springframework.web.servlet.DispatcherServlet
    		</servlet-class>
    		<load-on-startup>1</load-on-startup>
    	</servlet>
    	<servlet-mapping>
    		<servlet-name>spring</servlet-name>
    		<url-pattern>*.html</url-pattern>
    	</servlet-mapping>
    </web-app>
    
    
    Code language: HTML, XML (xml)

## Final Project Structure

Once all the source files and configuration files are in place, your project should look like below:

![spring-mvc-handle-interceptors-project](https://www.viralpatel.net/app/uploads/2012/11/spring-mvc-handle-interceptors-project.png)![spring-mvc-handle-interceptors-project](data:image/png;base64,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)

## Demo

Compile and execute the project in Eclipse. Open below URL in browser. **URL:**  http://localhost:8080/SpringMVC_Interceptor_example/

![spring-interceptor-example-demo](https://www.viralpatel.net/app/uploads/2012/11/spring-interceptor-example-demo.png)![spring-interceptor-example-demo](data:image/png;base64,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)

Check the server console logs. You must see following:
    
    
    Pre-handle
    Post-handle
    After completion handle

## Download Source Code

[**SpringMVC_Multi_Interceptor_example.zip (2.5 MB)**](https://www.viralpatel.net/app/uploads/2012/11/SpringMVC_Multi_Interceptor_example.zip)

__ Get our Articles via Email. Enter your email address.

Send Me Tutorials

Tags: [Spring](https://www.viralpatel.net/tag/spring/)[spring mvc](https://www.viralpatel.net/tag/spring-mvc/)[spring-3-mvc-series](https://www.viralpatel.net/tag/spring-3-mvc-series/)

  * [ __**Next story** How to update JSTL Locale dynamically](https://www.viralpatel.net/update-jstl-locale/)
  * [ __**Previous story** Eclipse: Ignore “not declare static final serialVersionUID” warning](https://www.viralpatel.net/eclipse-ignore-serialversionuid-warning/)


####  __You may also like...

  * [ ![Spring 4 MVC REST Controller Example \(JSON CRUD Tutorial\)](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAAAAAAALAAAAAABAAEAAAICRAEAOw==) ](https://www.viralpatel.net/spring-4-mvc-rest-example-json/ "Spring 4 MVC REST Controller Example \(JSON CRUD Tutorial\)")

####  [Spring 4 MVC REST Controller Example (JSON CRUD Tutorial)](https://www.viralpatel.net/spring-4-mvc-rest-example-json/ "Spring 4 MVC REST Controller Example \(JSON CRUD Tutorial\)")

  * [ ![Spring 3 MVC: Create Hello World application in Spring 3.0 MVC](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAAAAAAALAAAAAABAAEAAAICRAEAOw==) ](https://www.viralpatel.net/spring-3-mvc-create-hello-world-application-spring-3-mvc/ "Spring 3 MVC: Create Hello World application in Spring 3.0 MVC")

####  [Spring 3 MVC: Create Hello World application in Spring 3.0 MVC](https://www.viralpatel.net/spring-3-mvc-create-hello-world-application-spring-3-mvc/ "Spring 3 MVC: Create Hello World application in Spring 3.0 MVC")

  * [ ![Spring 3 MVC: Internationalization & Localization Tutorial with Example](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAAAAAAALAAAAAABAAEAAAICRAEAOw==) ](https://www.viralpatel.net/spring-3-mvc-internationalization-i18n-localization-tutorial-example/ "Spring 3 MVC: Internationalization & Localization Tutorial with Example")

####  [Spring 3 MVC: Internationalization & Localization Tutorial with Example](https://www.viralpatel.net/spring-3-mvc-internationalization-i18n-localization-tutorial-example/ "Spring 3 MVC: Internationalization & Localization Tutorial with Example")

  * [ ![Spring MVC HashMap Form Integration example](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAAAAAAALAAAAAABAAEAAAICRAEAOw==) ](https://www.viralpatel.net/spring-mvc-hashmap-form-example/ "Spring MVC HashMap Form Integration example")

####  [Spring MVC HashMap Form Integration example](https://www.viralpatel.net/spring-mvc-hashmap-form-example/ "Spring MVC HashMap Form Integration example")




### 37 Comments

  1. ![](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAAAAAAALAAAAAABAAEAAAICRAEAOw==) Pallavi says:

22 November, 2012, 11:36  

Nice Tutorial.

Reply

  2. ![](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAAAAAAALAAAAAABAAEAAAICRAEAOw==) sagar says:

3 December, 2012, 18:39  

i love you viral without you m nothing in this industry ……….. ;)

Reply

  3. ![](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAAAAAAALAAAAAABAAEAAAICRAEAOw==) praveen says:

4 January, 2013, 4:18  

Download source code downloading some other project source code. Please advise

Reply

  4. ![](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAAAAAAALAAAAAABAAEAAAICRAEAOw==) praveen says:

4 January, 2013, 4:25  

I added following dependencies but getting compilation error with these two imports in controller class  

    
        <dependency>
          <groupId>org.springframework</groupId>
          <artifactId>spring-webmvc</artifactId>
          <version>3.0.1.RELEASE</version>
      </dependency>
    import org.springframework.web.bind.annotation.RequestMapping;
    import org.springframework.web.bind.annotation.RequestMethod;
    
    

Reply

  5. ![](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAAAAAAALAAAAAABAAEAAAICRAEAOw==) Rajesh says:

25 January, 2013, 6:39  

Viral, Java 6 will be required for Annotations that you have used like @Override..

Reply

  6. ![](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAAAAAAALAAAAAABAAEAAAICRAEAOw==) [Trent Payne](http://kwutchak.trent.payne.name/) says:

28 January, 2013, 10:05  

Thanks!

This description solved my problem nicely!!

Reply

  7. ![](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAAAAAAALAAAAAABAAEAAAICRAEAOw==) Viral says:

5 March, 2013, 11:39  

I want to develop a complte web applicationn in spring frame work where I can connect to oracle DB and I have front end and data validation done

Please help me

Reply

  8. ![](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAAAAAAALAAAAAABAAEAAAICRAEAOw==) eugene says:

9 March, 2013, 4:30  

I encounterd error blow. why??? Please help me ^^;;

Caused By: org.xml.sax.SAXParseException: cvc-complex-type.2.4.c: The matching wildcard is strict, but no declaration can be found for element ‘mvc:interceptors’.

——————————  
xmlns:mvc=”http://www.springframework.org/schema/mvc”

Reply

     * ![](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAAAAAAALAAAAAABAAEAAAICRAEAOw==) rajimoonp says:

28 May, 2013, 16:51  

@eugene  
add xmlns:mvc=”http://www.springframework.org/schema/mvc” @ header

Reply

  9. ![](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAAAAAAALAAAAAABAAEAAAICRAEAOw==) donghai.wan says:

27 March, 2013, 15:35  

Thanks very much

Reply

  10. ![](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAAAAAAALAAAAAABAAEAAAICRAEAOw==) ggk@hotmail.com says:

8 April, 2013, 6:27  

Thank you very much!!!

Reply

  11. ![](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAAAAAAALAAAAAABAAEAAAICRAEAOw==) [naveen](http://naveenks.com/) says:

25 April, 2013, 6:19  

thank you so much for your post, a sensible example which i’ve seen after searching about 50 sites… cheers :)

Reply

  12. ![](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAAAAAAALAAAAAABAAEAAAICRAEAOw==) Ravi says:

18 May, 2013, 10:50  

Can anyone help me how to configure maven in eclipse?

Reply

     * ![](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAAAAAAALAAAAAABAAEAAAICRAEAOw==) [Viral Patel](http://viralpatel.net/) says:

18 May, 2013, 16:37  

@Ravi: Follow these steps to configure maven plugin in eclipse: [http://stackoverflow.com/a/8722910/113418](https://stackoverflow.com/a/8722910/113418)

Reply

     * ![](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAAAAAAALAAAAAABAAEAAAICRAEAOw==) subhashis says:

12 November, 2014, 19:10  

In eclipse go to

help -> eclipse marketplace -> search for m2e and install it

Reply

  13. ![](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAAAAAAALAAAAAABAAEAAAICRAEAOw==) kuldip soni says:

10 July, 2013, 17:32  

Hi Viral,

My functionality is when i click on link of my application page, it will open xml in another window.

i want to hide or change url of that window, how can i achive using above interceptor ?

Please help

Thanks

Reply

  14. ![](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAAAAAAALAAAAAABAAEAAAICRAEAOw==) Mounika says:

5 September, 2013, 19:50  

Can you please tell me the real time applications where we will use interceptors most..? What is use of pre handling, or post handling the requests. Please Explain me with any real time scenarios. Thanks in advance.

Reply

     * ![](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAAAAAAALAAAAAABAAEAAAICRAEAOw==) Michael C. says:

7 September, 2013, 4:38  

I can tell you what I use a HandlerInterceptor for. In my application, which is an e-commerce engine, I use a HandlerInterceptor to resolve certain things that all controllers will need to have at their disposal before they can render a response. I initialize certain things like the particular store they’re accessing, the user’s shopping cart, navigation UI, robots rules, client timezone, etc. If I didn’t do those things inside an interceptor, then I would have to do repeat all of those initializations inside of each controller method, which would make my code a lot more redundant and less readable. Whatever you find yourself repeating a lot in controller methods can be factored out and handled inside an interceptor. I hope that gives you some more insight.

Reply

     * ![](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAAAAAAALAAAAAABAAEAAAICRAEAOw==) raju says:

29 November, 2013, 19:57  

Hi,

These ‘interceptors’ are useful to validate requests from client.  
For Eg:  
It is useful to avoid spam requests By Validating the request according to Your app Requirements(You allow the request to Process Furthur only it has perticuls credentials).  
And you can Provide Secirity by Restricting the invalid requests to access the resources of your App.

Thanks & Regards  
raju.

Reply

     * ![](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAAAAAAALAAAAAABAAEAAAICRAEAOw==) krishna says:

4 July, 2014, 21:49  

we will interceptors used for setMaxAgeForSession, checkIfRequestIsAllowedWithoutLogIn some other purposes…

Reply

  15. ![](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAAAAAAALAAAAAABAAEAAAICRAEAOw==) Michael C. says:

7 September, 2013, 4:33  

Do you know of a way to intercept requests BEFORE a handler has been chosen? The reason I want to know is because some parts of my application have dynamic URLs (neither in XML nor in @RequestMapping annotations) that are stored in a database and updated via a web front-end. As such, static URL-to-controller mappings won’t work in my case (think of an app like a CMS where end users can choose their own URL for a particular page). Any ideas?

Reply

     * ![](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAAAAAAALAAAAAABAAEAAAICRAEAOw==) Micky says:

9 January, 2014, 22:35  

If you don’t know the complete URL then ServletFilters are way to go these work similar to interceptors this can be used on any java based web application.

Read more at [http://docs.oracle.com/cd/B14099_19/web.1012/b14017/filters.htm](https://docs.oracle.com/cd/B14099_19/web.1012/b14017/filters.htm)

Reply

  16. ![](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAAAAAAALAAAAAABAAEAAAICRAEAOw==) [Joseph](http://evonsdesigns.com/) says:

25 September, 2013, 20:21  

Great tutorial! Really simple and easy to follow. Thanks!! Using this to put a CorsFilter in.

Reply

  17. ![](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAAAAAAALAAAAAABAAEAAAICRAEAOw==) srinu says:

18 November, 2013, 12:47  

i have an error above code:

HTTP Status 500 – An exception occurred processing JSP page /index.jsp at line 1  
Stacktrace:  
org.apache.jasper.servlet.JspServletWrapper.handleJspException(JspServletWrapper.java:568)  
org.apache.jasper.servlet.JspServletWrapper.service(JspServletWrapper.java:455)  
org.apache.jasper.servlet.JspServlet.serviceJspFile(JspServlet.java:390)  
org.apache.jasper.servlet.JspServlet.service(JspServlet.java:334)  
javax.servlet.http.HttpServlet.service(HttpServlet.java:728)

Reply

     * ![](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAAAAAAALAAAAAABAAEAAAICRAEAOw==) isssss says:

19 November, 2013, 16:02  

write ur jsp code here,error in line1 of ur jsp, you hv written smthig that is nt accepted

Reply

  18. ![](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAAAAAAALAAAAAABAAEAAAICRAEAOw==) srinu says:

18 November, 2013, 12:48  

any one is help 2 me above http status…

Reply

  19. ![](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAAAAAAALAAAAAABAAEAAAICRAEAOw==) Mahendra says:

4 December, 2013, 9:37  

Any tell me how to close a session when browser tab closeed i am usin Spring ,Jsf 1.8 Icefaces

Reply

  20. ![](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAAAAAAALAAAAAABAAEAAAICRAEAOw==) naresh says:

8 January, 2014, 0:02  

hi patel

Great tutorial! Really simple and easy to follow. Thanks!!  
i need gosu technology sample project with source code  
please send me viralpatel very urjent …..

Reply

  21. ![](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAAAAAAALAAAAAABAAEAAAICRAEAOw==) Green says:

25 March, 2014, 16:14  

What if I want to inject interceptor logic for a certain method on a certain controller? Is there an easy to to achieve that? Literally I am looking for something like @Before or @After annotation in PlayFramework (see [http://www.playframework.com/documentation/1.2/controllers#interceptions](https://www.playframework.com/documentation/1.2/controllers#interceptions)) in spring

Reply

  22. ![](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAAAAAAALAAAAAABAAEAAAICRAEAOw==) Knight says:

15 April, 2014, 14:57  

Hi,

Really nice tutorial. I understood the whole concept. I only dont understand where have we linked the interceptor to handler. I mean how does the framework know that the HelloWorldInterceptor is to be called for request to HelloWorldController controller

Reply

  23. ![](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAAAAAAALAAAAAABAAEAAAICRAEAOw==) Seetesh says:

11 July, 2014, 14:22  

This example doesnt work on JBoss 7.1.1

Reply

  24. ![](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAAAAAAALAAAAAABAAEAAAICRAEAOw==) Seetesh says:

11 July, 2014, 14:58  

Example doesnt work on Jboss.

This line gives error

xmlns:mvc=”http://www.springframework.org/schema/mvc”

Reply

  25. ![](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAAAAAAALAAAAAABAAEAAAICRAEAOw==) Rajesh says:

18 February, 2015, 11:22  

Nice article Viral.  
Sometime back I implemented a timestamp ‘Filter’ which would take start timestamp when user enters the filter and another end timestamp just before returning the response. Since these timestamps were in the same method, I calculated the time taken to complete the request and was able to log it to file along with the request parameter.

How can I achieve it using interceptors ? (Since pre and post are separate methods, the local variable values are lost). I am relatively new to Spring so if there’s another way ..please point me to it.  
Regards, Rajesh

Reply

  26. ![](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAAAAAAALAAAAAABAAEAAAICRAEAOw==) [c.chandramohan](http://viralpatel.net/spring-3-mvc-create-hello-world-application-spring-3-mvc/) says:

10 May, 2016, 17:51  

hi viral,  
The spring helloworld example code demo is very useful to me.  
Thank you friend…

Reply

  27. ![](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAAAAAAALAAAAAABAAEAAAICRAEAOw==) Geet says:

18 July, 2016, 18:37  

where can i get pom file for this

Reply

  28. ![](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAAAAAAALAAAAAABAAEAAAICRAEAOw==) Clayton says:

22 December, 2016, 3:37  

Is it possible to use a parameter sent by an ajax post inside the preHandle method?

Reply

  29. ![](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAAAAAAALAAAAAABAAEAAAICRAEAOw==) Saurabh Kapoor says:

11 March, 2017, 10:10  

Nice tutorial, though by just using Sysout doesn’t solve problems. You could have included usage of Handler / ModelAndView during postHandle etc. Without those, this is mere the most basic one

Reply




### Leave a Reply Cancel reply

Required fields are marked 

Comment

Name *

Email *

Website

Save my name, email, and website in this browser for the next time I comment.

Follow:

  * [__](https://twitter.com/viralpatelnet "Twitter")
  * [__](https://github.com/viralpatel "Github")
  * [__](https://viralpatel.net/feed "RSS")


  
  


  
  


ViralPatel.net © 2022. All Rights Reserved.

  * [__](https://twitter.com/viralpatelnet "Twitter")
  * [__](https://github.com/viralpatel "Github")
  * [__](https://viralpatel.net/feed "RSS")


![](data:,)
