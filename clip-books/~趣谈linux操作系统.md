---
tags: #geekbang, #linux
---

## 入门
## Why?
    - __服务端应用__
      - 云计算、虚拟化、容器、大数据、人工智能，几乎都是基于 Linux 技术的。那些牛得不行的系统，团购、电商、打车、快递，都是部署在服务端，也几乎都是基于 Linux 技术的
    - __代码实现__
      - Linux 最大的优点就是开源。作为程序员，有了代码，啥都好办了。只要有足够的耐心，我们就可以一层一层看下去，看内核调度函数，看内存分配过程。理论理解起来不容易，但是一行行的“if-else”却不会产生歧义
      - 当你写代码的时候，大部分情况下都可以使用现成的数据结构和算法库，但是有些场景对于内存的使用需要限制到很小，对于搜索的时间需要限制到很小的时候，我们需要定制化一些数据结构，这个时候内核里面这些实现就很有参考意义了
    - __系统生态__
      - 假设，我们现在就是在做一家外包公司，我们的目标是把这家公司做上市。其中，操作系统就是这家外包公司的老板。我们把这家公司的发展阶段分为这样几个时期：
        - **初创期**:这个老板基于开放的营商环境(x86体系结构),创办一家外包公司(系统的启动)。因为一开始没有其他员工,老板需要亲自接项目(实模式)。'
        - '**发展期**:公司慢慢做大,项目越接越多(保护模式、多进程),为了管理各个外包项目,建立了项目管理体系(进程管理)、会议室管理体系(内存管理)、文档资料管理系统(文件系统)、售前售后体系(输入输出设备管理)。
        - **壮大期**:公司越来越牛,开始促进内部项目的合作(进程间通信)和外部公司合作(网络通信)。
        - **集团化**:公司的业务越来越多,会成立多家子公司(虚拟化),或者鼓励内部创业(容器化),这个时候公司就变成了集团。大管家的调度能力不再局限于一家公司,而是集团公司(Linux集群),从而成功上市(从单机操作系统到数据中心操作系统)。
## Test
  - ...
## Route
    - Linux 的灵活性也会使得你有 N 多种方法解决问题,从而事半功倍,你就会有一切尽在掌握的感觉
    - [[commandline]]
      - 在这样没有统一入口的情况下,就需要你对最基本的命令有所掌握
        - ==这个过程可能非常痛苦,在没有足够熟练地掌握命令行之前,你会发现干个非常小的事情都需要搜索半天,读很多文档,即便如此还不一定能得到期望的结果==。这个时候你一定不要气馁,坚持下去,继续看文档、查资料.
      - `When Done`
        - 慢慢你就会发现,大部分命令的行为模式都很像,你几乎不需要搜索就能完成大部分操作了
      - **鸟哥的 Linux 私房菜** / **Linux 系统管理技术手册**
    - __程序设计__ <- 系统调用 / glibc
      - __如果说使用命令行的人是吃馒头的,那写代码操作命令行的人就是做馒头的__
      - Linux 的系统调用非常多,而且每个函数都非常复杂,传入的参数、返回值、调用的方式等等都有很多讲究。这里面需要掌握很多 Linux 操作系统的原理,否则你会无法理解为什么应该这样调用。你会发现,你平时用的一个简单的命令行,却需要 N 个系统调用组合才能完成。其中每个系统调用都要进行深入地学习、读文档、做实验。
      - `When Done`
        - 大学里学的那些理论,你再回去看,现在就会开始有感觉了
      - **UNIX 环境高级编程**
    - __Linux 内核机制__
      - 你的角色要再次面临变化, **就像你蒸馒头时间长了,发现要蒸出更好吃的馒头,就必须要对面粉有所研究**.
      - 我不建议你直接看代码,因为 Linux 代码量太大,很容易迷失,找不到头绪。最好的办法是, __先了解一下 Linux 内核机制,知道基本的原理和流程就可以了__
      - `When Done`
        - 你会发现 Linux 这个复杂的系统开始透明起来。无论你是运维,还是开发,你都能大概知道背后发生的事情,并在出现异常的情况时,比较准确地定位到问题所在
      - **深入理解 LINUX 内核**
    - __Linux 内核代码__
      - 理论的描述和提炼虽然能够让你更容易看清全貌,但是容易让你忽略细节
      - **一开始阅读代码不要纠结一城一池的得失,不要每一行都一定要搞清楚它是干嘛的,而要聚焦于核心逻辑和使用场景**
      - `When Done`
        - 对于操作系统的原理,你应该就掌握得比较清楚了。就像蒸馒头的人已经将面粉加工流程烂熟于心。这个时候, 你就 __可以有针对性地去做课题,把所学和你现在做的东西结合起来重点突破__
        - 例如你是研究虚拟化的,就重点看 KVM 的部分; 如果你是研究网络的,就重点看内核协议栈的部分
      - **LINUX 内核源代码情景分析**
    - __Linux 定制组件__
      - 因为 Linux 有源代码,很多地方可以参考现有的实现,定制化自己的模块
      - 这个难度比较大,涉及的细节比较多,上一个阶段,我的建议是不计较一城一地的得失,不需要每个细节都搞清楚,这一个阶段要求就更高了
    - __真实场景开发__
      - 生产环境会有大量的不可控因素,尤其是集群规模大的更是如此,大量的运维经验是实战来的,不能光靠读书。
      - 如果你是开发,对内核进行少量修改容易,但是一旦面临真实的场景,需要考虑各种因素, __并发与并行,锁与保护,扩展性和兼容性,__ 都需要真实项目才能练出来
## 综述
## Subsystem
    - ![image.png](../assets/image_1645947936470_0.png)
## Several [[command]]
    - ![image.png](../assets/image_1645956348730_0.png)
    - [[ls]]
    - Install
      - 在 Windows 里面,最终会变成 C:\Program Files 下面的一个文件夹以及注册表里面的一些配置。对应 Linux 里面会放的更散一点。例如,主执行文件会放在 /usr/bin 或者 /usr/sbin 下面,其他的库文件会放在 /var 下面,配置文件会放在 /etc 下面
    - [[nohup]]
## 系统调用
    - [[linux-system-call]]
    -      > "一切皆文件"
      - 启动一个进程,需要一个程序文件,这是一个**二进制文件**。
      - 启动的时候,要加载一些配置文件,例如 yml、properties 等,这是文本文件;启动之后会打印一些日志,如果写到硬盘上,也是**文本文件**。
      - 但是如果我想把日志打印到交互控制台上,在命令行上唰唰地打印出来,这其实也是一个文件,是标准输出**stdout 文件**。
      - 这个进程的输出可以作为另一个进程的输入,这种方式称为**管道**,管道也是一个文件。
      - 进程可以通过网络和其他进程进行通信,建立的**Socket**,也是一个文件。
      - 进程需要访问外部设备,**设备**也是一个文件。
      - 文件都被存储在文件夹里面,其实**文件夹**也是一个文件。
      - 进程运行起来,要想看到进程运行的情况,会在 /proc 下面有对应的**进程号**,还是一系列文件。
      - 每个文件,Linux 都会分配一个**文件描述符**(File Descriptor),这是一个整数。有了这个文件描述符,我们就可以使用系统调用,查看或者干预进程运行的方方面面。
## 系统初始化
##
## x86
    - IBM 和 x86 的故事
      - IBM 开始做 IBM PC 时,一开始并没有让最牛的华生实验室去研发,而是交给另一个团队。一年时间,软硬件全部自研根本不可能完成,于是他们采用了英特尔的 8088 芯片作为 CPU,使用微软的 MS-DOS 做操作系统。
      - 谁能想到 IBM PC 卖的超级好,好到因为垄断市场而被起诉。IBM 就在被逼的情况下公开了一些技术,使得后来无数 IBM-PC 兼容机公司的出现,也就有了后来占据市场的惠普、康柏、戴尔等等。
      - 能够开放自己的技术是一件了不起的事。从技术和发展的层面来讲,它会使得一项技术大面积铺开,形成行业标准。就比如现在常用的 Android 手机,如果没有开放的 Android 系统,我们也没办法享受到这么多不同类型的手机。
      - 对于当年的 PC 机来说,其实也是这样。英特尔的技术因此成为了行业的开放事实标准。由于这个系列开端于 8086,因此称为 x86 架构
    - 计算机的工作模式
      - ![image.png](../assets/image_1645973090444_0.png)
## 进程管理
## ch01 进程
    - `build-essential` in [[ubuntu]]
```shell
        $ apt show build-essential
        ...
        Depends: libc6-dev | libc-dev, gcc (>= 4:9.2), g++ (>= 4:9.2), make, dpkg-dev (>= 1.17.11)
        ...
```
### Compiler
```cpp
        //process.c
        #include <stdio.h>
        #include <stdlib.h>
        #include <sys/types.h>
        #include <unistd.h>
        extern int create_process (char* program, char** arg_list);
        int create_process (char* program, char** arg_list)
        {
            pid_t child_pid;
            child_pid = fork ();
            if (child_pid != 0)
                return child_pid;
            else {
                execvp (program, arg_list);
                abort ();
            }
        }
        // createprocess.c
        #include <stdio.h>
        #include <stdlib.h>
        #include <sys/types.h>
        #include <unistd.h>
        extern int create_process (char* program, char** arg_list);
        int main ()
        {
            char* arg_list[] = {
                "ls",
                "-l",
                "/etc/yum.repos.d/",
                NULL
            };
            create_process ("ls", arg_list);
            return 0;
        }
```
      - ![image.png](../assets/image_1649658869823_0.png)
        - ELF
          - 可重定位文件 (Relocatable File) `.o`
            ![image.png](../assets/image_1649658995290_0.png)
            - 可重定位:
            - 文件的头 用于描述整个文件
              - 文件格式在内核中有定义，分别为 `struct elf32_hdr` 和 `struct elf64_hdr`
            - `.text`：放编译好的二进制可执行代码
            - `.data`：已经初始化好的全局变量
            - `.rodata`：只读数据，例如字符串常量、const 的变量
            - `.bss`：未初始化全局变量，运行时会置 0
            - `.symtab`：符号表，记录的则是函数和变量
            - `.strtab`：字符串表、字符串常量和变量名
            - 局部变量是放在栈里面, 在程序运行过程中随时分配空间, 随时释放的
            - 编译的时候先做预处理工作, 如将头文件嵌入到正文中，将定义的宏展开，然后编译过程，-> `.o` 文件 (ELF 第一种类型)
              - ELF made by section(节)
          - 可执行文件
            ![image.png](../assets/image_1649660911584_0.png)
            - 这些 `section` 是多个`.o` 文件合并过的
            - 将小的 `section` 合成了大的段 `segment`，并且在最前面加一个段头表 (Segment Header Table)
            - 在代码里面的定义为 `struct elf32_phdr` 和 `struct elf64_phdr`，这里面除了有对于段的描述之外，最重要的是 p_vaddr，这个是这个段加载到内存的虚拟地址。在 ELF 头里面，有一项 e_entry，也是个虚拟地址，是这个程序运行的入口。
          - 共享对象文件 (Shared Object) ref -> ((6253d4ec-85ba-4879-b2db-71ba04b8b9b8))
            - diff
              - 一个`.interp` 的 Segment
                - 这里面是 `ld-linux.so`，动态链接器, 运行时的链接动作都是它做的
              - 两个 `section`
                - `.plt`: 过程链接表 (Procedure Linkage Table, PLT)
                - `.got.plt`: 全局偏移量表 (Global Offset Table，GOT)
            - `dynamiccreateprocess` 这个程序要调用 `libdynamicprocess.so` 里的 `create_process` 函数
            - 编译 -> 在 `PLT` 里面建立一项 `PLT[x]` -> 二进制中直接调用 `PLT[x]` 里面的代理代码 -> 代理代码在运行时到 `GOT` (`GOT[y]`: 运行时 `create_process` 函数在内存中真正的地址) 找真正的 `create_process` 函数
            - `GOT[y]` -> 回调 `PLT` -> 调用 `PLT[0]` -> 调用 `GOT[2]`( `ld-linux.so` 的入口函数) -> 拿到 `create_process ` 函数地址, 下次，PLT[x] 的代理函数就能够直接调用了
          - alalysis
            - `readelf`: 分析 ELF 的信息
            - `objdump`: 显示二进制文件的信息
            - `hexdump`: 查看文件的十六进制编码
            - `nm`: 关于指定文件中符号的信息
### Link
      - 静态链接库
```shell
          ar cr libstaticprocess.a process.o
          #archives, 将一系列对象文件（.o）归档为一个文件
          gcc -o staticcreateprocess createprocess.o -L. -lstaticprocess
          # -L 表示在当前目录下找.a 文件
          # -lstaticprocess 会自动补全文件名, 如加前缀 lib，后缀.a，变成 libstaticprocess.a
          # 找到这个.a 文件后，将里面的 process.o 取出来，和 createprocess.o 做一个链接
          # 形成二进制执行文件 staticcreateprocess
```
      - 动态链接库 (Shared Libraries)
```shell
          gcc -shared -fPIC -o libdynamicprocess.so process.o
          gcc -o dynamiccreateprocess createprocess.o -L. -ldynamicprocess
```
          - 当运行这个程序的时候，首先寻找动态链接库，然后加载它。默认情况下，系统在 /lib 和 /usr/lib 文件夹下寻找动态链接库。如果找不到就会报错，我们可以设定 `export LD_LIBRARY_PATH=.` 环境变量，程序运行时会在此环境变量指定的文件夹下寻找动态链接库。
    - [[exec]]
## ch02 线程
```cpp
      #include <pthread.h>
      #include <stdio.h>
      #include <stdlib.h>
      #mark:  NUM_OF_TASKS 5
      void *downloadfile(void *filename){
         printf("I am downloading the file %s!\n", (char *)filename);
         sleep(10);
         long downloadtime = rand()%100;
         printf("I finish downloading the file within %d minutes!\n", downloadtime);
         pthread_exit((void *)downloadtime);
        //当一个线程退出的时候，就会发送信号给其他所有同进程的线程
      }
      int main(int argc, char *argv[]){
         char files[NUM_OF_TASKS][20]={"file1.avi","file2.rmvb","file3.mp4","file4.wmv","file5.flv"};
         pthread_t threads[NUM_OF_TASKS];
         int rc;
         int t;
         int downloadtime;
         pthread_attr_t thread_attr;
         pthread_attr_init(&thread_attr);
         pthread_attr_setdetachstate(&thread_attr,PTHREAD_CREATE_JOINABLE);
         // The detach state attribute determines whether a thread created using the thread
         // attributes  object attr will be created in a joinable or a detached state.
         for(t=0;t<NUM_OF_TASKS;t++){
           printf("creating thread %d, please help me to download %s\n", t, files[t]);
           rc = pthread_create(&threads[t], &thread_attr, downloadfile, (void *)files[t]);
           //[1] 参数是线程对象
           //[2] 线程属性
           //[3] 线程运行函数
           //[4] 线程运行函数的参数
           if (rc){
             printf("ERROR; return code from pthread_create() is %d\n", rc);
             exit(-1);
           }
         }
         pthread_attr_destroy(&thread_attr);
         for(t=0;t<NUM_OF_TASKS;t++){
           pthread_join(threads[t],(void**)&downloadtime);
           // 获取返回值并传给主线程
           printf("Thread %d downloads the file %s in %d minutes.\n",t,files[t],downloadtime);
         }
         pthread_exit(NULL);
      }
```
    - ![image.png](../assets/image_1649665932703_0.png)
```shell
      gcc download.c -lpthread
```
### Data
      - ![image.png](../assets/image_1649666236716_0.png)
        - 线程栈上的本地数据
          - 管理栈 `ulimit [-a][-s]`
          - 修改 `int pthread_attr_setstacksize(pthread_attr_t *attr, size_t stacksize);`
          - 线程栈之间还会有小块区域，用来隔离保护各自的栈空间。一旦另一个线程踏入到这个隔离区，就会引发段错误
        - 在整个进程里共享的全局数据
        - 线程私有数据 (Thread Specific Data)
          - 声明 `int pthread_setspecific(pthread_key_t key, const void *value)`
            - 创建一个 key，伴随着一个析构函数
          - 设置 key 对应的 value
            - `int pthread_setspecific(pthread_key_t key, const void *value)`
          - 获取 key 对应的 value
            - `void *pthread_getspecific(pthread_key_t key)`
          - 而等到线程退出的时候，就会调用析构函数释放 value
### Protected
      - Mutex (Mutual Exclusion), 互斥
```cpp
          #include <pthread.h>
          #include <stdio.h>
          #include <stdlib.h>
          #mark:  NUM_OF_TASKS 5
          int money_of_tom = 100;
          int money_of_jerry = 100;
          // 第一次运行去掉下面这行
          pthread_mutex_t g_money_lock;
          void *transfer(void *notused){
            pthread_t tid = pthread_self();
            printf("Thread %u is transfering money!\n", (unsigned int)tid);
            // 第一次运行去掉下面这行
            pthread_mutex_lock(&g_money_lock);
            sleep(rand()%10);
            money_of_tom+=10;
            sleep(rand()%10);
            money_of_jerry-=10;
            // 第一次运行去掉下面这行
            pthread_mutex_unlock(&g_money_lock);
            printf("Thread %u finish transfering money!\n", (unsigned int)tid);
            pthread_exit((void *)0);
          }
          int main(int argc, char *argv[]){
            pthread_t threads[NUM_OF_TASKS];
            int rc;
            int t;
            // 第一次运行去掉下面这行
            pthread_mutex_init(&g_money_lock, NULL);
            for(t=0;t<NUM_OF_TASKS;t++){
              rc = pthread_create(&threads[t], NULL, transfer, NULL);
              if (rc){
                printf("ERROR; return code from pthread_create() is %d\n", rc);
                exit(-1);
              }
            }
            for(t=0;t<100;t++){
              // 第一次运行去掉下面这行
              pthread_mutex_lock(&g_money_lock);
              printf("money_of_tom + money_of_jerry = %d\n", money_of_tom + money_of_jerry);
              // 第一次运行去掉下面这行
              pthread_mutex_unlock(&g_money_lock);
            }
            // 第一次运行去掉下面这行
            pthread_mutex_destroy(&g_money_lock);
            pthread_exit(NULL);
          }
```
          - ![image.png](../assets/image_1649667136198_0.png)
```cpp
          #include <pthread.h>
          #include <stdio.h>
          #include <stdlib.h>
          #mark:  NUM_OF_TASKS 3
          #mark:  MAX_TASK_QUEUE 11
          char tasklist[MAX_TASK_QUEUE]="ABCDEFGHIJ";
          int head = 0;
          int tail = 0;
          int quit = 0;
          pthread_mutex_t g_task_lock;
          pthread_cond_t g_task_cv;
          void *coder(void *notused){
            pthread_t tid = pthread_self();
            while(!quit){
              pthread_mutex_lock(&g_task_lock);
              while(tail == head){
                if(quit){
                  pthread_mutex_unlock(&g_task_lock);
                  pthread_exit((void *)0);
                }
                printf("No task now! Thread %u is waiting!\n", (unsigned int)tid);
                pthread_cond_wait(&g_task_cv, &g_task_lock);
                printf("Have task now! Thread %u is grabing the task !\n", (unsigned int)tid);
              }
              char task = tasklist[head++];
              pthread_mutex_unlock(&g_task_lock);
              printf("Thread %u has a task %c now!\n", (unsigned int)tid, task);
              sleep(5);
              printf("Thread %u finish the task %c!\n", (unsigned int)tid, task);
            }
            pthread_exit((void *)0);
          }
          int main(int argc, char *argv[]){
            pthread_t threads[NUM_OF_TASKS];
            int rc;
            int t;
            pthread_mutex_init(&g_task_lock, NULL);
            pthread_cond_init(&g_task_cv, NULL);
            for(t=0;t<NUM_OF_TASKS;t++){
              rc = pthread_create(&threads[t], NULL, coder, NULL);
              if (rc){
                printf("ERROR; return code from pthread_create() is %d\n", rc);
                exit(-1);
              }
            }
            sleep(5);
            for(t=1;t<=4;t++){
              pthread_mutex_lock(&g_task_lock);
              tail+=t;
              printf("I am Boss, I assigned %d tasks, I notify all coders!\n", t);
              pthread_cond_broadcast(&g_task_cv);
              pthread_mutex_unlock(&g_task_lock);
              sleep(20);
            }
            pthread_mutex_lock(&g_task_lock);
            quit = 1;
            pthread_cond_broadcast(&g_task_cv);
            pthread_mutex_unlock(&g_task_lock);
            pthread_mutex_destroy(&g_task_lock);
            pthread_cond_destroy(&g_task_cv);
            pthread_exit(NULL);
          }
```
          - ![image.png](../assets/image_1649668596808_0.png)
## ch03 progress [[data-structure]]
    - ![image.png](../assets/image_1650000073242_0.png)
### 进程链表
```c
        struct list_head    tasks;
```
        via: https://github.com/torvalds/linux/blob/a19944809fe9942e6a96292490717904d0690c21/include/linux/sched.h#L854=
      - ![image.png](../assets/image_1650003276235_0.png)
#### 任务 ID
```c
          pid_t pid;  // process id
          pid_t tgid; // thread group ID
          struct task_struct *group_leader;
```
          via: https://github.com/torvalds/linux/blob/master/include/linux/sched.h & https://docs.huihoo.com/doxygen/linux/kernel/3.7/include_2linux_2sched_8h_source.html
          - 只有主线程
            - pid, tgid, group_leader 全指向自己
          - 有其他线程
            - 线程有自己的 pid，tgid 就是进程的主线程的 pid，group_leader 指向的就是进程的主线程
#### 信号处理
```c
          /* Signal handlers: */
          struct signal_struct  *signal;
          struct sighand_struct *sighand;   // 正在通过信号处理函数进行处理
          sigset_t        blocked;    // 被阻塞暂不处理
          sigset_t        real_blocked;
          sigset_t        saved_sigmask;
          struct sigpending   pending;    // 尚等待处理
          unsigned long     sas_ss_sp;    // 开辟新的栈专门用于信号处理
          size_t          sas_ss_size;
          unsigned int      sas_ss_flags;
```
#### 任务状态
```c
           volatile long  state;    /* -1 unrunnable, 0 runnable, >0 stopped */
           int      exit_state;
           unsigned int   flags;
```
        - state（状态）可以取的值定义在 include/linux/sched.h 头文件中
```c
            // bitset set
            /* Used in tsk->state: */
            #mark:  TASK_RUNNING                    0
            #mark:  TASK_INTERRUPTIBLE              1
            #mark:  TASK_UNINTERRUPTIBLE            2
            #mark:  __TASK_STOPPED                  4
            #mark:  __TASK_TRACED                   8
            /* Used in tsk->exit_state: */
            #mark:  EXIT_DEAD                       16
            #mark:  EXIT_ZOMBIE                     32
            #mark:  EXIT_TRACE                      (EXIT_ZOMBIE | EXIT_DEAD)
            /* Used in tsk->state again: */
            #mark:  TASK_DEAD                       64
            #mark:  TASK_WAKEKILL                   128
            #mark:  TASK_WAKING                     256
            #mark:  TASK_PARKED                     512
            #mark:  TASK_NOLOAD                     1024
            #mark:  TASK_NEW                        2048
            #mark:  TASK_STATE_MAX                  4096
```
        - ![image.png](../assets/image_1650000764075_0.png)
          - `TASK_RUNNING`: 进程在时刻准备运行的状态
          - 在运行中的进程，一旦要进行一些 I/O 操作，需要等待 I/O 完毕，这个时候会释放 CPU，进入睡眠状态
            - 睡眠状态
              - `TASK_INTERRUPTIBLE`，可中断的睡眠状态
                - 信号来被唤醒 -> 唤醒后不继续刚才的操作，而是进行信号处理
              - `TASK_UNINTERRUPTIBLE`，不可中断的睡眠状态
                - 死等 I/O 操作完成
                - 重启电脑
          - `TASK_KILLABLE`，可以终止的新睡眠状态
            - 运行原理类似 `TASK_UNINTERRUPTIBLE`
            - 但可以响应致命信号
          - `TASK_WAKEKILL` 接收到致命信号时唤醒进程
```c
              #mark:  TASK_KILLABLE           (TASK_WAKEKILL | TASK_UNINTERRUPTIBLE)
```
          - TASK_STOPPED
            - 在进程接收到 SIGSTOP、SIGTTIN、SIGTSTP 或者 SIGTTOU 信号之后进入该状态
          - TASK_TRACED
            - 进程被 debugger 等进程监视，进程执行被调试程序所停止
            - 当一个进程被另外的进程所监视，每一个信号都会让进程进入该状态。
            - 一旦一个进程要结束，先进入的是 EXIT_ZOMBIE 状态，但是这个时候它的父进程还没有使用 wait() 等系统调用来获知它的终止信息，此时进程就成了僵尸进程
          - EXIT_DEAD 是进程的最终状态
          - EXIT_ZOMBIE 和 EXIT_DEAD 也可以用于 exit_state
          - 上面的进程状态和进程的运行、调度有关系，
#### Flags 标志
            - 在 flags 字段中，被定义称为宏，以 PF 开头。
```c
              #mark:  PF_EXITING    0x00000004
              #mark:  PF_VCPU     0x00000010
              #mark:  PF_FORKNOEXEC 0x00000040
```
            - PF_EXITING
              - 正在退出
              - 当有这个 flag 的时候，在函数 find_alive_thread 中，找活着的线程，遇到有这个 flag 的，就直接跳过
            - PF_VCPU
              - 进程运行在虚拟 CPU 上
              - 在函数 account_system_time 中，统计进程的系统运行时间，如果有这个 flag，就调用 account_guest_time，按照客户机的时间进行统计
            - PF_FORKNOEXEC
              - fork 完了，还没有 exec
              - 在 _do_fork 函数里面调用 copy_process，这个时候把 flag 设置为 PF_FORKNOEXEC。当 exec 中调用了 load_elf_binary 的时候，又把这个 flag 去掉
#### 进程调度
        - 状态切换
```c
          // 是否在运行队列上
          int             on_rq;
          // 优先级
          int             prio;
          int             static_prio;
          int             normal_prio;
          unsigned int        rt_priority;
          // 调度器类
          const struct sched_class  *sched_class;
          // 调度实体
          struct sched_entity     se;
          struct sched_rt_entity    rt;
          struct sched_dl_entity    dl;
          // 调度策略
          unsigned int        policy;
          // 可以使用哪些 CPU
          int             nr_cpus_allowed;
          cpumask_t         cpus_allowed;
          struct sched_info     sched_info;
```
#### 运行统计信息
```c
          u64       utime;        // 用户态消耗的 CPU 时间
          u64       stime;        // 内核态消耗的 CPU 时间
          unsigned long nvcsw;        // 自愿 (voluntary) 上下文切换计数
          unsigned long nivcsw;       // 非自愿 (involuntary) 上下文切换计数
          u64       start_time;     // 进程启动时间，不包含睡眠时间
          u64       real_start_time;  // 进程启动时间，包含睡眠时间
```
#### 进程亲缘关系
        - ![image.png](../assets/image_1650001657755_0.png)
```c
          struct task_struct __rcu *real_parent;  /* real parent process */
          struct task_struct __rcu *parent;     /* recipient of SIGCHLD, wait4() reports */
          struct list_head children;          /* list of my children */
          struct list_head sibling;           /* linkage in my parent's children list */
```
          - parent 指向其父进程。当它终止时，必须向它的父进程发送信号。
          - children 表示链表的头部。链表中的所有元素都是它的子进程。
          - sibling 用于把当前进程插入到兄弟链表中。
            - 通常情况下，real_parent 和 parent 是一样的
            - 当子进程作为父进程时候, real_parent 和 parent 不一样
#### 进程权限
        - 项目组权限的控制范畴
```c
            /* Objective and real subjective task credentials (COW): */
            const struct cred __rcu         *real_cred;
            /* Effective (overridable) subjective task credentials (COW): */
            const struct cred __rcu         *cred;
```
          - `Objective` -> “谁能操作我”，很显然，这个时候我就是被操作的对象
          - `Subjective` -> “我能操作谁”，这个时候我就是 Subjective，那个要被我操作的就是 Objectvie
          - `real_cred` 就是说明谁能操作我这个进程
          - `cred` 就是说明我这个进程能够操作谁
```c
              struct cred {
              ......
                      kuid_t          uid;            /* real UID of the task */
                      kgid_t          gid;            /* real GID of the task */
                      kuid_t          suid;           /* saved UID of the task */
                      kgid_t          sgid;           /* saved GID of the task */
                      kuid_t          euid;           /* effective UID of the task */
                      kgid_t          egid;           /* effective GID of the task */
                      kuid_t          fsuid;          /* UID for VFS ops */
                      kgid_t          fsgid;          /* GID for VFS ops */
              ......
                      kernel_cap_t    cap_inheritable; /* caps our children can inherit */
                      kernel_cap_t    cap_permitted;  /* caps we're permitted */
                      kernel_cap_t    cap_effective;  /* caps we can actually use */
                      kernel_cap_t    cap_bset;       /* capability bounding set */
                      kernel_cap_t    cap_ambient;    /* Ambient capability set */
              ......
              } __randomize_layout;
```
              - `uid` 和 `gid`
                - 谁启动的进程，就是谁的 ID
                - 权限审核的时候，往往不比较这两个，也就是说不大起作用
              - `euid` 和 `egid`，effective user/group id
                - 当这个进程要操作消息队列、共享内存、信号量等对象的时候，其实就是在比较这个用户和组是否有权限
              - `suid` 和 `fsgid`，filesystem user/group id
                - 对文件操作会审核的权限
              - ![image.png](../assets/image_1650002704970_0.png)
              - `chmod u+s program` -> 设置 `set-user-ID` 的标识位，把游戏的权限变成 `rwsr-xr-x`
                - `uid` 当然还是用户 A; `euid` 和 `fsuid` 都改成用户 B
              - ==一个进程可以随时通过 setuid 设置用户 ID==
                - 游戏程序的用户 B 的 ID 还会保存在一个地方，这就是 suid 和 sgid，也就是 saved uid 和 save gid
                - 这样就可以很方便地使用 setuid，通过设置 uid 或者 suid 来改变权限。
        - `capabilities` 位图
```c
            #mark:  CAP_CHOWN             0
            #mark:  CAP_KILL              5
            #mark:  CAP_NET_BIND_SERVICE  10
            #mark:  CAP_NET_RAW           13
            #mark:  CAP_SYS_MODULE        16
            #mark:  CAP_SYS_RAWIO         17
            #mark:  CAP_SYS_BOOT          22
            #mark:  CAP_SYS_TIME          25
            #mark:  CAP_AUDIT_READ        37
            #mark:  CAP_LAST_CAP          CAP_AUDIT_READ
```
          - 粒度小
          - cap_permitted 表示进程能够使用的权限。但是真正起作用的是 cap_effective。cap_permitted 中可以包含 cap_effective 中没有的权限。一个进程可以在必要的时候，放弃自己的某些权限，这样更加安全。假设自己因为代码漏洞被攻破了，但是如果啥也干不了，就没办法进一步突破。
          - cap_inheritable 表示当可执行文件的扩展属性设置了 inheritable 位时，调用 exec 执行该程序会继承调用者的 inheritable 集合，并将其加入到 permitted 集合。但在非 root 用户下执行 exec 时，通常不会保留 inheritable 集合，但是往往又是非 root 用户，才想保留权限，所以非常鸡肋。
          - cap_bset，也就是 capability bounding set，是系统中所有进程允许保留的权限。如果这个集合中不存在某个权限，那么系统中的所有进程都没有这个权限。即使以超级用户权限执行的进程，也是一样的。
          - 这样有很多好处。例如，系统启动以后，将加载内核模块的权限去掉，那所有进程都不能加载内核模块。这样，即便这台机器被攻破，也做不了太多有害的事情。
          - cap_ambient 是比较新加入内核的，就是为了解决 cap_inheritable 鸡肋的状况，也就是，非 root 用户进程使用 exec 执行一个程序的时候，如何保留权限的问题。当执行 exec 的时候，cap_ambient 会被添加到 cap_permitted 中，同时设置到 cap_effective 中。
#### 内存管理
        - mm_struct
```c
          struct mm_struct                *mm;
          struct mm_struct                *active_mm;
```
#### 文件与文件系统
```c
          /* Filesystem information: */
          struct fs_struct                *fs;
          /* Open file information: */
          struct files_struct             *files;
```
### 用户态的执行和内核态的执行串起来
```c
        struct thread_info    thread_info;
        void  *stack;
```
    - 用户态函数栈
      - x86
        - ![image.png](../assets/image_1650005541305_0.png)
        - ESP (Extended Stack Pointer): 栈顶指针寄存器
          - 入栈操作 Push 和出栈操作 Pop 指令，会自动调整 ESP 的值
        - EBP (Extended Base Pointer): 栈基地址指针寄存器
          - 指向当前栈帧的最底部
        - A 调用 B，A 的栈里面包含 A 函数的局部变量，然后是调用 B 的时候要传给它的参数，然后返回 A 的地址，这个地址也应该入栈，这就形成了 A 的栈帧。接下来就是 B 的栈帧部分了，先保存的是 A 栈帧的栈底位置，也就是 EBP。因为在 B 函数里面获取 A 传进来的参数，就是通过这个指针获取的，接下来保存的是 B 的局部变量等等。当 B 返回的时候，返回值会保存在 EAX 寄存器中，从栈中弹出返回地址，将指令跳转回去，参数也从栈中弹出，然后继续执行 A。
      - x64
        - ![image.png](../assets/image_1650004463135_0.png)
        - `ax` 保存函数调用的返回结果
        - `rsp` 栈顶指针寄存器
          - 指向栈顶位置
          - 堆栈的 Pop 和 Push 操作会自动调整 rsp
        - `rbp` 栈基指针寄存器
          - 指向当前栈帧的起始位置
        - `rdi`、`rsi`、`rdx`、`rcx`、`r8`、`r9`: 参数传递
    - 内核态函数栈
      - ![image.png](../assets/image_1650003890869_0.png)
    - x86 vs x64
      - ![image.png](../assets/image_1650004552227_0.png)
## ch04 调度
    - ![image.png](../assets/image_1650006220845_0.png)
    - ![image.png](../assets/image_1650006602228_0.png)
## ch05 进程创建
    - ![image.png](../assets/image_1650007561931_0.png)
## ch06 线程创建
    - ![image.png](../assets/image_1650007954430_0.png)
## 网络系统
  - 网络分层
    - 两种网络协议模型
      - ![image.png](image_1654591907792_0.png)
    - 应用层 <- 通信 (**Socket 系统调用**) -> 内核
      - Socket 属于操作系统的概念，而非网络协议分层的概念
      - 操作系统选择对网络协议的实现模式
        - 二到四层的处理代码在内核里面
          - 用层例如浏览器、Nginx、Tomcat 都是用户态的
          - 内核里面对于网络包的处理是不区分应用的
        - 四层再往上，就需要区分网络包发给哪个应用
          - 在传输层的 TCP 和 UDP 协议里面，都有端口的概念，不同的应用监听不同的端口
            - 服务端 Nginx 监听 80
            - Tomcat 监听 8080
            - 客户端浏览器监听一个随机端口
            - FTP 客户端监听另外一个随机端口
        - 七层的处理代码让应用自己去做
        - 两者需要跨内核态和用户态通信 (Socket)
  - 发送数据包
    - ![image.png](image_1654591992089_0.png)
    - ![image.png](image_1654591701492_0.png)
    - 在客户端浏览器，我们将请求封装为 HTTP 协议，通过 Socket 发送到内核。内核的网络协议栈里面，在 TCP 层创建用于维护连接、序列号、重传、拥塞控制的数据结构，将 HTTP 包加上 TCP 头，发送给 IP 层，IP 层加上 IP 头，发送给 MAC 层，MAC 层加上 MAC 头，从硬件网卡发出去。
    - 网络包会先到达网络 1 的交换机。我们常称交换机为二层设备，这是因为，交换机只会处理到第二层，然后它会将网络包的 MAC 头拿下来，发现目标 MAC 是在自己右面的网口，于是就从这个网口发出去。
    - 网络包会到达中间的 Linux 路由器，它左面的网卡会收到网络包，发现 MAC 地址匹配，就交给 IP 层，在 IP 层根据 IP 头中的信息，在路由表中查找。下一跳在哪里，应该从哪个网口发出去？在这个例子中，最终会从右面的网口发出去。我们常把路由器称为三层设备，因为它只会处理到第三层。
    - 从路由器右面的网口发出去的包会到网络 2 的交换机，还是会经历一次二层的处理，转发到交换机右面的网口。
    - 最终网络包会被转发到 Linux 服务器 B，它发现 MAC 地址匹配，就将 MAC 头取下来，交给上一层。IP 层发现 IP 地址匹配，将 IP 头取下来，交给上一层。TCP 层会根据 TCP 头中的序列号等信息，发现它是一个正确的网络包，就会将网络包缓存起来，等待应用层的读取。
    - 应用层通过 Socket 监听某个端口，因而读取的时候，内核会根据 TCP 头中的端口号，将网络包发给相应的应用。
    - HTTP 层的头和正文，是应用层来解析的。通过解析，应用层知道了客户端的请求，例如购买一个商品，还是请求一个网页。当应用层处理完 HTTP 的请求，会将结果仍然封装为 HTTP 的网络包，通过 Socket 接口，发送给内核。
    - 内核会经过层层封装，从物理网口发送出去，经过网络 2 的交换机，Linux 路由器到达网络 1，经过网络 1 的交换机，到达 Linux 服务器 A。在 Linux 服务器 A 上，经过层层解封装，通过 socket 接口，根据客户端的随机端口号，发送给客户端的应用程序，浏览器。于是浏览器就能够显示出一个绚丽多彩的页面了。
  - Function in [[system-c]] / [[cpp]]
```c
      int socket(int domain, int type, int protocol);
```
      - domain: 使用 IP 层协议
        - `AF_INET` 表示 IPv4
        - `AF_INET6` 表示 IPv6。
      - type: 类型
        - `SOCK_STREAM`
          - TCP 面向流的
        - `SOCK_DGRAM`
          - UDP 面向数据报
        - `SOCK_RAW`
          - 可以直接操作 IP 层，或者非 TCP 和 UDP 的协议
            - ICMP
      - protocol: 协议
        - IPPROTO_TCP
        - IPPTOTO_UDP
  - TCP
    - ![image.png](image_1654673717275_0.png)
    - bind
      - IP 地址和端口号
      - 三次握手
        - 客户端和服务端的状态通过三次网络交互，达到初始状态是协同的状态
        - 内核完成
```c
        int bind(int sockfd, const struct sockaddr *addr, socklen_t addrlen);
        /* sockfd: socket 文件描述符
         */
        struct sockaddr_in {
          __kernel_sa_family_t  sin_family; /* Address family (IPv4, AF_INET) */
          __be16        sin_port; /* Port number            */
          struct in_addr    sin_addr; /* Internet address (IP Address)  */
          /* Pad to size of `struct sockaddr'. */
          unsigned char   __pad[__SOCK_SIZE__ - sizeof(short int) -
              sizeof(unsigned short int) - sizeof(struct in_addr)];
        };
        struct in_addr {
          __be32  s_addr;
        };
```
        - `be`: “big-endian” via [[encoding/character/endian]]
          - 如果在网络上传输超过 1 Byte 的类型, 就要区分大端 (Big Endian) & 小端 (Little Endian)
        - 客户端不需要 bind?
          - 不关心客户端 (不会被访问) 监听到了哪里, 浏览器 随机分配一个端口就可以
        - `TCP/IP` 栈: 大端
          - `x86`: 小端
          - 发出转换
    - listen
```c
        int listen(int sockfd, int backlog);
```
      - 服务端只需要调用 accept，等待内核完成了至少一个连接的建立，才返回
```c
          int accept(int sockfd, struct sockaddr *addr, socklen_t *addrlen);
```
        - 如果没有一个连接完成了三次握手，accept 就一直等待
        - 如果有多个客户端发起连接，并且在内核里面完成了多个三次握手，建立了多个连接，这些连接会被放在一个队列里面
```c
      int connect(int sockfd, const struct sockaddr *addr, socklen_t addrlen);
```
    - 用到的 socket
      - 监听 socket
      - 已连接 socket
  - UDP
    - ![image.png](image_1654699111792_0.png)
    - 对于 UDP 来讲, 甚至都不存在客户端和服务端的概念
      - 只要有一个 socket，多台机器就可以任意通信
        - 每次通信时，调用 sendto 和 recvfrom，都要传入 IP 地址和端口
```c
      ssize_t sendto(int sockfd, const void *buf, size_t len, int flags, const struct sockaddr *dest_addr, socklen_t addrlen);
      ssize_t recvfrom(int sockfd, void *buf, size_t len, int flags, struct sockaddr *src_addr, socklen_t *addrlen);
```
  - Socket 内核 #[[data-structure]]
## References
  - [EM italics parent of a parent SPAN going on next line · Issue #111 · GitMurf/roam-highlighter · GitHub](https://github.com/GitMurf/roam-highlighter/issues/111)