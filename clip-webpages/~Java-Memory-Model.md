---
title: "Java-Memory-Model"
created: 2025-03-16T22:46:01
modified: 2025-03-16T22:46:01
description: "The Java memory model specifies how the Java virtual machine and Java programs and threads work with the memory in the computer your Java programs run on."
source: "https://jenkov.com/tutorials/java-concurrency/java-memory-model.html"
tags:
tags-link:
type: "archive-web"
---
The Java memory model specifies how the Java virtual machine works with the computer's memory (RAM). The Java virtual machine is a model of a whole computer so this model naturally includes a memory model - AKA the Java memory model.  
Java 内存模型指定了 Java 虚拟机如何与计算机内存 (RAM) 配合使用。Java 虚拟机是整个计算机的模型，因此该模型自然包含内存模型 - 又称为 Java 内存模型。

It is very important to understand the Java memory model if you want to design correctly behaving concurrent programs. The Java memory model specifies how and when different threads can see values written to shared variables by other threads, and how to synchronize access to shared variables when necessary.  
如果您想设计正确运行的并发程序，了解 Java 内存模型非常重要。Java 内存模型指定不同线程如何以及何时可以看到其他线程写入共享变量的值，以及如何在必要时同步对共享变量的访问。

The original Java memory model was insufficient, so the Java memory model was revised in Java 1.5. This version of the Java memory model is still in use in Java today (Java 14+).  
原有的 Java 内存模型存在不足，因此在 Java 1.5 中对 Java 内存模型进行了修订。此版本的 Java 内存模型在今天的 Java 中仍在使用（Java 14+）。

## Java Memory Model Tutorial Video  
Java 内存模型教程视频

In case you prefer video, I have a video version of this tutorial available here:  
如果您更喜欢视频，我有本教程的视频版本，可在此处获取：  
[Java Memory Model Tutorial Video  
Java 内存模型教程视频](https://www.youtube.com/watch?v=LCSqZyjBwWA&list=PLL8woMHwr36EDxjUoCzboZjedsnhLP1j4&index=4)

[![Java Memory Model Tutorial Video](https://jenkov.com/images/java-concurrency/java-memory-model-video-screenshot.jpg)](https://www.youtube.com/watch?v=LCSqZyjBwWA&list=PLL8woMHwr36EDxjUoCzboZjedsnhLP1j4&index=4 "Java Memory Model Tutorial Video")

## The Internal Java Memory Model  
内部 Java 内存模型

The Java memory model used internally in the JVM divides memory between thread stacks and the heap. This diagram illustrates the Java memory model from a logic perspective:  
JVM 内部使用的 Java 内存模型将内存分为线程堆栈和堆。下图从逻辑角度说明了 Java 内存模型：

![The Java Memory Model From a Logic Perspective](https://jenkov.com/images/java-concurrency/java-memory-model-1.png)

Each thread running in the Java virtual machine has its own thread stack. The thread stack contains information about what methods the thread has called to reach the current point of execution. I will refer to this as the "call stack". As the thread executes its code, the call stack changes.  
Java 虚拟机中运行的每个线程都有自己的线程堆栈。线程堆栈包含有关线程调用了哪些方法以到达当前执行点的信息。我将其称为“调用堆栈”。当线程执行其代码时，调用堆栈会发生变化。

The thread stack also contains all local variables for each method being executed (all methods on the call stack). A thread can only access it's own thread stack. Local variables created by a thread are invisible to all other threads than the thread who created it. Even if two threads are executing the exact same code, the two threads will still create the local variables of that code in each their own thread stack. Thus, each thread has its own version of each local variable.  
线程堆栈还包含每个正在执行的方法（调用堆栈上的所有方法）的所有局部变量。线程只能访问自己的线程堆栈。线程创建的局部变量对于创建它的线程以外的所有其他线程都是不可见的。即使两个线程正在执行完全相同的代码，这两个线程仍将在各自的线程堆栈中创建该代码的局部变量。因此，每个线程都有每个局部变量的自己的版本。

All local variables of primitive types ( `boolean`, `byte`, `short`, `char`, `int`, `long`, `float`, `double`) are fully stored on the thread stack and are thus not visible to other threads. One thread may pass a copy of a pritimive variable to another thread, but it cannot share the primitive local variable itself.  
所有原始类型的局部变量（ `boolean` ， `byte` ， `short` ， `char` ， `int` ， `long` ， `float` 、 `double` ）完全存储在线程堆栈中，因此对其他线程不可见。一个线程可以将原始变量的副本传递给另一个线程，但它不能共享原始局部变量本身。

The heap contains all objects created in your Java application, regardless of what thread created the object. This includes the object versions of the primitive types (e.g. `Byte`, `Integer`, `Long` etc.). It does not matter if an object was created and assigned to a local variable, or created as a member variable of another object, the object is still stored on the heap.  
堆包含 Java 应用程序中创建的所有对象，无论哪个线程创建了该对象。这包括基本类型的对象版本（例如 `Byte` 、 `Integer` 、 `Long` 等）。无论对象是创建并分配给局部变量，还是作为另一个对象的成员变量创建，该对象仍存储在堆中。

Here is a diagram illustrating the call stack and local variables stored on the thread stacks, and objects stored on the heap:  
下面的图表说明了存储在线程堆栈上的调用堆栈和局部变量以及存储在堆上的对象：

![The Java Memory Model showing where local variables and objects are stored in memory.](https://jenkov.com/images/java-concurrency/java-memory-model-2.png)

A local variable may be of a primitive type, in which case it is totally kept on the thread stack.  
局部变量可能是原始类型，在这种情况下，它完全保存在线程堆栈上。

A local variable may also be a reference to an object. In that case the reference (the local variable) is stored on the thread stack, but the object itself if stored on the heap.  
局部变量也可能是对某个对象的引用。在这种情况下，引用（局部变量）存储在线程堆栈上，但对象本身存储在堆上。

An object may contain methods and these methods may contain local variables. These local variables are also stored on the thread stack, even if the object the method belongs to is stored on the heap.  
对象可能包含方法，这些方法可能包含局部变量。即使该方法所属的对象存储在堆上，这些局部变量也存储在线程堆栈上。

An object's member variables are stored on the heap along with the object itself. That is true both when the member variable is of a primitive type, and if it is a reference to an object.  
对象的成员变量与对象本身一起存储在堆中。当成员变量是原始类型，还是对对象的引用时，都是如此。

Static class variables are also stored on the heap along with the class definition.  
静态类变量也与类定义一起存储在堆上。

Objects on the heap can be accessed by all threads that have a reference to the object. When a thread has access to an object, it can also get access to that object's member variables. If two threads call a method on the same object at the same time, they will both have access to the object's member variables, but each thread will have its own copy of the local variables.  
所有引用该对象的线程都可以访问堆上的对象。当一个线程可以访问某个对象时，它也可以访问该对象的成员变量。如果两个线程同时调用同一对象上的方法，它们都可以访问该对象的成员变量，但每个线程都有自己的局部变量副本。

Here is a diagram illustrating the points above:  
下图说明了上述观点：

![The Java Memory Model showing references from local variables to objects, and from object to other objects.](https://jenkov.com/images/java-concurrency/java-memory-model-3.png)

Two threads have a set of local variables. One of the local variables (`Local Variable 2`) point to a shared object on the heap (Object 3). The two threads each have a different reference to the same object. Their references are local variables and are thus stored in each thread's thread stack (on each). The two different references point to the same object on the heap, though.  
两个线程有​​一组局部变量。其中一个局部变量（ `Local Variable 2` ）指向堆上的共享对象（对象 3）。两个线程对同一对象有不同的引用。它们的引用是局部变量，因此存储在每个线程的线程堆栈中（每个线程上）。但是，两个不同的引用指向堆上的同一个对象。

Notice how the shared object (Object 3) has a reference to Object 2 and Object 4 as member variables (illustrated by the arrows from Object 3 to Object 2 and Object 4). Via these member variable references in Object 3 the two threads can access Object 2 and Object 4.  
注意共享对象（对象 3）如何将对对象 2 和对象 4 的引用作为成员变量（由从对象 3 到对象 2 和对象 4 的箭头表示）。通过对象 3 中的这些成员变量引用，两个线程可以访问对象 2 和对象 4。

The diagram also shows a local variable which point to two different objects on the heap. In this case the references point to two different objects (Object 1 and Object 5), not the same object. In theory both threads could access both Object 1 and Object 5, if both threads had references to both objects. But in the diagram above each thread only has a reference to one of the two objects.  
该图还显示了一个局部变量，它指向堆上的两个不同对象。在这种情况下，引用指向两个不同的对象（对象 1 和对象 5），而不是同一个对象。理论上，如果两个线程都引用了这两个对象，那么这两个线程都可以访问对象 1 和对象 5。但在上图中，每个线程只引用这两个对象中的一个。

So, what kind of Java code could lead to the above memory graph? Well, code as simple as the code below:  
那么，什么样的 Java 代码可能导致上述内存图？好吧，代码就像下面的代码一样简单：

```
public class MyRunnable implements Runnable() {

    public void run() {
        methodOne();
    }

    public void methodOne() {
        int localVariable1 = 45;

        MySharedObject localVariable2 =
            MySharedObject.sharedInstance;

        //... do more with local variables.

        methodTwo();
    }

    public void methodTwo() {
        Integer localVariable1 = new Integer(99);

        //... do more with local variable.
    }
}
```
```
public class MySharedObject {

    //static variable pointing to instance of MySharedObject

    public static final MySharedObject sharedInstance =
        new MySharedObject();

    //member variables pointing to two objects on the heap

    public Integer object2 = new Integer(22);
    public Integer object4 = new Integer(44);

    public long member1 = 12345;
    public long member2 = 67890;
}
```

If two threads were executing the `run()` method then the diagram shown earlier would be the outcome. The `run()` method calls `methodOne()` and `methodOne()` calls `methodTwo()`.  
如果两个线程都在执行 `run()` 方法，则结果将如上图所示。run `run()` 方法调用 `methodOne()` ， `methodOne()` 又调用 `methodTwo()` 。

`methodOne()` declares a primitive local variable (`localVariable1` of type `int`) and an local variable which is an object reference (`localVariable2`).  
`methodOne()` 声明了一个原始局部变量 ( `localVariable1` 类型为 `int` ) 和一个作为对象引用的局部变量 ( `localVariable2` )。

Each thread executing `methodOne()` will create its own copy of `localVariable1` and `localVariable2` on their respective thread stacks. The `localVariable1` variables will be completely separated from each other, only living on each thread's thread stack. One thread cannot see what changes another thread makes to its copy of `localVariable1`.  
每个执行 `methodOne()` 线程都会创建自己的 `localVariable1` 副本，并且 `localVariable2` 位于各自的线程堆栈上。localVariable1 `localVariable1` 将完全彼此分离，仅存在于每个线程的线程堆栈上。一个线程无法看到另一个线程对其 `localVariable1` 副本所做的更改。

Each thread executing `methodOne()` will also create their own copy of `localVariable2`. However, the two different copies of `localVariable2` both end up pointing to the same object on the heap. The code sets `localVariable2` to point to an object referenced by a static variable. There is only one copy of a static variable and this copy is stored on the heap. Thus, both of the two copies of `localVariable2` end up pointing to the same instance of `MySharedObject` which the static variable points to. The `MySharedObject` instance is also stored on the heap. It corresponds to Object 3 in the diagram above.  
每个执行 `methodOne()` 线程也会创建自己的 `localVariable2` 副本。但是， `localVariable2` 的两个不同副本最终都指向堆上的同一个对象。代码将 `localVariable2` 设置为指向静态变量引用的对象。静态变量只有一个副本，并且此副本存储在堆上 `MySharedObject` 因此， `localVariable2` 的两个副本最终都指向静态变量指向的 `MySharedObject` 的同一个实例。MySharedObject 实例也存储在堆上。它对应于上图中的对象 3。

Notice how the `MySharedObject` class contains two member variables too. The member variables themselves are stored on the heap along with the object. The two member variables point to two other `Integer` objects. These `Integer` objects correspond to Object 2 and Object 4 in the diagram above.  
请注意， `MySharedObject` 类也包含两个成员变量。成员变量本身与对象一起存储在堆上。这两个成员变量指向另外两个 `Integer` 对象。这些 `Integer` 对象对应于上图中的对象 2 和对象 4。

Notice also how `methodTwo()` creates a local variable named `localVariable1`. This local variable is an object reference to an `Integer` object. The method sets the `localVariable1` reference to point to a new `Integer` instance. The `localVariable1` reference will be stored in one copy per thread executing `methodTwo()`. The two `Integer` objects instantiated will be stored on the heap, but since the method creates a new `Integer` object every time the method is executed, two threads executing this method will create separate `Integer` instances. The `Integer` objects created inside `methodTwo()` correspond to Object 1 and Object 5 in the diagram above.  
还要注意 `methodTwo()` 如何创建一个名为 `localVariable1` 的局部变量。此局部变量是指向 `Integer` 对象的对象引用。该方法将 `localVariable1` 引用设置为指向新的 `Integer` 实例。localVariable1 引用将在每个执行 `methodTwo()` 线程中存储一份副本。实例化的两个 `Integer` 对象将存储在堆上 `localVariable1` 但由于该方法每次执行时都会创建一个新的 `Integer` 对象，因此执行此方法的两个线程将创建单独的 `Integer` 实例。在 `methodTwo()` ) 中创建的 `Integer` 对象对应于上图中的对象 1 和对象 5。

Notice also the two member variables in the class `MySharedObject` of type `long` which is a primitive type. Since these variables are member variables, they are still stored on the heap along with the object. Only local variables are stored on the thread stack.  
还要注意 `MySharedObject` 类中的两个 long 类型的成员变量 `long` 是原始类型。由于这些变量是成员变量，因此它们仍然与对象一起存储在堆上。只有局部变量存储在线程堆栈上。

## Hardware Memory Architecture  
硬件内存架构

Modern hardware memory architecture is somewhat different from the internal Java memory model. It is important to understand the hardware memory architecture too, to understand how the Java memory model works with it. This section describes the common hardware memory architecture, and a later section will describe how the Java memory model works with it.  
现代硬件内存架构与 Java 内部内存模型有些不同。了解硬件内存架构也很重要，因为这样才能了解 Java 内存模型如何与其协同工作。本节介绍常见的硬件内存架构，后面的部分将介绍 Java 内存模型如何与其协同工作。

Here is a simplified diagram of modern computer hardware architecture:  
以下是现代计算机硬件架构的简化图：

![Modern hardware memory architecture.](https://jenkov.com/images/java-concurrency/java-memory-model-4.png)

A modern computer often has 2 or more CPUs in it. Some of these CPUs may have multiple cores too. The point is, that on a modern computer with 2 or more CPUs it is possible to have more than one thread running simultaneously. Each CPU is capable of running one thread at any given time. That means that if your Java application is multithreaded, one thread per CPU may be running simultaneously (concurrently) inside your Java application.  
现代计算机通常有 2 个或更多 CPU。其中一些 CPU 可能还有多个核心。关键是，在具有 2 个或更多 CPU 的现代计算机上，可以同时运行多个线程。每个 CPU 都能够在任何给定时间运行一个线程。这意味着，如果您的 Java 应用程序是多线程的，则每个 CPU 的一个线程可能在您的 Java 应用程序内同时（并发）运行。

Each CPU contains a set of registers which are essentially in-CPU memory. The CPU can perform operations much faster on these registers than it can perform on variables in main memory. That is because the CPU can access these registers much faster than it can access main memory.  
每个 CPU 都包含一组寄存器，这些寄存器本质上是 CPU 内存。CPU 对这些寄存器执行操作的速度比对主内存中的变量执行操作的速度快得多。这是因为 CPU 访问这些寄存器的速度比访问主内存的速度快得多。

Each CPU may also have a CPU cache memory layer. In fact, most modern CPUs have a cache memory layer of some size. The CPU can access its cache memory much faster than main memory, but typically not as fast as it can access its internal registers. So, the CPU cache memory is somewhere in between the speed of the internal registers and main memory. Some CPUs may have multiple cache layers (Level 1 and Level 2), but this is not so important to know to understand how the Java memory model interacts with memory. What matters is to know that CPUs can have a cache memory layer of some sort.  
每个 CPU 也可能有一个 CPU 缓存层。事实上，大多数现代 CPU 都有一个一定大小的缓存层。CPU 访问缓存的速度比访问主内存快得多，但通常不如访问内部寄存器的速度快。因此，CPU 缓存的速度介于内部寄存器和主内存之间。一些 CPU 可能有多个缓存层（第 1 级和第 2 级），但这对于理解 Java 内存模型如何与内存交互并不那么重要。重要的是要知道 CPU 可以有某种缓存层。

A computer also contains a main memory area (RAM). All CPUs can access the main memory. The main memory area is typically much bigger than the cache memories of the CPUs.  
计算机还包含主内存区域 (RAM)。所有 CPU 都可以访问主内存。主内存区域通常比 CPU 的缓存大得多。

Typically, when a CPU needs to access main memory it will read part of main memory into its CPU cache. It may even read part of the cache into its internal registers and then perform operations on it. When the CPU needs to write the result back to main memory it will flush the value from its internal register to the cache memory, and at some point flush the value back to main memory.  
通常，当 CPU 需要访问主内存时，它会将部分主内存读入其 CPU 缓存。它甚至可能将部分缓存读入其内部寄存器，然后对其执行操作。当 CPU 需要将结果写回主内存时，它会将值从其内部寄存器刷新到缓存，并在某个时候将值刷新回主内存。

The values stored in the cache memory is typically flushed back to main memory when the CPU needs to store something else in the cache memory. The CPU cache can have data written to part of its memory at a time, and flush part of its memory at a time. It does not have to read / write the full cache each time it is updated. Typically the cache is updated in smaller memory blocks called "cache lines". One or more cache lines may be read into the cache memory, and one or mor cache lines may be flushed back to main memory again.  
当 CPU 需要在缓存中存储其他内容时，缓存中存储的值通常会刷新回主内存。CPU 缓存可以一次将数据写入其部分内存，也可以一次刷新其部分内存。每次更新时，它不必读取/写入整个缓存。通常，缓存在称为“缓存行”的较小内存块中更新。一条或多条缓存行可能会被读入缓存，一条或多条缓存行可能会再次刷新回主内存。

## Bridging The Gap Between The Java Memory Model And The Hardware Memory Architecture  
弥合 Java 内存模型与硬件内存架构之间的差距

As already mentioned, the Java memory model and the hardware memory architecture are different. The hardware memory architecture does not distinguish between thread stacks and heap. On the hardware, both the thread stack and the heap are located in main memory. Parts of the thread stacks and heap may sometimes be present in CPU caches and in internal CPU registers. This is illustrated in this diagram:  
如前所述，Java 内存模型和硬件内存架构不同。硬件内存架构不区分线程堆栈和堆。在硬件上，线程堆栈和堆都位于主内存中。线程堆栈和堆的部分有时可能存在于 CPU 缓存和内部 CPU 寄存器中。下图说明了这一点：

![The division of thread stack and heap among CPU internal registers, CPU cache and main memory.](https://jenkov.com/images/java-concurrency/java-memory-model-5.png)

When objects and variables can be stored in various different memory areas in the computer, certain problems may occur. The two main problems are:  
当对象和变量可以存储在计算机中各种不同的内存区域中时，可能会出现某些问题。两个主要问题是：

- Visibility of thread updates (writes) to shared variables.  
线程对共享变量的更新（写入）的可见性。
- Race conditions when reading, checking and writing shared variables.  
读取、检查和写入共享变量时的竞争条件。

Both of these problems will be explained in the following sections.  
以下章节将解释这两个问题。

### Visibility of Shared Objects  
共享对象的可见性

If two or more threads are sharing an object, without the proper use of either `volatile` declarations or synchronization, updates to the shared object made by one thread may not be visible to other threads.  
如果两个或多个线程共享一个对象，如果没有正确使用 `volatile` 声明或同步，则一个线程对共享对象的更新可能对其他线程不可见。

Imagine that the shared object is initially stored in main memory. A thread running on CPU one then reads the shared object into its CPU cache. There it makes a change to the shared object. As long as the CPU cache has not been flushed back to main memory, the changed version of the shared object is not visible to threads running on other CPUs. This way each thread may end up with its own copy of the shared object, each copy sitting in a different CPU cache.  
假设共享对象最初存储在主内存中。在 CPU 1 上运行的线程随后将共享对象读入其 CPU 缓存。在那里，它对共享对象进行更改。只要 CPU 缓存尚未刷新回主内存，共享对象的更改版本对在其他 CPU 上运行的线程就不可见。这样，每个线程最终可能会拥有自己的共享对象副本，每个副本都位于不同的 CPU 缓存中。

The following diagram illustrates the sketched situation. One thread running on the left CPU copies the shared object into its CPU cache, and changes its `count` variable to 2. This change is not visible to other threads running on the right CPU, because the update to `count` has not been flushed back to main memory yet.  
下图说明了大致情况。在左侧 CPU 上运行的一个线程将共享对象复制到其 CPU 缓存中，并将其 `count` 变量更改为 2。此更改对于在右侧 CPU 上运行的其他线程不可见，因为对 `count` 的更新尚未刷新回主内存。

![Visibility Issues in the Java Memory Model.](https://jenkov.com/images/java-concurrency/java-memory-model-6.png)

To solve this problem you can use [Java's volatile keyword](https://jenkov.com/tutorials/java-concurrency/volatile.html). The `volatile` keyword can make sure that a given variable is read directly from main memory, and always written back to main memory when updated.  
为了解决这个问题，你可以使用 [Java 的 volatile 关键字](https://jenkov.com/tutorials/java-concurrency/volatile.html) 。 `volatile` 关键字可以确保给定变量直接从主内存中读取，并在更新时始终写回主内存。

### Race Conditions  竞争条件

If two or more threads share an object, and more than one thread updates variables in that shared object, [race conditions](https://jenkov.com/tutorials/java-concurrency/race-conditions-and-critical-sections.html) may occur.  
如果两个或多个线程共享一个对象，并且多个线程更新该共享对象中的变量， 可能会出现[竞争状况](https://jenkov.com/tutorials/java-concurrency/race-conditions-and-critical-sections.html) 。

Imagine if thread A reads the variable `count` of a shared object into its CPU cache. Imagine too, that thread B does the same, but into a different CPU cache. Now thread A adds one to `count`, and thread B does the same. Now `var1` has been incremented two times, once in each CPU cache.  
想象一下，如果线程 A 将共享对象的变量 `count` 读入其 CPU 缓存。再想象一下，线程 B 执行相同操作，但读入不同的 CPU 缓存。现在线程 A 将 `count` 加一，线程 B 也执行相同操作。现在 `var1` 已递增两次，每次在 CPU 缓存中。

If these increments had been carried out sequentially, the variable `count` would be been incremented twice and had the original value + 2 written back to main memory.  
如果这些增量按顺序执行，变量 `count` 将增加两次，并将原始值 + 2 写回到主存储器。

However, the two increments have been carried out concurrently without proper synchronization. Regardless of which of thread A and B that writes its updated version of `count` back to main memory, the updated value will only be 1 higher than the original value, despite the two increments.  
但是，两次递增是并发进行的，没有进行适当的同步。无论线程 A 和 B 中的哪一个将其更新后的 `count` 写回到主内存，尽管进行了两次递增，更新后的值都只会比原始值高 1。

This diagram illustrates an occurrence of the problem with race conditions as described above:  
下图说明了上述竞争条件问题的发生：

![Race Condition Issues in the Java Memory Model.](https://jenkov.com/images/java-concurrency/java-memory-model-7.png)

To solve this problem you can use a [Java synchronized block](https://jenkov.com/tutorials/java-concurrency/synchronized.html). A synchronized block guarantees that only one thread can enter a given critical section of the code at any given time. Synchronized blocks also guarantee that all variables accessed inside the synchronized block will be read in from main memory, and when the thread exits the synchronized block, all updated variables will be flushed back to main memory again, regardless of whether the variable is declared volatile or not.  
为了解决这个问题，您可以使用 [Java 同步块](https://jenkov.com/tutorials/java-concurrency/synchronized.html) 。同步块保证在任意给定时间只有一个线程可以进入代码的给定关键部分。同步块还保证同步块内访问的所有变量都将从主内存中读取，并且当线程退出同步块时，所有更新的变量都将再次刷新回主内存，无论变量是否被声明为 volatile。