---
title: "手把手教-如何模拟IC加密卡"
created: 2025-05-11T12:43:06
modified: 2025-05-11T12:43:06
description: "免责声明：本文涉及的技术仅供安全学习和教学用途，禁止非法使用！！！ 前言现在生活中少不了各种卡，公交卡、地铁卡、银行卡、门禁卡等，它们都是什么卡？ID卡？IC卡？另外带NFC功能的手机也能刷卡使用，笔者通过…"
source: "https://zhuanlan.zhihu.com/p/81384126"
tags:
tags-link:
type: "archive-web"
---
免责声明：本文涉及的技术仅供安全学习和教学用途，禁止非法使用！！！

## 前言

现在生活中少不了各种卡，公交卡、地铁卡、银行卡、门禁卡等，它们都是什么卡？ID卡？IC卡？另外带NFC功能的手机也能刷卡使用，笔者通过本文科普一下关于卡的知识，另外文中还有模拟加密卡等一系列干货，各位要看到最后哦！！！

## ID和IC

**ID卡**：全称为身份识别卡（Identification Card），是一种不可写入的感应卡，含固定的编号，主要有台湾SYRIS的EM格式、美国HIDMOTOROLA等各类ID卡，

**IC卡**：全称集成电路卡（Integrated Circuit Card），又称智能卡（Smart Card）。可读写，容量大，有加密功能，数据记录可靠，使用更方便，如一卡通系统，消费系统等，目前主要有PHILIPS的Mifare系列卡

**主要区别**：ID卡不可写入数据，其记录内容(卡号)只可由芯片生产厂一次性写入，开发商只可读出卡号加以利用,无法根据系统的实际需要制订新的号码管理制度；而IC卡不仅可由授权用户读出大量数据，而且亦可由授权用户写入大量数据(如新的卡号,用户的权限,用户资料等)，IC卡所记录内容可反复擦写

IC卡由于其固有的信息安全、便于携带、比较完善的标准化等优点，在身份认证、银行、电信、公共交通、车场管理等领域正得到越来越多的应用，例如二代身份证，银行的电子钱包，电信的手机SIM卡，公共交通的公交卡、地铁卡，用于收取停车费的停车卡、小区门禁卡等

IC卡按结构分有：接触式IC卡和非接触式IC卡

**接触式IC卡**，该类卡是通过IC卡读写设备的触点与IC卡的触点接触后进行数据的读写

![](https://pica.zhimg.com/v2-dea0bb2581fb089bb052adce61764756_r.jpg)

接触式IC卡和读卡机

**非接触式IC卡**，该类卡与卡设备无电路接触，而是通过非接触式的读写技术进行读写（例如RFID、NFC），其内嵌芯片除了CPU、逻辑单元、存储单元外，增加了射频收发电路。该类卡一般用在使用频繁、信息量相对较少、可靠性要求较高的场合

![](https://pic3.zhimg.com/v2-b5c330e1d23fe6012e18a884e2ba42be_r.jpg)

IC 白卡IC 白卡

![](https://pic2.zhimg.com/v2-a5b7ed88b2780cc1c2c1537c4d8ee897_r.jpg)

IC钥匙扣IC钥匙扣

![](https://pic4.zhimg.com/v2-3ecc1e7f700af2d8f8e8daa90a80db51_r.jpg)

IC滴胶卡IC滴胶卡

![](https://picx.zhimg.com/v2-ec563e2b3736daef0fc213e573c558b9_r.jpg)

IC手机贴IC手机贴

NFC是现在主流的非接触式IC卡的读卡技术，其全称是近场通信（near field communication），是基于无线射频识别RFID（Radio Frequency Identification）技术发展起来的一种近距离无线通信技术，与RFID一样，NFC也是通过频谱中无线频率部分的电磁感应耦合方式传递，但两者之间还是存在很大的区别。NFC的传输范围比RFID小，RFID的传输范围可以达到0~1m，但由于NFC采取了独特的信号衰减技术，相对于RFID来说NFC具有成本低、带宽高、能耗低等特点。

NFC技术主要特征如下：

1\. 用于近距离(10cm以内)安全通信的无线通信技术

2\. 射频频率：13.56MHz

3\. 射频兼容：ISO 14443，ISO 15693，Felica标准

4\. 数据传输速度：106kbit/s，212 kbit/s，424kbit/s

5\. 现在手机都包含NFC功能，其主板上嵌入了NFC模块，具有三种功能模式：NFC手机作为识读设备(读写器)、NFC手机作为被读设备(卡模拟)、NFC手机之间的点对点通信应用

## IC卡基础知识

IC卡中最常见的是NXP Mifare系列卡，根据卡内使用芯片的不同，分为

l Mifare S50，简称M1卡，是最常见的卡，出厂固化UID，可存储修改数据

l Mifare UltraLight，简称M0卡，低成本卡，出厂固化UID，可存储修改数据

l Mifare UID Chinese magic card，简称UID卡，M1卡的变异版本，可修改UID，国外叫做中国魔术卡，可以用来完整克隆M1 S50卡的数据；但是现在新的读卡系统通过检测卡片对特殊指令的回应，可以检测出UID卡，因此可以来拒绝UID卡的访问，来达到屏蔽复制卡的功能

l 针对UID卡被屏蔽的问题，另外还有变异版本FUID卡和CUID卡，FUID卡的UID只能修改一次，起防屏蔽作用，专门对付物业升级的防复卡和防复读头；CUID卡则是针对FUID卡做的优化，支持UID号重复擦写，无需锁卡自动起防屏蔽作用

以标准M1卡为例，其容量为1K字节，总共分为16个扇区，每个扇区分为4个数据块，每个数据块16个字节

每个扇区中的块按照0 ~ 3编号，第3个块中包含KEYA（密钥A）、控制位、KEYB（密钥B），每个扇区可以通过它包含的密钥A或者密钥B单独加密

0扇区0块是特殊的数据块，用于存放制造商代码，包括芯片序列号UID，ATQA和SAK

非加密卡和加密卡的区别就是，非加密卡中所有扇区的KEYA和KEYB数值都是默认值FFFFFFFFFFFF；而加密卡中，其中有扇区的KEYA和KEYB不等于FFFFFFFFFFFF，部分扇区加密的卡称半加密卡，所有扇区都加密的卡称全加密卡

![](https://picx.zhimg.com/v2-afca473d98e1f2a744f48dd0ec82e95b_r.jpg)

M1卡数据结构

手机中安装MCT（mifare classic tool），无需root，可读取mifare系列IC卡的数据

![](https://picx.zhimg.com/v2-ebdd86b83cf6632d0c89b68f12c30eb1_r.jpg)

![](https://pic1.zhimg.com/v2-cff4b29981dd7406ace17582b996a614_r.jpg)

MCT读取的数据MCT读取的数据

## 加密卡解密

## 解密设备

对于加密的IC卡，如果想读取卡中的数据，首先需要获取所有扇区的KEYA或者KEYB，一般密钥都是保密的，我们手上只有卡的情况下，解密则需要通过硬件支持了，比如pn532、acr122u、proxmark3等，笔者使用的是Proxmark3，忽略性价比因素，相比于其它傻瓜式设备，proxmark3的功能更全面些，可玩性也更高

![](https://pic2.zhimg.com/v2-70adc718d0eb3c693726647fe7520cef_r.jpg)

![](https://pic2.zhimg.com/v2-dcbc0000c76c19dea06e05e5d082eb49_r.jpg)

Proxmark3

![](https://pic3.zhimg.com/v2-57730b3603a4064c332f11a70e5fade4_r.jpg)

读取IC卡

Proxmark3是由Jonathan Westhues设计并且开发的开源硬件，其主要用RFID的嗅探、读取以及克隆等的操作

官方网站：[http://www.proxmark.org/](http://www.proxmark.org/)

官方论坛：[http://www.proxmark.org/forum/index.php](http://www.proxmark.org/forum/index.php)

官方固件（Github）：[https://github.com/Proxmark/proxmark3/](https://github.com/Proxmark/proxmark3/)

![](https://pic4.zhimg.com/v2-f5b7854dc6d775d161ff5ad03519f0a5_r.jpg)

官方固件更新记录：最近更新2019/03/15

除了官方软件，还有其它大神的软件：Proxbrute、EMV、Iceman

![](https://pic4.zhimg.com/v2-83a6aceb56c483d9e32fda8c8c9be0dd_r.jpg)

笔者用的是冰人（iceman）固件：[https://github.com/iceman1001/proxmark3](https://github.com/iceman1001/proxmark3)

![](https://pic3.zhimg.com/v2-16f6a1e21a6a445aaae5a2137f378a88_r.jpg)

冰人固件更新记录：最近更新2019/03/06

## 解密方法

有了设备，开始IC卡解密，基本的思路：读取卡片信息 --> 获取任意扇区的密钥 --> 用已知扇区密钥求所有扇区密钥 --> 读出卡片所有数据

**第一步：读取卡片信息**

用USB连接proxmark3后，安装完驱动，可以在设备管理器中查看设备串口号

![](https://pica.zhimg.com/v2-c4c58f1e909d72d21a2f453951e34c96_r.jpg)

串口识别COM4

打开PM3 Universal GUI软件，选择 COM4 连接proxmark3

![](https://picx.zhimg.com/v2-67bdf958fbb2677d789c5ed2873cedbf_r.jpg)

查看Proxmark3的固件版本，发送指令：

![](https://pica.zhimg.com/v2-d3511dbc8f35f07700c628cb9256f0c4_r.jpg)

已刷冰人固件

在IC卡感应位置放上IC卡

![](https://pica.zhimg.com/v2-beca901cacd93a602d1a0b401625c026_r.jpg)

然后读取卡片信息，发送指令：

![](https://picx.zhimg.com/v2-17c268ac90caabfa79ed310bd6545815_r.jpg)

**第二步：获取任意扇区的密钥**

共有四种办法：

a) PRNG漏洞攻击得0扇区密钥

b) 默认密码扫描获得密钥

c) 嗅探读卡机与卡片交互数据获得密钥

d) 模拟成M1卡刷卡后获取密钥

a. PRNG漏洞攻击DARKSIDE ATTACK，发送指令：

> PRNG漏洞，是国外的安全研究人员发现，Mifare Classic采用的是Crypto-1私有加密算法，器算法的特点就是对称式的密码算法或者说是私钥密码系统。其主要组成部分是伪随机数发生器（PRNG）、48位的线性反馈移位寄存器（LFSR）以及非线性函数。由于算法中的Filter函数的设计出现缺陷，导致变线性反馈移位寄存器的后8位数值就有可能得到所对应的Keystream。这个缺陷类似于802.11b WEP算法，不同的明文有极高的可能性呗相同的Keystream，是的整个加密算法出现了漏洞

![](https://pic4.zhimg.com/v2-8c891be82205c5bee4f5c6e0b41f1d73_r.jpg)

找到有效密钥 ffffffffffff

b. 默认密码扫描Test Block Keys

c. 嗅探和d. 模拟都需要去现场，获取卡片或者天线 和读卡器之间通讯数据，分析数据得到密钥，比较麻烦笔者也未尝试，一般是前两种方法无法得到密钥的前提下才去现场嗅探

**第三步：用已知扇区密钥求所有扇区密钥**

利用嵌套认证MFOC漏洞，使用任何一个扇区的已知密钥（在第二步中获得）攻击，获取其它所有扇区的密钥，发送指令：

l hf mf nested 1 0 A FFFFFFFFFFFF t

其中“FFFFFFFFFFFF”是第二步中找到的有效密钥，“t”表示将找到的密钥导入仿真器内存中

![](https://pic3.zhimg.com/v2-31f411b7085a2e3c45b36ea7e92f924e_r.jpg)

res列全是 1 表示所有扇区密钥已找到

打印密钥，确认密钥已存入内存，发送指令：

![](https://pica.zhimg.com/v2-a980ba8778d9dfd2283d726d5a36ee60_r.jpg)

**第四步：读出卡片所有数据**

第三步中解密出的所有扇区密钥已保存在仿真器内存中

通过密钥将卡片数据读出，也保存在仿真器内存中，发送指令：

最后将仿真器内存中的卡片数据保存位文件TestData.eml，发送指令：

![](https://pic4.zhimg.com/v2-0adf62a12ee7b49bca080b2c9f38c4c3_r.jpg)

打开TestData.eml文件，可以看到所有扇区的数据都成功读取

![](https://picx.zhimg.com/v2-0d72991366d0c6050e2572d2c8e474a7_r.jpg)

## 加密卡复制

加密卡解密得到密钥，所有扇区的数据也可以读取出来，有了数据就可以复制到新IC卡中，笔者所在小区物业办张新卡需要￥30，笔者表示不服，自己解密复制卡的成本就几块钱

将数据写入卡中有两种方法：用Proxmark3写卡 或者 用手机MCT应用写卡

## Proxmark3写卡

**写UID卡：**

准备一张UID卡，读取卡片信息，其中Answers to magic commands: Yes表示这张卡是中国魔术卡（UID卡）

![](https://pic1.zhimg.com/v2-ac375f4f54b18d5f76749d068849a1b2_r.jpg)

写数据到UID卡中，发送指令：

![](https://pic2.zhimg.com/v2-a1f0a34be8a44cc2ceb1a57087daace9_r.jpg)

读出UID卡每个扇区中数据，以确认是否成功写入，发送指令：

![](https://picx.zhimg.com/v2-3da60ecae48b0c69b765523cf16bca35_r.jpg)

**cload**和**cgetsc**命令是专门针对UID卡的，换成其它类型卡比如CUID卡则无效

![](https://pic1.zhimg.com/v2-7d35516f3a25409391485e436f3e95b0_r.jpg)

**写CUID卡：**

那么写CUID卡该如何操作呢？现在大部分门禁系统都加入了屏蔽系统，使用复制的UID卡会出现只能使用一次，下次刷卡无效的情况，而CUID卡防屏蔽解决了这个问题，所以笔者继续研究如何写CUID卡，写CUID卡需要指令：

```text
hf mf wrbl blknum A/B KEYA/KEYB 000102030405060708090A0B0C0D0E0F
```

麻烦的是该指令每次只写1个块的数据，而卡中总共64块，所以需要执行64条指令，手动执行肯定比较耗时耗力，因此笔者写了lua脚本（cuidwrite.lua）自动执行写64块的操作

![](https://pic3.zhimg.com/v2-ea9d19427051244c73e07a74366acc1c_r.jpg)

......

![](https://pic4.zhimg.com/v2-af088e4a3fd5e92fdee6b586600a6d1f_r.jpg)

CUID写操作脚本执行

读取CUID卡片信息，其中Answers to magic commands: NO，只有UID卡才会返回YES

![](https://pic2.zhimg.com/v2-52be173328b5a370fdc4f7408bce9f59_r.jpg)

## MCT写卡

MCT写卡需要数据和密钥，可以只添加密钥，然后利用密钥直接读取卡片数据

1）编辑/增加密钥 ：新建密钥文件TestKey，进入密钥编辑页面，将密钥数据从电脑上复制然后粘贴进来

![](https://pic1.zhimg.com/v2-cff4b29981dd7406ace17582b996a614_r.jpg)

2）读取原卡数据：将原卡放在手机NFC感应区域，在MCT中选择正确的密钥TestKey，所有扇区数据就能成功读取

如果选择不正确的密钥，则无法读取完整数据

![动图封面](https://pic2.zhimg.com/v2-a05d8b99afbc26915df309b4b11e6f35_b.jpg)

3）保存数据至转储文件

![动图封面](https://pic2.zhimg.com/v2-100e0b4f17687b302e2b8850e564fe9d_b.jpg)

4）数据写入新卡：准备一张空白UID卡，识别卡片后，选择密钥文件和转储文件，选择扇区，等待写入完成即可

![](https://zhuanlan.zhihu.com/p/)

这么简单就完事了，还是太天真？

重新读取卡片数据确认，在MCT里选择比较转储功能，发现卡中0扇区0块的数据与转储文件不同，这说明0扇区0块的数据没有成功写入

![](https://pic1.zhimg.com/v2-5e56a7445232e41e6d58876b89b521e8_r.jpg)

后来笔者研究了下，原来需要在写转储时勾选 “高级：使能厂商块写入”选项，勾上这个选项后另外单独写一次0扇区

![](https://pic2.zhimg.com/v2-7d0fecf17297e3fb55d67637cfa2c077_r.jpg)

但是反复尝试了UID卡，这种方法也无法写入0扇区；尝试了CUID卡，这种方法可以写入0扇区

注：MCT方式只能写CUID卡，用MCT写卡没有Proxmark3稳定，有时会出现写坏锁死CUID卡的情况

## IC卡模拟（手机、手环）

**MIUI门卡**

小米MIUI推出了门卡模拟的功能，不仅可以将卡数据写入到手机中，而且手环也可以，当然需要写特殊手段，但是为了安全考量，小米官方都不支持加密卡的模拟

![](https://pic4.zhimg.com/v2-19635fc0f4d4c495501e45e4bd83138f_r.jpg)

笔者的小米MIX2板载NFC芯片是NXP 80T19

NXP 80T19芯片其模拟的卡类型属于NXP JCOP系列，Proxmark3的官方固件是不支持JCOP卡，后来笔者是刷了冰人固件才能正常识别MIX2模拟的门卡

NXP JCOP系列芯片卡是恩智浦NXP公司在高安全性的解决方案高性能产品。广泛应用如银行与金融，移动通信，公共交通，访客访问和网络接入等领域。支持接触式、非接触式、支持接触式与非接触式读写，内含有一个JCOP版本操作系统，并提供40 k-80K字节EEPROM存储器。NXP JCOP系列芯片卡出厂带传输密钥（Transport Key），需要经过初始化后，方可访问卡片内置的COS系统，因为此类芯片卡的安全系列非常高。

小米MIUI推出的门卡功能有两个模式：模拟实体门卡和添加虚拟门卡

![](https://picx.zhimg.com/v2-591e33b1a4955d359ada2d8713644e43_r.jpg)

**模拟实体门卡**

这个功能是将实体卡中的数据读取出来，然后通过手机模拟实体卡，将卡模拟到手机后，可以只带手机在刷卡机处刷卡，无需再另外带实体卡，轻便出行。可读取的门卡包括普通白卡、钥匙扣之类的IC卡

![](https://pic4.zhimg.com/v2-231ac76b0eb716027b35011cf405aafb_r.jpg)

但是模拟的卡中不包括加密卡，如果卡被识别为加密卡，则会提示“加密卡不支持模拟”

非加密卡，可以成功模拟，模拟过程中需要证件和密码认证，这功能必须进行安全因素的考量

![](https://zhuanlan.zhihu.com/p/)

![](https://zhuanlan.zhihu.com/p/)

手机放在IC卡感应器

![](https://pic2.zhimg.com/v2-75dbf86fa54f90fbc5e76988e06a064b_r.jpg)

Proxmark3读出的模拟门卡信息，UID与实体IC卡的相同

**添加虚拟门卡**

虚拟门卡可以根据场景开卡，选择自定义空白卡，相当于由MIUI自动生成一张0扇区不可更改的IC卡，剩下的扇区数据可以随意写入。如果物业允许，在物业处开通虚拟门卡的权限即可，不过一般小区物业不会同意的

![](https://pic3.zhimg.com/v2-dd295df68e860c2fda8a4028c096bde6_r.jpg)

虚拟门卡开卡

![](https://pic2.zhimg.com/v2-7d06782195675959d01f4e24620ad7b5_r.jpg)

Proxmark3读取到的虚拟门卡信息，UID由MIUI自动分配

**模拟加密卡**

现实中有个需求就是，想把手上的IC卡写到手机中，虚拟门卡是因其UID是由MIUI自动分配的，且生成后不可更改，虚拟门卡没条件开通门禁系统权限的条件下，只能选择模拟实体卡的功能了，但是模拟实体卡有个问题，前文中也提到过，现在使用的IC卡基本都是加密卡，模拟实体卡功能又不支持加密卡，那就没有办法了吗？

答案是肯定的，可以模拟加密卡，前方高能！！！真正的干货来了！！！

模拟加密卡的思路：获取加密卡数据 --> 只写UID信息到实体UID白卡中 --> 模拟UID白卡 --> 往模拟卡中写入加密数据

**第一步：获取加密卡数据**

用Proxmark3获取加密卡的密钥，然后读取所有加密数据，方法前文中有讲

**第二步：只写UID信息到实体UID白卡中**

Proxmark3上更换一张UID空白卡，然后写0扇区0块数据

![](https://pica.zhimg.com/v2-beca901cacd93a602d1a0b401625c026_r.jpg)

发送指令：

```text
hf mf csetblk 0 7295B829760804000214F34CBDBE2F1D
```

![](https://pic1.zhimg.com/v2-7e60ead467ff30a188109de92de844e0_r.jpg)

只写了0扇区0块的UID卡，因为未写加密数据，这张UID卡目前还是一张非加密卡

**第三步：模拟UID白卡**

手机上使用MIUI门卡的标准功能，模拟写了0扇区0块的UID卡

![](https://pic4.zhimg.com/v2-c3f10c65a17132c1b96d72bb184c14fd_r.jpg)

这一步相当于已将加密卡的0扇区写入到手机中

**第四步：往模拟卡中写入加密数据**

手机切换到卡模式，然后放在Proxmark3感应区域

![](https://zhuanlan.zhihu.com/p/)

用Proxmark3往手机的模拟门卡里写入加密数据，发送指令：

```text
hf mf restore 1 u 7295B829
```

![](https://pic2.zhimg.com/v2-b43c2b8c53ee81c2addef8f3f8c27a09_r.jpg)

. . .

![](https://picx.zhimg.com/v2-e3233bd58dff5987254825877b787c41_r.jpg)

1 ~ 63块数据成功写入

这一步写入了1 ~ 63块数据，但是0扇区0块数据无法写入，没关系因为0扇区0块数据已经在第三步中写入了

至此，所有扇区数据已写入到手机中，加密卡模拟成功完成

手机中可以设定刷卡方式设置，选择默认快捷卡片，只要靠近读卡器，手机自动唤醒切换到卡模式，并且首选默认快捷卡片

笔者模拟了公司门禁卡、小区物业门禁卡，加上MI Pay绑定的信用卡用于刷公交地铁，出行基本就不用带一堆卡了，一个手机全搞定

![](https://pic1.zhimg.com/v2-f40f815963741c4522d1d501110eeef0_r.jpg)

## 手环模拟

小米手环3 NFC版也可以通过相同方法模拟加密卡

![](https://pic2.zhimg.com/v2-6ab3e206f48dcaffc693059b7a957565_r.jpg)

## 总结

关于模拟加密卡功能，科技方便生活码农生活，笔者只尝试了小米系产品，另外华为系也有类似的门卡功能，等笔者手上有华为手机了另做尝试，苹果系则是要等iOS开方NFC权限，不知道红年马月了