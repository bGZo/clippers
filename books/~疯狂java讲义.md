---
cover: https://img3.doubanio.com/view/subject/s/public/s27273703.jpg
author: 李刚
created: 2022-11-25T00:00:00
isbn: 9787121155789
lang: chinese
published: 20120101
rating: ⭐⭐⭐
status: book/done
tags: java, deprecated
type: book/dev
douban: https://book.douban.com/subject/10436048
weread: https://weread.qq.com/web/bookDetail/239324a05a6578239cd415d
modified: 2025-03-30T22:49:35
---

## Backgroud
  - [Java 从开始到放弃 求大佬推荐一本书 - V2EX](https://v2ex.com/t/714143)
  - [《On Java 8》中文版 | OnJava8](https://lingcoder.github.io/OnJava8/#/)
  - [java - What is the regex to extract all the emojis from a string? - Stack Overflow](https://stackoverflow.com/questions/24840667/what-is-the-regex-to-extract-all-the-emojis-from-a-string)
  - [IDE doesn't provide a code completion suggestion for the 'extends' keyword while I'm trying to create a class inside a local scope (method)](https://youtrack.jetbrains.com/issue/SCL-15854)

## Content
  - 如何学习 Java
  - 前言
  - 第 1 章 Java 语言概述
    - 1.1 Java 语言的发展简史
    - 1.2 Java 的竞争对手及各自优势
    - 1.3 Java 程序运行机制
    - 1.4 开发 Java 的准备
    - 1.5 第一个 Java 程序
    - 1.6 Java 程序的基本规则
    - 1.7 垃圾回收机制
    - 1.8 何时开始使用 IDE 工具
    - 1.9 本章小结
  - 第 2 章 理解面向对象
    - 2.1 面向对象
    - 2.2 UML（统一建模语言）介绍
    - 2.3 Java 的面向对象特征
    - 2.4 本章小结
  - 第 3 章 数据类型和运算符
    - 3.1 注释
    - 3.2 标识符和关键字
    - 3.3 数据类型分类
    - 3.4 基本数据类型
    - 3.5 基本类型的类型转换
    - 3.6 直接量
    - 3.7 运算符
    - [ ] #gtd/todo 3.8 本章小结
        - 1.定义学生、老师、教室 3 个类，为 3 个类编写文档注释，并使用 javadoc 工具来生成 API 文档。
      - 2.通过 API 文档查询 Math 类的方法，打印出如下所示的近似圆，只要给定不同半径，圆的大小随之发生改变（如果需要使用复杂的数学运算，可以查阅 Math 类的方法或者参考 7.3 节的内容）
  - 第 4 章 流程控制与数组
    - 4.1 顺序结构
    - 4.2 分支结构
    - 4.3 循环结构
    - 4.4 控制循环结构
    - 4.5 数组类型
    - 4.6 深入数组
    - [ ] #gtd/todo 4.7 本章小结
        - 1.实现一个按字节来截取字符串的子串的方法，功能类似于 String 类的 substring() 方法，String 类是按字符截取的，例如 " 中国 abc".substring(1,3)，将返回 " 国 a"。这里要求按字节截取，一个英文字符当一字节，一个中文字符当两字节。
      - 2.编写一个程序，将浮点数转换成人民币读法字符串，例如，将 1006.333 转换为壹千零陆元叁角叁分。
      - 3.编写控制台的五子棋游戏。
  - 第 5 章 面向对象（上）
    - 5.1 类和对象
    - 5.2 方法详解
    - 5.3 成员变量和局部变量
    - 5.4 隐藏和封装
    - 5.5 深入构造器
    - 5.6 类的继承
    - 5.7 多态
    - 5.8 继承与组合
    - 5.9 初始化块
      id: 63e72783-9c4d-4975-8316-8eefaa9e9f64
      - 初始化块的语法格式如下

```java
          [修饰符] { // 修饰符只能是static (静态初始化块)
            //   始化块的可执行性代码
            ...
          }
```

          - e.g.

```java
            public class Person{
              //定义一个初始化块
              {
                int a=6;
                //在初始化块中
                if (a > 4){
                  System.out.println("Person初始化块：局部变量a的值大于4");
                }
                System.out.println("Person的第 1 个初始化块");
              }
              //定义第二个初始化块
              {
                System.out.println("Person的第 2 个初始化块");
              }
              //定义无参数的构造器
              public Person(){
                System.out.println("Person类的无参数构造器");
              }
              public static void main(String[] args){
                new Person();
              }
            }
```

            Run

```
            Person初始化块：局部变量a的值大于4
            Person的初始化块
            Person的第二个初始化块
            Person类的无参数构造器
```

      - 初始化块 #vs 构造器
        - **初始化块**的形式 (2)
          - 普通初始化块
            id: 63807c3f-cff0-4935-a3d7-a580e537b24a
          - 静态初始化块 / 类初始化块
            id: 638089b8-87e7-45e1-bcfb-bdfe8cd70efc
            - **执行顺序**: ((638089b8-87e7-45e1-bcfb-bdfe8cd70efc)) > ((63807c3f-cff0-4935-a3d7-a580e537b24a))

```java
                class Root{
                  static{
                    System.out.println("Root的静态初始化块");
                  }
                  {
                    System.out.println("Root的普通初始化块");
                  }
                  public Root(){
                    System.out.println("Root的无参数的构造器");
                  }
                }
                class Mid extends Root{
                    static{
                            System.out.println("Mid的静态初始化块");
                    }
                    {
                            System.out.println("Mid的普通初始化块");
                    }
                    public Mid(){
                            System.out.println("Mid的无参数的构造器");
                    }
                    public Mid(String msg){
                            //通过this调用同一类中重载的构造器
                            this();
                            System.out.println("Mid的带参数构造器，其参数值："
                                + msg);
                    }
                }
                class Leaf extends Mid{
                    static{
                            System.out.println("Leaf的静态初始化块");
                    }
                    {
                            System.out.println("Leaf的普通初始化块");
                    }
                    public Leaf(){
                            //通过super调用父类中有一个字符串参数的构造器
                            super("疯狂Java讲义");
                            System.out.println("执行Leaf的构造器");
                    }
                }
                public class Test{
                  public static void main(String[] args){
                    new Leaf();
                    new Leaf();
                  }
                }
```

                Run

```
                Root的静态初始化块
                Mid的静态初始化块
                Leaf的静态初始化块
                Root的普通初始化块
                Root的无参数的构造器
                Mid的普通初始化块
                Mid的无参数的构造器
                Mid的带参数构造器，其参数值：疯狂Java讲义
                Leaf的普通初始化块
                执行Leaf的构造器
                Root的普通初始化块
                Root的无参数的构造器
                Mid的普通初始化块
                Mid的无参数的构造器
                Mid的带参数构造器，其参数值：疯狂Java讲义
                Leaf的普通初始化块
                执行Leaf的构造器
```

                #weird-code
                - ==系统将在类初始化阶段执行静态初始化块, 而不是在创建对象时才执行, 并且如结果所示, 只会执行一次==
                - 静态初始化只会在初始化类的时候运行, 所以第二次创建 `Leaf()` 的时候没有了前三行
            - 静态初始化块不能访问非静态成员, 包括不能访问实例Field和实例方法
        - 初始化块 是 构造器的补充
          - **执行顺序** == 源程序中的**排列顺序**, 一般 初始化 先于 构造器

```java
            public class InstanceInitTest{
              {
                a = 6; //先执行初始化块将a Field赋值为6
                b = 6;
              }
              int a=9; //再执行将 a Field赋值为9
              int b;
              public static void main(String[] args){
                System.out.println(new InstanceInitTest().a);
                System.out.println(new InstanceInitTest().b);
              }
            }
```

            Run

```
            9
            6
```

            #weird-code
            - 当Java创建一个对象时，**系统先为该对象的所有实例Field分配内存**（前提是该类已经被加载过了），接着程序开始对这些实例变量执行初始化，其初始化顺序是：先执行初始化块或声明Field时指定的初始值，再执行构造器里指定的初始值。
              - ==这里的意思是: 先扫一遍变量, 分配内存, 然后赋值则从上而下来, 变量 `a` 在静态块的值为`6`, 却被后面非静态块的赋值给覆盖掉了==
        - 形式上, 初始化块 不能接收任何参数
          - 如果有一段初始化处理代码对所有对象完全相同，且无须接收任何参数，就可以把这段初始化处理代码提取到初始化块中
        - 创建一个Java对象时
          - 初始化块与构造器类似，**不仅会执行该类的普通初始化块和构造器**，而且**系统会一直上溯到 `java.lang.Object` 类**，先执行 `java.lang.Object` 类的初始化块，开始执行 `java.lang.Object` 的构造器，依次向下执行其父类的初始化块，开始执行其父类的构造器……最后才执行该类的初始化块和构造器，返回该类的对象
    - 5.10 本章小结
      - 1.定义普通人、老师、班主任、学生、学校，提供适当的Field、方法用于描述其内部数据和行为方式，并提供主类使之运行。要求有良好的封装性，将不同类放在不同的包下面，增加文档注释，生成API文档
      - 2.改写第1题的程序，利用组合来实现类复用。
  - 第 6 章 面向对象（下）
    - 6.1 Java 7 增强的包装类 (Wrapper Class)
      - 原因
        - 8 种基本数据类型不支持面向对象的编程机制，也不具备“对象”的特性
          (没有 Field、方法可以被调用)
          - Java 之所以提供这 8 种基本数据类型，主要是为了照顾程序员传统的习惯
      - 局限
        - 所有引用类型的变量都继承了 Object 类，都可当成 Object 类型变量使用。==但基本数据类型的变量就不可以，如果有个方法需要 Object 类型的参数，但实际需要的值却是 2、3 等数值，这可能就比较难以处理==
      - 转换 & 基本类型变量
        - ![image.png](../assets/book/疯狂Java讲义/image_1669431134278_0.png)
      - 转换 & 字符串
        - ![image.png](../assets/book/疯狂Java讲义/image_1669431783672_0.png)
        - 利用包装类提供的 `parseXxx(String s)` 静态方法
          (除了 Character 之外的所有包装类都提供了该方法)
        - 利用包装类提供的 `Xxx(String s)` 构造器

```java
            public class Primitive2String{
              public static void main(String[] args){
                String intStr="123";
                //把一个特定字符串转换成int变量
                int it1=Integer.parseInt(intStr);
                int it2=new Integer(intStr);
                System.out.println(it2);
                String floatStr="4.56";
                //把一个特定字符串转换成float变量
                float ft1=Float.parseFloat(floatStr);
                float ft2=new Float(floatStr);
                System.out.println(ft2);
                //把一个float变量转换成String变量
                String ftStr=String.valueOf(2.345f);
                System.out.println(ftStr);
                //把一个double变量转换成String变量
                String dbStr=String.valueOf(3.344);
                System.out.println(dbStr);
                //把一个boolean变量转换成String变量
                String boolStr=String.valueOf(true);
                System.out.println(boolStr.toUpperCase());
              }
            }
```

      - Compare
        - & **数值类型**的值

```java
            Integer a=new Integer(6);
            System.out.println("6的包装类实例是否大于5.0" + (a > 5.0));
```

            Run

```
            true
```

        - & 包装类的实例

```java
            System.out.println("比较2个包装类的实例是否相等："
                               + (new Integer(2)==new Integer(2)));
```

            Run

```
            false
```

            #weird-code
            - ==只有两个包装类引用指向同一个对象时才会返回true==
        - & 自动装箱 边界超限

```java
            //通过自动装箱，允许把基本类型值赋值给包装类实例
            Integer ina=2;
            Integer inb=2;
            //输出true
            System.out.println("两个2自动装箱后是否相等：" + (ina==inb));
            Integer biga=128;
            Integer bigb=128;
            //输出false
            System.out.println("两个128自动装箱后是否相等：" + (biga==bigb));
```

            Run

```
            两个2自动装箱后是否相等：true
            两个128自动装箱后是否相等：false
```

            #weird-code
            - 查看Java系统中java.lang.Integer类的源代码，如下所示

```java
              //定义一个长度为256的Integer数组
              static final Integer[] cache=new Integer[-(-128) + 127 + 1];
              static {
                //执行初始化，创建-128到127的Integer实例，并放入cache数组中
                for(int i=0; i < cache.length; i++)
                  cache[i]=new Integer(i - 128);
              }
```

              - ==系统把一个 -128～127 之间的整数自动装箱成 Integer 实例，并放入了一个名为 cache 的数组中缓存起来。如果以后把一个 -128～127 之间的整数自动装箱成一个 Integer 实例时，实际上是直接指向对应的数组元素，因此 -128～127 之间的同一个整数自动装箱成 Integer 实例时，永远都是引用cache数组的同一个数组元素，所以它们全部相等；但每次把一个不在-128～127范围内的整数自动装箱成 Integer 实例时，系统总是重新创建一个 Integer 实例，所以出现程序中的运行结果==
              - But why?
                - **Java也把一些创建成本大、需要频繁使用的对象缓存起来，从而提高程序的运行性能**
        - Java 7为所有的包装类都提供了一个静态的 `compare(xxx val1, xxx val2)` 方法，这样开发者就可以通过包装类提供的 `compare(xxx val1, xxx val2)` 方法来比较两个基本类型值的大小
    - 6.2 处理对象
      - `toString` 方法
        - 一个“自我描述”方法
        - 该方法通常用于实现这样一个功能
          - 当程序员直接打印该对象时，系统将会输出该对象的“自我描述”信息，用以告诉外界该对象具有的状态信息。
      - `==` & `equals`
        - `"hello"` #vs `new String("hello")`
          - 当Java程序直接使用形如"hello"的字符串直接量（包括可以在编译时就计算出来的字符串值）时，JVM将会使用 **常量池(constant pool)** 来管理这些字符串
            - **常量池(constant pool)**
              - ==管理在编译期被确定并被保存在已编译的.class文件中的一些数据==。它包括了关于类、方法、接口中的常量，还包括字符串常量
          - 当使用new String("hello")时，JVM会先使用常量池来管理"hello"直接量，再调用String类的构造器来创建一个新的String对象，新创建的String对象被保存在堆内存中
            - ==换句话说，new String("hello")一共产生了两个对象("常量池+堆")==

```JAVA
            public class StringCompareTest{
              public static void main(String[] args){
                //s1直接引用常量池中的"疯狂Java"
                String s1="疯狂Java";
                String s2="疯狂";
                String s3="Java";
                //s4后面的字符串值可以在编译期就确定下来
                //s4直接引用常量池中的"疯狂Java"
                String s4="疯狂" + "Java";
                //s5后面的字符串值可以在编译期就确定下来
                //s5直接引用常量池中的"疯狂Java"
                String s5="疯" + "狂" + "Java";
                //s6后面的字符串值不能在编译期就确定下来
                //不能引用常量池中的字符串
                String s6=s2 + s3;
                //使用new调用构造器将会创建一个新的String对象
                //s7引用堆内存中新创建的String对象
                String s7=new String("疯狂Java");
                //输出true
                System.out.println(s1==s4);
                //输出true
                System.out.println(s1==s5);
                //输出false
                System.out.println(s1==s6);
                //输出false
                System.out.println(s1==s7);
              }
            }
```

        - Object 默认提供的 equals()只是比较对象的地址
          - 即 Object类的equals方法比较的结果与==运算符比较的结果完全相同
          - 通常而言，正确地重写 `equals`方法 应该满足下列条件
            - 自反性
              - 对任意x，x.equals(x)一定返回true
            - 对称性
              - 对任意x和y，如果y.equals(x)返回true，则x.equals(y)也返回true。
            - 传递性
              - 对任意x, y, z，如果x.equals(y)返回ture，y.equals(z)返回true，则x.equals(z)一定返回true。
            - 一致性
              - 对任意x和y，如果对象中用于等价比较的信息没有改变，那么无论调用x.equals(y)多少次，返回的结果应该保持一致，要么一直是true，要么一直是false。
            - 对任何不是 null 的 x，x.equals(null) 一定返回 false。

```java
            class Person{
              private String name;
              private String idStr;
              public Person(){}
              public Person(String name , String idStr){
                this.name=name;
                this.idStr=idStr;
              }
              //此处省略name和idStr的setter和getter方法
              //重写equals方法，提供自定义的相等标准
              public boolean equals(Object obj){
                // 如果两个对象为同一个对象
                if (this==obj)
                  return true;
                //当obj不为null，且它是Person类的实例时
                if (obj !=null && obj.getClass()==Person.class){
                  Person personObj=(Person)obj;
                  //并且当前对象的idStr与obj对象的idStr相等才可判断两个对象相等
                  if (this.getIdStr().equals(personObj.getIdStr())){
                    return true;
                  }
                }
                return false;
              }
            }
            public class OverrideEqualsRight{
              public static void main(String[] args){
                Person p1=new Person("孙悟空" , "12343433433");
                Person p2=new Person("孙行者" , "12343433433");
                Person p3=new Person("孙悟饭" , "99933433");
                //p1和p2的idStr相等，所以输出true
                System.out.println("p1和p2是否相等？"
                                   + p1.equals(p2));
                //p2和p3的idStr不相等，所以输出false
                System.out.println("p2和p3是否相等？"
                                   + p2.equals(p3));
              }
            }
```

            - 判断obj是否为Person类的实例时，为何不用obj instanceof Person来判断呢？
              - 对于 `instanceof` 运算符而言，当前面对象是后面类的实例或其子类的实例时都将返回true，所以实际上重写 `equals()方法` 判断两个对象是否为同一个类的实例时使用instanceof是有问题的。
                - 比如有一个Teacher类型的变量 t，如果判断 `t instanceof Person`，这也将返回 `true`
                  - 但对于重写equals()方法的要求而言，通常要求两个对象是同一个类的实例，因此使用 `instanceof` 运算符不太合适。
                  - 改为使用 `t.getClass()==Person.class` 比较合适。这行代码用到了反射基础，读者可参考第18章来理解此行代码
    - 6.3 类成员
      description: "static关键字修饰的成员就是类成员, 类成员属于整个类，不属于单个实例"
      - 理解类成员
        - Java 成员 (5)
          - Field
            - 当系统第一次准备使用该类时，系统会为该类Field分配内存空间，类Field开始生效，直到该类被卸载，该类的类Field所占有的内存才被系统的垃圾回收机制回收。类Field生存范围几乎等同于该类的生存范围。当类初始化完成后，类Field也被初始化完成
            - 类Field既可通过类来访问，也可通过类的对象来访问
              - ==当通过对象来访问类Field时，系统会在底层转换为通过该类来访问类Field==
                - c\# 不允许通过对象访问类Field，对象只能访问实例Field；类Field必须通过类来访问
            - 同一类的 **所有实例的类 Field 共享同一块内存区**
          - 方法
            - 类方法与类Field类似，**当使用实例来访问类成员时，实际上依然是委托给该类来访问类成员**，即使某个实例为null，它也可以访问它所属类的类成员
          - 构造器 (**static关键字不能修饰**)
          - 初始化块
            - 静态初始化块
          - 内部类（包括接口、枚举）
      - 单例 (Singleton) 类
    - 6.4 final修饰符
      - > 有的书上介绍说final修饰的变量不能被赋值，这种说法是错误的！
        严格的说法是，**final修饰的变量不可被改变**，一旦获得了初始值，该final变量的值就不能被重新赋值
      - final 成员变量
        - 不要在初始化之前就访问成员变量的值。例如下面程序将会引起错误
          - `java: variable age might not have been initialized`
      - final 局部变量
      - final修饰基本类型变量和引用类型变量的区别
        - 和 [[cpp]] 中 `const int *p` 和 `int* const p` 相类似
      - 可执行“宏替换”的final变量
        - final修饰符的一个重要用途就是定义“宏变量”。当定义final变量时就为该变量指定了初始值，而且该初始值可以在编译时就确定下来，那么这个final变量本质上就是一个“宏变量”，编译器会把程序中所有用到该变量的地方直接替换成该变量的值
          - 和 [[cpp]] 中的 `#mark: ` 类似

```java
            public class FinalLocalTest{
              public static void main(String[] args){
                //定义一个普通局部变量
                final int a=5;
                System.out.println(a);
              }
            }
```

            - ==变量a其实根本不存在==，当程序执行 `System.out.println(a)`;代码时，实际转换为执行 `System.out.println(5)`
      - final方法
      - final类
      - 不可变类
      - 缓存实例的不可变类
    - 6.5 抽象类
    - 6.6 更彻底的抽象：接口
    - 6.7 内部类
    - 6.8 枚举类
    - 6.9 对象与垃圾回收
    - 6.10 修饰符的适用范围
    - 6.11 使用JAR文件
    - [ ] #gtd/todo 6.12 本章小结
        - 定义一个类，该类用于封装一桌梭哈游戏，这个类应该包含桌上剩下的牌的信息，并包含5个玩家的状态信息：他们各自的位置、游戏状态（正在游戏或已放弃）、手上已有的牌等信息。如果有可能，这个类还应该实现发牌方法，这个方法需要控制从谁开始发牌，不要发牌给放弃的人，并修改桌上剩下的牌。
  - 第 7 章 与运行环境交互
    - 7.1 与用户互动
    - 7.2 系统相关
    - 7.3 常用类
    - 7.4 处理日期的类
    - 7.5 正则表达式
    - 7.6 国际化与格式化
    - [ ] #gtd/todo 7.7 本章小结
        - 1.改写第 4 章练习中的五子棋游戏，通过正则表达式保证用户输入必须合法
      - 2.改写第 8 章练习中的梭哈游戏，为该程序增加国际化功能，并使用正则表达式保证用户输入必须合法。
  - 第 8 章 Java 集合
    - 8.1 Java 集合概述
      - Collection 集合体系的继承树
        - ![image.png](../assets/book\疯狂Java讲义/image_1669792231200_0.png)
      - Map 体系的继承树
        - ![image.png](../assets/book\疯狂Java讲义/image_1669792360682_0.png)
      - 三种集合示意图
        - ![image.png](../assets/book\疯狂Java讲义/image_1669792469833_0.png)
      - 对于 Set、List、Queue 和 Map 四种集合，最常用的实现类在图中以灰色区域覆盖
        - HashSet
        - TreeSet
        - ArrayList
        - ArrayDeque
        - LinkedList 和 HashMap
        - TreeMap
    - 8.2 Collection 和 Iterator 接口
      - Collection 接口
        - APIs
          - boolean add(Object o)
            - 该方法用于向集合里添加一个元素。如果集合对象被添加操作改变了，则返回 true
          - boolean addAll(Collection c)
            - 该方法把集合 c 里的所有元素添加到指定集合里。如果集合对象被添加操作改变了，则返回 true
          - void clear()
            - 清除集合里的所有元素，将集合长度变为 0
          - boolean contains(Object o)
            - 返回集合里是否包含指定元素
          - boolean containsAll(Collection c)
            - 返回集合里是否包含集合 c 里的所有元素
          - boolean isEmpty()
            - 返回集合是否为空。当集合长度为 0 时返回 true，否则返回 false
          - Iterator iterator()
            - 返回一个 Iterator 对象，用于遍历集合里的元素
          - boolean remove(Object o)
            - 删除集合中的指定元素 o，当集合中包含了一个或多个元素 o 时，这些元素将被删除，该方法将返回 true
          - boolean removeAll(Collection c)
            - 从集合中删除集合 c 里包含的所有元素（相当于用调用该方法的集合减集合 c），如果删除了一个或一个以上的元素，则该方法返回 true
          - boolean retainAll(Collection c)
            - 从集合中删除集合 c 里不包含的元素（相当于把调用该方法的集合变成该集合和集合 c 的交集），如果该操作改变了调用该方法的集合，则该方法返回 true
          - int size()
            - 该方法返回集合里元素的个数
          - Object[] toArray()
            - 该方法把集合转换成一个数组，所有的集合元素变成对应的数组元素。
        - 在普通情况下，当我们把一个对象“丢进”集合中后，**集合会忘记这个对象的类型——也就是说，系统把所有的集合元素都当成 Object 类的实例进行处理**
          - 从 JDK 1.5 以后，这种状态得到了改进
            - 可以使用泛型来限制集合里元素的类型, 并让集合记住所有集合元素的类型
      - Iterator 接口
        - APIs
          - boolean hasNext()
            - 如果被迭代的集合元素还没有被遍历，则返回 true
          - Object next()
            - 返回集合里的下一个元素
          - void remove()
            - 删除集合里上一次 next 方法返回的元素。

```java
          public class IteratorTest{
            public static void main(String[] args){
              //创建一个集合
              Collection books=new HashSet();
              books.add("轻量级Java EE企业应用实战");
              books.add("疯狂Java讲义");
              books.add("疯狂Android讲义");
              //获取books集合对应的迭代器
              Iterator it=books.iterator();
              while(it.hasNext()){
                //it.next()方法返回的数据类型是Object类型
                //需要强制类型转换
                String book=(String)it.next();
                System.out.println(book);
                if (book.equals("疯狂Java讲义"))
                  //从集合中删除上一次next方法返回的元素
                  it.remove();
                //对book变量赋值，不会改变集合元素本身
                book="测试字符串";   //①
              }
              System.out.println(books);
            }
          }
```

          - **修改迭代变量的值对集合元素本身没有任何影响**
            - 当使用Iterator对集合元素进行迭代时，Iterator并不是把集合元素**本身**传给了迭代变量，而是**把集合元素的值传给了迭代变量**
        - 只有通过 Iterator 的remove方法删除上一次next方法返回的集合元素才可以
          - 否则将会引发java.util.Concurrent ModificationException异常

```java
            public class IteratorErrorTest{
              public static void main(String[] args){
                //创建一个集合
                Collection books=new HashSet();
                books.add("轻量级Java EE企业应用实战");
                books.add("疯狂Java讲义");
                books.add("疯狂Android讲义");
                //获取books集合对应的迭代器
                Iterator it=books.iterator();
                while(it.hasNext()){
                  String book=(String)it.next();
                  System.out.println(book);
                  if (book.equals("疯狂Android讲义")){
                    //使用Iterator迭代过程中，不可修改集合元素，下面代码引发异常
                    books.remove(book);
                  }
                }
              }
            }
```

            -              > 上面程序如果改为删除“疯狂Java讲义”字符串，则不会引发异常，这样可能有些读者会“心存侥幸”地想：在迭代时好像也可以删除集合元素啊

```java
                public class Test {
                  public static void main(String[] args) {
                    Collection books=new HashSet();
                    books.add("轻量级Java EE企业应用实战"); books.add("疯狂Java讲义");books.add("疯狂Java讲义2");books.add("疯狂Android讲义");
                    Iterator it=books.iterator();
                    while(it.hasNext()){
                      String book=(String)it.next();
                      if (book.equals("疯狂Java讲义")){
                        books.remove(book);
                      }
                    }
                    System.out.println(books);
                  }
                }
```

                #weird-code Why???
                - 在next方法中存在集合的修改校验方法，==**当remove最后一个参数时，hasNext方法返回为false，不会执行后面的next方法，所以删除最后一个元素时不会报错**==；ArrayList的hasNext在迭代完最后一个元素后会再进入一次循环，所以换成ArrayList即使是删除最后一个元素也会报错；单线程建议使用迭代器的remove方法
                  - ==并不是不能修改，使用foreach过程中要修改，只能使用迭代器中的remove去修改，**否则在源码内部表示修改次数的变量不会改变**，在检测（每次foreach都会检测，检测表示修改变量次数的变量）时候就会引发异常==
            - 实际上这是一种危险的行为：对于HashSet以及后面的ArrayList等，迭代时删除元素都会导致异常——**==只有在删除集合中的某个特定元素时才不会抛出异常，这是由集合类的实现代码决定的，程序员不应该这么做==**
        - Iterator迭代器 **快速失败 (fail-fast) 机制**
          - 一旦在迭代过程中检测到该集合已经被修改 (通常是程序中的其他线程修改)，程序立即引发ConcurrentModificationException异常，而不是显示修改后的结果，这样可以避免共享资源而引发的潜在问题
      - 使用 foreach 循环遍历集合元素
        - Java 5 提供的foreach循环迭代访问集合元素更加便捷

```java
          public class ForeachTest{
            public static void main(String[] args){
              //创建一个集合
              Collection books=new HashSet();
              books.add(new String("轻量级Java EE企业应用实战"));
              books.add(new String("疯狂Java讲义"));
              books.add(new String("疯狂Android讲义"));
              for (Object obj : books){
                //此处的book变量也不是集合元素本身
                String book=(String)obj;
                System.out.println(book);
                if (book.equals("疯狂Android讲义")){
                  //下面代码会引发ConcurrentModificationException异常
                  books.remove(book);    //①
                }
              }
              System.out.println(books);
            }
          }
```

        - **在foreach循环中修改迭代变量的值也没有任何实际意义**
          - foreach循环中的迭代变量也不是集合元素本身，系统只是依次把集合元素的值赋给迭代变量
        - **当使用foreach循环迭代访问集合元素时，该集合也不能被改变，**
          - 否则将引发Concurrent ModificationException异常
    - 8.3 Set集合
      - Set集合与Collection基本上完全一样，**它没有提供任何额外的方法**。实际上Set就是Collection，只是行为略有不同（Set不允许包含重复元素）
      - 如果试图把两个相同的元素加入同一个Set集合中，则添加操作失败，**add方法返回false**，且新元素不会被加入
      - Set判断两个对象相同不是使用==运算符，**而是根据equals方法**
        - **只要两个对象用equals方法比较返回false，Set就会接受这两个对象**
          - **极端的情况**, 甚至这两个对象是同一个对象，Set也可把它们当成两个对象处理

```java
          public class SetTest{
            public static void main(String[] args){
              Set books=new HashSet();
              //添加一个字符串对象
              books.add(new String("疯狂Java讲义"));
              //再次添加一个字符串对象
              //因为两个字符串对象通过equals方法比较相等
              //所以添加失败，返回false
              boolean result=books.add(new String("疯狂Java讲义"));
              //从下面输出看到集合只有一个元素
              System.out.println(result + "-->" + books);
            }
          }
```

      - HashSet实现类
        - Hash算法来存储集合中的元素，因此具有很好的**存取和查找性能**
        - HashSet具有以下特点
          - 不能保证元素的排列顺序，顺序有可能发生变化
          - 不是同步的
            - 如果多个线程同时访问一个HashSet，假设有两个或者两个以上线程同时修改了HashSet集合时，则必须通过代码来保证其同步
          - 集合元素值可以是null
        - 如果有两个元素通过equals()方法比较返回true，但**它们的hashCode()方法返回值不相等**，HashSet将会把它们存储在不同的位置，依然可以添加成功

```java
            //类A的equals()方法总是返回true，但没有重写其hashCode()方法
            class A{
              public boolean equals(Object obj){
                return true;
              }
            }
            //类B的hashCode()方法总是返回1，但没有重写其equals()方法
            class B{
              public int hashCode(){
                return 1;
              }
            }
            //类C的hashCode()方法总是返回2，且重写了其equals()方法
            class C{
              public int hashCode(){
                return 2;
              }
              public boolean equals(Object obj){
                return true;
              }
            }
            public class HashSetTest{
              public static void main(String[] args){
                HashSet books=new HashSet();
                //分别向books集合中添加两个A对象、两个B对象、两个C对象
                books.add(new A());
                books.add(new A());
                books.add(new B());
                books.add(new B());
                books.add(new C());
                books.add(new C());
                System.out.println(books);
              }
            }
```

            Run

```
            [B@1, B@1, C@2, A@5483cd, A@9931f5]
```

            - **如果两个对象通过equals()方法比较返回true，这两个对象的hashCode值也应该相同**
              - ==当把一个对象放入HashSet中时，如果需要重写该对象对应类的equals()方法，则也应该重写其hashCode()方法==
            - 甚至, 如果`hashCode()`相同, `equals()`不同将更麻烦, **同一地址拉链过多会性能下降**
          - 重写hashCode()方法
            - 基本规则
              - 在程序运行过程中，同一个对象多次调用hashCode()方法应该返回相同的值
              - 当两个对象通过equals()方法比较返回true时, 这两个对象的hashCode()方法应返回相等的值
              - 对象中用作equals()方法比较标准的Field, 都应该用来计算hashCode值
            - 一般规则
              -                1. 把对象内每个有意义的Field（即每个用做equals()方法比较标准的Field）计算出一个int类型的hashCode值。计算方式如表
                - ![image.png](../assets/book\疯狂Java讲义/image_1669793460334_0.png)
              - 用第1步计算出来的多个hashCode值组合计算出一个hashCode值返回

```java
                  return f1.hashCode() + (int)f2;
```

                  - 为了避免直接相加产生偶然相等（两个对象的f1、f2 Field并不相等，但它们的和恰好相等），可以通过为各Field乘以任意一个质数后再相加。例如如下

```java
                      return f1.hashCode() * 17+ (int)f2 * 13;
```

        - **当向HashSet中添加可变对象时，必须十分小心**
          - 如果修改HashSet集合中的对象，有可能导致该对象与集合中的其他对象相等，从而导致HashSet无法准确访问该对象

```java
            class R{
              int count;
              public R(int count){
                this.count=count;
              }
              public String toString(){
                return "R[count:" + count + "]";
              }
              public boolean equals(Object obj){
                if(this==obj)
                  return true;
                if (obj !=null && obj.getClass()==R.class){
                  R r=(R)obj;
                  if (r.count==this.count){
                    return true;
                  }
                }
                return false;
              }
              public int hashCode(){
                return this.count;
              }
            }
            public class HashSetTest2{
              public static void main(String[] args){
                HashSet hs=new HashSet();
                hs.add(new R(5));
                hs.add(new R(-3));
                hs.add(new R(9));
                hs.add(new R(-2));
                //打印HashSet集合，集合元素没有重复
                System.out.println(hs);
                //取出第一个元素
                Iterator it=hs.iterator();
                R first=(R)it.next();
                //为第一个元素的count实例变量赋值
                first.count=-3;    //①
                //再次输出HashSet集合，集合元素有重复元素
                System.out.println(hs);
                //删除count为-3的R对象
                hs.remove(new R(-3));   //②
                //可以看到被删除了一个R元素
                System.out.println(hs);
                //输出false
                System.out.println("hs是否包含count为-3的R对象？"
                                   + hs.contains(new R(-3)));
                //输出false
                System.out.println("hs是否包含count为5的R对象？"
                                   + hs.contains(new R(5)));
              }
            }
```

            - 当试图删除count为-3的R对象时，HashSet会计算出该对象的hashCode值，从而找出该对象在集合中的保存位置，然后把此处的对象与count为-3的R对象通过equals()方法进行比较，如果相等则删除该对象
              - HashSet只有第三个元素才满足该条件（**第一个元素实际上保存在count为5的R对象对应的位置**），所以第三个元素被删除
              - 至于第一个count为-3的R对象，**它保存在count为5的R对象对应的位置，但使用equals()方法拿它和count为5的R对象比较时又返回false**——这将导致HashSet不可能准确访问该元素
      - LinkedHashSet类
        - 当遍历LinkedHashSet集合里的元素时，LinkedHashSet将会按元素的添加顺序来访问集合里的元素
        - LinkedHashSet需要维护元素的插入顺序，因此性能略低于HashSet的性能，**但在迭代访问Set里的全部元素时将有很好的性能，因为它以链表来维护内部顺序**
          #Question [performance - Why are linked lists faster than arrays? - Stack Overflow](https://stackoverflow.com/questions/5445131/why-are-linked-lists-faster-than-arrays)
      - TreeSet实现类
        description: "SortedSet接口的实现类，可以确保集合元素处于排序状态"
        - 与HashSet集合相比，TreeSet还提供了如下几个额外的方法
          - Comparator comparator()
            - 如果TreeSet采用了定制排序，则该方法返回定制排序所使用的Comparator；如果TreeSet采用了自然排序，则返回null
          - Object first()
            - 返回集合中的第一个元素
          - Object last()
            - 返回集合中的最后一个元素
          - Object lower(Object e)
            - 返回集合中位于指定元素之前的元素（即小于指定元素的最大元素，参考元素不需要是TreeSet集合里的元素）
          - Object higher (Object e)
            - 返回集合中位于指定元素之后的元素（即大于指定元素的最小元素，参考元素不需要是TreeSet集合里的元素）
          - SortedSet subSet(fromElement, toElement)
            - 返回此Set的子集合，范围从fromElement（包含）到toElement（不包含）
          - SortedSet headSet(toElement)
            - 返回此Set的子集，由小于toElement的元素组成。

```java
            public class TreeSetTest{
              public static void main(String[] args){
                TreeSet nums=new TreeSet();
                //向TreeSet中添加四个Integer对象
                nums.add(5);
                nums.add(2);
                nums.add(10);
                nums.add(-9);
                //输出集合元素，看到集合元素已经处于排序状态
                System.out.println(nums);
                //输出集合里的第一个元素
                System.out.println(nums.first());
                //输出集合里的最后一个元素
                System.out.println(nums.last());
                //返回小于4的子集，不包含4
                System.out.println(nums.headSet(4));
                //返回大于5的子集，如果Set中包含5，子集中也包含5
                System.out.println(nums.tailSet(5));
                //返回大于等于-3、小于4的子集
                System.out.println(nums.subSet(-3 , 4));
              }
            }
```

        - 采用**红黑树**的数据结构来存储集合元素, 2 种**排序方法**
          - 自然排序 (default)
            description: "TreeSet会调用集合元素的compareTo(Object obj)方法来比较元素之间的大小关系，然后将集合元素按升序排列"
            - 实现了Comparable接口的常用类
              - BigDecimal、BigInteger以及所有的数值型对应的包装类
                - 按它们对应的数值大小进行比较
              - Character
                - 按字符的UNICODE值进行比较
              - Boolean
                - true对应的包装类实例大于false对应的包装类实例
              - String
                - 按字符串中字符的UNICODE值进行比较
              - Date、Time
                - 后面的时间、日期比前面的时间、日期大。
            - 如果试图把一个对象添加到TreeSet时，则该对象的类必须实现Comparable接口，否则程序将会抛出异常
              - **只有第一个元素无须实现Comparable接口**，后面添加的所有元素都必须实现Comparable接口。
                - 当试图从TreeSet中取出元素时，依然会引发ClassCastException异常

```java
                  class Err{ }
                  public class TreeSetErrorTest{
                    public static void main(String[] args){
                      TreeSet ts=new TreeSet();
                      //向TreeSet集合中添加两个Err对象
                      ts.add(new Err());
                      ts.add(new Err());  //①
                    }
                  }
```

              - 向TreeSet中添加的应该是同一个类的对象，否则也会引发ClassCastException异常
                - 大部分类在实现compareTo(Object obj)方法时，都需要将被比较对象obj强制类型转换成相同类型，因为只有相同类的两个实例才会比较大小。当试图把一个对象添加到TreeSet集合时，TreeSet会调用该对象的compareTo(Object obj)方法与集合中的其他元素进行比较——这就要求集合中的其他元素与该元素是同一个类的实例

```java
                  public class TreeSetErrorTest2{
                    public static void main(String[] args){
                      TreeSet ts=new TreeSet();
                      //向TreeSet集合中添加两个对象
                      ts.add(new String("Struts权威指南"));
                      ts.add(new Date());   //①
                    }
                  }
```

            - 如果向TreeSet中添加的对象是程序员自定义类的对象，则可以向TreeSet中添加多种类型的对象，前提是用户自定义类实现了Comparable接口，实现该接口时实现的compareTo(Object obj)方法没有进行强制类型转换
              - 但当试图取出TreeSet里的集合数据时，不同类型的元素依然会发生ClassCastException异常
            - 当把一个对象加入TreeSet集合中时，TreeSet调用该对象的compareTo(Object obj)方法与容器中的其他对象比较大小，然后根据红黑树结构找到它的存储位置
              - 如果两个对象通过compareTo(Object obj)方法比较相等，新对象将无法添加到TreeSet集合中
            - 重写该对象对应类的equals()方法时，应**保证该方法与compareTo(Object obj)方法有一致的结果**
              - **如果两个对象通过equals()方法比较返回true时，这两个对象通过compareTo(Object obj)方法比较应返回0**

```java
              class R implements Comparable{
                int count;
                public R(int count){
                  this.count=count;
                }
                public String toString(){
                  return "R[count:" + count + "]";
                }
                //重写equals()方法，根据count来判断是否相等
                public boolean equals(Object obj){
                  if (this==obj){
                    return true;
                  }
                  if(obj !=null && obj.getClass()==Z.class){
                    R r=(R)obj;
                    if (r.count==this.count){
                      return true;
                    }
                  }
                  return false;
                }
                //重写compareTo()方法，根据count来比较大小
                public int compareTo(Object obj) {
                  R r=(R)obj;
                  return count > r.count ? 1 :
                  count < r.count ? -1 : 0;
                }
              }
              public class TreeSetTest3{
                public static void main(String[] args){
                  TreeSet ts=new TreeSet();
                  ts.add(new R(5));
                  ts.add(new R(-3));
                  ts.add(new R(9));
                  ts.add(new R(-2));
                  //打印TreeSet集合，集合元素是有序排列的
                  System.out.println(ts);   //①
                  //取出第一个元素
                  R first=(R)ts.first();
                  //对第一个元素的count赋值
                  first.count=20;
                  //取出最后一个元素
                  R last=(R)ts.last();
                  //对最后一个元素的count赋值，与第二个元素的count相同
                  last.count=-2;
                  //再次输出将看到TreeSet里的元素处于无序状态，且有重复元素
                  System.out.println(ts);   //②
                  //删除Field被改变的元素，删除失败
                  System.out.println(ts.remove(new R(-2)));   //③
                  System.out.println(ts);
                  //删除Field没有改变的元素，删除成功
                  System.out.println(ts.remove(new R(5)));  //④
                  System.out.println(ts);
                }
              }
```

              - 一旦改变了TreeSet集合里可变元素的Field，当再试图删除该对象时，TreeSet也会删除失败（甚至集合中原有的、Field没被修改但与修改后元素相等的元素也无法删除）
              - TreeSet可以删除没有被修改Field，且不与其他被修改Field的对象重复的对象
          - 定制排序
            - 如果需要实现定制排序, 如降序排列, 则可以通过Comparator接口的帮助
              - 该接口里包含一个int compare(T o1, T o2)方法
                - 该方法用于比较o1和o2的大小：
                  - 如果该方法返回正整数，则表明o1大于o2
                  - 如果该方法返回0，则表明o1等于o2
                  - 如果该方法返回负整数，则表明o1小于o2
              - 如果需要实现定制排序，则需要在创建TreeSet集合对象时，提供一个Comparator对象与该TreeSet集合关联，由该Comparator对象负责集合元素的排序逻辑

```java
                class M{
                  int age;
                  public M(int age){
                    this.age=age;
                  }
                  public String toString(){
                    return "M[age:" + age + "]";
                  }
                }
                public class TreeSetTest4{
                  public static void main(String[] args){
                    TreeSet ts=new TreeSet(new Comparator(){
                      //根据M对象的age属性来决定大小
                      public int compare(Object o1, Object o2)
                      {
                        M m1=(M)o1;
                        M m2=(M)o2;
                        return m1.age > m2.age ? -1
                          : m1.age < m2.age ? 1 : 0;
                      }
                    });
                    ts.add(new M(5));
                    ts.add(new M(-3));
                    ts.add(new M(9));
                    System.out.println(ts);
                  }
                }
```

                - TreeSet判断两个集合元素相等的标准是：通过Comparator比较两个元素返回了0，这样TreeSet不会把第二个元素添加到集合中
      - EnumSet实现类
        - EnumSet在内部以位向量的形式存储，这种存储形式非常紧凑、高效
          - EnumSet对象占用内存很小，而且运行效率很好。尤其是进行批量操作（如调用containsAll和retainAll方法）时，如果其参数也是EnumSet集合，则该批量操作的执行速度也非常快。
        - 不允许加入null元素
          - 如果试图插入null元素，EnumSet将抛出NullPointerException异常
          - 如果只是想判断EnumSet是否包含null元素或试图删除null元素都不会抛出异常，只是删除操作将返回false，因为没有任何null元素被删除
        - APIs
          - static EnumSet allOf(Class elementType)
            - 创建一个包含指定枚举类里所有枚举值的EnumSet集合
          - static EnumSet complementOf(EnumSet s)
            - 创建一个其元素类型与指定EnumSet里元素类型相同的EnumSet集合，新EnumSet集合包含原EnumSet集合所不包含的、此枚举类剩下的枚举值（即新EnumSet集合和原EnumSet集合的集合元素加起来就是该枚举类的所有枚举值）
          - static EnumSet copyOf(Collection c)
            - 使用一个普通集合来创建EnumSet集合
          - static EnumSet copyOf(EnumSet s)
            - 创建一个与指定EnumSet具有相同元素类型、相同集合元素的EnumSet集合
          - static EnumSet noneOf(Class elementType)
            - 创建一个元素类型为指定枚举类型的空EnumSet。

```java
            enum Season{ SPRING,SUMMER,FALL,WINTER }
            public class EnumSetTest{
              public static void main(String[] args){
                //创建一个EnumSet集合，集合元素就是Season枚举类的全部枚举值
                EnumSet es1=EnumSet.allOf(Season.class);
                //输出[SPRING,SUMMER,FALL,WINTER]
                System.out.println(es1);
                //创建一个EnumSet空集合，指定其集合元素是Season类的枚举值
                EnumSet es2=EnumSet.noneOf(Season.class);
                //输出[]
                System.out.println(es2);
                //手动添加两个元素
                es2.add(Season.WINTER);
                es2.add(Season.SPRING);
                //输出[SPRING,WINTER]
                System.out.println(es2);
                //以指定枚举值创建EnumSet集合
                EnumSet es3=EnumSet.of(Season.SUMMER , Season.WINTER);
                //输出[SUMMER,WINTER]
                System.out.println(es3);
                EnumSet es4=EnumSet.range(Season.SUMMER , Season.WINTER);
                //输出[SUMMER,FALL,WINTER]
                System.out.println(es4);
                //新创建的EnumSet集合元素和es4集合元素有相同的类型
                //es5集合元素 + es4集合元素=Season枚举类的全部枚举值
                EnumSet es5=EnumSet.complementOf(es4);
                //输出[SPRING]
                System.out.println(es5);
              }
            }
```

    - 8.4 List集合
      description: 代表一个元素有序、可重复的集合. 集合中每个元素都有其对应的顺序索引
      - `List`接口和`List Iterator`接口
        - APIs
          - void add(int index, Object element)
            - 将元素element插入到List集合的index处
          - boolean addAll(int index, Collection c)
            - 将集合c所包含的所有元素都插入到List集合的index处
          - Object get(int index)
            - 返回集合index索引处的元素
          - int indexOf(Object o)
            - 返回对象o在List集合中第一次出现的位置索引
          - int lastIndexOf(Object o)
            - 返回对象o在List集合中最后一次出现的位置索引
          - Object remove(int index)
            - 删除并返回index索引处的元素
          - Object set(int index, Object element)
            - 将index索引处的元素替换成element对象，返回新元素
          - List subList(int fromIndex, int toIndex)
            - 返回从索引fromIndex（包含）到索引toIndex（不包含）处所有集合元素组成的子集合
        - ==与Set集合相比，List增加了根据索引来插入、替换和删除集合元素的方法==

```java
          public class ListTest{
            public static void main(String[] args){
              List books=new ArrayList();
              //向books集合中添加三个元素
              books.add(new String("轻量级Java EE企业应用实战"));
              books.add(new String("疯狂Java讲义"));
              books.add(new String("疯狂Android讲义"));
              System.out.println(books);
              //将新字符串对象插入在第二个位置
              books.add(1 , new String("疯狂Ajax讲义"));
              for (int i=0 ; i < books.size() ; i++ )
              {
                System.out.println(books.get(i));
              }
              //删除第三个元素
              books.remove(2);
              System.out.println(books);
              //判断指定元素在List集合中的位置：输出1，表明位于第二位
              System.out.println(
                books.indexOf(new String("疯狂Ajax讲义")));  //①
              //将第二个元素替换成新的字符串对象
              books.set(1, new String("疯狂Java讲义"));
              System.out.println(books);
              //将books集合的第二个元素（包括）
              //到第三个元素（不包括）截取成子集合
              System.out.println(books.subList(1 , 2));
            }
          }
```

          - `List` 独特用法 -- **根据位置索引来访问集合中的元素**
            - 一种新的遍历集合元素的方法: 使用普通的for循环来遍历集合元素
          - `List` 判断两个对象相等: equals()方法返回 true 即可

```java
              class A{
                public boolean equals(Object obj){
                  return true;
                }
              }
              public class ListTest2{
                public static void main(String[] args){
                  List books=new ArrayList();
                  books.add(new String("轻量级Java EE企业应用实战"));
                  books.add(new String("疯狂Java讲义"));
                  books.add(new String("疯狂Android讲义"));
                  System.out.println(books);
                  //删除集合中的A对象，将导致第一个元素被删除
                  books.remove(new A());    //①
                  System.out.println(books);
                  //删除集合中的A对象，再次删除集合中的第一个元素
                  books.remove(new A());    //②
                  System.out.println(books);
                }
              }
```

              Run

```
              [轻量级Java EE企业应用实战, 疯狂Java讲义, 疯狂Android讲义]
              [疯狂Java讲义, 疯狂Android讲义]
              [疯狂Android讲义]
```

              #weird-code
              - 从上面运行结果可以看出，执行①行代码时，程序试图删除一个A对象，List将会调用该A对象的equals()方法依次与集合元素进行比较，如果该equals()方法以某个集合元素作为参数时返回true，List将会删除该元素
        - 迭代器 `ListIterator()`
          - ListIterator接口在Iterator接口基础上增加了如下方法。
            - boolean hasPrevious()
              - 返回该迭代器关联的集合是否还有上一个元素
            - Object previous()
              - 返回该迭代器的上一个元素
            - void add()
              - 在指定位置插入一个元素。

```java
            public class ListIteratorTest{
              public static void main(String[] args){
                String[] books={
                  "疯狂Java讲义",
                  "轻量级Java EE企业应用实战"
                  };
                List bookList=new ArrayList();
                for (int i=0; i < books.length ; i++ ){
                  bookList.add(books[i]);
                }
                ListIterator lit=bookList.listIterator();
                while (lit.hasNext()){
                  System.out.println(lit.next());
                  lit.add("-------分隔符-------");
                }
                System.out.println("=======下面开始反向迭代=======");
                while(lit.hasPrevious()){
                  System.out.println(lit.previous());
                }
              }
            }
```

            Run

```
            疯狂Java讲义
            轻量级Java EE企业应用实战
            =======下面开始反向迭代=======
            -------分隔符-------
            轻量级Java EE企业应用实战
            -------分隔符-------
            疯狂Java讲义
```

      - `ArrayList` 和 `Vector` 实现类
        - 两者都是基于数组实现的List类
          - 一个动态的、允许再分配的Object[]数组
            - ArrayList或Vector对象使用initialCapacity参数来设置该数组的长度，当向ArrayList或Vector中添加元素超出了该数组的长度时，它们的initialCapacity会自动增加
            - 无须关心ArrayList或Vector的initialCapacity。但如果向ArrayList或Vector集合中添加大量元素时，可使用ensureCapacity(int minCapacity)方法一次性地增加initialCapacity。这可以减少重分配的次数，从而提高性能
            - 空的ArrayList或Vector集合时不指定initialCapacity参数，则Object[]数组的长度默认为10
          - ArrayList和Vector还提供了如下两个方法来重新分配Object[]数组
            - void ensureCapacity(int minCapacity)
              - 将ArrayList或Vector集合的Object[]数组长度增加minCapacity
            - void trimToSize()
              - 调整ArrayList或Vector集合的Object[]数组长度为当前元素的个数。程序可调用该方法来减少ArrayList或Vector集合对象占用的存储空间
        - ArrayList #vs Vector
          - 在用法上几乎完全相同
            - 但Vector是一个古老的集合（从JDK 1.0就有了）
              - 那时候Java还没有提供系统的集合框架，所以Vector里提供了一些方法名很长的方法，例如addElement(Object obj)，实际上这个方法与add (Object obj)没有任何区别
              - 从JDK 1.2以后，Java提供了系统的集合框架，就将Vector改为实现List接口，作为List的实现之一，从而导致Vector里有一些功能重复的方法
          - ArrayList是线程不安全的，当多个线程访问同一个ArrayList集合时，如果有超过一个线程修改了ArrayList集合，则程序必须手动保证该集合的同步性；但Vector集合则是线程安全的，无须程序保证该集合的同步性
          - 因为Vector是线程安全的，所以Vector的性能比ArrayList的性能要低。实际上，即使需要保证List集合线程安全，也同样不推荐使用Vector实现类。后面会介绍一个Collections工具类，它可以将一个ArrayList变成线程安全的
          - Vector还提供了一个Stack子类，它用于模拟“栈”这种数据结构
            - 与Java中的其他集合一样，进栈出栈的都是Object，因此从栈中取出元素后必须进行类型转换，除非你只是使用Object具有的操作。
            - Stack类里提供了如下几个方法
              - Object peek()
                - 返回“栈”的第一个元素，但并不将该元素“pop”出栈
              - Object pop()
                - 返回“栈”的第一个元素，并将该元素“pop”出栈
              - void push(Object item)
                - 将一个元素“push”进栈，最后一个进“栈”的元素总是位于“栈”顶
            - ==由于Stack继承了Vector，因此它也是一个非常古老的Java集合类，它是线程安全的，性能比较差，因此现在的程序中一般较少使用Stack类。如果程序需要使用“栈”这种数据结构，则可以**考虑使用LinkedList** (实现了Deque接口)==
      - 固定长度的 `List`
        - `Arrays.asList(Object... a)` 方法
          - 把一个数组或指定个数的对象转换成一个List集合
            - 这个List集合既不是ArrayList实现类的实例，也不是Vector实现类的实例，而是**Arrays的内部类ArrayList的实例**
              - `Arrays.ArrayList` 是**一个固定长度的List集合**，==程序只能遍历访问该集合里的元素，不可增加、删除该集合里的元素==
                - `UnsupportedOperationException异常`
    - 8.5 Queue集合
      - `Queue` 接口
        - APIs
          - void add(Object e)
            - 将指定元素加入此队列的尾部
          - Object element()
            - 获取队列头部的元素，但是不删除该元素
          - boolean offer(Object e)
            - 将指定元素加入此队列的尾部。当使用有容量限制的队列时，此方法通常比add(Object e)方法更好
          - Object peek()
            - 获取队列头部的元素，但是不删除该元素。如果此队列为空，则返回null
          - Object poll()
            - 获取队列头部的元素，并删除该元素。如果此队列为空，则返回null
          - Object remove()
            - 获取队列头部的元素，并删除该元素
        - `PriorityQueue` 实现类
          description: 比较标准的队列实现类
          - 保存队列元素的顺序**不是按加入队列的顺序，而是按队列元素的大小进行重新排序**
            - `peek() / poll()方法` 取出队列中最小的元素时
              - 并不是取出最先进入队列的元素
                - 违反了队列的最基本规则：先进先出 (FIFO)
          - 不允许插入null元素
          - 2 种排序方式
            - 自然排序
              - 元素必须实现了Comparable接口，而且应该是同一个类的多个实例
                - 否则可能导致ClassCastException异常
            - 定制排序
              - 传入一个Comparator对象，该对象负责对队列中的所有元素进行排序
                - 不要求队列元素实现Comparable接口
      - `Deque` 接口
        description: "Deque接口是Queue接口的子接口, 它代表一个双端队列, 可以同时从两端来添加、删除, Deque接口里定义了一些双端队列的方法，这些方法允许从两端来操作队列的元素"
        - APIs ( (双端)队列 / 栈 )
          - void addFirst(Object e)
            - 将指定元素插入该双端队列的开头
          - void addLast(Object e)
            - 将指定元素插入该双端队列的末尾
          - Iterator descendingIterator()
            - 返回该双端队列对应的迭代器，该迭代器将以逆向顺序来迭代队列中的元素
          - Object getFirst()
            - 获取但不删除双端队列的第一个元素
          - Object getLast()
            - 获取但不删除双端队列的最后一个元素
          - boolean offerFirst(Object e)
            - 将指定元素插入该双端队列的开头
          - boolean offerLast(Object e)
            - 将指定元素插入该双端队列的末尾
          - Object peekFirst()
            - 获取但不删除该双端队列的第一个元素；
            - **如果此双端队列为空，则返回null**
          - Object peekLast()
            - 获取但不删除该双端队列的最后一个元素；
            - **如果此双端队列为空，则返回null**
          - Object pollFirst()
            - 获取并删除该双端队列的第一个元素；
            - **如果此双端队列为空，则返回null**
          - Object pollLast()
            - 获取并删除该双端队列的最后一个元素；
            - **如果此双端队列为空，则返回null**
          - Object pop()（栈方法）
            - pop出该双端队列所表示的栈的栈顶元素。相当于removeFirst()
          - void push(Object e)（栈方法）
            - 将一个元素push进该双端队列所表示的栈的栈顶。相当于addFirst(e)
          - Object removeFirst()
            - 获取并删除该双端队列的第一个元素
          - Object removeFirstOccurrence(Object o)
            - 删除该双端队列的第一次出现的元素o
          - removeLast()
            - 获取并删除该双端队列的最后一个元素
          - removeLastOccurrence(Object o)
            - 删除该双端队列的最后一次出现的元素o
        - #vs Queue
          - ![image.png](../assets/book/疯狂Java讲义/image_1669730105777_0.png)
        - #vs Stack
          - ![image.png](../assets/book/疯狂Java讲义/image_1669731339426_0.png)
        - `ArrayDeque` 实现类
          - 基于数组实现的双端队列
          - 创建Deque时同样可指定一个numElements参数，该参数用于指定Object[]数组的长度
            - 如果不指定numElements参数，Deque底层数组的长度为16
          - ArrayList和ArrayDeque两个集合类的实现机制基本相似

```java
            public class ArrayDequeTest{
              public static void main(String[] args){
                ArrayDeque stack=new ArrayDeque();
                //依次将三个元素push入“栈”
                stack.push("疯狂Java讲义");
                stack.push("轻量级Java EE企业应用实战");
                stack.push("疯狂Android讲义");
                //输出：[疯狂Java讲义, 轻量级Java EE企业应用实战 , 疯狂Android讲义]
                System.out.println(stack);
                //访问第一个元素，但并不将其pop出“栈”，输出：疯狂Android讲义
                System.out.println(stack.peek());
                //依然输出：[疯狂Java讲义, 轻量级Java EE企业应用实战 , 疯狂Android讲义]
                System.out.println(stack);
                //pop出第一个元素，输出：疯狂Android讲义
                System.out.println(stack.pop());
                //输出：[疯狂Java讲义, 轻量级Java EE企业应用实战]
                System.out.println(stack);
              }
            }
```

        - `LinkedList` 实现类
          - 实现了 2 种接口
            - List集合
              - 随机访问元素
            - Deque接口
              - 双端队列 / 栈

```java
            public class LinkedListTest{
              public static void main(String[] args){
                LinkedList books=new LinkedList();
                books.offer("疯狂Java讲义");             // 队尾
                books.push("轻量级Java EE企业应用实战"); // 栈顶
                books.offerFirst("疯狂Android讲义");     // 队头 (栈顶)
                for (int i=0; i < books.size() ; i++ )
                  System.out.println(books.get(i));
                System.out.println(books.peekFirst());     // 栈顶 (访问但不删除)
                System.out.println(books.peekLast());     // 队尾 (访问但不删除)
                System.out.println(books.pop());         // 栈顶出栈
                System.out.println(books);
                System.out.println(books.pollLast());    // 队尾 (访问并删除)
                System.out.println(books);
              }
            }
```

            Run

```
            疯狂Android讲义
            轻量级Java EE企业应用实战
            疯狂Java讲义
            疯狂Android讲义
            疯狂Java讲义
            疯狂Android讲义
            [轻量级Java EE企业应用实战, 疯狂Java讲义]
            疯狂Java讲义
            [轻量级Java EE企业应用实战]
```

          - 随机访问集合元素时性能较差
          - 在插入、删除元素时性能非常出色（只需改变指针所指的地址即可）
            - 对于所有的内部基于数组的集合实现 (ArrayList、ArrayDeque), **使用随机访问的性能比使用Iterator迭代访问的性能要好**
              - 随机访问会被映射成对数组元素的访问
      - 各种线性表的性能分析
        - ![image.png](../assets/book/疯狂Java讲义/image_1669735285691_0.png)

```java
          public class PerformanceTest{
            public static void main(String[] args){
              //创建一个字符串数组
              String[] tst1=new String[900000];
              //动态初始化数组元素
              for (int i=0; i < 900000; i++)
                tst1[i]=String.valueOf(i);
              ArrayList al=new ArrayList();
              //将所有的数组元素加入ArrayList集合中
              for (int i=0; i < 900000 ; i++)
                al.add(tst1[i]);
              LinkedList ll=new LinkedList();
              //将所有的数组元素加入LinkedList集合中
              for (int i=0; i < 900000 ; i++)
                ll.add(tst1[i]);
              //迭代访问ArrayList集合的所有元素，并输出迭代时间
              long start=System.currentTimeMillis();
              for (Iterator it=al.iterator();it.hasNext() ; )
                it.next();
              System.out.println("迭代ArrayList集合元素的时间:"
                                 + (System.currentTimeMillis() - start));
              //迭代访问LinkedList集合的所有元素，并输出迭代时间
              start=System.currentTimeMillis();
              for (Iterator it=ll.iterator();it.hasNext() ; )
                it.next();
              System.out.println("迭代LinedList集合元素的时间:"
                                 + (System.currentTimeMillis() - start));
            }
          }
```

          Run

```shell
          迭代ArrayList集合元素的时间:7
          迭代LinedList集合元素的时间:11
          # 结果非常随机
```

```shell
            java -Xms128m -Xmx512m PerformanceTest
```

            - `-Xms`
              - 设置JVM的堆内存初始大小
            - `-Xmx`
              - 设置JVM的堆内存最大大小（最好不要超过物理内存大小）
            - #question ==为什么IDEA 可以直接运行???==
          - 如果需要遍历List集合元素. 性能选择
            - ArrayList、Vector集合
              - **随机访问方法（get）来遍历集合元素**
            - LinkedList集合
              - 迭代器（Iterator）来遍历集合元素
          - 如果需要经常执行插入、删除操作来改变List集合的大小
            - 应该使用LinkedList集合，而不是ArrayList
              - 使用ArrayList、Vector集合需要经常重新分配内部数组的大小，其时间开销常常是使用LinkedList的时间开销的几十倍，效果很差
          - 如果有多个线程需要同时访问List集合中的元素
            - **可考虑使用Collections将集合包装成线程安全的集合**
    - 8.6 Map
      - HashMap和Hashtable实现类
      - LinkedHashMap实现类
      - Properties读写属性文件
        description: Hashtable类的子类; 该对象在处理属性文件时特别方便（Windows操作平台上的ini文件就是一种属性文件)
        - Properties类可以把Map对象和属性文件关联起来，从而可以把Map对象中的key-value对写入属性文件中，也可以把属性文件中的“属性名=属性值”加载到Map对象中
          - 由于属性文件里的属性名、属性值只能是字符串类型，所以Properties里的key、value都是字符串类型
        - APIs
          - String getProperty(String key)
            - 获取Properties中指定属性名对应的属性值，类似于Map的get(Object key)方法
          - String getProperty(String key, String defaultValue)
            - 该方法与前一个方法基本相似。该方法多一个功能，如果Properties中不存在指定的key时，则该方法指定默认值
          - Object setProperty(String key, String value)
            - 设置属性值，类似于Hashtable的put()方法。
          - void load(InputStream inStream)
            - 从属性文件（以输入流表示）中加载key-value对，把加载到的key-value对追加到Properties里（Properties是Hashtable的子类，它不保证key-value对之间的次序）
          - void store(OutputStream out, String comments)
            - 将Properties中的key-value对输出到指定的属性文件（以输出流表示）中。

```java
            public class PropertiesTest{
              public static void main(String[] args)
                throws Exception {
                Properties props=new Properties();
                //向Properties中添加属性
                props.setProperty("username" , "yeeku");
                props.setProperty("password" , "123456");
                //将Properties中的key-value对保存到a.ini文件中
                props.store(new FileOutputStream("a.ini")
                            , "comment line");   //①
                //新建一个Properties对象
                Properties props2=new Properties();
                //向Properties中添加属性
                props2.setProperty("gender" , "male");
                //将a.ini文件中的key-value对追加到props2中
                props2.load(new FileInputStream("a.ini") );   //②
                System.out.println(props2);
              }
            }
```

            Run

```shell
            {password=123456, gender=male, username=yeeku}
```

            File

```shell
            #comment line
            #Wed Nov 30 18:09:55 SGT 2022
            password=123456
            username=yeeku
```

      - SortedMap接口和TreeMap实现类
      - SortedMap接口和TreeMap实现类
      - WeakHashMap实现类
      - IdentityHashMap实现类
      - EnumMap实现类
      - 各Map实现类的性能分析
    - 8.7 HashSet和HashMap的性能选项
    - 8.8 操作集合的工具类：Collections
      - 排序操作
        - APIs
          - static void reverse(List list)
            - 反转指定List集合中元素的顺序
          - static void shuffle(List list)
            - 对List集合元素进行随机排序（shuffle方法模拟了“洗牌”动作）
          - static void sort(List list)
            - 根据元素的自然顺序对指定List集合的元素按升序进行排序
          - static void sort(List list, Comparator c)
            - 根据指定Comparator产生的顺序对List集合元素进行排序
          - static void swap(List list, int i, int j)
            - 将指定List集合中的i处元素和j处元素进行交换
          - static void rotate(List list , int distance)
            - 当distance为正数时，将list集合的后distance个元素“整体”移到前面
            - 当distance为负数时，将list集合的前distance个元素“整体”移到后面。
            - 该方法不会改变集合的长度。

```java
          public class ShowHand{
            //定义该游戏最多支持多少个玩家
            private final int PLAY_NUM=5;
            //定义扑克牌的所有花色和数值
            private String[] types={"方块", "草花", "红心", "黑桃"};
            private String[] values={"2" , "3" , "4" , "5"
              , "6" , "7" , "8" , "9", "10"
              , "J" , "Q" , "K" , "A"};
            //cards是一局游戏中剩下的扑克牌
            private List<String> cards=new LinkedList<String>();
            //定义所有的玩家
            private String[] players=new String[PLAY_NUM];
            //所有玩家手上的扑克牌
            private List<String>[] playersCards=new List[PLAY_NUM];
            /**
            * 初始化扑克牌，放入52张扑克牌
            * 并且使用shuffle方法将它们按随机顺序排列
            */
            public void initCards(){
              for (int i=0 ; i < types.length ; i++ )
                for (int j=0; j < values.length ; j++ )
                  cards.add(types[i] + values[j]);
              //随机排列
              Collections.shuffle(cards);
            }
            /**
            * 初始化玩家，为每个玩家分派用户名
            */
            public void initPlayer(String... names){
              if (names.length > PLAY_NUM || names.length < 2){
                //校验玩家数量，此处使用异常机制更合理
                System.out.println("玩家数量不对");
                return ;
              } else {
                //初始化玩家用户名
                for (int i=0; i < names.length ; i++ )
                  players[i]=names[i];
              }
            }
            /**
            * 初始化玩家手上的扑克牌，开始游戏时每个玩家手上的扑克牌为空
            * 程序使用一个长度为0的LinkedList来表示
            */
            public void initPlayerCards(){
              for (int i=0; i < players.length ; i++ ){
                if (players[i] !=null && !players[i].equals(""))
                  playersCards[i]=new LinkedList<String>();
              }
            }
            /**
            * 输出全部扑克牌，该方法没有实际作用，仅用作测试
            */
            public void showAllCards(){
              for (String card : cards )
                System.out.println(card);
            }
            /**
            * 派扑克牌
            * @param first 最先派给谁
            */
            public void deliverCard(String first){
              //调用ArrayUtils工具类的search方法
              //查询出指定元素在数组中的索引
              // int firstPos=ArrayUtils.search(players, first);
              // ArrayUtils is included with apache package https://www.reddit.com/r/learnprogramming/comments/wxbcaj/why_do_i_get_the_error_arrayutils_cannot_be/
              int firstPos = -1;
              for (int i = 0; i < players.length; i++) {
                if(players[i].equals(first)){
                  firstPos = i;
                  break;
                }
              }
              if(firstPos == -1) return;
              //依次给位于该指定玩家之后的每个玩家派扑克牌
              for (int i=firstPos; i < PLAY_NUM ; i ++){
                if (players[i] !=null){
                  playersCards[i].add(cards.get(0));
                  cards.remove(0);
                }
              }
              //依次给位于该指定玩家之前的每个玩家派扑克牌
              for (int i=0; i < firstPos ; i ++){
                if (players[i] !=null){
                  playersCards[i].add(cards.get(0));
                  cards.remove(0);
                }
              }
            }
            /**
            * 输出玩家手上的扑克牌
            * 实现该方法时，应该控制每个玩家看不到别人的第一张牌，但此处没有增加该功能
            */
            public void showPlayerCards(){
              for (int i=0; i < PLAY_NUM ; i++ ){
                //当该玩家不为空时
                if (players[i] !=null){
                  //输出玩家
                  System.out.print(players[i] + " ： " );
                  //遍历输出玩家手上的扑克牌
                  for (String card : playersCards[i])
                    System.out.print(card + "\t");
                }
                System.out.print("\n");
              }
            }
            public static void main(String[] args){
              ShowHand sh=new ShowHand();
              sh.initPlayer("电脑玩家" , "孙悟空");
              sh.initCards();
              sh.initPlayerCards();
              //下面测试所有扑克牌，没有实际作用
              sh.showAllCards();
              System.out.println("---------------");
              //下面从"孙悟空"开始派牌
              sh.deliverCard("孙悟空");
              sh.showPlayerCards();
              /*
              这个地方需要增加处理：
              1.牌面最大的玩家下注
              2.其他玩家是否跟注
              3.游戏是否只剩一个玩家?如果是，则此玩家胜利了
              4.如果已经是最后一张扑克牌，则需要比较剩下玩家的牌面大小
              */
              //再次从"电脑玩家"开始派牌
              sh.deliverCard("电脑玩家");
              sh.showPlayerCards();
            }
          }
```

      - 查找、替换操作
        - APIs
          - static int binarySearch(List list, Object key)
            - 使用二分搜索法搜索指定的List集合，以获得指定对象在List集合中的索引
            - 如果要使该方法可以正常工作，则必须保证List中的元素已经处于**有序状态**
              - 无法操作 `String`
          - static Object max(Collection coll)
            - 根据元素的自然顺序，返回给定集合中的最大元素
          - static Object max(Collection coll, Comparator comp)
            - 根据Comparator指定的顺序，返回给定集合中的最大元素
          - static Object min(Collection coll)
            - 根据元素的自然顺序，返回给定集合中的最小元素static Object min(Collection coll, Comparator comp)
            - 根据Comparator指定的顺序，返回给定集合中的最小元素
          - static void fill(List list, Object obj)
            - 使用指定元素obj替换指定List集合中的所有元素
          - static int frequency(Collection c, Object o)
            - 返回指定集合中指定元素的出现次数
          - static int indexOfSubList(List source, List target)
            - 返回子List对象在父List对象中第一次出现的位置索引
            - 如果父List中没有出现这样的子List，则返回-1
          - static int lastIndexOfSubList(List source, List target)
            - 返回子List对象在父List对象中最后一次出现的位置索引
            - 如果父List中没有出现这样的子List，则返回-1
          - static boolean replaceAll(List list, Object oldVal, Object newVal)
            - 使用一个新值newVal替换List对象的所有旧值oldVal

```java
          public class SearchTest{
            public static void main(String[] args){
              ArrayList nums=new ArrayList();
              nums.add(2);
              nums.add(-5);
              nums.add(3);
              nums.add(0);
              //输出:[2, -5, 3, 0]
              System.out.println(nums);
              //输出最大元素，将输出3
              System.out.println(Collections.max(nums));
              //输出最小元素，将输出-5
              System.out.println(Collections.min(nums));
              //将nums中的0使用1来代替
              Collections.replaceAll(nums , 0 , 1);
              //输出:[2, -5, 3, 1]
              System.out.println(nums);
              //判断-5 在List集合中出现的次数，返回1
              System.out.println(Collections.frequency(nums , -5));
              //对nums集合排序
              Collections.sort(nums);
              //输出:[-5, 1, 2, 3]
              System.out.println(nums);
              //只有排序后的List集合才可用二分法查询，输出3
              System.out.println(Collections.binarySearch(nums , 3));
            }
          }
```

      - 同步控制
        - 提供了多个synchronizedXxx()方法
          - 将指定集合包装成线程同步的集合
            - 解决多线程并发访问集合时的线程安全问题
        - Java中常用的集合框架中的实现类 `HashSet`、`TreeSet`、`ArrayList`、`ArrayDeque`、`LinkedList`、`HashMap`和`TreeMap`都是线程不安全的

```java
          public class SynchronizedTest{
            public static void main(String[] args){
              //下面程序创建了4个同步的集合对象
              Collection c=Collections
                .synchronizedCollection(new ArrayList());
              List list=Collections.synchronizedList(new ArrayList());
              Set s=Collections.synchronizedSet(new HashSet());
              Map m=Collections.synchronizedMap(new HashMap());
            }
          }
```

      - 设置不可变集合
        - APIs (此处的集合既可以是List，也可以是Set，还可以是Map)
          - emptyXxx()
            - 返回一个空的、不可变的集合对象
          - singletonXxx()
            - 返回一个只包含指定对象（只有一个或一项元素）的、不可变的集合对象
          - unmodifiableXxx
            - 返回指定集合对象的不可变视图

```java
          public class UnmodifiableTest{
            public static void main(String[] args){
              //创建一个空的、不可改变的List对象
              List unmodifiableList=Collections.emptyList();
              //创建一个只有一个元素，且不可改变的Set对象
              Set unmodifiableSet=Collections.singleton("疯狂Java讲义");
              //创建一个普通的Map对象
              Map scores=new HashMap();
              scores.put("语文" , 80);
              scores.put("Java" , 82);
              //返回普通的Map对象对应的不可变版本
              Map unmodifiableMap=Collections.unmodifiableMap(scores);
              //下面任意一行代码都将引发UnsupportedOperationException异常
              unmodifiableList.add("测试元素");   //①
              unmodifiableSet.add("测试元素");   //②
              unmodifiableMap.put("语文" , 90);   //③
            }
          }
```

    - 8.9 烦琐的接口：Enumeration
      - 是Iterator迭代器的“古老版本”
        - 从JDK 1.0开始，Enumeration接口就已经存在了（Iterator从JDK 1.2才出现）
      - APIs
        - boolean hasMoreElements( )
          - 如果此迭代器还有剩下的元素，则返回true
        - Object nextElement( )
          - 返回该迭代器的下一个元素，如果还有的话（否则抛出异常）
      - >[!tip]
        > 在计算机行业有一条规则：**加入任何规则都必须慎之又慎，因为以后无法删除规则**
    - 8.10 本章小结
      - 将本章未完成的梭哈游戏补充完整，不断地添加梭哈规则，开发一个控制台的梭哈游戏
  - 第 9 章 泛型
    - 9.1 泛型入门
      - Object 通用性好, 但有 2 个问题
        - 集合对元素类型没有任何限制
          - 例如，想创建一个只能保存 Dog 对象的集合，但程序也可以轻易地将 Cat 对象“丢”进去，所以可能引发异常
        - “丢进”集合时丢失了对象的状态信息, 取出还需要进行强制类型转换
          - 既增加了编程的复杂度，也可能引发 ClassCastException 异常
      - 编译时不检查类型的异常
      - 手动实现编译时检查类型

```java
          // 自定义一个StrList集合类，使用组合的方式来复用ArrayList类
          class StrList{
            private List strList=new ArrayList();
            // 定义StrList的add方法
            public boolean add(String ele){
              return strList.add(ele);
            }
            // 重写get()方法，将get()方法的返回值类型改为String类型
            public String get(int index){
              return (String)strList.get(index);
            }
            public int size(){
              return strList.size();
            }
          }
          public class CheckType{
            public static void main(String[] args){
              // 创建一个只想保存字符串的List集合
              StrList strList=new StrList();
              strList.add("疯狂Java讲义");
              strList.add("疯狂Android讲义");
              strList.add("轻量级Java EE企业应用实战");
              // 下面语句不能把Integer对象“丢进”集合中，否则将引起编译错误
              strList.add(5);    //①
              System.out.println(strList);
              for (int i=0; i < strList.size() ; i++ ){
                // 因为StrList里元素的类型就是String类型
                //所以无须进行强制类型转换
                String str=strList.get(i);
              }
            }
          }
```

          Run(程序将无法通过编译。因为StrList只接受String对象作为元素)

```
          java: incompatible types: int cannot be converted to java.lang.String
```

          - 从代码的健壮性角度来看，该方法极其有用，而且使用get()方法返回集合元素时，无须进行类型转换。
          - 局限性
            - 程序员需要定义大量的List子类
        - Java 5 以后，引入了“**参数化类型 (parameterized type)**”的概念, 也叫**泛型 (Generic)**
          - 允许我们在创建集合时指定集合元素的类型
      - 使用泛型
        id: 63880f45-37f7-4ed3-a30b-606c5f23dee1
      - Java 7泛型的 "菱形" 语法 (`<>`)
        - Java 7开始, 在构造器后不需要带完整的泛型信息, 只要一对尖括号(<>)即可
          - Java 7以前，带泛型的接口、类定义变量，那么调用构造器创建对象时构造器的后面也必须带泛型
    - 9.2 深入泛型
      - 定义泛型接口、类

```java
          // 定义接口时指定了一个类型形参，该形参名为E
          public interface List<E>{
            // 在该接口里，E可作为类型使用
            // 下面方法可以使用E作为参数类型
            void add(E x);
            Iterator<E> iterator();   //①
            //...
          }
          // 定义接口时指定了一个类型形参，该形参名为E
          public interface Iterator<E>{
            // 在该接口里E完全可以作为类型使用
            E next();
            boolean hasNext();
            //...
          }
          // 定义该接口时指定了两个类型形参，其形参名为K、V
          public interface Map<K , V>{
            // 在该接口里K、V完全可以作为类型使用
            Set<K> keySet()   //②
            V put(K key, V value)
            //...
          }
```

          - 允许在定义接口、类时声明类型形参，类型形参在整个接口、类体内可当成类型使用，几乎所有可使用普通类型的地方都可以使用这种类型形参
      - 从泛型类派生子类

```java
          // ERROR!!! 定义类A继承Apple类，Apple类不能跟类型形参
          // public class A extends Apple<T>{ }
```

```java
          // 使用Apple类时为T形参传入String类型
          public class A extends Apple<String>
          // 使用Apple类时，没有为T形参传入实际的类型参数
          public class A extends Apple
```

          - 如果从Apple<String>类派生子类，则在Apple类中所有使用T类型形参的地方都将被替换成String类型
            - **它的子类会继承到==String getInfo()和void setInfo(String info)两个方法==**
              - 如果子类需要重写父类的方法，就必须注意这一点

```java
              public class A1 extends Apple<String>{
                // 正确重写了父类的方法，返回值
                // 与父类Apple<String>的返回值完全相同
                public String getInfo(){
                  return "子类" + super.getInfo();
                }
                /*
                // 下面方法是错误的，重写父类方法时返回值类型不一致
                public Object getInfo(){
                return "子类";
                }
                */
              }
```

            - 如果使用Apple类时没有传入实际的类型参数，Java编译器可能发出警告：使用了未经检查或不安全的操作——这就是泛型检查的警告
              - 如果希望看到该警告提示的更详细信息，则可以通过为 `javac` 命令增加 `-Xlint:unchecked` 选项来实现

```java
                public class A2 extends Apple{
                  // 重写父类的方法
                  public String getInfo(){
                    // super.getInfo()方法返回值是Object类型
                    // 所以加toString()才返回String类型
                    return super.getInfo().toString();
                  }
                }
```

      - 并不存在泛型类

```java
          // 分别创建List<String>对象和List<Integer>对象
          List<String> l1=new ArrayList<>();
          List<Integer> l2=new ArrayList<>();
          // 调用getClass()方法来比较l1和l2的类是否相等
          System.out.println(l1.getClass()==l2.getClass());
```

          Run

```shell
          true #不管泛型的实际类型参数是什么，它们在运行时总有同样的类（class）
```

          - 对于Java来说，它们依然被当成同一个类处理，在内存中也只占用一块内存空间，因此在静态方法、静态初始化块或者静态变量的声明和初始化中不允许使用类型形参

```java
              public class R<T>{
                // 下面代码错误，不能在静态Field声明中使用类型形参
                static T info;
                T age;
                public void foo(T msg){}
                // 下面代码错误，不能在静态方法声明中使用类型形参
                public static void bar(T msg){}
              }
```

            - 由于系统中并不会真正生成泛型类，所以instanceof运算符后不能使用泛型类

```java
                Collection cs=new ArrayList<String>();
                // 下面代码编译时引起错误：instanceof 运算符后不能使用泛型类
                if (cs instanceof List<String>) {...}
```

    - 9.3 类型通配符 Wildcard Characters

```java
        class Test{
          public void test(List<Object> c){
            for (int i=0; i < c.size(); i++)
              System.out.println(c.get(i));
          }
          public static void main(String[] args) {
            // 创建一个List<String>对象
            List<String> strList=new ArrayList<>();
            // 将strList作为参数来调用前面的test方法
            test(strList);   //①
          }
        }
```

        Run
        `java: incompatible types: java.util.List<java.lang.String> cannot be converted to java.util.List<java.lang.Object>`
        - 这表明List<String>对象不能被当成List<Object>对象使用
          - **List<String>类并不是List<Object>类的子类**
            - ==如果Foo是Bar的一个子类型（子类或者子接口），而G是具有泛型声明的类或接口， G<Foo>并不是G<Bar>的子类型！这一点非常值得注意，因为它与我们的习惯看法不同==
            - 数组和泛型有所不同，==那么Foo[]依然是Bar[]的子类型==
      - Java泛型的设计原则
        - 只要代码在编译时没有出现警告，就不会遇到运行时ClassCastException异常
      - 在Java的早期设计中，允许Integer[]数组赋值给Number[]变量存在缺陷，因此Java在泛型设计时进行了改进，它不再允许把List<Integer>对象赋值给List<Number>变量
        #question
        - [oracle11g - Difference between number and integer datatype in oracle dictionary views - Stack Overflow](https://stackoverflow.com/questions/13494010/difference-between-number-and-integer-datatype-in-oracle-dictionary-views)
      - 使用类型通配符 `?`

```java
          public void test(List<?> c){
            for (int i=0; i < c.size(); i++){
              System.out.println(c.get(i));
            }
          }
```

        - 这种带通配符的List仅表示它是各种泛型List的父类，并不能把元素加入到其中
        - 把get()的返回值赋给一个Object类型的变量 / 放在任何希望是Object类型的地方

```java
          // 定义一个抽象类Shape
          public abstract class Shape{
            public abstract void draw(Canvas c);
          }
          // 定义Shape的子类Circle
          public class Circle extends Shape{
            // 实现画图方法，以打印字符串来模拟画图方法实现
            public void draw(Canvas c)
              System.out.println("在画布" + c + "上画一个圆");
          }
          // 定义Shape的子类Rectangle
          public class Rectangle extends Shape{
            // 实现画图方法，以打印字符串来模拟画图方法实现
            public void draw(Canvas c)
              System.out.println("把一个矩形画在画布" + c + "上");
          }
          public class Canvas{
            // 同时在画布上绘制多个形状
            public void drawAll(List<?> shapes){
              // NOTE: 如果使用 List<Shape> 将会在后面调用 add 的时候编译失败
              // 因为 List<Circle>/List<Rectangle> 并不是List<Shape>的子类型
              for (Shape s : shapes){
                Shape s=(Shape)obj;
                s.draw(this);
              }
            }
          }
```

          - A Better Way

```java
            public class Canvas{
              // 同时在画布上绘制多个形状，使用被限制的泛型通配符
              public void drawAll(List<? extends Shape> shapes){
                for (Shape s : shapes)
                  s.draw(this);
              }
            }
```

            - List<?extends Shape>可以表示List<Circle>、List<Rectangle>的父类
              - 只要List后尖括号里的类型是Shape的子类型即可
              - Shape 称为这个通配符(?)的上限 (upper bound)(包含)
            - 因为我们不知道这个受限制的通配符的具体类型，所以不能把Shape对象或其子类的对象加入这个泛型集合中
      - 设定类型通配符的上限

```java
          public class Apple <T extends Number>{
            T col;
            public static void main(String[] args){
              Apple<Integer> ai=new Apple<>();
              Apple<Double> ad=new Apple<>();
              // 下面代码将引发编译异常，下面代码试图把String类型传给T形参
              // 但String不是Number的子类型，所以引起编译错误
              Apple<String> as=new Apple<>();    //①
            }
          }
```

        - 在一种更极端的情况下，程序需要为类型形参设定多个上限 (1个父类上限, 多个接口上限)

```java
            // 表明T类型必须是Number类或其子类，并必须实现java.io.Serializable接口
            public class Apple<T extends Number & java.io.Serializable>{
              // ...
            }
```

            - 如果需要为类型形参指定类上限，类上限必须位于第一位
    - 9.4 泛型方法 (Generic Method, Java 5) #Question
      - 定义

```java
          修饰符 <T , S> 返回值类型 方法名(形参列表) {
            // 方法体...
          }
```

```java
            public class GenericMethodTest{
              // 声明一个泛型方法，该泛型方法中带一个T类型形参
              static <T> void fromArrayToCollection(T[] a, Collection<T> c){
                for (T o : a)
                  c.add(o);
              }
              public static void main(String[] args){
                Object[] oa=new Object[100];
                Collection<Object> co=new ArrayList<>();
                // 下面代码中T代表Object类型
                fromArrayToCollection(oa, co);
                String[] sa=new String[100];
                Collection<String> cs=new ArrayList<>();
                // 下面代码中T代表String类型
                fromArrayToCollection(sa, cs);
                // 下面代码中T代表Object类型
                fromArrayToCollection(sa, co);
                Integer[] ia=new Integer[100];
                Float[] fa=new Float[100];
                Number[] na=new Number[100];
                Collection<Number> cn=new ArrayList<>();
                // 下面代码中T代表Number类型
                fromArrayToCollection(ia, cn);
                // 下面代码中T代表Number类型
                fromArrayToCollection(fa, cn);
                // 下面代码中T代表Number类型
                fromArrayToCollection(na, cn);
                // 下面代码中T代表Object类型
                fromArrayToCollection(na, co);
                // 下面代码中T代表String类型，但na是一个Number数组
                // 因为Number既不是String类型，也不是它的子类
                // 所以出现编译错误
                //fromArrayToCollection(na, cs);
              }
            }
```

      - 泛型方法 vs 类型通配符
        - 大多数时候都可以使用泛型方法来代替类型通配符

```java
            public interface Collection<E>{
              boolean containsAll(Collection<?> c);
              boolean addAll(Collection<? extends E> c);
              //...
            }
```

            - 改写

```java
              public interface Collection<E>{
                boolean <T> containsAll(Collection<T> c);
                boolean <T extends E> addAll(Collection<T> c);
                // ...
              }
```

        - 泛型方法允许类型形参被用来表示
          - 方法的**个或多个参数之间 / 方法返回值**与**参数**之间的类型依赖关系
            - 如果没有这样的类型依赖关系，就不应该使用泛型方法
          - 如果某个方法中一个形参（a）的类型或返回值的类型依赖于另一个形参（b）的类型，则形参（b）的类型声明不应该使用通配符
            - 因为形参（a）或返回值的类型依赖于该形参（b）的类型，如果形参（b）的类型无法确定，程序就无法定义形参（a）的类型。在这种情况下，只能考虑使用在方法签名中声明类型形参——也就是泛型方法

```java
          public class Collections{
            public static <T> void copy(List<T> dest, List<? extends T> src){...}
            //...
          }
```

          - 使用的是类型通配符，而不是泛型方法的原因
            - 该方法无须向src集合中添加元素，也无须修改src集合里的元素
          - 将上面的方法签名改为使用泛型方法，不使用类型通配符

```java
            class Collections{
              public static <T , S extends T> void copy(List<T> dest, List<S> src){...}
              // ...
            }
```

            - S仅使用了一次，**没有其他参数的类型、方法返回值的类型依赖于它，那类型形参S就没有存在的必要**，即可以用通配符来代替S
        - 类型通配符既可以在方法签名中定义形参的类型，也可以用于定义变量的类型；但泛型方法中的类型形参必须在对应方法中显式声明
      - Java 7的“菱形”语法与泛型构造器
        - 如果程序显式指定了泛型构造器中声明的类型形参的实际类型，则不可以使用“菱形”语法

```java
            // MyClass类声明中的E形参是String类型
            // 泛型构造器中声明的T形参是Integer类型
            MyClass<String> mc1=new MyClass<>(5);
            // 显式指定泛型构造器中声明的T形参是Integer类型
            MyClass<String> mc2=new <Integer> MyClass<String>(5);
            // MyClass类声明中的E形参是String类型
            // 如果显式指定泛型构造器中声明的T形参是Integer类型
            // 此时就不能使用“菱形”语法，下面代码是错的
            //MyClass<String> mc3=new <Integer> MyClass<>(5);
```

      - 设定通配符下限 `<? super Type>`

```java
          public static <T> T copy(Collection<T> dest , Collection<? extends T> src){
            T last=null;
            for (T ele : src){
              last=ele;
              dest.add(ele);
            }
            return last;
          }
```

          - bug
            - 程序只能用T来笼统地表示各种src集合的元素类型
              - 当遍历src集合的元素时，src元素的类型是不确定的 (但可以肯定它是T的子类)

```java
                  List<Number> ln=new ArrayList<>();
                  List<Integer> li=new ArrayList<>();
                  // 下面代码引起编译错误
                  Integer last=copy(ln , li);
```

                - 与copy方法签名的形参类型进行对比即得到T的实际类型是Number，而不是Integer类型
                  - copy方法的返回值也是Number类型，而不是Integer类型!
              - 不管src集合元素的类型是什么, 只要 dest 与 src 相同或是前者的父类即可 #understand-in-this-way
                - `<? super Type>`: 表示它必须是Type本身，或是Type的父类

```java
                  public class MyUtils{
                    // 下面dest集合元素的类型必须与src集合元素的类型相同，或是其父类
                    public static <T> T copy(Collection<? super T> dest
                                             , Collection<T> src){
                      T last=null;
                      for (T ele  : src){
                        last=ele;
                        dest.add(ele);
                      }
                      return last;
                    }
                    public static void main(String[] args){
                      List<Number> ln=new ArrayList<>();
                      List<Integer> li=new ArrayList<>();
                      li.add(5);
                      // 此处可准确地知道最后一个被复制的元素是Integer类型
                      // 与src集合元素的类型相同
                      Integer last=copy(ln , li);   //①
                      // 可以保证程序的①处调用后推断出
                      // 最后一个被复制的元素类型是Integer
                      // 而不是笼统的Number类型
                      System.out.println(ln);
                    }
                  }
```

      - 泛型方法与方法重载

```java
          public class MyUtils{
            public static <T> void copy(Collection<T> dest , Collection<? extends T> src)
            {...}   //①
            public static <T> T copy(Collection<? super T> dest , Collection<T> src)
            {...}   //②
          }
```

          - 2个方法
            - 2个参数都是Collection对象
            - 前一个集合里的集合元素类型是后一个集合里集合元素类型的父类
          - 可以共存, 但编译错误, 因为调用时难以分辨是哪一个方法.
    - 9.5 擦除和转换
      - raw type (原始类型)
        - 如果没有为这个泛型类指定实际的类型参数，默认是声明该参数时指定的第一个上限类型
      - 擦除

```java
          class Apple <T extends Number>{
            T size;
            public Apple() {}
            public Apple(T size){
              this.size=size;
            }
            public void setSize(T size){
              this.size=size;
            }
            public T getSize(){
              return this.size;
            }
          }
          public class ErasureTest{
            public static void main(String[] args){
              Apple<Integer> a=new Apple<>(6);   //①
              // a的getSize()方法返回Integer对象
              Integer as=a.getSize();
              // 把a对象赋给Apple变量，丢失尖括号里的类型信息
              Apple b=a;     //②
              // b只知道size的类型是Number
              Number size1=b.getSize();
              // 下面代码引起编译错误
              // 因为 Apple 的类型形参的上限是Number类
              // 所以编译器依然知道b的getSize()方法返回Number类型
              // 但具体是Number的哪个子类就不清楚了
              Integer size2=b.getSize();  //③
            }
          }
```

      - 转换

```java
          public class ErasureTest2{
            public static void main(String[] args){
              List<Integer> li=new ArrayList<>();
              li.add(6);
              li.add(9);
              List list=li;
              // 下面代码引起“未经检查的转换”警告，编译、运行时完全正常
              List<String> ls=list;    //①
              // 只要访问ls里的元素，如下代码将引发运行时异常
              // ClassCastException
              System.out.println(ls.get(0));
            }
          }
```

    - 9.6 泛型与数组
      - 只能声明 `List<String>[]` 形式的数组
        - 不能创建 `ArrayList<String>[10]` 这样的数组对象

```java
        public static void main(String[] args){
          /**
          1. List<String>[] lsa=new List<String>[10];
              代码不能这么写, 编译过不去, java: generic array creation
          2. List<String>[] lsa=new ArrayList[10];
               把ArrayList[10]对象赋给List<String>[]变量时
             会有编译警告 [unchecked] 未经检查的转换
          3. BETTER: Java允许创建无上限的通配符泛型数组
          */  List<?>[] lsa=new ArrayList<?>[10];
          Object[] oa=(Object[]) lsa;
          List<Integer> li=new ArrayList<Integer>();
          li.add(new Integer(3));
          oa[1]=li;
          Object target=lsa[1].get(0);
          if (target instanceof String){
            // 程序需要将lsa的第一个数组元素的第一个集合元素强制类型转换为String类型
            // 通过instanceof运算符来保证它的数据类型
            // Otherwise ClassCastException Exception
            // 下面代码安全了
            String s=(String) target;
          }
        }
```

    - 9.7 本章小结
  - 第 10 章 异常处理
    - 10.1 异常概述
    - 10.2 异常处理机制
    - 10.3 Checked 异常和 Runtime 异常体系
    - 10.4 使用 throw 抛出异常
    - 10.5 Java 的异常跟踪栈
      - 异常的传播
        - 只要异常没有被完全捕获 (包括异常没有被捕获 / 异常被处理后重新抛出了新异常)
          - 异常从发生异常的方法逐渐向外传播
          - 首先传给该方法的调用者，该方法调用者再次传给其调用者……
          - 直至最后传到 main 方法
            - 如果 main 方法依然没有处理该异常, JVM 会中止该程序, 并打印异常的跟踪栈信息
      - **最后发布的程序中，应该避免使用它**
        - 而应该对捕获的异常进行适当的处理，而不是简单地将异常的跟踪栈信息打印出来
    - 10.6 异常处理规则
      - 4 个目标
        - 使程序代码混乱最小化
        - 捕获并保留诊断信息
        - 通知合适的人员
        - 采用合适的方式结束异常活动
      -        1. 不要过度使用异常, **只有对外部的、不能确定和预知的运行时错误才使用异常**
        - 应该避免的 2 种情况
          - 把异常和普通错误混淆在一起，不再编写任何错误处理代码，而是以简单地抛出异常来代替所有的错误处理
          - 使用异常处理来代替流程控制
      -        2. 不要使用过于庞大的try块
        - 把大块的 try 块分割成多个可能出现异常的程序段落，并把它们放在单独的 try 块中，从而分别捕获并处理异常。
      -        3. 避免使用Catch All语句

```java
          try{
            // 可能引发Checked异常的代码
          }
          catch (Throwable t){
            //进行异常处理
            t.printStackTrace();
          }
```

          - 所有的异常都采用相同的处理方式
            - 这将导致无法对不同的异常分情况处理，如果要分情况处理，则需要在catch块中使用分支语句进行控制，这是得不偿失的做法
          - 可能将程序中的错误、Runtime异常等可能导致程序终止的情况全部捕获到，从而“压制”了异常
            - 如果出现了一些“关键”异常，那么此异常也会被“静悄悄”地忽略。
      -        4. 不要忽略捕获到的异常
        - 适当措施
          - 处理异常
            - 对异常进行合适的修复，然后绕过异常发生的地方继续执行；或者用别的数据进行计算，以代替期望的方法返回值；或者提示用户重新操作……总之，对于Checked异常，程序应该尽量修复
          - 重新抛出新异常
            - 把当前运行环境下能做的事情尽量做完，然后进行异常转译，把异常包装成当前层的异常，重新抛出给上层调用者
          - 在合适的层处理异常
            - 如果当前层不清楚如何处理异常，就不要在当前层使用catch语句来捕获该异常，直接使用throws声明抛出该异常，让上层调用者来负责处理该异常。
    - [ ] #gtd/todo 10.7 本章小结
        - 1.改写第4章的五子棋游戏程序，为该程序增加异常处理机制，让程序更加健壮。
      - 2.改写第8章的梭哈游戏程序，为该程序增加异常处理机制。
  - ~~第 11 章 AWT 编程~~
    - 11.1 GUI（图形用户界面）和 AWT
    - 11.2 AWT 容器
    - 11.3 布局管理器
    - 11.4 AWT 常用组件
    - 11.5 事件处理
    - 11.6 AWT 菜单
    - 11.7 在 AWT 中绘图
    - 11.8 处理位图
    - 11.9 剪贴板
    - 11.10 拖放功能
    - 11.11 本章小结
  - ~~第 12 章 Swing 编程~~
    - 12.1 Swing 概述
    - 12.2 Swing 基本组件的用法
    - 12.3 Swing 中的特殊容器
    - 12.4 Swing 简化的拖放功能
    - 12.5 Java 7 新增的 Swing 功能
    - 12.6 使用 JProgressBar、ProgressMonitor 和 BoundedRangeModel 创建进度条
    - 12.7 使用 JSlider 和 BoundedRangeModel 创建滑动条
    - 12.8 使用 JSpinner 和 SpinnerModel 创建微调控制器
    - 12.9 使用 JList、JComboBox 创建列表框
    - 12.10 使用 JTree 和 TreeModel 创建树
    - 12.11 使用 JTable 和 TableModel 创建表格
    - 12.12 使用 JFormattedTextField 和 JTextPane 创建格式文本
    - 12.13 本章小结
  - 第 13 章 MySQL 数据库与 JDBC 编程
    - 13.1 JDBC 基础
      - JDBC (JavaDatabase Connectivity, Java 数据库连接)
        description: 一种可以执行 SQL 语句的 JavaAPI (接口)
        - 使用 JDBC 开发的数据库应用可以**跨平台运行**，而且可以**跨数据库** (标准的 SQL)
      - JDBC 驱动程序
        - 数据库驱动程序负责将 JDBC 调用映射成特定的数据库调用
          - ![image.png](../assets/book\疯狂Java讲义/image_1669970273482_0.png)
          - ODBC, Open Database Connectivity, 开放数据库连接
            - ODBC 和 JDBC 很像，严格地说，应该说 JDBC 模仿了 ODBC 的设计
            - ODBC 也允许应用程序通过一组通用的 API 访问不同的数据库管理系统，从而使得基于 ODBC 的应用程序可以在不同的数据库之间切换。
            - 同样, ODBC 也需要各数据库厂商提供相应的驱动程序, 而 ODBC 则负责管理这些驱动程序
            - #vs JDBC
              - ODBC 更复杂，ODBC 中有几个命令需要配置很多复杂的选项，而 JDBC 则采用简单、直观的方式来管理数据库连接
              - JDBC 比 ODBC 安全性更高，更易部署
          - 类型
            - JDBC–ODBC 桥
              - 最早实现的 JDBC 驱动程序
              - 目的是为了快速推广 JDBC
              - 这种驱动将 JDBC API 映射到 ODBC API
                - JDBC-ODBC 也需要驱动 (由 Sun 公司提供实现)
            - 直接将 JDBC API 映射成数据库特定的客户端 API
              - 这种驱动包含特定数据库的本地代码，用于访问特定数据库的客户端
            - 支持三层结构的 JDBC 访问方式 #jdbc
              description: 表现层（UI）、业务逻辑层（BLL）、数据访问层（DAL）
              - 主要用于 Applet 阶段
              - 通过 Applet 访问数据库
            - 纯 Java 的，直接与数据库实例交互
              - 这种驱动是智能的，它知道数据库使用的底层协议
              - 这种驱动是**目前最流行的 JDBC 驱动**。
    - 13.2 SQL 语法 #mysql #Question (重新深入学一遍)
      - 安装数据库
      - 关系数据库基本概念和 MySQL 基本命令
      - SQL 语句基础
      - DDL 语句
      - 数据库约束
      - 索引
      - DML 语句语法
      - 数据库函数
      - 分组和组函数
      - 多表连接查询
      - 子查询
    - 13.3 JDBC 的典型用法
      - JDBC 常用接口和类简介
        - DriverManager
          description: 用于管理 JDBC 驱动的服务类。程序中使用该类的主要功能是获取 Connection 对象
          - public static synchronized Connection getConnection(String url,String user,String pass) throws SQLException
            - 该方法获得 url 对应数据库的连接
        - Connection
          description: 代表数据库连接对象. 每个 Connection 代表一个物理连接会话
          - Statement createStatement() throws SQLExcetpion
            - 返回一个 Statement 对象
          - PreparedStatement prepareStatement(String sql) throws SQLExcetpion
            - 返回**预编译的 Statement 对象**, 即将 SQL 语句提交到数据库进行预编译
          - CallableStatement prepareCall(String sql) throws SQLExcetpion
            - 返回 CallableStatement 对象，该对象用于**调用存储**过程
          - Savepoint setSavepoint()
            - 创建一个保存点
          - Savepoint setSavepoint(String name)
            - 以指定名字来创建一个保存点
          - void setTransactionIsolation(int level)
            - 设置事务的隔离级别
          - void rollback()
            - 回滚事务
          - void rollback(Savepoint savepoint)
            - 将事务回滚到指定的保存点
          - void setAutoCommit(boolean autoCommit)
            - 关闭自动提交，打开事务
          - void commit()
            - 提交事务
          - NOTE
            - 只有获得了 Statement 之后才可执行 SQL 语句
            - **PreparedStatement、CallableStatement**是 Statement 的子类
            - Java 7
              - setSchema(String schema); getSchema()
              - setNetworkTimeout(Executor executor, int milliseconds)、getNetworkTimeout()
        - Statement
          description: " 用于执行 SQL 语句的工具接口。该对象既可用于执行 DDL、DCL 语句，也可用于执行 DML 语句，还可用于执行 SQL 查询。当执行 SQL 查询时，返回查询到的结果集 "
          - ResultSet executeQuery(String sql)throws SQLException
            - 只能用于执行查询语句
            - 返回查询结果对应的 ResultSet 对象
          - int executeUpdate(String sql)throws SQLExcetion
            - 用于
              - 执行 DML 语句
              - 执行 DDL 语句
                - 执行 DDL 语句将返回 0
            - 返回受影响的行数
          - boolean execute(String sql)throws SQLException
            - 可执行任何 SQL 语句
            - 如果执行后第一个结果为 ResultSet 对象，则返回 true；
            - 如果执行后第一个结果为受影响的行数或没有任何结果，则返回 false
          - Java 7
            - closeOnCompletion()
              - 如果 Statement 执行了该方法，则当所有依赖于该 Statement 的 ResultSet 关闭时，该 Statement 会自动关闭
            - isCloseOnCompletion()
              - 判断该 Statement 是否打开了“closeOnCompletion”
        - PreparedStatement
          description: " 预编译的 Statement 对象。PreparedStatement 是 Statement 的子接口。相对于 Statement 而言，使用 PreparedStatement 执行 SQL 语句时，无须再传入 SQL 语句，只要为预编译的 SQL 语句传入参数值即可 "
          - void setXxx(int parameterIndex,Xxx value)
            - 该方法根据传入参数值的类型不同，需要使用不同的方法
            - 传入的值根据索引传给 SQL 语句中指定位置的参数。
          - executeUpdate()、executeQuery() 和 execute()
            - 这三个方法无须接收 SQL 字符串, 只要为这些命令传入参数即可
              - 因为 PreparedStatement 对象已经预编译了 SQL 命令
          - > [!note]
            > 性能更好
            - 它允许数据库预编译 SQL 语句 (这些 SQL 语句通常带有参数)，以后每次只改变 SQL 命令的参数，避免数据库每次都需要编译 SQL 语句
        - ResultSet
          description: " 结果集对象。该对象包含访问查询结果的方法，ResultSet 可以通过列索引或列名获得列数据。它包含了如下常用方法来移动记录指针 "
          - void close()throws SQLException
            - 释放 ResultSet 对象
          - boolean absolute(int row)
            - 将结果集的记录指针移动到第 row 行
            - 如果 row 是负数，则移动到倒数第 row 行
            - 如果移动后的记录指针指向一条有效记录，则该方法返回 true
          - void beforeFirst()
            - 将 ResultSet 的记录指针定位到首行之前
            - **这是 ResultSet 结果集记录指针的初始状态**——记录指针的起始位置位于第一行之前
          - boolean first()
            - 将 ResultSet 的记录指针定位到首行
            - 如果移动后的记录指针指向一条有效记录，则该方法返回 true
          - boolean previous()
            - 将 ResultSet 的记录指针定位到上一行
            - 如果移动后的记录指针指向一条有效记录，则该方法返回 true
          - boolean next()
            - 将 ResultSet 的记录指针定位到下一行
            - 如果移动后的记录指针指向一条有效记录，则该方法返回 true
          - boolean last()
            - 将 ResultSet 的记录指针定位到最后一行
            - 如果移动后的记录指针指向一条有效记录，则该方法返回 true
          - void afterLast()
            - 将 ResultSet 的记录指针定位到最后一行之后。
          - > [!note]
            > 在 JDK 1.4 以前, ResultSet 的记录指针只能向下移动, 而且每次只能移动一格

          - 当把记录指针移动到指定行之后, ResultSet 可通过来获取当前行、指定列的值
            - getXxx(int columnIndex)
              - 根据列索引获取值
            - getXxx(String columnLabel)
              - 根据列名获取值
            - Java7 **2 个泛型方法**，它们可以获取任意类型的值
              - <T> T getObject(int columnIndex,Class<T> type)
              - <T> T getObject(String columnLabel, Class<T>type)
      - JDBC 编程步骤
        - 1. 加载数据库驱动
          - Class 类的 forName() 静态方法来加载驱动

```java
            // 加载MySQL的驱动
            Class.forName("com.mysql.jdbc.Driver");
            // 加载Oracle的驱动
            Class.forName("oracle.jdbc.driver.OracleDriver");
```

            - 加载驱动时并不是真正使用数据库的驱动类，只是使用**数据库驱动类名的字符串**而已
        - 2. 通过DriverManager获取数据库连接

```java
            //获取数据库连接
            DriverManager.getConnection(String url,String user,String pass)
```

            - 数据库URL通常遵循如下写法: `jdbc:subprotocol:other stuff`
              - jdbc 固定
              - subprotocol指定连接到特定数据库的驱动
              - other和stuff 不固定的
        - 3. 通过Connection对象创建Statement对象
          - createStatement()
            - 创建基本的Statement对象
          - prepareStatement(String sql)
            - 根据传入的SQL语句创建预编译的Statement对象
          - prepareCall(String sql)
            - 根据传入的SQL语句创建CallableStatement对象
        - 4. 使用Statement执行SQL语句
          - execute()
            - 可以执行任何SQL语句，但比较麻烦
          - executeUpdate()
            - 主要用于执行DML和DDL语句
            - 执行DML语句返回受SQL语句影响的行数，执行DDL语句返回0
          - executeQuery()
            - 只能执行查询语句，执行后返回代表查询结果的ResultSet对象
        - 5. 操作结果集
          - 如果执行的SQL语句是查询语句，则执行结果将返回一个ResultSet对象，该对象里保存了SQL语句查询的结果
            - next()、previous()、first()、last()、beforeFirst()、afterLast()、absolute()等移动记录指针的方法
            - getXxx()方法获取记录指针指向行、特定列的值。该方法既可使用列索引作为参数，也可使用列名作为参数。
              - 使用**列索引作为参数性能更好**
              - 使用**列名作为参数可读性更好**
          - ![image.png](../assets/book\疯狂Java讲义/image_1670042902761_0.png)
        - 6. 回收数据库资源，包括关闭ResultSet、Statement和Connection等资源

```java
          public class ConnMySql{
            public static void main(String[] args) throws Exception{
              // 1.加载驱动，使用反射知识，现在记住这么写
              Class.forName("com.mysql.jdbc.Driver");
              try(
                // 2.使用DriverManager获取数据库连接
                // 其中返回的Connection就代表了Java程序和数据库的连接
                // 不同数据库的URL写法需要查驱动文档，用户名、密码由DBA分配
                Connection conn=DriverManager.getConnection(
                  "jdbc:mysql://127.0.0.1:3306/select_test"
                  , "root" , "32147");
                // 3.使用Connection来创建一个Statement对象
                Statement stmt=conn.createStatement();
                // 4.执行SQL语句
                /*
                Statement有三种执行SQL语句的方法：
                1.execute()可执行任何SQL语句-返回一个boolean值
                  如果执行后第一个结果是ResultSet，则返回true，否则返回false
                2.executeQuery()执行select语句 - 返回查询到的结果集
                3.executeUpdate()用于执行DML语句- 返回一个整数
                  代表被SQL语句影响的记录条数
                */
                ResultSet rs=stmt.executeQuery(
                  "select s.* , teacher_name"
                  + " from student_table s , teacher_table t"
                  + " where t.teacher_id=s.java_teacher")
              ){
                // ResultSet有一系列的getXxx(列索引 | 列名)方法，用于获取记录指针
                // 指向行、特定列的值，不断地使用next()将记录指针下移一行
                // 如果移动之后记录指针依然指向有效行，则next()方法返回true
                while(rs.next()){
                  System.out.println(rs.getInt(1) + "\t"
                                     + rs.getString(2) + "\t"
                                     + rs.getString(3) + "\t"
                                     + rs.getString(4));
                }
              }
            }
          }
```

          - 本程序采用了自动关闭资源的 **try语句来关闭各种数据库资源**
            id: 63bf6c48-0fba-45ab-85a0-c2d712743600
            - **Java 7**改写了Connection、Statement、ResultSet等接口
            - 它们都继承了AutoCloseable接口，因此它们都可以由try语句来关闭
    - 13.4 执行SQL语句的方式
      - 使用executeUpdate方法执行DDL和DML语句
        - **当需要把应用程序从开发环境移植到生产环境时，无须修改源代码，只需要修改配置文件 (mysql.ini) 即可**
        - DDL

```java
            public class ExecuteDDL{
              private String driver;
              private String url;
              private String user;
              private String pass;
              public void initParam(String paramFile)
                throws Exception{
                //使用Properties类来加载属性文件
                Properties props=new Properties();
                props.load(new FileInputStream(paramFile));
                driver=props.getProperty("driver");
                url=props.getProperty("url");
                user=props.getProperty("user");
                pass=props.getProperty("pass");
              }
              public void createTable(String sql)throws Exception{
                //加载驱动
                Class.forName(driver);
                try(
                  //获取数据库连接
                  Connection conn=DriverManager.getConnection(url , user , pass);
                  //使用Connection来创建一个Statement对象
                  Statement stmt=conn.createStatement();
                ){
                  //执行DDL语句，创建数据表
                  stmt.executeUpdate(sql);
                }
              }
              public static void main(String[] args) throws Exception{
                ExecuteDDL ed=new ExecuteDDL();
                ed.initParam("mysql.ini");
                ed.createTable("create table jdbc_test "
                               + "( jdbc_id int auto_increment primary key, "
                               + "jdbc_name varchar(255), "
                               + "jdbc_desc text);");
                System.out.println("-----建表成功-----");
              }
            }
```

        - DML

```java
            public class ExecuteDML{
              private String driver;
              private String url;
              private String user;
              private String pass;
              public void initParam(String paramFile)
                throws Exception{
                //使用Properties类来加载属性文件
                Properties props=new Properties();
                props.load(new FileInputStream(paramFile));
                driver=props.getProperty("driver");
                url=props.getProperty("url");
                user=props.getProperty("user");
                pass=props.getProperty("pass");
              }
              public int insertData(String sql)throws Exception{
                //加载驱动
                Class.forName(driver);
                try(
                  //获取数据库连接
                  Connection conn=DriverManager.getConnection(url, user , pass);
                  //使用Connection来创建一个Statement对象
                  Statement stmt=conn.createStatement();
                ){
                  //执行DML语句，返回受影响的记录条数
                  return stmt.executeUpdate(sql);
                }
              }
              public static void main(String[] args)throws Exception{
                ExecuteDML ed=new ExecuteDML();
                ed.initParam("mysql.ini");
                int result=ed.insertData("insert into jdbc_test(jdbc_name,jdbc_desc)"
                                         + "select s.student_name , t.teacher_name "
                                         + "from student_table s , teacher_table t "
                                         + "where s.java_teacher=t.teacher_id;");
                System.out.println("--系统中共有" + result + "条记录受影响--");
              }
            }
```

      - 使用execute方法执行SQL语句
        - 使用execute()方法执行SQL语句的返回值只是boolean值
          - 它表明执行该SQL语句是否返回了ResultSet对象
        - Statement提供了如下两个方法来获取执行结果
          - getResultSet()
            - 获取该Statement执行查询语句所返回的ResultSet对象
          - getUpdateCount()
            - 获取该Statement()执行DML语句所影响的记录行数

```java
          public class ExecuteSQL{
            private String driver;
            private String url;
            private String user;
            private String pass;
            public void initParam(String paramFile)throws Exception{
              // 使用Properties类来加载属性文件
              Properties props=new Properties();
              props.load(new FileInputStream(paramFile));
              driver=props.getProperty("driver");
              url=props.getProperty("url");
              user=props.getProperty("user");
              pass=props.getProperty("pass");
            }
            public void executeSql(String sql)throws Exception{
              // 加载驱动
              Class.forName(driver);
              try(
                // 获取数据库连接
                Connection conn=DriverManager.getConnection(url, user , pass);
                // 使用Connection来创建一个Statement对象
                Statement stmt=conn.createStatement();
              ){
                // 执行SQL语句，返回boolean值表示是否包含ResultSet
                boolean hasResultSet=stmt.execute(sql);
                //如果执行后有ResultSet结果集
                if (hasResultSet){
                  try(
                    // 获取结果集
                    ResultSet rs=stmt.getResultSet()
                  ){
                    // ResultSetMetaData是用于分析结果集的元数据接口
                    ResultSetMetaData rsmd=rs.getMetaData();
                    int columnCount=rsmd.getColumnCount();
                    // 迭代输出ResultSet对象
                    while (rs.next()){
                      // 依次输出每列的值
                      for (int i=0 ; i < columnCount ; i++ ){
                        System.out.print(rs.getString(i + 1) + "\t");
                      }
                      System.out.print("\n");
                    }
                  }
                } else {
                  System.out.println("该SQL语句影响的记录有"
                                     + stmt.getUpdateCount() + "条");
                }
              }
            }
            public static void main(String[] args) throws Exception{
              ExecuteSQL es=new ExecuteSQL();
              es.initParam("mysql.ini");
              System.out.println("------执行删除表的DDL语句-----");
              es.executeSql("drop table if exists my_test");
              System.out.println("------执行建表的DDL语句-----");
              es.executeSql("create table my_test"
                            + "(test_id int auto_increment primary key, "
                            + "test_name varchar(255))");
              System.out.println("------执行插入数据的DML语句-----");
              es.executeSql("insert into my_test(test_name) "
                            + "select student_name from student_table");
              System.out.println("------执行查询数据的查询语句-----");
              es.executeSql("select * from my_test");
            }
          }
```

      - 使用PreparedStatement执行SQL语句
        - 可以使用**占位符**来填充 SQL, 然后预编译后存在PreparedStatement对象中
          - 使用该对象多次高效地执行该语句

```java
          // 创建一个PreparedStatement对象
          pstmt=conn.prepareStatement("insert into student_table values(null,?,1)");
```

          - 在执行SQL语句之前必须为这些参数传入参数值
            - PreparedStatement提供了一系列的setXxx(int index , Xxx value)方法来传入参数值
              - 如果程序很清楚PreparedStatement预编译SQL语句中各参数的类型，则使用相应的setXxx()方法来传入参数即可
              - 如果程序不清楚预编译SQL语句中各参数的类型，则可以使用setObject()方法来传入参数，由PreparedStatement来负责类型转换
        - 使用Statement和PreparedStatement分别插入100条记录的对比
          - 使用Statement需要传入100条SQL语句，但使用PreparedStatement则只需要传入1条预编译的SQL语句，然后100次为该PreparedStatement的参数设值即可

```java
            public class PreparedStatementTest{
              private String driver;
              private String url;
              private String user;
              private String pass;
              public void initParam(String paramFile)throws Exception{
                // 使用Properties类来加载属性文件
                Properties props=new Properties();
                props.load(new FileInputStream(paramFile));
                driver=props.getProperty("driver");
                url=props.getProperty("url");
                user=props.getProperty("user");
                pass=props.getProperty("pass");
                // 加载驱动
                Class.forName(driver);
              }
              public void insertUseStatement()throws Exception{
                long start=System.currentTimeMillis();
                try(
                  // 获取数据库连接
                  Connection conn=DriverManager.getConnection(url, user , pass);
                  // 使用Connection来创建一个Statement对象
                  Statement stmt=conn.createStatement();
                ){
                  // 需要使用100条SQL语句来插入100条记录
                  for (int i=0; i < 100 ; i++ ){
                    stmt.executeUpdate("insert into student_table values("
                                       + " null ,'姓名" + i + "' , 1)");
                  }
                  System.out.println("使用Statement费时:"
                                     + (System.currentTimeMillis() - start));
                }
              }
              public void insertUsePrepare()throws Exception{
                long start=System.currentTimeMillis();
                try(
                  // 获取数据库连接
                  Connection conn=DriverManager.getConnection(url, user , pass);
                  // 使用Connection来创建一个PreparedStatement对象
                  PreparedStatement pstmt=conn.prepareStatement(
                    "insert into student_table values(null,?,1)");
                ){
                  // 100次为PreparedStatement的参数设值，就可以插入100条记录
                  for (int i=0; i < 100 ; i++ ){
                    pstmt.setString(1 , "姓名" + i);
                    pstmt.executeUpdate();
                  }
                  System.out.println("使用PreparedStatement费时:"
                                     + (System.currentTimeMillis() - start));
                }
              }
              public static void main(String[] args) throws Exception{
                PreparedStatementTest pt=new PreparedStatementTest();
                pt.initParam("mysql.ini");
                pt.insertUseStatement();
                pt.insertUsePrepare();
              }
            }
```

        - PerparedStatement 优点
          - 1. 预编译更加高效
          - 2. 不易出错, 无需大量拼接字符串
          -            3. 防止SQL注入

```sql
              -- 利用SQL注入后生成的SQL语句
              select * from jdbc_test where jdbc_name='' or true or '' and jdbc_desc=''
```

        -          >[!note]
          > **SQL语句中的占位符参数只能代替普通值**
          - 不要使用占位符参数代替表名、列名等数据库对象
          - 更不要用占位符参数来代替SQL语句中的insert、select等关键字
      - 使用CallableStatement调用存储过程 #Question

```sql
          delimiter //
              create procedure add_pro(a int , b int, out sum int)
                  begin
                      set sum=a + b;
                  end;
              //
```

```java
          public class CallableStatementTest{
            private String driver;
            private String url;
            private String user;
            private String pass;
            public void initParam(String paramFile)throws Exception{
              // 使用Properties类来加载属性文件
              Properties props=new Properties();
              props.load(new FileInputStream(paramFile));
              driver=props.getProperty("driver");
              url=props.getProperty("url");
              user=props.getProperty("user");
              pass=props.getProperty("pass");
            }
            public void callProcedure()throws Exception{
              // 加载驱动
              Class.forName(driver);
              try(
                // 获取数据库连接
                Connection conn=DriverManager.getConnection(url, user , pass);
                // 使用Connection来创建一个CallableStatement对象
                CallableStatement cstmt=conn.prepareCall(
                  "{call add_pro(?,?,?)}");
              ){
                cstmt.setInt(1, 4);
                cstmt.setInt(2, 5);
                // 注册CallableStatement的第三个参数是int类型
                cstmt.registerOutParameter(3, Types.INTEGER);
                // 执行存储过程
                cstmt.execute();
                // 获取并输出存储过程传出参数的值
                System.out.println("执行结果是: " + cstmt.getInt(3));
              }
            }
            public static void main(String[] args) throws Exception{
              CallableStatementTest ct=new CallableStatementTest();
              ct.initParam("mysql.ini");
              ct.callProcedure();
            }
          }
```

    - 13.5 管理结果集
      - 可滚动、可更新的结果集
        description: 可以使用absolute()、previous()、afterLast()等方法自由移动记录指针的ResultSet被称为可滚动的结果集 (**>= Java5**)
        - 以默认方式打开的ResultSet是不可更新的，如果希望创建可更新的ResultSet，则必须在创建Statement或PreparedStatement时传入如额外的参数 (**resultSetType, resultSetConcurrency**)
          - resultSetType (3)
            description: ResultSet的类型
            - ResultSet.TYPE_FORWARD_ONLY
              - 该常量控制记录指针只能向前移动。这是JDK 1.4以前的默认值
            - ResultSet.TYPE_SCROLL_INSENSITIVE
              - 该常量控制记录指针可以自由移动（可滚动结果集）
              - 但底层数据的改变不会影响ResultSet的内容
            - ResultSet.TYPE_SCROLL_SENSITIVE
              - 该常量控制记录指针可以自由移动（可滚动结果集）
              - 而且底层数据的改变会影响ResultSet的内容
            - >[!note]
              > 可滚动结果集的两个值**需要底层数据库驱动的支持**
              对于有些数据库驱动来说，这两个常量并没有太大的区别
          - resultSetConcurrency(2)
            description: 并发类型
            - ResultSet.CONCUR_READ_ONLY
              - 该常量指示ResultSet是只读的并发模式（默认）
            - ResultSet.CONCUR_UPDATABLE
              - 该常量指示ResultSet是可更新的并发模式
        - 可更新的结果集还需要满足如下 2 个条件
          - 所有数据都应该来自一个表
          - 选出的数据集必须包含主键列

```java
          public class ResultSetTest{
            private String driver;
            private String url;
            private String user;
            private String pass;
            public void initParam(String paramFile)throws Exception{
              // 使用Properties类来加载属性文件
              Properties props=new Properties();
              props.load(new FileInputStream(paramFile));
              driver=props.getProperty("driver");
              url=props.getProperty("url");
              user=props.getProperty("user");
              pass=props.getProperty("pass");
            }
            public void query(String sql)throws Exception{
              // 加载驱动
              Class.forName(driver);
              try(
                // 获取数据库连接
                Connection conn=DriverManager.getConnection(url, user , pass);
                // 使用Connection来创建一个PreparedStatement对象
                // 传入控制结果集可滚动、可更新的参数
                PreparedStatement pstmt=conn.prepareStatement(
                    sql,
                    ResultSet.TYPE_SCROLL_INSENSITIVE,
                    ResultSet.CONCUR_UPDATABLE
                );
                ResultSet rs=pstmt.executeQuery();
              ){
                rs.last();
                int rowCount=rs.getRow();
                for (int i=rowCount; i > 0 ; i-- ){
                  rs.absolute(i);
                  System.out.println(rs.getString(1) + "\t"
                                     + rs.getString(2) + "\t" + rs.getString(3));
                  // 修改记录指针所指记录、第2列的值
                  rs.updateString(2 , "学生名" + i);
                  // 提交修改
                  rs.updateRow();
                }
              }
            }
            public static void main(String[] args) throws Exception{
              ResultSetTest rt=new ResultSetTest();
              rt.initParam("mysql.ini");
              rt.query("select * from student_table");
            }
          }
```

      - 处理Blob (Binary Long Object) 类型数据
        - 数据库
          - 插入 PreparedStatement
            - setBinaryStream(int parameterIndex, InputStream x)
              - 为指定参数传入二进制输入流
              - 可以实现将Blob数据保存到数据库的功能
          - 取出 ResultSet
            - getBlob(int columnIndex)
              - 返回一个Blob对象，Blob对象提供了getBinaryStream()方法来获取该Blob数据的输入流，也可以使用Blob对象提供的getBytes()方法直接取出该Blob对象封装的二进制数
        - e.g. 上传图片到数据库
          - 为了把图片放入数据库，本程序先使用如下SQL语句来建立一个数据表

```sql
              create table img_table(
                img_id int auto_increment primary key,
                img_name varchar(255),
                -- 创建一个mediumblob类型的数据列，用于保存图片数据
                img_data mediumblob
              );
              -- 用 mediumblob 不用 blob 是因为
              -- MySQL数据库里的blob类型最多只能存储 64KB内容，这可能不够满足实际用途
              -- 该类型的数据列可以存储16MB内容
```

          - 实现图片“上传”
            - 实际上就是将图片保存到数据库，并在右边的列表框中显示图片的名字
          - 当用户双击列表框中的图片名时，左边窗口将显示该图片
            - 实质就是根据选中的ID从数据库里查找图片，并将其显示出来

```java
            // 创建一个ImageHolder类，用于封装图片名、图片ID
            class ImageHolder{
                // 封装图片的ID
                private int id;
                // 封装图片的名字
                private String name;
                public ImageHolder(){}
                public ImageHolder(int id , String name){
                    this.id=id;
                    this.name=name;
                }
                // id的setter和getter方法
                public void setId(int id){
                    this.id=id;
                }
                public int getId(){
                    return this.id;
                }
                // name的setter和getter方法
                public void setName(String name){
                    this.name=name;
                }
                public String getName(){
                    return this.name;
                }
                // 重写toString方法，返回图片名
                public String toString(){
                    return name;
                }
            }
```

```java
            // 创建FileFilter的子类，用以实现文件过滤功能
            class ExtensionFileFilter extends FileFilter{
                private String description="";
                private ArrayList<String> extensions=new ArrayList<>();
                // 自定义方法，用于添加文件扩展名
                public void addExtension(String extension){
                    if (!extension.startsWith(".")){
                        extension="." + extension;
                        extensions.add(extension.toLowerCase());
                    }
                }
                // 用于设置该文件过滤器的描述文本
                public void setDescription(String aDescription){
                    description=aDescription;
                }
                // 继承FileFilter类必须实现的抽象方法，返回该文件过滤器的描述文本
                public String getDescription(){
                    return description;
                }
                // 继承FileFilter类必须实现的抽象方法，判断该文件过滤器是否接受该文件
                public boolean accept(File f){
                    // 如果该文件是路径，则接受该文件
                    if (f.isDirectory()) return true;
                    // 将文件名转为小写（全部转为小写后比较，用于忽略文件名大小写）
                    String name=f.getName().toLowerCase();
                    // 遍历所有可接受的扩展名，如果扩展名相同，则该文件就可接受
                    for (String extension : extensions){
                        if (name.endsWith(extension)){
                            return true;
                        }
                    }
                    return false;
                }
            }
```

```java
            public class BlobTest {
                JFrame jf=new JFrame("图片管理程序");
                private static Connection conn;
                private static PreparedStatement insert;
                private static PreparedStatement query;
                private static PreparedStatement queryAll;
                // 定义一个DefaultListModel对象
                private DefaultListModel<ImageHolder> imageModel
                        =new DefaultListModel<>();
                private JList<ImageHolder> imageList=new JList<>(imageModel);
                private JTextField filePath=new JTextField(26);
                private JButton browserBn=new JButton("...");
                private JButton uploadBn=new JButton("上传");
                private JLabel imageLabel=new JLabel();
                // 以当前路径创建文件选择器
                JFileChooser chooser=new JFileChooser(".");
                // 创建文件过滤器
                ExtensionFileFilter filter=new ExtensionFileFilter();
                static{
                    try{
                        Properties props=new Properties();
                        props.load(new FileInputStream("mysql.ini"));
                        String driver=props.getProperty("driver");
                        String url=props.getProperty("url");
                        String user=props.getProperty("user");
                        String pass=props.getProperty("pass");
                        Class.forName(driver);
                        // 获取数据库连接
                        conn=DriverManager.getConnection(url , user , pass);
                        // 创建执行插入的PreparedStatement对象
                        // 该对象执行插入后可以返回自动生成的主键
                        insert=conn.prepareStatement("insert into img_table"
                                + " values(null,?,?)" ,
                                Statement.RETURN_GENERATED_KEYS);
                        // 创建两个PreparedStatement对象，用于查询指定图片，查询所有图片
                        query=conn.prepareStatement("select img_data from img_table"
                                + " where img_id=?");
                        queryAll=conn.prepareStatement("select img_id, "
                                + " img_name from img_table");
                    } catch (Exception e){
                        e.printStackTrace();
                    }
                }
                public void init()throws SQLException{
                    // -------初始化文件选择器--------
                    filter.addExtension("jpg");
                    filter.addExtension("jpeg");
                    filter.addExtension("gif");
                    filter.addExtension("png");
                    filter.setDescription("图片文件(*.jpg,*.jpeg,*.gif,*.png)");
                    chooser.addChoosableFileFilter(filter);
                    // 禁止“文件类型”下拉列表中显示“所有文件”选项
                    chooser.setAcceptAllFileFilterUsed(false);
                    // ---------初始化程序界面---------
                    fillListModel();
                    filePath.setEditable(false);
                    // 只能单选
                    imageList.setSelectionMode(ListSelectionModel.SINGLE_SELECTION);
                    JPanel jp=new JPanel();
                    jp.add(filePath);
                    jp.add(browserBn);
                    browserBn.addActionListener(new ActionListener(){
                        public void actionPerformed(ActionEvent event){
                            // 显示文件对话框
                            int result=chooser.showDialog(jf , "浏览图片文件上传");
                            // 如果用户选择了APPROVE（赞同）按钮，即打开，保存等效按钮
                            if(result==JFileChooser.APPROVE_OPTION){
                                filePath.setText(chooser.getSelectedFile().getPath());
                            }
                        }
                    });
                    jp.add(uploadBn);
                    uploadBn.addActionListener(new ActionListener(){
                        public void actionPerformed(ActionEvent avt){
                            // 如果上传文件的文本框有内容
                            if (filePath.getText().trim().length() > 0){
                                // 将指定文件保存到数据库
                                upload(filePath.getText());
                                // 清空文本框内容
                                filePath.setText("");
                            }
                        }
                    });
                    JPanel left=new JPanel();
                    left.setLayout(new BorderLayout());
                    left.add(new JScrollPane(imageLabel) , BorderLayout.CENTER);
                    left.add(jp , BorderLayout.SOUTH);
                    jf.add(left);
                    imageList.setFixedCellWidth(160);
                    jf.add(new JScrollPane(imageList) , BorderLayout.EAST);
                    imageList.addMouseListener(new MouseAdapter(){
                        public void mouseClicked(MouseEvent e){
                            // 如果双击鼠标
                            if (e.getClickCount() >=2){
                                // 取出选中的List项
                                ImageHolder cur=(ImageHolder)imageList.
                                        getSelectedValue();
                                try{
                                    // 显示选中项对应的Image
                                    showImage(cur.getId());
                                }
                                catch (SQLException sqle){
                                    sqle.printStackTrace();
                                }
                            }
                        }
                    });
                    jf.setSize(620, 400);
                    jf.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
                    jf.setVisible(true);
                }
                // ----------查找img_table表填充ListModel----------
                public void fillListModel()throws SQLException{
                    try(
                            // 执行查询
                            ResultSet rs=queryAll.executeQuery()
                    ){
                        // 先清除所有元素
                        imageModel.clear();
                        // 把查询的全部记录添加到ListModel中
                        while (rs.next()){
                            imageModel.addElement(new ImageHolder(rs.getInt(1)
                                    ,rs.getString(2)));
                        }
                    }
                }
                // ---------将指定图片放入数据库---------
                public void upload(String fileName){
                    // 截取文件名
                    String imageName=fileName.substring(fileName.lastIndexOf('\\')
                            + 1 , fileName.lastIndexOf('.'));
                    File f=new File(fileName);
                    try(
                            InputStream is=new FileInputStream(f)
                    ){
                        // 设置图片名参数
                        insert.setString(1, imageName);
                        // 设置二进制流参数
                        insert.setBinaryStream(2, is , (int)f.length());
                        int affect=insert.executeUpdate();
                        if (affect==1){
                            // 重新更新ListModel，让JList显示最新的图片列表
                            fillListModel();
                        }
                    }catch (Exception e){
                        e.printStackTrace();
                    }
                }
                // ---------根据图片ID来显示图片----------
                public void showImage(int id)throws SQLException{
                    // 设置参数
                    query.setInt(1, id);
                    try(
                            // 执行查询
                            ResultSet rs=query.executeQuery()
                    ){
                        if (rs.next()){
                            // 取出Blob列
                            Blob imgBlob=rs.getBlob(1);
                            // 取出Blob列里的数据
                            ImageIcon icon=new ImageIcon(imgBlob.getBytes(1L
                                    ,(int)    imgBlob.length()));
                            imageLabel.setIcon(icon);
                        }
                    }
                }
                public static void main(String[] args)throws SQLException{
                    new BlobTest().init();
                }
            }
```

      - 使用ResultSetMetaData分析结果集
        - MetaData
          id: 638ae342-457b-47db-ba95-245ca837ec5e
          description: "元数据，即描述其他数据的数据"
          - DatabaseMetaData则封装了描述Database的数据
          - ResultSetMetaData 封装了描述 ResultSet 对象的数据
        - ResultSet里包含一个getMetaData()方法
          - 返回该ResultSet对应的ResultSetMetaData对象
        - ResultSetMetaData对常用的方法
          - int getColumnCount()
            - 返回该ResultSet的列数量
          - String getColumnName(int column)
            - 返回指定索引的列名
          - int getColumnType(int column)
            - 返回指定索引的列类型
        - 查询执行器

```java
            public class QueryExecutor{
              JFrame jf=new JFrame("查询执行器");
              private JScrollPane scrollPane;
              private JButton execBn=new JButton("查询");
              //用于输入查询语句的文本框
              private JTextField sqlField=new JTextField(45);
              private static Connection conn;
              private static Statement stmt;
              //采用静态初始化块来初始化Connection、Statement对象
              static{
                try{
                  Properties props=new Properties();
                  props.load(new FileInputStream("mysql.ini"));
                  String drivers=props.getProperty("driver");
                  String url=props.getProperty("url");
                  String username=props.getProperty("user");
                  String password=props.getProperty("pass");
                  // 加载数据库驱动
                  Class.forName(drivers);
                  // 取得数据库连接
                  conn=DriverManager.getConnection(url, username, password);
                  stmt=conn.createStatement();
                }catch (Exception e){
                  e.printStackTrace();
                }
              }
              // --------初始化界面的方法---------
              public void init(){
                JPanel top=new JPanel();
                top.add(new JLabel("输入查询语句："));
                top.add(sqlField);
                top.add(execBn);
                // 为执行按钮、单行文本框添加事件监听器
                execBn.addActionListener(new ExceListener());
                sqlField.addActionListener(new ExceListener());
                jf.add(top , BorderLayout.NORTH);
                jf.setSize(640, 480);
                jf.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
                jf.setVisible(true);
              }
              // 定义监听器
              class ExceListener implements ActionListener{
                public void actionPerformed(ActionEvent evt){
                  // 删除原来的Jtable（JTable使用scrollPane来包装）
                  if (scrollPane !=null){
                    jf.remove(scrollPane);
                  }
                  try(
                    // 根据用户输入的SQL语句执行查询
                    ResultSet rs=stmt.executeQuery(sqlField.getText());
                  ){
                    // 取出ResultSet的MetaData
                    ResultSetMetaData rsmd=rs.getMetaData();
                    Vector<String> columnNames=new Vector<>();
                    Vector<Vector<String>> data=new Vector<>();
                    // 把ResultSet的所有列名添加到Vector里
                    for (int i=0 ; i < rsmd.getColumnCount(); i++ ){
                      columnNames.add(rsmd.getColumnName(i + 1));
                    }
                    // 把ResultSet的所有记录添加到Vector里
                    while (rs.next()){
                      Vector<String> v=new Vector<>();
                      for (int i=0 ; i < rsmd.getColumnCount(); i++ ){
                        v.add(rs.getString(i + 1));
                      }
                      data.add(v);
                    }
                    // 创建新的JTable
                    JTable table=new JTable(data , columnNames);
                    scrollPane=new JScrollPane(table);
                    // 添加新的Table
                    jf.add(scrollPane);
                    // 更新主窗口
                    jf.validate();
                  }catch (Exception e){
                    e.printStackTrace();
                  }
                }
              }
              public static void main(String[] args){
                new QueryExecutor().init();
              }
            }
```

            - >[!note]
              > **使用ResultSetMetaData需要一定的系统开销**，因此如果在编程过程中已经知道ResultSet里包含多少列，以及每列的列名、类型等信息，就没有必要使用ResultSetMetaData来分析该ResultSet对象了
    - 13.6 Java 7的RowSet 1.1 #Question
      - RowSet接口继承了ResultSet接口, 包含如下常用子接口
        - 长连接
          - JdbcRowSet
        - 可离线
          - CachedRowSet
          - FilteredRowSet
          - JoinRowSet
          - WebRowSet
      - RowSet vs ResultSet
        - RowSet默认是可滚动、可更新、可序列化的结果集
        - 作为JavaBean使用，因此能方便地在网络上传输，用于同步两端的数据
        - 对离线RowSet而言，程序在创建RowSet时已把数据从底层数据库读取到了内存，因此可以充分利用计算机的内存，从而降低数据库服务器的负载，提高程序性能
      - ![image.png](../assets/book\疯狂Java讲义/image_1670066197908_0.png)
      - Java 7新增的RowSetFactory与RowSet
      - 离线RowSet

```java
          public class CachedRowSetTest{
            private static String driver;
            private static String url;
            private static String user;
            private static String pass;
            public void initParam(String paramFile)throws Exception{
              // 使用Properties类来加载属性文件
              Properties props=new Properties();
              props.load(new FileInputStream(paramFile));
              driver=props.getProperty("driver");
              url=props.getProperty("url");
              user=props.getProperty("user");
              pass=props.getProperty("pass");
            }
            public CachedRowSet query(String sql)throws Exception{
              // 加载驱动
              Class.forName(driver);
              // 获取数据库连接
              Connection conn=DriverManager.getConnection(url, user , pass);
              Statement stmt=conn.createStatement();
              ResultSet rs=stmt.executeQuery(sql);
              // 使用RowSetProvider创建RowSetFactory
              RowSetFactory factory=RowSetProvider.newFactory();
              // 创建默认的CachedRowSet实例
              CachedRowSet cachedRs=factory.createCachedRowSet();
              // 使用ResultSet装填RowSet
              cachedRs.populate(rs);   //①
              // 关闭资源
              rs.close();
              stmt.close();
              conn.close();
              return cachedRs;
            }
            public static void main(String[] args)throws Exception {
              CachedRowSetTest ct=new CachedRowSetTest();
              ct.initParam("mysql.ini");
              CachedRowSet rs=ct.query("select * from student_table");
              rs.afterLast();
              // 向前滚动结果集
              while (rs.previous()){
                System.out.println(rs.getString(1)
                                   + "\t" + rs.getString(2)
                                   + "\t" + rs.getString(3));
                if (rs.getInt("student_id")==3){
                  // 修改指定记录行
                  rs.updateString("student_name", "孙悟空");
                  rs.updateRow();
                }
              }
              // 重新获取数据库连接
              Connection conn=DriverManager.getConnection(url
                                                          , user , pass);
              conn.setAutoCommit(false);
              // 把对RowSet所做的修改同步到底层数据库
              rs.acceptChanges(conn);
            }
          }
```

      - 离线RowSet的查询分页
        - 为了防止 SQL 内容过多导致内存溢出
        - CachedRowSet提供了分页功能
          - 一次只装载ResultSet里的某几条记录, 避免CachedRowSet占内存过大的问题
        - APIs
          - populate(ResultSet rs, int startRow)
            - 使用给定的ResultSet装填RowSet
            - 从ResultSet的第startRow条记录开始装填
          - setPageSize(int pageSize)
            - 设置CachedRowSet每次返回多少条记录
          - previousPage()
            - 在底层ResultSet可用的情况下，让CachedRowSet读取上一页记录
          - nextPage()
            - 在底层ResultSet可用的情况下，让CachedRowSet读取下一页记录。

```java
          public class CachedRowSetPage{
            private String driver;
            private String url;
            private String user;
            private String pass;
            public void initParam(String paramFile)throws Exception{
              // 使用Properties类来加载属性文件
              Properties props=new Properties();
              props.load(new FileInputStream(paramFile));
              driver=props.getProperty("driver");
              url=props.getProperty("url");
              user=props.getProperty("user");
              pass=props.getProperty("pass");
            }
            public CachedRowSet query(String sql , int pageSize
                                      , int page)throws Exception{
              // 加载驱动
              Class.forName(driver);
              try(
                // 获取数据库连接
                Connection conn=DriverManager.getConnection(url, user , pass);
                Statement stmt=conn.createStatement();
                ResultSet rs=stmt.executeQuery(sql);
              ){
                // 使用RowSetProvider创建RowSetFactory
                RowSetFactory factory=RowSetProvider.newFactory();
                // 创建默认的CachedRowSet实例
                CachedRowSet cachedRs=factory.createCachedRowSet();
                // 设置每页显示pageSize条记录
                cachedRs.setPageSize(pageSize);
                // 使用ResultSet装填RowSet，设置从第几条记录开始
                cachedRs.populate(rs , (page - 1) * pageSize + 1);
                return cachedRs;
              }
            }
            public static void main(String[] args)throws Exception{
              CachedRowSetPage cp=new CachedRowSetPage();
              cp.initParam("mysql.ini");
              CachedRowSet rs=cp.query("select * from student_table" , 3 , 2);   //①
              // 向后滚动结果集
              while (rs.next()){
                System.out.println(rs.getString(1)
                                   + "\t" + rs.getString(2)
                                   + "\t" + rs.getString(3));
              }
            }
          }
```

          - 30,32 两行粗体字代码就是使用CachedRowSet实现分页的关键代码
          - 39 行代码显示要查询第2页的记录，每页显示3条记录
          - 运行上面程序，可以看到程序只会显示从第4行到第6行的记录，实现了分页
    - 13.7 事务处理
      - 事务的概念和MySQL事务支持
      - JDBC的事务支持
        - Connection默认打开自动提交，即关闭事务
          - 每条SQL语句一旦执行，便会立即提交到数据库，永久生效，无法对回滚

```java
          // 关闭自动提交，开启事务
          conn.setAutoCommit(false);
          // 提交事务
          conn.commit();
          // 回滚事务
          conn.rollback();
```

        - Connection提供了两个方法来设置中间点
          - Savepoint setSavepoint()
            - 在当前事务中创建一个未命名的中间点
            - 返回代表该中间点的Savepoint对象
          - Savepoint setSavepoint(String name)
            - 在当前事务中创建一个具有指定名称的中间点
            - 返回代表该中间点的Savepoint对象
      - 批量更新

```java
          // 保存当前的自动的提交模式
          boolean autoCommit=conn.getAutoCommit();
          // 关闭自动提交
          conn.setAutoCommit(false);
          Statement stmt=conn.createStatement();
          // 使用Statement同时收集多条SQL语句
          stmt.addBatch(sql1);
          stmt.addBatch(sql2);
          stmt.addBatch(sql3);
          //...
          // 同时提交所有的SQL语句
          stmt.executeBatch();
          // 提交修改
          conn.commit();
          // 恢复原有的自动提交模式
          conn.setAutocommit(autoCommit);
```

          - 返回一个int[]数组
            - 因为使用Statement执行DDL、DML语句都将返回一个int值，而执行多条DDL、DML语句将会返回多个int值，多个int值就组成了这个int[]数组
          - 如果在批量更新的addBatch()方法中添加了select查询语句
            - 程序将直接出现错误
    - 13.8 分析数据库信息
      - 使用DatabaseMetaData分析数据库信息

```java
          public class DatabaseMetaDataTest{
            private String driver;
            private String url;
            private String user;
            private String pass;
            public void initParam(String paramFile)throws Exception{
              // 使用Properties类来加载属性文件
              Properties props=new Properties();
              props.load(new FileInputStream(paramFile));
              driver=props.getProperty("driver");
              url=props.getProperty("url");
              user=props.getProperty("user");
              pass=props.getProperty("pass");
            }
            public void info() throws Exception{
              // 加载驱动
              Class.forName(driver);
              try(
                // 获取数据库连接
                Connection conn=DriverManager.getConnection(url, user , pass);
              ){
                // 获取DatabaseMetaData对象
                DatabaseMetaData dbmd=conn.getMetaData();
                // 获取MySQL支持的所有表类型
                ResultSet rs=dbmd.getTableTypes();
                System.out.println("--MySQL支持的表类型信息--");
                printResultSet(rs);
                // 获取当前数据库的全部数据表
                rs=dbmd.getTables(null,null, "%" , new String[]{"TABLE"});
                System.out.println("--当前数据库里的数据表信息--");
                printResultSet(rs);
                // 获取student_table表的主键
                rs=dbmd.getPrimaryKeys(null , null, "student_table");
                System.out.println("--student_table表的主键信息--");
                printResultSet(rs);
                // 获取当前数据库的全部存储过程
                rs=dbmd.getProcedures(null , null, "%");
                System.out.println("--当前数据库里的存储过程信息--");
                printResultSet(rs);
                // 获取teacher_table表和student_table表之间的外键约束
                rs=dbmd.getCrossReference(null,null, "teacher_table"
                                          , null, null, "student_table");
                System.out.println("--teacher_table表和student_table表之间"
                                   + "的外键约束--");
                printResultSet(rs);
                // 获取student_table表的全部数据列
                rs=dbmd.getColumns(null, null, "student_table", "%");
                System.out.println("--student_table表的全部数据列--");
                printResultSet(rs);
              }
            }
            public void printResultSet(ResultSet rs)throws SQLException{
              ResultSetMetaData rsmd=rs.getMetaData();
              // 打印ResultSet的所有列标题
              for (int i=0 ; i < rsmd.getColumnCount() ; i++ ){
                System.out.print(rsmd.getColumnName(i + 1) + "\t");
              }
              System.out.print("\n");
              // 打印ResultSet里的全部数据
              while (rs.next()){
                for (int i=0; i < rsmd.getColumnCount() ; i++ ){
                  System.out.print(rs.getString(i + 1) + "\t");
                }
                System.out.print("\n");
              }
              rs.close();
            }
            public static void main(String[] args)
              throws Exception{
              DatabaseMetaDataTest dt=new DatabaseMetaDataTest();
              dt.initParam("mysql.ini");
              dt.info();
            }
          }
```

      - 使用 (数据库的) 系统表分析数据库信息
        - Mysql 用 information_schema 数据库来保存了大量的系统表, 常用的
          - tables
            - 存放数据库里所有数据表的信息
          - schemata
            - 存放数据库里所有数据库（与MySQL的Schema对应）的信息
          - views
            - 存放数据库里所有视图的信息
          - columns
            - 存放数据库里所有列的信息
          - triggers
            - 存放数据库里所有触发器的信息
          - routines
            - 存放数据库里所有存储过程和函数的信息
          - key_column_usage
            - 存放数据库里所有具有约束的键信息
          - table_constraints
            - 存放数据库里全部约束的表信息
          - statistics
            - 存放数据库里全部索引的信息。
      - 选择合适的分析方式
    - 13.9 使用连接池管理连接
      - 连接池解决方案
        - 程序启动时，系统主动建立足够的数据库连接，并将这些连接组成一个连接池
        - 每次应用程序请求数据库连接时，无须重新打开连接，而是从连接池中取出已有的连接使用，使用完后不再关闭数据库连接，而是直接将连接归还给连接池
      - 资源池 (Resource Pool)
        description: "用于解决资源的频繁请求﹑释放所造成的性能下降"
        - JDBC 2.0规范引入了数据库连接池技术
        - 数据库连接池是Connection对象的工厂
      - DataSource(数据源)接口
        description: "包含连接池和连接池管理两部分; 习惯上经常把DataSource称为连接池"
        - 商用服务器（如WebLogic、WebSphere）等提供实现
        - 开源组织提供实现（如DBCP和C3P0等）
      - DBCP数据源
      - C3P0数据源
    - 13.10 本章小结
      - 1.开发C/S结构的图书销售管理系统，要求实现两个模块：① 后台管理，包括管理种类、管理图书库存（可以上传图书封面图片）、出版社管理；② 销售前台，包括查询图书资料（根据种类、书名、出版社）、销售图书（会影响库存），并记录每条销售信息，统计每天、每月的销售情况。
      - 2.开发MySQL企业管理器，功能类似于SQLyog。
  - 第 14 章 Annotation (注释) #Question
    - Annotation
      description: (>=JDK 5) A kind of **metadata** that makes references to the data itself but is not an actual part of it (Annotation 本身)
      - 这些标记可以在编译、类加载、运行时被读取，并执行相应的处理
      - 程序开发人员可以在不改变原有逻辑的情况下，在源文件中嵌入一些补充的信息
        - 代码分析工具、开发工具和部署工具可以通过这些补充信息进行验证或者进行部署
      - java.lang.Annotation 是一个接口
        - 程序可以通过反射来获取指定程序元素的 Annotation 对象
          - 通过 Annotation 对象来取得注释里的元数据
      - 访问和处理 Annotation 的工具统称 APT (Annotation Processing Tool)
    - 14.1 基本 Annotation
    - 14.2 JDK 的元 Annotation
    - 14.3 自定义 Annotation
    - 14.4 编译时处理 Annotation
    - 14.5 本章小结
  - 第 15 章 输入/输出
    - Point
      - Java 的 IO 流使用了一种装饰器设计模式, 将 IO 流分成
        - 底层节点流
          - 和底层的物理存储节点直接关联
            - 不同的物理节点获取节点流的方式可能存在一定的差异
        - 上层处理流
          - 但程序可以把不同的物理节点流包装成统一的处理流
            - 从而允许程序使用统一的输入、输出代码来读取不同的物理存储节点的资源
      - Java 7 在 java.nio 及其子包下提供了一系列全新的 API, 对原有新 IO 的升级 (NIO 2)
        - 程序可以更高效地进行输入、输出操作
      - 除此之外，Java 对象的序列化机制把内存中的 Java 对象转换成二进制字节流，把 Java 对象存储到磁盘里，或者在网络上传输 Java 对象
        - 这也是 Java 提供分布式编程的重要基础
    - 15.1 File 类
      - 访问文件和目录
        - APIs
          - 访问文件名相关的方法
            - String getName()
              - 返回此 File 对象所表示的文件名或路径名
                （如果是路径，则返回最后一级子路径名）
            - String getPath()
              - 返回此 File 对象所对应的路径名
            - File getAbsoluteFile()
              - 返回此 File 对象所对应的绝对路径所对应的 File 对象
            - String getAbsolutePath()
              - 返回此 File 对象所对应的绝对路径名
            - String getParent()
              - 返回此 File 对象所对应目录（最后一级子目录）的父目录名
            - boolean renameTo(File newName)
              - 重命名此 File 对象所对应的文件或目录
              - 如果重命名成功，则返回 true；否则返回 false
          - 文件检测相关的方法
            - boolean exists()
              - 判断 File 对象所对应的文件或目录是否存在
            - boolean canWrite()
              - 判断 File 对象所对应的文件和目录是否可写
            - boolean canRead()
              - 判断 File 对象所对应的文件和目录是否可读
            - boolean isFile()
              - 判断 File 对象所对应的是否是文件，而不是目录
            - boolean isDirectory()
              - 判断 File 对象所对应的是否是目录，而不是文件
            - boolean isAbsolute()
              - 判断 File 对象所对应的文件或目录是否是绝对路径
              - **该方法消除了不同平台的差异，可以直接判断 File 对象是否为绝对路径**
                - 在 UNIX/Linux/BSD 等系统上，如果路径名开头是一条斜线（/），则表明该 File 对象对应一个绝对路径
                - 在 Windows 等系统上，如果路径开头是盘符，则说明它是一个绝对路径
          - 获取常规文件信息
            - long lastModified()
              - 返回文件的最后修改时间
            - long length()
              - 返回文件内容的长度
          - 文件操作相关的方法
            - boolean createNewFile()
              - 当此 File 对象所对应的文件不存在时，该方法将新建一个该 File 对象所指定的新文件
              - 如果创建成功则返回 true；否则返回 false
            - boolean delete()
              - 删除 File 对象所对应的文件或路径
            - static File createTempFile(String prefix, String suffix)
              - 在默认的临时文件目录中创建一个临时的空文件，使用给定前缀、系统生成的随机数和给定后缀作为文件名
              - 这是一个静态方法，可以直接通过 File 类来调用
              - prefix 参数必须至少是 3 个字节长
                - 建议前缀使用一个短的、有意义的字符串，比如 "hjb" 或 "mail"
              - suffix 参数可以为 null，在这种情况下，将使用默认的后缀“.tmp”
            - static File createTempFile(String prefix, String suffix, File directory)
              - 在 directory 所指定的目录中创建一个临时的空文件，使用给定前缀、系统生成的随机数和给定后缀作为文件名
              - 这是一个静态方法，可以直接通过 File 类来调用
            - void deleteOnExit()
              - 注册一个删除钩子
              - 指定当 Java 虚拟机退出时，删除 File 对象所对应的文件和目录
          - 目录操作相关的方法
            - boolean mkdir()
              - 试图创建一个 File 对象所对应的目录
              - 如果创建成功，则返回 true；否则返回 false
              - 调用该方法时 File 对象必须对应一个路径，而不是一个文件
            - String[] list()
              - 列出 File 对象的所有子文件名和路径名，返回 String 数组
            - File[] listFiles()
              - 列出 File 对象的所有子文件和路径，返回 File 数组
            - static File[] listRoots()
              - 列出系统所有的根路径
              - 这是一个静态方法，可以直接通过 File 类来调用
              - 上面详细列出了 File 类的常用方法，下面程序以几个简单方法来测试一下 File 类的功能

```java
          public class FileTest{
            public static void main(String[] args)
              throws IOException{
              // 以当前路径来创建一个File对象
              File file=new File(".");
              // 直接获取文件名，输出一点
              System.out.println(file.getName());
              // 获取相对路径的父路径可能出错，下面代码输出null
              System.out.println(file.getParent());
              // 获取绝对路径
              System.out.println(file.getAbsoluteFile());
              // 获取上一级路径
              System.out.println(file.getAbsoluteFile().getParent());
              // 在当前路径下创建一个临时文件
              File tmpFile=File.createTempFile("aaa", ".txt", file);
              // 指定当JVM退出时删除该文件
              tmpFile.deleteOnExit();
              // 以系统当前时间作为新文件名来创建新文件
              File newFile=new File(System.currentTimeMillis() + "");
              System.out.println("newFile对象是否存在：" + newFile.exists());
              // 以指定newFile对象来创建一个文件
              newFile.createNewFile();
              // 以newFile对象来创建一个目录，因为newFile已经存在
              // 所以下面方法返回false，即无法创建该目录
              newFile.mkdir();
              // 使用list()方法列出当前路径下的所有文件和路径
              String[] fileList=file.list();
              System.out.println("====当前路径下所有文件和路径如下====");
              for (String fileName : fileList){
                System.out.println(fileName);
              }
              // listRoots()静态方法列出所有的磁盘根路径
              File[] roots=File.listRoots();
              System.out.println("====系统所有根路径如下====");
              for (File root : roots){
                System.out.println(root);
              }
            }
          }
```

          Run

```shell
          .
          null
          /home/bgzocg/demo/tasks/java/basic/.
          /home/bgzocg/demo/tasks/java/basic
          newFile对象是否存在：false
          ====当前路径下所有文件和路径如下====
          src
          .idea
          aaa3502749091242537545.txt
          basic.iml
          out
          readme.md
          1670135197787
          ====系统所有根路径如下====
          /
```

      - 文件过滤器
        - list()方法中可以接收一个FilenameFilter参数
          - 通过该参数可以只列出符合条件的文件
          - FilenameFilter接口里包含了一个accept(File dir, String name)方法
            - 该方法将依次对指定File的所有子目录或者文件进行迭代
            - 如果该方法返回true，则list()方法会列出该子目录或者文件

```java
          public class FilenameFilterTest{
            public static void main(String[] args){
              File file=new File(".");
              String[] nameList=file.list(new MyFilenameFilter());
              for(String name : nameList){
                System.out.println(name);
              }
            }
          }
          // 实现自己的FilenameFilter实现类
          class MyFilenameFilter implements FilenameFilter{
            public boolean accept(File dir, String name){
              // 如果文件名以.java结尾，或者文件对应一个路径，则返回true
              return name.endsWith(".java")
                || new File(name).isDirectory();
            }
          }
```

    - 15.2 理解Java的IO流
      - 流的分类
        - 1.输入流和输出流
        - 2.字节流和字符流
          - 字节流操作的数据单元是 **8位** 的字节
          - 字符流操作的数据单元是 **16位** 的字符
        - 3.节点流和处理流
          - 节点流 / 低级流 (Low Level Stream)
            description: "可以从/向一个特定的IO设备 (如磁盘/网络) 读/写数据的流 "
            - ![image.png](../assets/book\疯狂Java讲义/image_1670136988567_0.png)
          - 处理流 / 高级流 (==装饰器设计模式==)
            description: 用于对一个已存在的流进行连接或封装; 通过封装后的流来实现数据读/写功能
            - ![image.png](../assets/book\疯狂Java讲义/image_1670137003368_0.png)
            - 好处
              - 只要使用相同的处理流，程序就可以采用完全相同的输入/输出代码来访问不同的数据源
                - 随着处理流所包装节点流的变化，程序实际所访问的数据源也相应地发生变化
      - 流的概念模型 -- “水管”
        description: Java把所有设备里的**有序数据**抽象成流模型; 简化了输入/输出处理
        - Java的IO流的40多个类都是从如下4个抽象基类派生的
          - InputStream/Reader
            - 所有输入流的基类，前者是字节输入流，后者是字符输入流
          - OutputStream/Writer
            - 所有输出流的基类，前者是字节输出流，后者是字符输出流
        - 输入流
          - ![image.png](../assets/book\疯狂Java讲义/image_1670137341705_0.png)
          - 输入流使用**隐式的记录指针**来表示当前正准备从哪个“水滴”开始读取
          - 每当程序从InputStream或Reader里取出一个或多个“水滴”后，记录指针自动向后移动
        - 输出流
          - ![image.png](../assets/book\疯狂Java讲义/image_1670137367741_0.png)
          - 输出流同样采用隐式的记录指针来标识当前水滴即将放入的位置
          - 每当程序向OutputStream或Writer里输出一个或多个水滴后，记录指针自动向后移动
        - 流的灵活性
          - 性能的提高
            - 主要以增加缓冲的方式来提高输入/输出的效率
          - 操作的便捷
            - 处理流可能提供了一系列便捷的方法来一次输入/输出大批量的内容，而不是输入/输出一个或多个“水滴”
          - 处理流可以“嫁接”在任何已存在的流的基础之上
            - 这就允许Java应用程序采用相同的代码、透明的方式来访问不同的输入/输出设备的数据流
            - ![image.png](../assets/book/疯狂Java讲义/image_1670137663535_0.png)
              - Java程序无须理会输入/输出节点是磁盘、网络还是其他的输入/输出设备，程序只要将这些节点流包装成处理流，就可以使用相同的输入/输出代码来读写不同的输入/输出设备的数据。
    - 15.3 字节流和字符流
      - InputStream和Reader
        - InputStream APIs
          - int read()
            - 从输入流中读取单个字节（相当于从水管中取出一滴水）
            - 返回所读取的字节数据（字节数据可直接转换为int类型）
          - int read(byte[] b)
            - 从输入流中最多读取b.length个字节的数据，并将其存储在字节数组b中
            - 返回实际读取的字节数
          - int read(byte[] b, int off, int len)
            - 从输入流中最多读取len个字节的数据，并将其存储在数组b中，放入数组b中时，并不是从数组起点开始，而是从off位置开始
            - 返回实际读取的字节数
        - Reader APIs
          - int read()
            - 从输入流中读取单个字符（相当于从水管中取出一滴水）
            - 返回所读取的字符数据（字符数据可直接转换为int类型）
          - int read(char[] cbuf)
            - 从输入流中最多读取cbuf.length个字符的数据，并将其存储在字符数组cbuf中
            - 返回实际读取的字符数
          - int read(char[] cbuf, int off, int len)
            - 从输入流中最多读取len个字符的数据，并将其存储在字符数组cbuf中，放入数组cbuf中时，并不是从数组起点开始，而是从off位置开始
            - 返回实际读取的字符数
        - 直到read(char[] cbuf)或read(byte[] b)方法返回-1，即表明到了**输入流的结束点**
        - 抽象类实例
          - FileInputStream

```java
              public class FileInputStreamTest{
                public static void main(String[] args) throws IOException{
                  // 创建字节输入流
                  FileInputStream fis=new FileInputStream(
                    "FileInputStreamTest.java");
                  // 创建一个长度为1024的“竹筒”
                  byte[] bbuf=new byte[1024];
                  // 用于保存实际读取的字节数
                  int hasRead=0;
                  // 使用循环来重复“取水”过程
                  while ((hasRead=fis.read(bbuf)) > 0 ){
                    // 取出“竹筒”中的水滴（字节），将字节数组转换成字符串输入
                    System.out.print(new String(bbuf , 0 , hasRead ));
                  }
                  // 关闭文件输入流，放在finally块里更安全
                  fis.close();
                }
              }
```

              - ==与JDBC编程一样，程序里打开的文件IO资源不属于内存里的资源，垃圾回收机制无法回收该资源，所以应该**显式关闭文件IO资源**==
          - FileReader

```java
              public class FileReaderTest{
                public static void main(String[] args) throws IOException{
                  try(
                    // 创建字符输入流
                    FileReader fr=new FileReader("FileReaderTest.java");
                  ){
                    // 创建一个长度为32的“竹筒”
                    char[] cbuf=new char[32];
                    // 用于保存实际读取的字符数
                    int hasRead=0;
                    // 使用循环来重复“取水”过程
                    while ((hasRead=fr.read(cbuf)) > 0 ){
                      // 取出“竹筒”中的水滴（字符），将字符数组转换成字符串输入！
                      System.out.print(new String(cbuf , 0 , hasRead));
                    }
                  } catch (IOException ex) {
                    ex.printStackTrace();
                  }
                }
              }
```

              - **Java 7**改写了所有的IO资源类，它们都实现了AutoCloseable接口，因此都可通过自动关闭资源的try语句来关闭这些IO流
          - 除此之外，InputStream和Reader还支持如下几个方法来移动记录指针
            - void mark(int readAheadLimit)
              - 在记录指针当前位置记录一个标记（mark）
            - boolean markSupported()
              - 判断此输入流是否支持mark()操作，即是否支持记录标记
            - void reset()
              - 将此流的记录指针重新定位到上一次记录标记（mark）的位置
            - long skip(long n)
              - 记录指针向前移动n个字节/字符
      - OutputStream和Writer
        - 两个流都提供了如下3个方法
          - void write(int c)
            - 将指定的字节/字符输出到输出流中，其中c既可以代表字节，也可以代表字符
          - void write(byte[]/char[] buf)
            - 将字节数组/字符数组中的数据输出到指定输出流中
          - void write(byte[]/char[] buf, int off, int len)
            - 将字节数组/字符数组中从off位置开始，长度为len的字节/字符输出到输出流中
          - Writer里还包含如下两个方法
            (Writer可以用字符串来代替字符数组，即以String对象作为参数)
            - void write(String str)
              - 将str字符串里包含的字符输出到指定输出流中
            - void write(String str, int off, int len)
              - 将str字符串里从off位置开始，长度为len的字符输出到指定输出流中
          - e.g.
            - 复制文件

```java
                public class FileOutputStreamTest{
                  public static void main(String[] args){
                    try(
                      // 创建字节输入流
                      FileInputStream fis=new FileInputStream(
                        "FileOutputStreamTest.java");
                      // 创建字节输出流
                      FileOutputStream fos=new FileOutputStream("newFile.txt");
                    ){
                      byte[] bbuf=new byte[32];
                      int hasRead=0;
                      // 循环从输入流中取出数据
                      while ((hasRead=fis.read(bbuf)) > 0 ){
                        // 每读取一次，即写入文件输出流，读了多少，就写多少
                        fos.write(bbuf , 0 , hasRead);
                      }
                    }catch (IOException ioe){
                      ioe.printStackTrace();
                    }
                  }
                }
```

            - 直接输出字符串内容

```java
                public class FileWriterTest{
                  public static void main(String[] args){
                    try(
                      FileWriter fw=new FileWriter("poem.txt");
                    ){
                      fw.write("锦瑟 - 李商隐\r\n");
                      fw.write("锦瑟无端五十弦，一弦一柱思华年。\r\n");
                      fw.write("庄生晓梦迷蝴蝶，望帝春心托杜鹃。\r\n");
                      fw.write("沧海月明珠有泪，蓝田日暖玉生烟。\r\n");
                      fw.write("此情可待成追忆，只是当时已惘然。\r\n");
                    } catch (IOException ioe) {
                      ioe.printStackTrace();
                    }
                  }
                }
```

        -          >[!note]
          > Java的很多输出流默认都提供了缓冲功能，其实我们没有必要刻意去记忆哪些流有缓冲功能、哪些流没有，**只要正常关闭所有的输出流即可保证程序正常**
          - 关闭输出流 2 个作用
            - 保证流的物理资源被回收
            - 将输出流缓冲区中的数据flush到物理节点里
              (因为在执行close()方法之前，自动执行输出流的flush()方法)
    - 15.4 输入/输出流体系
      - 处理流的用法
        - 使用处理流来包装节点流，程序通过处理流来执行输入/输出功能，让节点流与底层的I/O设备、文件交互
          - 只要流的构造器参数不是一个物理节点，而是已经存在的流，那么这种流就一定是处理流
          - 所有节点流都是直接以物理IO节点作为构造器参数的
        - 好处
          - 1.对开发人员来说，使用处理流进行输入/输出操作更简单
          - 2.使用处理流的执行效率更高。
        - e.g. PrintStream处理流来包装OutputStream

```java
            public class PrintStreamTest{
              public static void main(String[] args){
                try(
                  FileOutputStream fos=new FileOutputStream("test.txt");
                  PrintStream ps=new PrintStream(fos);
                ){
                  // 使用PrintStream执行输出
                  ps.println("普通字符串");
                  // 直接使用PrintStream输出对象
                  ps.println(new PrintStreamTest());
                }catch (IOException ioe){
                  ioe.printStackTrace();
                }
              }
            }
```

            - 在使用处理流包装了底层节点流之后，关闭输入/输出流资源时，只要关闭最上层的处理流即可
              - 关闭最上层的处理流时，系统会自动关闭被该处理流包装的节点流
      - 输入/输出流体系, 常用的流分类
        - java.io.*
          ![image.png](../assets/book/疯狂Java讲义/image_1670150536232_0.png)
          **粗体字**: 节点流，必须直接与指定的物理节点关联;
          *斜体字*: 抽象基类，无法直接创建实例
          - Java为了实现更好的设计，它把IO流按功能分成了许多类，而每类中又分别提供了字节流和字符流（当然有些流无法提供字节流，有些流无法提供字符流），字节流和字符流里又分别提供了输入流和输出流两大类，所以导致整个输入/输出流体系格外复杂
        - 一个规则
          - 如果进行输入/输出的内容是文本内容，则应该考虑使用字符流
          - 如果进行输入/输出的内容是二进制内容，则应该考虑使用字节流
        - 其他包下
          - 诸如AudioInputStream、CipherInputStream、DeflaterInputStream、ZipInputStream等具有访问音频文件、加密/解密、压缩/解压等功能的字节流
      - 转换流
        - Java 没有把字符流转换成字节流的转换流
          - 字节流比字符流的使用范围更广，但字符流比字节流操作方便
          - 如果有一个流已经是字符流了，也就是说，是一个用起来更方便的流，为什么要转换成字节流呢？
            - 反之，如果现在有一个字节流，但我们知道这个字节流的内容都是文本内容，那么把它转换成字符流来处理就会更方便一些，所以Java只提供了将字节流转换成字符流的转换流，没有提供将字符流转换成字节流的转换流
        - e.g. 获取键盘输入为例
          - Java使用System.in代表标准输入(键盘输入)，但它是InputStream类的实例，使用不太方便，而且键盘输入内容都是文本内容，所以**可以使用InputStreamReader将其转换成字符输入流**，普通的Reader读取输入内容时依然不太方便，我们可以**将普通的Reader再次包装成BufferedReader**，利用BufferedReader的readLine()方法可以一次读取一行内容

```java
            public class KeyinTest{
              public static void main(String[] args){
                try(
                  // 将Sytem.in对象转换成Reader对象
                  InputStreamReader reader=new InputStreamReader(System.in);
                  //将普通的Reader包装成BufferedReader
                  BufferedReader br=new BufferedReader(reader);
                ){
                  String buffer=null;
                  //采用循环方式来逐行地读取
                  while ((buffer=br.readLine()) !=null){
                    //如果读取的字符串为"exit"，则程序退出
                    if (buffer.equals("exit")){
                      System.exit(1);
                    }
                    //打印读取的内容
                    System.out.println("输入内容为:" + buffer);
                  }
                } catch (IOException ioe) {
                  ioe.printStackTrace();
                }
              }
            }
```

      - 推回输入流
        - `PushbackInputStream` / `PushbackReader`
          - void unread(byte[]/char[] buf)
            - 将一个字节/字符数组内容推回到推回缓冲区里，从而允许重复读取刚刚读取的内容
          - void unread(byte[]/char[] b, int off, int len)
            - 将一个字节/字符数组里从off开始，长度为len字节/字符的内容推回到推回缓冲区里，从而允许重复读取刚刚读取的内容
          - void unread(int b)
            - 将一个字节/字符推回到推回缓冲区里，从而允许重复读取刚刚读取的内容

```java
          public class PushbackTest{
            public static void main(String[] args){
              try(
                // 创建一个PushbackReader对象，指定推回缓冲区的长度为64
                PushbackReader pr=new PushbackReader(new FileReader(
                  "PushbackTest.java") , 64);
              ){
                char[] buf=new char[32];
                // 用以保存上次读取的字符串内容
                String lastContent="";
                int hasRead=0;
                // 循环读取文件内容
                while ((hasRead=pr.read(buf)) > 0){
                  // 将读取的内容转换成字符串
                  String content=new String(buf , 0 , hasRead);
                  int targetIndex=0;
                  // 将上次读取的字符串和本次读取的字符串拼起来
                  // 查看是否包含目标字符串, 如果包含目标字符串
                  if ((targetIndex=(lastContent + content)
                       .indexOf("new PushbackReader")) > 0){
                    // 将本次内容和上次内容一起推回缓冲区
                    pr.unread((lastContent + content).toCharArray());
                    // 指定读取前面len个字符
                    int len=targetIndex > 32 ? 32 : targetIndex;
                    // 再次读取指定长度的内容（就是目标字符串之前的内容）
                    pr.read(buf , 0 , len);
                    // 打印读取的内容
                    System.out.print(new String(buf , 0 ,len));
                    System.exit(0);
                  } else {
                    // 打印上次读取的内容
                    System.out.print(lastContent);
                    // 将本次内容设为上次读取的内容
                    lastContent=content;
                  }
                }
              }catch (IOException ioe){
                ioe.printStackTrace();
              }
            }
          }
```

    - 15.5 重定向标准输入/输出
      - 在System类里提供了如下3个重定向标准输入/输出的方法
        - static void setErr(PrintStream err)
          - 重定向 “标准”错误输出流
        - static void setIn(InputStream in)
          - 重定向“标准”输入流
        - static void setOut(PrintStream out)
          - 重定向 “标准”输出流
      - e.g.
        - 重定向标准输入

```java
            public class RedirectIn{
              public static void main(String[] args){
                try(
                  FileInputStream fis=new FileInputStream("RedirectIn.java");
                ){
                  // 将标准输入重定向到fis输入流
                  System.setIn(fis);
                  // 使用System.in创建Scanner对象，用于获取标准输入
                  Scanner sc=new Scanner(System.in);
                  // 增加下面一行只把回车作为分隔符
                  sc.useDelimiter("\n");
                  // 判断是否还有下一个输入项
                  while(sc.hasNext()){
                    // 输出输入项
                    System.out.println("键盘输入的内容是：" + sc.next());
                  }
                } catch (IOException ex){
                  ex.printStackTrace();
                }
              }
            }
```

        - 重定向标准输出

```java
            public class RedirectOut{
              public static void main(String[] args){
                try(
                  // 一次性创建PrintStream输出流
                  PrintStream ps=new PrintStream(new FileOutputStream("out.txt"));
                ){
                  // 将标准输出重定向到ps输出流
                  System.setOut(ps);
                  // 向标准输出输出一个字符串
                  System.out.println("普通字符串");
                  // 向标准输出输出一个对象
                  System.out.println(new RedirectOut());
                }catch (IOException ex){
                  ex.printStackTrace();
                }
              }
            }
```

    - 15.6 Java虚拟机读写其他进程的数据
    - 15.7 RandomAccessFile
      description: "如果我们希望只访问文件部分内容，而不是把文件从头读到尾，使用RandomAccessFile将是更好的选择"
      - APIs
        - long getFilePointer()
          - 返回文件记录指针的当前位置
        - void seek(long pos)
          - 将文件记录指针定位到pos位置
        - RandomAccessFile 构造器 Mode
          - "r"
            - 以只读方式打开指定文件
            - 如果试图对该RandomAccessFile执行写入方法,都将抛出IOException异常
          - "rw"
            - 以读、写方式打开指定文件
            - 如果该文件尚不存在，则尝试创建该文件
          - "rws"
            - 以读、写方式打开指定文件
            - 相对于"rw"模式，还要求对文件的内容或元数据的每个更新都同步写入到底层存储设备
          - "rwd"
            - 以读、写方式打开指定文件
            - 相对于"rw"模式，还要求对文件内容的每个更新都同步写入到底层存储设备。
      - e.g.
        - 程序将从300字节处开始读、写

```java
            public class RandomAccessFileTest{
              public static void main(String[] args){
                try(
                  RandomAccessFile raf=new RandomAccessFile(
                    "RandomAccessFileTest.java" , "r");
                ){
                  // 获取RandomAccessFile对象文件指针的位置，初始位置是0
                  System.out.println("RandomAccessFile的文件指针的初始位置："
                                     + raf.getFilePointer());
                  // 移动raf的文件记录指针的位置
                  raf.seek(300);
                  byte[] bbuf=new byte[1024];
                  // 用于保存实际读取的字节数
                  int hasRead=0;
                  // 使用循环来重复“取水”过程
                  while ((hasRead=raf.read(bbuf)) > 0 ){
                    // 取出“竹筒”中的水滴（字节），将字节数组转换成字符串输入
                    System.out.print(new String(bbuf , 0 , hasRead ));
                  }
                }catch (IOException ex){
                  ex.printStackTrace();
                }
              }
            }
```

        - 追加内容
          - 程序应该先将记录指针移动到文件最后，然后开始向文件中输出内容

```java
            public class AppendContent{
              public static void main(String[] args){
                try(
                  //以读、写方式打开一个RandomAccessFile对象
                  RandomAccessFile raf=new RandomAccessFile("out.txt" , "rw");
                ){
                  //将记录指针移动到out.txt文件的最后
                  raf.seek(raf.length());
                  raf.write("追加的内容！\r\n".getBytes());
                }catch (IOException ex){
                  ex.printStackTrace();
                }
              }
            }
```

        - 向指定文件、指定位置插入内容
          - 程序需要先把插入点后面的内容读入缓冲区
            - 等把需要插入的数据写入文件后，再将缓冲区的内容追加到文件后面

```java
            public class InsertContent{
              public static void insert(String fileName , long pos
                                    , String insertContent) throws IOException{
                File tmp=File.createTempFile("tmp" , null);
                tmp.deleteOnExit();
                try(
                  RandomAccessFile raf=new RandomAccessFile(fileName , "rw");
                  // 创建一个临时文件来保存插入点后的数据
                  FileOutputStream tmpOut=new FileOutputStream(tmp);
                  FileInputStream tmpIn=new FileInputStream(tmp);
                ){
                  raf.seek(pos);
                  // ------下面代码将插入点后的内容读入临时文件中保存------
                  byte[] bbuf=new byte[64];
                  // 用于保存实际读取的字节数
                  int hasRead=0;
                  // 使用循环方式读取插入点后的数据
                  while ((hasRead=raf.read(bbuf)) > 0 ){
                    // 将读取的数据写入临时文件
                    tmpOut.write(bbuf , 0 , hasRead);
                  }
                  // ----------下面代码用于插入内容----------
                  // 把文件记录指针重新定位到pos位置
                  raf.seek(pos);
                  // 追加需要插入的内容
                  raf.write(insertContent.getBytes());
                  // 追加临时文件中的内容
                  while ((hasRead=tmpIn.read(bbuf)) > 0 ){
                    raf.write(bbuf , 0 , hasRead);
                  }
                }
              }
              public static void main(String[] args)
                throws IOException{
                insert("InsertContent.java" , 45 , "插入的内容\r\n");
              }
            }
```

        - #project 多线程断点的网络下载工具
          - 可通过RandomAccessFile类来实现
          - 所有的下载工具在下载开始时都会建立两个文件
            - 一个是与被下载文件大小相同的空文件
            - 一个是记录文件指针的位置文件
          - 下载工具用多条线程启动输入流来读取网络数据，并使用RandomAccessFile将从网络上读取的数据写入前面建立的空文件中，每写一些数据后，记录文件指针的文件就分别记下每个RandomAccessFile当前的文件指针位置
            - 网络断开后，再次开始下载时，每个RandomAccessFile都根据记录文件指针的文件中记录的位置继续向下写数据
    - 15.8 对象序列化 #Question
      - 目标 - 允许把内存中的Java对象转换成平台无关的二进制流, 其他程序获得这种二进制流，都可以将这种二进制流恢复成原来的Java对象
        - 从而允许把这种二进制流持久地保存在**磁盘**上
        - 通过网络将这种二进制流传输到另一个**网络节点**
      - 序列化的含义和意义
        - 对象的序列化 (Serialize)
          - 将一个Java对象写入IO流中
        - 对象的反序列化 (Deserialize)
          - 从IO流中恢复该Java对象
        - 为了让某个类是可序列化的，该类必须实现如下两个接口之一
          (**标记接口, 无须实现任何方法，只表明该类的实例是可序列化的**)
          - Serializable
          - Externalizable
        -          >[!note]
          > **序列化机制是Java EE平台的基础**, 建议程序创建的每个JavaBean类都实现Serializable
          - 所有可能在网络上传输的对象的类都应该是可序列化的，否则程序将会出现异常
            - 比如**RMI (Remote Method Invoke，即远程方法调用，JavaEE的基础)** 过程中的参数和返回值
              - RMI又是Java EE技术的基础
              - 所有的分布式应用常常需要跨平台、跨网络，所以要求所有传递的参数、返回值必须实现序列化
          - 所有需要保存到磁盘里的对象的类都必须可序列化
            - 比如Web应用中需要保存到HttpSession或ServletContext属性的Java对象
      - 使用对象流实现序列化
        - 2 个步骤 序列化
          - 1.创建一个ObjectOutputStream，这个输出流是一个处理流，所以必须建立在其他节点流的基础之上

```java
              // 创建个ObjectOutputStream输出流
              ObjectOutputStream oos=new ObjectOutputStream(
                new FileOutputStream("object.txt"));
```

          - 2.调用ObjectOutputStream对象的writeObject()方法输出可序列化对象

```java
              // 将一个Person对象输出到输出流中
              oos.writeObject(per);
```

        - 2 个步骤 反序列化
          - 1.创建一个ObjectInputStream输入流，这个输入流是一个处理流，所以必须建立在其他节点流的基础之上

```JAVA
              // 创建一个ObjectInputStream输入流
              ObjectInputStream ois=new ObjectInputStream(
                new FileInputStream("object.txt"));
```

          - 2.调用ObjectInputStream对象的readObject()方法读取流中的对象
            - 该方法返回一个Object类型的Java对象
            - 如果程序知道该Java对象的类型，则可以将该对象强制类型转换成其真实的类型

```JAVA
              // 从输入流中读取一个Java对象，并将其强制类型转换为Person类
              Person p=(Person)ois.readObject();
```

        - e.g. Serializable Person

```java
            public class Person
              implements java.io.Serializable{
              private String name;
              private int age;
              // 注意此处没有提供无参数的构造器
              public Person(String name , int age){
                System.out.println("有参数的构造器");
                this.name=name;
                this.age=age;
              }
              // 省略name与age的setter和getter方法
              // ...
            }
```

```JAVA
            public class WriteObject{
              public static void main(String[] args){
                try(
                  // 创建一个ObjectOutputStream输出流
                  ObjectOutputStream oos=new ObjectOutputStream(
                    new FileOutputStream("object.txt"));
                ){
                  Person per=new Person("孙悟空", 500);
                  // 将per对象写入输出流
                  oos.writeObject(per);
                } catch (IOException ex) {
                  ex.printStackTrace();
                }
              }
            }
```

          - 反序列化

```java
            public class ReadObject{
              public static void main(String[] args){
                try(
                  // 创建一个ObjectInputStream输入流
                  ObjectInputStream ois=new ObjectInputStream(
                    new FileInputStream("object.txt"));
                ){
                  // 从输入流中读取一个Java对象，并将其强制类型转换为Person类
                  Person p=(Person)ois.readObject();
                  System.out.println("名字为：" + p.getName()
                                     + "\n年龄为：" + p.getAge());
                }catch (Exception ex){
                  ex.printStackTrace();
                }
              }
            }
```

          - 反序列化读取的仅仅是Java对象的数据
            - 不是Java类，因此采用反序列化恢复Java对象时，必须提供该Java对象所属类的class文件，否则将会引发ClassNotFoundException异常
          - 反序列化机制无须通过构造器来初始化Java对象
            - Person类只有一个有参数的构造器，没有无参数的构造器，而且该构造器内有一个普通的打印语句。当反序列化读取Java对象时，并没有看到程序调用该构造器
          - 如果使用序列化机制向文件中写入了多个Java对象，使用反序列化机制恢复对象时必须按实际写入的顺序读取
          - 当一个可序列化类有多个父类时（包括直接父类和间接父类），这些父类要么有无参数的构造器，要么也是可序列化的, 否则反序列化时将抛出InvalidClassException异常
            - 如果父类是不可序列化的，只是带有无参数的构造器，则该父类中定义的Field值不会序列化到二进制流中
      - 对象引用的序列化
      - 自定义序列化
      - 另一种自定义序列化机制
    - 15.9 NIO
    - 15.10 Java 7的NIO.2
    - 15.11 本章小结
      - 1.编写仿Windows记事本的小程序
      - 2.编写一个命令行工具，这个命令行工具就像Windows提供的cmd命令一样，可以执行各种常见的命令，如dir、md、copy、move等
      - 3.完善第12章的仿EditPlus的编辑器，提供文件的打开、保存等功能
  - 第 16 章 多线程
    - 16.1 线程概述
    - 16.2 线程的创建和启动
    - 16.3 线程的生命周期
    - 16.4 控制线程
    - 16.5 线程同步
    - 16.6 线程通信
    - 16.7 线程组和未处理的异常
    - 16.8 线程池
    - 16.9 线程相关类
    - 16.10 本章小结
  - 第 17 章 网络编程
    - 17.1 网络编程的基础知识
    - 17.2 Java 的基本网络支持
    - 17.3 基于 TCP 协议的网络编程
    - 17.4 基于 UDP 协议的网络编程
    - 17.5 使用代理服务器
    - [ ] #gtd/todo 17.6 本章小结
        - 1.开发仿 FlashGet 的断点续传、多线程下载工具
      - 2.开发基于 C/S 结构的游戏大厅
      - 3.扩展 LanTalk 开发局域网内的即时通信、数据传输工具
  - 第 18 章 类加载机制与反射
    - Java 类加载器除了根类加载器之外，其他类加载器都是使用 Java 语言编写
      - 程序员完全可以开发自己的类加载器
        - 通过使用自定义类加载器，可以完成一些特定的功能
    - 18.1 类的加载、连接和初始化
      - JVM 和类
        - 当系统出现以下几种情况时，JVM 进程将被终止
          - 程序运行到最后正常结束
          - 程序运行到使用 System.exit() 或 Runtime.getRuntime().exit() 代码处结束程序
          - 程序执行过程中遇到未捕获的异常或错误而结束
          - 程序所在平台强制结束了 JVM 进程
      - 类的加载 -> 系统为之生成**一个对应的 Class 对象**
        - 当程序主动使用某个类时
          - 如果该类还未被加载到内存中，则系统会通过**加载、连接、初始化 3 个步骤来对该类进行初始化** (类加载或类初始化)
        - 类加载是将类的 class 文件读入内存, 并为之创建一个 java.lang.Class 对象
          - 程序中使用任何类时, 系统都会为之建立一个 java.lang.Class 对象
        - 类也是一种对象
          - 就像我们说概念主要用于定义、描述其他事物，但概念本身也是一种事物，那么概念本身也需要被描述
          - 每个类是一批具有相同特征的对象的抽象（或者说概念），而系统中所有的类实际上也是实例，它们都是 java.lang.Class 的实例
        - 由**类加载器**完成，类加载器通常由 JVM 提供，这些类加载器也是前面所有程序运行的基础，JVM 提供的这些类加载器通常被称为**系统类加载器**
          - 开发者可以通过继承 ClassLoader 基类来创建自己的类加载器
          - 通过使用不同的类加载器，可以从不同来源加载类的二进制数据
        - 加载类的 4 种来源
          - **[绝大部分]** 从本地文件系统加载 class 文件
          - **[常见]** 从 JAR 包加载 class 文件
          - 通过网络加载 class 文件
          - 把一个 Java 源文件动态编译，并执行加载
        - Java 虚拟机规范允许系统预先加载某些类
      - 类的连接 (3)
        - 验证
          - 用于检验被加载的类是否有正确的内部结构，并和其他类协调一致
        - 准备
          - 负责为类的静态 Field 分配内存，并设置默认初始值
        - 解析
          - 将类的二进制数据中的符号引用替换成直接引用
      - 类初始化的时机
        - 虚拟机负责, 主要就是对静态 Field 进行初始化
        - 指定初值有 2 种方式
          - 声明静态 Field 时指定初始值
          - 使用静态初始化块为静态 Field 指定初始值
        - JVM 初始化一个类 3 个步骤
          - 1.假如这个类还没有被加载和连接，则程序先加载并连接该类
          - 2.假如该类的直接父类还没有被初始化，则先初始化其直接父类
            - 递归执行上层类
              - 使得 JVM 最先初始化的总是 java.lang.Object 类
          - 3.假如类中有初始化语句，则系统依次执行这些初始化语句
      - 类初始化的时机
        - 6 种情况下, Java 会初始化类或接口
          - 创建类的实例
            - new 操作符来创建实例
            - 反射来创建实例
            - 反序列化的方式来创建实例
          - 调用某个类的静态方法
          - 访问某个类或接口的静态 Field，或为该静态 Field 赋值
          - 使用反射方式来强制创建某个类或接口对应的 java.lang.Class 对象
            - 例如代码：Class.forName("Person")
              - 如果系统还未初始化 Person 类，则这行代码将会导致该 Person 类被初始化，并返回 Person 类对应的 java.lang.Class 对象
          - 初始化某个类的子类
            - 当初始化某个类的子类时，该子类的所有父类都会被初始化
          - 直接使用 java.exe 命令来运行某个主类
            - 当运行某个主类时，程序会先初始化该主类
        - > [!note]
          > “宏变量” 不会被初始化

        - 当使用 ClassLoader 类的 loadClass() 方法来加载某个类时，该方法只是加载该类，并不会执行该类的初始化
          - 使用 Class 的 forName() 静态方法才会导致强制初始化该类
    - 18.2 类加载器
      - 类加载器简介
        - 负责将.class 文件（可能在磁盘上，也可能在网络上）加载到内存中，并为之生成对应的 java.lang.Class 对象
        - 一旦一个类被载入 JVM 中，同一个类就不会被再次载入了
          - “同一个类” 范围
            - 在 Java 中，一个类用其**全限定类名**（包括包名和类名）作为标识
            - 在 JVM 中，一个类用其**全限定类名和其类加载器**作为其唯一标识
            - 例如，如果在 pg 的包中有一个名为 Person 的类，被类加载器 ClassLoader 的实例 kl 负责加载，则该 Person 类对应的 Class 对象在 JVM 中表示为（Person、pg、kl）
              - 这意味着两个类加载器加载的同名类：（Person、pg、kl）和（Person、pg、kl2）是不同的、它们所加载的类也是完全不同、互不兼容的
          - 当 JVM 启动时，会形成由 3 个类加载器组成的初始类加载器层次结构
            - Bootstrap ClassLoader
              - 引导/原始/根类加载器
              - 负责加载 Java 的核心类
              - 在 Sun 的 JVM 中，当执行 java.exe 命令时，使用 -Xbootclasspath 选项或使用 -D 选项指定 sun.boot.class.path 系统属性值可以指定加载附加的类
              - 根类加载器非常特殊，它并不是 java.lang.ClassLoader 的子类，而是由 JVM 自身实现的
              - e.g. 获得根类加载器所加载的核心类库

```java
                  public class BootstrapTest{
                    public static void main(String[] args){
                      // 获取根类加载器所加载的全部URL数组
                      URL[] urls=sun.misc.Launcher.
                        getBootstrapClassPath().getURLs();
                      // 遍历、输出根类加载器加载的全部URL
                      for (int i=0; i < urls.length; i++){
                        System.out.println(urls[i].toExternalForm());
                      }
                    }
                  }
```

                  Run

```shell
                  file:/usr/lib/jvm/java-8-openjdk-amd64/jre/lib/resources.jar
                  file:/usr/lib/jvm/java-8-openjdk-amd64/jre/lib/rt.jar
                  file:/usr/lib/jvm/java-8-openjdk-amd64/jre/lib/sunrsasign.jar
                  file:/usr/lib/jvm/java-8-openjdk-amd64/jre/lib/jsse.jar
                  file:/usr/lib/jvm/java-8-openjdk-amd64/jre/lib/jce.jar
                  file:/usr/lib/jvm/java-8-openjdk-amd64/jre/lib/charsets.jar
                  file:/usr/lib/jvm/java-8-openjdk-amd64/jre/lib/jfr.jar
                  file:/usr/lib/jvm/java-8-openjdk-amd64/jre/classes
```

                  - 读者应该明白为什么程序中可以使用String、System这些核心类库
                    - 因为这些核心类库都在 `rt.jar` 文件中
                      - Java基础类库
                      - Java doc里面看到的所有的类的class文件
            - Extension ClassLoader
              - 扩展类加载器
              - 负责加载JRE的扩展目录 (%JAVA_HOME%/jre/lib/ext 或者 由java.ext.dirs系统属性指定的目录) 中JAR包的类
              - 通过这种方式，就可以为Java扩展核心类以外的新功能，只要我们把自己开发的类打包成JAR文件，然后放入 %JAVA_HOME%/jre/lib/ext路径即可
            - System ClassLoader
              - 系统类加载器
              - 负责在JVM启动时加载来自java命令的-classpath选项、java.class.path系统属性，或CLASSPATH环境变量所指定的JAR包和类路径
              - 程序可以通过ClassLoader的静态方法getSystemClassLoader()来获取系统类加载器
                - 如果没有特别指定，则用户自定义的类加载器都以类加载器作为父加载器
      - 类加载机制
        - JVM的主要有 3 种类加载机制
          - 全盘负责
            - 当一个类加载器负责加载某个Class时，该Class所依赖的和引用的其他Class也将由该类加载器负责载入，除非显式使用另外一个类加载器来载入
          - 父类委托
            - 先让parent (父)类加载器试图加载该Class
              - 只有在父类加载器无法加载该类时才尝试从自己的类路径中加载该类
          - 缓存机制
            - 保证所有加载过的Class都会被缓存
            - 当程序中需要使用某个Class时，类加载器先从缓存区中搜寻该Class，只有当缓存区中不存在该Class对象时，系统才会读取该类对应的二进制数据，并将其转换成Class对象，存入缓存区中
            - >[!note]
              > 修改了Class后，必须重新启动JVM，程序所做的修改才会生效
        - >[!note]
          > 类加载器间的父子关系并不是类继承上的父子关系
          而是**类加载器实例之间的关系**
        - JVM中4种类加载器的层次结构
          - ![image.png](../assets/book/疯狂Java讲义/image_1670210036004_0.png)

```java
            public class ClassLoaderPropTest{
              public static void main(String[] args)
                throws IOException{
                // 获取系统类加载器
                ClassLoader systemLoader=ClassLoader.getSystemClassLoader();
                System.out.println("系统类加载器：" + systemLoader);
                /*
                获取系统类加载器的加载路径——通常由CLASSPATH环境变量指定
                如果操作系统没有指定CLASSPATH环境变量，则默认以当前路径作为
                系统类加载器的加载路径
                */
                Enumeration<URL> em1=systemLoader.getResources("");
                while(em1.hasMoreElements()){
                  System.out.println(em1.nextElement());
                }
                // 获取系统类加载器的父类加载器，得到扩展类加载器
                ClassLoader extensionLader=systemLoader.getParent();
                System.out.println("扩展类加载器：" + extensionLader);
                System.out.println("扩展类加载器的加载路径："
                                   + System.getProperty("java.ext.dirs"));
                System.out.println("扩展类加载器的parent: "
                                   + extensionLader.getParent());
              }
            }
```

            Run

```shell
            系统类加载器：sun.misc.Launcher$AppClassLoader@75b84c92
            file:/home/bgzocg/demo/tasks/java/basic/out/production/basic/
            扩展类加载器：sun.misc.Launcher$ExtClassLoader@4aa298b7
            扩展类加载器的加载路径：/usr/lib/jvm/java-8-openjdk-amd64/jre/lib/ext:/usr/java/packages/lib/ext
            扩展类加载器的parent: null
```

            - 系统类加载器的加载路径是程序运行的当前路径
            - 扩展类加载器的加载路径是D:\Java\jdk1.7.0 \jre\lib\ext
            - 扩展类加载器的父加载器是null，并不是根类加载器
              - 因为**根类加载器并没有继承ClassLoader抽象类**
                - 所以扩展类加载器的getParent()方法返回null
                  - 但实际上，扩展类加载器的父类加载器是根类加载器
                    - 只是根类加载器并不是Java实现的
                - 系统类加载器是AppClassLoader的实例，扩展类加载器是ExtClassLoader的实例。实际上，这两个类都是URLClassLoader类的实例
        - 类加载器加载Class大致要经过 8 个步骤
          - 1.检测此Class是否载入过（即在缓存区中是否有此Class）
            - 如果有则直接进入第8步，否则接着执行第2步
          - 2.检测父类加载器是否存在
            - 如果没有父类加载器，则要么parent一定是根类加载器，要么本身就是根类加载器，则跳到第4步执行；
            - 如果父类加载器存在，则接着执行第3步
          - 3.请求使用父类加载器去载入目标类
            - 如果成功载入则跳到第8步
            - 否则接着执行第5步
          - 4.请求使用根类加载器来载入目标类
            - 如果成功载入则跳到第8步
            - 否则跳到第7步
          - 5.当前类加载器尝试寻找Class文件 (从与此ClassLoader相关的类路径中寻找)
            - 如果找到则执行第6步
            - 如果找不到则跳到第7步
          - 6.从文件中载入Class
            - 成功载入后跳到第8步
          - 7.抛出ClassNotFoundException异常
          - 8.返回对应的java.lang.Class对象
      - [ ] #gtd/todo 创建并使用自定义的类加载器
        - [ ] #gtd/todo URLClassLoader类
      - 18.3 通过反射查看类信息
      - 对象在运行时都会出现 2 种类型
        - 编译时类型
        - 运行时类型
        - e.g. `Person p=new Student();`
          - 生成一个p变量，该变量的编译时类型为Person，运行时类型为Student
        - 程序需要在运行时发现对象和类的真实信息，我们有2种做法
          - 1.假设在编译时和运行时都完全知道类型的具体信息
            - 直接先使用instanceof运算符进行判断
            - 再利用强制类型转换将其转换成其运行时类型的变量即可
              ==(5.7)==
          - 2.编译时根本无法预知该对象和类可能属于哪些类，程序只依靠运行时信息来发现该对象和类的真实信息，这就必须使用**反射**
      - 获得Class对象 (3 种方式)
        - 1.使用Class类的forName(String clazzName)静态方法
          - 该方法需要传入字符串参数
            - 该字符串参数的值是某个类的**全限定类名** (必须添加完整包名)
        - 2.调用某个类的class属性来获取该类对应的Class对象
          - 例如，Person.class将会返回Person类对应的Class对象
        - 3.调用某个对象的getClass()方法
          - java.lang.Object类中的一个方法，所以所有的Java对象都可以调用该方法，该方法将会返回该对象所属类对应的Class对象。
        -          >[!note]
          > 第 2 种方式 代码更安全 / 程序性能更好
          - 无须调用方法，所以性能更好
          - 程序在编译阶段就可以检查需要访问的Class对象是否存在
      - 从Class中获取信息
        - 获取Class对应类所包含的构造器 (4个方法)
          - Connstructor<T> getConstructor(Class<?>... parameterTypes)
            - 返回此Class对象对应类的指定public构造器
          - Constructor<?>[] getConstructors()
            - 返回此Class对象对应类的所有public构造器
          - Constructor<T> getDeclaredConstructor(Class<?>...parameterTypes)
            - 返回此Class对象对应类的指定构造器，与构造器的访问权限无关
          - Constructor<?>[] getDeclaredConstructors()
            - 返回此Class对象对应类的所有构造器，与构造器的访问权限无关
        - 获取Class对应类所包含的方法 (4个方法)
          - Method getMethod(String name, Class<?>... parameterTypes)
            - 返回此Class对象对应类的指定public方法
          - Method[] getMethods()
            - 返回此Class对象所表示的类的所有public方法
          - Method getDeclaredMethod(String name, Class<?>...parameterTypes)
            - 返回此Class对象对应类的指定方法，与方法的访问权限无关
          - Method[] getDeclaredMethods()
            - 返回此Class对象对应类的全部方法，与方法的访问权限无关
        - 访问Class对应类所包含的Field (4个方法)
          - Field getField(String name)
            - 返回此Class对象对应类的指定public Field
          - Field[] getFields()
            - 返回此Class对象对应类的所有public Field
          - Field getDeclaredField(String name)
            - 返回此Class对象对应类的指定Field，与Field的访问权限无关
          - Field[] getDeclaredFields()
            - 返回此Class对象对应类的全部Field，与Field的访问权限无关
        - 访问Class对应类上所包含的Annotation (3 个方法)
          - <A extends Annotation> A getAnnotation(Class<A>annotationClass)
            - 试图获取该Class对象对应类上指定类型的Annotation
            - 如果该类型的注释不存在，则返回null
          - Annotation[] getAnnotations()
            - 返回该Class对象对应类上的所有Annotation
          - Annotation[] getDeclaredAnnotations()
            - 返回直接修饰该Class对应类的所有Annotation
        - 访问该Class对象对应类包含的内部类
          - Class<?>[] getDeclaredClasses()
            - 返回该Class对象对应类里包含的全部内部类
        - 访问该Class对象对应类所在的外部类
          - Class<?> getDeclaringClass()
            - 返回该Class对象对应类所在的外部类
        - 访问该Class对象对应类所继承的父类、所实现的接口等
          - Class<?>[] getInterfaces()
            - 返回该Class对象对应类所实现的全部接口
        - 访问该Class对象对应类所继承的父类
          - Class<? super T> getSuperclass()
            - 返回该Class对象对应类的超类的Class对象
        - 获取Class对象对应类的修饰符、所在包、类名等基本信息
          - int getModifiers()
            - 返回此类或接口的所有修饰符
            - 修饰符由public、protected、private、final、static、abstract等对应的常量组成，返回的整数应使用Modifier工具类的方法来解码，才可以获取真实的修饰符
          - Package getPackage()
            - 获取此类的包
          - String getName()
            - 以字符串形式返回此Class对象所表示的类的名称
          - String getSimpleName()
            - 以字符串形式返回此Class对象所表示的类的简称
        - 判断该类是否为接口、枚举、注释类型等
          - boolean isAnnotation()
            - 返回此Class对象是否表示一个注释类型（由@interface定义）
          - boolean isAnnotationPresent(Class<? extends Annotation> annotationClass)
            - 判断此Class对象是否使用了Annotation注释修饰
          - boolean isAnonymousClass()
            - 返回此Class对象是否是一个匿名类
          - boolean isArray()
            - 返回此Class对象是否表示一个数组类
          - boolean isEnum()
            - 返回此Class对象是否表示一个枚举（由enum关键字定义）
          - boolean isInterface()
            - 返回此Class对象是否表示一个接口（使用interface定义）
          - boolean isInstance(Object obj)
            - 判断obj是否是此Class对象的实例，该方法可以完全代替instanceof操作符

```java
          public void info(){}
          public void info(String str){}
          public void info(String str , Integer num){}
          public static void main(String []args){
            // 获取第 2 个info方法
            clazz.getMethod("info" , String.class);
            // 获取第 3 个info方法
            clazz.getMethod("info" , String.class, Integer.class);
          }
```

```java
          // 使用两个注释修饰该类
          @SuppressWarnings(value="unchecked")
          @Deprecated
          public class ClassTest{
            // 为该类定义一个私有的构造器
            private ClassTest(){}
            // 定义一个有参数的构造器
            public ClassTest(String name){
              System.out.println("执行有参数的构造器");
            }
            // 定义一个无参数的info方法
            public void info(){
              System.out.println("执行无参数的info方法");
            }
            // 定义一个有参数的info方法
            public void info(String str){
              System.out.println("执行有参数的info方法"
                                 + "，其str参数值：" + str);
            }
            // 定义一个测试用的内部类
            class Inner{ }
            public static void main(String[] args)
              throws Exception{
              // 下面代码可以获取ClassTest对应的Class
              Class<ClassTest> clazz=ClassTest.class;
              // 获取该Class对象所对应类的全部构造器
              Constructor[] ctors=clazz.getDeclaredConstructors();
              System.out.println("ClassTest的全部构造器如下：");
              for (Constructor c : ctors){
                System.out.println(c);
              }
              // 获取该Class对象所对应类的全部public构造器
              Constructor[] publicCtors=clazz.getConstructors();
              System.out.println("ClassTest的全部public构造器如下：");
              for (Constructor c : publicCtors){
                System.out.println(c);
              }
              // 获取该Class对象所对应类的全部public方法
              Method[] mtds=clazz.getMethods();
              System.out.println("ClassTest的全部public方法如下：");
              for (Method md : mtds){
                System.out.println(md);
              }
              // 获取该Class对象所对应类的指定方法
              System.out.println("ClassTest里带一个字符串参数的info方法为："
                                 + clazz.getMethod("info" , String.class));
              // 获取该Class对象所对应类的全部注释
              Annotation[] anns=clazz.getAnnotations();
              System.out.println("ClassTest的全部Annotation如下：");
              for (Annotation an : anns){
                System.out.println(an);
              }
              System.out.println("该Class元素上的@SuppressWarnings注释为："
                                 + clazz.getAnnotation(SuppressWarnings.class));
              // 获取该Class对象所对应类的全部内部类
              Class<?>[] inners=clazz.getDeclaredClasses();
              System.out.println("ClassTest的全部内部类如下：");
              for (Class c : inners){
                System.out.println(c);
              }
              // 使用Class.forName()方法加载ClassTest的Inner内部类
              Class inClazz=Class.forName("ClassTest$Inner");
              // 通过getDeclaringClass()访问该类所在的外部类
              System.out.println("inClazz对应类的外部类为：" +
                                 inClazz.getDeclaringClass());
              System.out.println("ClassTest的包为：" + clazz.getPackage());
              System.out.println("ClassTest的父类为：" + clazz.getSuperclass());
            }
          }
```

          Run

```shell
          Test的全部构造器如下：
          private cc.bgzo.Test()
          public cc.bgzo.Test(java.lang.String)
          Test的全部public构造器如下：
          public cc.bgzo.Test(java.lang.String)
          Test的全部public方法如下：
          public void cc.bgzo.Test.info()
          public void cc.bgzo.Test.info(java.lang.String)
          public static void cc.bgzo.Test.main(java.lang.String[]) throws java.lang.Exception
          public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException
          public final native void java.lang.Object.wait(long) throws java.lang.InterruptedException
          public final void java.lang.Object.wait() throws java.lang.InterruptedException
          public boolean java.lang.Object.equals(java.lang.Object)
          public java.lang.String java.lang.Object.toString()
          public native int java.lang.Object.hashCode()
          public final native java.lang.Class java.lang.Object.getClass()
          public final native void java.lang.Object.notify()
          public final native void java.lang.Object.notifyAll()
          Test里带一个字符串参数的info方法为：public void cc.bgzo.Test.info(java.lang.String)
          Test的全部Annotation如下：
          @java.lang.Deprecated()
          该Class元素上的@SuppressWarnings注释为：null
          Test的全部内部类如下：
          class cc.bgzo.Test$Inner
          inClazz对应类的外部类为：class cc.bgzo.Test
          Test的包为：package cc.bgzo
          Test的父类为：class java.lang.Object
```

    - 18.4 使用反射生成并操作对象
    - 18.5 使用反射生成JDK动态代理
    - 18.6 反射和泛型
      - Java5的Class类增加了泛型功能, 允许使用泛型来限制Class类
        - String.class的类型实际上是Class<String>
        - 如果Class对应的类暂时未知，则使用Class<?>
        - 通过**在反射中使用泛型，可以避免使用反射生成的对象需要强制类型转换**
      - 泛型和Class类
        - e.g. 提供一个简单的对象工厂，该对象工厂可以根据指定类来提供该类的实例

```java
            public class YeekuObjectFactory{
              public static Object getInstance(String clsName){
                try{
                  // 创建指定类对应的Class对象
                  Class cls=Class.forName(clsName);
                  // 返回使用该Class对象创建的实例
                  return cls.newInstance();
                } catch(Exception e) {
                  e.printStackTrace();
                  return null;
                }
              }
            }
```

            - Return 的是一个 Object, 拿到之后会强制类型转换

```java
                // 获取实例后需要强制类型转换
                Date d=(Date)YeekuObjectFactory.getInstance("java.util.Date");
                // 运行时异常的一种情况
                // JFrame f=(JFrame)YeekuObjectFactory.getInstance("java.util.Date");
```

            - 解决运行时异常的一种情况, 用泛型

```java
                public class YeekuObjectFactory2{
                  public static <T> T getInstance(Class<T> cls){
                    try{
                      return cls.newInstance();
                    } catch(Exception e) {
                      e.printStackTrace();
                      return null;
                    }
                  }
                  public static void main(String[] args){
                    // 获取实例后无须类型转换
                    Date d=YeekuObjectFactory2.getInstance(Date.class);
                    JFrame f=YeekuObjectFactory2.getInstance(JFrame.class);
                  }
                }
```

              - 数组需要特定的写法

```java
                  // public static Object newInstance(Class<?> componentType, int... dimensions)
                  public static <T> T[] newInstance(Class<T> componentType, int length)
```

```java
                  public class CrazyitArray{
                    // 对Array的newInstance方法进行包装
                    @SuppressWarnings("unchecked")
                    public static <T> T[] newInstance(Class<T> componentType, int length){
                      return (T[])Array.newInstance(componentType , length);  //①
                    }
                    public static void main(String[] args){
                      // 使用YeekuArray的newInstance()创建一维数组
                      String[] arr=CrazyitArray.newInstance(String.class , 10);
                      // 使用YeekuArray的newInstance()创建二维数组
                      // 在这种情况下，只要设置数组元素的类型是int[]即可
                      int[][] intArr=CrazyitArray.newInstance(int[].class , 5);
                      arr[5]="疯狂Java讲义";
                      // intArr是二维数组，初始化该数组的第二个数组元素
                      // 二维数组的元素必须是一维数组
                      intArr[1]=new int[]{23, 12};
                      System.out.println(arr[5]);
                      System.out.println(intArr[1]\[1]);
                    }
                  }
```

      - 使用反射来获取泛型信息
        - 获得指定Field的类型

```java
            // 获取Field对象f的类型
            Class<?> a=f.getType();
            // 获得Field实例的泛型类型
            Type gType=f.getGenericType();
```

          - 将Type对象强制类型转换为ParameterizedType对象，ParameterizedType代表被参数化的类型，也就是增加了泛型限制的类型
          - ParameterizedType类提供了如下两个方法
            - getRawType()
              - 返回没有泛型信息的原始类型
            - getActualTypeArguments()
              - 返回泛型参数的类型

```java
          public class GenericTest{
            private Map<String , Integer> score;
            public static void main(String[] args)
              throws Exception{
              Class<GenericTest> clazz=GenericTest.class;
              Field f=clazz.getDeclaredField("score");
              // 直接使用getType()取出Field类型只对普通类型的Field有效
              Class<?> a=f.getType();
              // 下面将看到仅输出java.util.Map
              System.out.println("score的类型是:" + a);
              // 获得Field实例f的泛型类型
              Type gType=f.getGenericType();
              // 如果gType类型是ParameterizedType对象
              if(gType instanceof ParameterizedType){
                // 强制类型转换
                ParameterizedType pType=(ParameterizedType)gType;
                // 获取原始类型
                Type rType=pType.getRawType();
                System.out.println("原始类型是：" + rType);
                // 取得泛型类型的泛型参数
                Type[] tArgs=pType.getActualTypeArguments();
                System.out.println("泛型类型是:");
                for (int i=0; i < tArgs.length; i++){
                  System.ou
                }
              }else{
                System.out.println("获取泛型类型出错！");
              }
            }
          }
```

    - [ ] #gtd/todo 18.7 本章小结
        - 1.开发一个工具类，该工具类提供一个eval()方法，实现JavaScript中eval函数的功能——可以动态运行一行或多行程序代码。例如eval("System.out.println(\"aa\")")，将输出aa
      - 2.开发一个对象工厂池，这个对象工厂池不仅可以管理对象的String类型属性值，还可以管理容器中对象的其他类型的属性值，甚至可以将对象属性设置成引用到容器中其他对象（这就是Spring所提出的控制反转，即IoC）。

- ---

#thought

  - Book 对于学习的指导意义不言自明, 当我面对成千上万的 API 的时候, 我不可能系统的学习一篇, 当然 API 也不会根据使用频率做个试试排序, 我不知道到底要学习哪一个, 学习到何种程度, 这个时候, Book 里面列出来的条目就颇有价值了, 至少, 你要把这些 API 嚼烂了, 视频也是同理, 但是我不喜欢视频, 如果老师毫无个人魅力, 我只会唾弃他和他手中的东西.
    - 显然大学老师在这方面做得有恃无恐, 一点都不上心, 尸位素餐, 嗯, 很恶心.
#Comment
  - [**一般**, 属于经典但不推荐, 因为有点过时] 一开始没看出版时间, 发现真的有点过时了... 但是市面上的视频资料讲得又不够深入, 实在是难以发现高质量的教材.
