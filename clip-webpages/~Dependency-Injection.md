---
title: "Dependency-Injection"
created: 2025-03-16T22:14:31
modified: 2025-03-16T22:27:51
description: "This tutorial series explains the basics of dependency injection."
source: "https://jenkov.com/tutorials/dependency-injection/index.html"
tags:
tags-link:
type: "archive-web"
---

Dependency Injection (DI) has been a hot topic since 2007-2008. Lots have already been said and written about depencency injection, yet I feel there is more to say. This trail will explain and explore dependency injection and related concepts. Below is a list of the topics covered in this trail. The list is repeated at the top right of every page in this trail.

自 2007-2008 年以来，依赖注入 (DI) 一直是一个热门话题。关于依赖注入，已经有很多讨论和写作，但我觉得还有更多要说的。本篇将解释和探索依赖注入和相关概念。以下是本篇涵盖的主题列表。本篇的每一页右上角都重复了该列表。

Dependency injection is an expression coined in Martin Fowler's article [Inversion of Control Containers and the Dependency Injection Pattern](http://www.martinfowler.com/articles/injection.html). This is an nice article, but it misses some of the benefits of dependency injection containers. Therefore I also disagree with the articles conclusion, but more on that in a different text.

依赖注入是 Martin Fowler 在他的文章中提出的一个术语 [控制反转容器和依赖注入模式](http://www.martinfowler.com/articles/injection.html) 。这是一篇不错的文章，但它忽略了依赖注入容器的一些好处。因此，我也不同意这篇文章的结论，但我会在其他文章中对此进行更详细的讨论。

## Dependency Injection Tutorial Video

依赖注入教程视频

![](https://www.youtube.com/watch?v=Hm2fTv9wikI)

## Dependency Injection Explained 依赖注入解释

Dependency injection is a style of object configuration in which an objects fields and collaborators are set by an external entity. In other words objects are configured by an external entity. Dependency injection is an alternative to having the object configure itself. This may sound a bit abstract so let's look at a simple example:

依赖注入是一种对象配置方式，其中对象字段和协作者由外部实体设置。换句话说，对象由外部实体配置。依赖注入是对象自行配置的替代方法。这听起来可能有点抽象，让我们看一个简单的例子：

```
  public class MyDao {

    protected DataSource dataSource =
    new DataSourceImpl("driver", "url", "user", "password");

    //data access methods...
    public Person readPerson(int primaryKey) {...}

  }
```

This DAO (Data Access Object) class, MyDao, needs a javax.sql.DataSource instance in order to obtain database connections. The database connections are used to read from and write data to the database, for instance Person objects.

这个 DAO（数据访问对象）类 MyDao 需要一个 javax.sql.DataSource 实例来获取数据库连接。数据库连接用于从数据库读取数据和向数据库写入数据，例如 Person 对象。

Notice how the MyDao class instantiates a DataSourceImpl instance as its needed DataSource. The fact that the MyDao class needs a DataSource implemenation means that it "depends" on it. It cannot carry out its work without a DataSource implementation. Therefore, MyDao has a "dependency" on the DataSource interface and on some implementation of it.

注意 MyDao 类如何实例化 DataSourceImpl 实例作为其所需的 DataSource。MyDao 类需要 DataSource 实现这一事实意味着它“依赖”它。没有 DataSource 实现，它就无法开展工作。因此，MyDao 对 DataSource 接口及其某些实现具有“依赖性”。

The MyDao class itself instantiates a DataSourceImpl as its DataSource implementation. Therefore the MyDao class is said to "satisfy its own dependencies". When a class satisfies its own dependencies it automatically also depends on the classes it satisfies the dependencies with. In this case MyDao now also depends on DataSourceImpl, and on the four hardcoded string values passed as parameter to the DataSourceImpl constructor. You cannot use a different value for the four strings, nor use a different implementation of the DataSource interface, without changing the code.

MyDao 类本身实例化 DataSourceImpl 作为其 DataSource 实现。因此，MyDao 类被称为“满足其自身的依赖项”。当一个类满足其自身的依赖项时，它会自动依赖于它所满足依赖项的类。在这种情况下，MyDao 现在还依赖于 DataSourceImpl，以及作为参数传递给 DataSourceImpl 构造函数的四个硬编码字符串值。如果不更改代码，您不能对这四个字符串使用不同的值，也不能使用 DataSource 接口的不同实现。

==As you can see, when a class satisfies its own dependencies it becomes inflexible with regards to these dependencies. This is bad.== This means, that if you need to change the dependencies you will have to change the code. In this example, if you need to use a different database, you will need to change the MyDao class. If you have many DAO classes implemented like this you will need to change them all. In addition, you cannot unit test the MyDao class using a mock DataSource implementation. You can only use the DataSourceImpl. It doesn't take much brains to figure out that this is a bad idea.

如您所见，当一个类满足其自身的依赖关系时，它对这些依赖关系就变得不灵活。这很糟糕。这意味着，如果您需要更改依赖关系，则必须更改代码。在此示例中，如果您需要使用不同的数据库，则需要更改 MyDao 类。如果您有许多像这样实现的 DAO 类，则需要更改它们全部。此外，您无法使用模拟 DataSource 实现对 MyDao 类进行单元测试。您只能使用 DataSourceImpl。不难看出这是一个坏主意。

Let's change the design a little:

让我们稍微改变一下设计：

```
public class MyDao {

  protected DataSource dataSource = null;

  public MyDao(String driver, String url, String user, String password){
    this.dataSource = new DataSourceImpl(driver, url, user, password);
  }

  //data access methods...
  public Person readPerson(int primaryKey) {...}

}
```

Notice how the DataSourceImpl instantiation is moved into a constructor. The constructor takes four parameters which are the four values needed by the DataSourceImpl. Though the MyDao class still depends on these four values, it no longer satisfies these dependencies itself. They are provided by whatever class creating a MyDao instance. ==The values are said to be "injected" into the MyDao constructor. Hence the term "dependency injection"==. It is now possible to change the database driver, url, user name and password used by the MyDao class, without changing the MyDao class.

注意 DataSourceImpl 实例化是如何移到构造函数中的。构造函数采用四个参数，即 DataSourceImpl 所需的四个值。尽管 MyDao 类仍然依赖这四个值，但它本身不再满足这些依赖关系。它们由创建 MyDao 实例的任何类提供。这些值被称为“注入”到 MyDao 构造函数中。因此有“依赖注入”一词。现在可以更改 MyDao 类使用的数据库驱动程序、url、用户名和密码，而无需更改 MyDao 类。

Dependency injection is not restricted to constructors. You can also inject dependencies using setter methods, or directly into public fields.

依赖注入并不局限于构造函数。您还可以使用 setter 方法或直接将依赖项注入公共字段。

The MyDao class can still be made more independent. It still depends on both the DataSource interface and the DataSourceImpl class. There is no need for it to depend on more than the DataSource interface. This can be achieved by injecting a DataSource into the constructor instead of the four string parameters. Here is how that looks:

MyDao 类仍然可以变得更加独立。它仍然依赖于 DataSource 接口和 DataSourceImpl 类。它不需要依赖 DataSource 接口以外的其他接口。这可以通过将 DataSource 注入构造函数而不是四个字符串参数来实现。如下所示：

```
  public class MyDao {

    protected DataSource dataSource = null;
    
    public MyDao(DataSource dataSource){
      this.dataSource = dataSource;
    }

    
    //data access methods...
    public Person readPerson(int primaryKey) {...}

  }
```

Now the MyDao class no longer depends on the DataSourceImpl class, or the four strings needed by the DataSourceImpl constructor. You can now inject any DataSource implementation into the MyDao constructor.

现在 MyDao 类不再依赖于 DataSourceImpl 类，也不再依赖于 DataSourceImpl 构造函数所需的四个字符串。现在您可以将任何 DataSource 实现注入到 MyDao 构造函数中。

## Dependency Injection Chaining 依赖注入链

The example in the previous section is a bit simplified, and doesn't do dependency injection full justice. You may argue that the dependency is now moved from the MyDao class to each client using the MyDao class. Clients now have to know about some DataSource implementation to be able to inject it into the MyDao constructor. Here is an example:

上一节中的示例有些简化，并没有完全体现依赖注入的本质。您可能会认为依赖项现在已从 MyDao 类移至每个使用 MyDao 类的客户端。客户端现在必须了解一些 DataSource 实现，才能将其注入 MyDao 构造函数中。以下是示例：

```
  public class MyBizComponent{

    public void changePersonStatus(Person person, String status){

       MyDao dao = new MyDao(
            new DataSourceImpl("driver", "url", "user", "password"));

       Person person = dao.readPerson(person.getId());
       person.setStatus(status);
       dao.update(person);
    }

  }
```

As you can see the MyBizComponent now depends on the DataSourceImpl class and the four strings needed by its constructor. This is even worse than having the MyDao depend on them because the MyBizComponent now depends on classes and information that it isn't using itself. Furthermore the DataSourceImpl and constructor parameter belongs to a different abstraction layer. A layer below the MyBizComponent - the DAO layer.

如您所见，MyBizComponent 现在依赖于 DataSourceImpl 类及其构造函数所需的四个字符串。这比 MyDao 依赖它们更糟糕，因为 MyBizComponent 现在依赖于它自己不使用的类和信息。此外，DataSourceImpl 和构造函数参数属于不同的抽象层。MyBizComponent 下面的一层 - DAO 层。

The solution is to continue the dependency injection all the way up through the layers. The MyBizComponent should only depend on a MyDao instance. Here is how that looks:

解决方案是继续将依赖注入贯穿到各个层。MyBizComponent 应该只依赖于 MyDao 实例。如下所示：

```
public class MyBizComponent{

    protected MyDao dao = null;

    public MyBizComponent(MyDao dao){
       this.dao = dao;
    }
    

    public void changePersonStatus(Person person, String status){
       Person person = dao.readPerson(person.getId());
       person.setStatus(status);
       dao.update(person);
    }

  }
```

Again the dependency, MyDao, is injected into the class via the constructor. Now the MyBizComponent only depends on the MyDao class. If MyDao was an interface you could even switch implementation without the MyBizComponent knowing about it.

再次，依赖项 MyDao 通过构造函数注入到类中。现在 MyBizComponent 仅依赖于 MyDao 类。如果 MyDao 是一个接口，您甚至可以在 MyBizComponent 不知情的情况下切换实现。

This dependency injection pattern is continued all the way up the layers of your application, from the lowest data accessing layers up to the user interface (if any).

这种依赖注入模式一直延续到应用程序的各个层，从最低的数据访问层一直到用户界面（如果有）。
