---
title: "为什么Firmware既提供ACPI-又提供Smbios表呢"
created: 2025-03-13T19:33:54
modified: 2025-03-13T19:33:54
description: "UEFI要除了初始化硬件，还提供了两张表：SMBIOS table和ACPI table。两个表的侧重点不同：SMBIOS重点在于…"
source: "https://www.zhihu.com/question/619432704/answer/3571376762"
tags:
tags-link:
type: "archive-web"
---
UEFI要除了初始化硬件，还提供了两张表：SMBIOS table和ACPI table。两个表的侧重点不同：

- SMBIOS重点在于主板/平台的信息汇报，信息流是单向的，如CPU、内存、PCIe、槽位、主板上料件等等信息，甚至可以和BMC、EC、AMT等结合做资产管理；
- ACPI重点在于控制，数据流和控制流是双向的。ACPI的前期重点在于CPU和外设等的电源、功耗和性能汇报和控制，后期加了越来越多的东西，但本质还是控制，报告的信息如设备树，也是为了让OS知道有哪些设备，之间是什么关系，有什么控制方式等。ACPI有很多表，还有很多Method等，Method是控制流自不待言，甚至静态表里面也暴露了很多寄存器或者MMIO，用于操作系统来进行控制。

OS实际上是通过ACPI和BIOS来交互的，而不是像SMBIOS那样一过性的单向汇报。但如果想要在OS起来后，再通过动态修改ACPI所在的内存来动态修改ACPI还是不可行的，因为OS会把这块内存的内容copy到自己的一块私有内存中，原来的就不用了。要修改ACPI，我们业内叫做Patch ACPI Table，还是应该在BIOS ReadyToBoot之前，修改对应内存。