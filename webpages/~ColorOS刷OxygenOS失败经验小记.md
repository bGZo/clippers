---
created: 2024-08-10T12:00:00
source: https://www.coolapk.com/feed/53858973?shareKey=ZWViYTUyZTM3OTcwNjZhZjQ0YzI~
type: archive-web
modified: 2025-01-15T11:38:15
---

oneplus11，ColorOS 刷 OxygenOS 失败经验小记 序言：由于类原生的 rom 采用的内核是不支持加载 gki 内核模块的 lineageOS 的 msm8550-5.15 内核，所以我决定选择使用支持 gki 内核的 oxygenOS 失败阶段是这样的。我首先通过 9008 模式刷了 ColorOS13-A29 版，然后通过 fastboot enhance 工具进入 fastbootd 模式刷入 oxygenod14…501 全球版（可视与欧版一致）。结果 ocdt 无论是刷 cph2449 还是保持国行原厂（PHB110）的，均可进入系统，扬声器无声音且播放视频时常卡顿（原因不明。属硬件解码不正常？），打电话听筒时是有声的。cph2449 基带正常，国行 ocdt 显示无基带（其实基带相关文件还在，只是不正常工作了）。同样方式刷了 oxygenod14…304 欧版也是一样。刷机后均进 recovery 清过数据，且排除 abl 分区影响。 后经多番尝试，成功刷入工作正常的 oxygen 步骤如此。先刷 oxygen13 欧版 (我用的是 13.1.0.595) 且刷 cph2449 的 ocdt（顺序忘了，但我肯定地认为不重要），然后开机激活进系统确认扬声器正常（这个步骤的必要性不确定）。随即我又尝试了通过 OTA(本地更新) 的方式刷了 oxygenod14…501 全球版（可视与欧版一致），进系统后扬声器正常，视频播放正常。进 recovery 再次清除数据后，激活进系统，扬声器与视频播放仍然正常。 下面时失败过程中获取的有帮助的信息的截图。感谢各机油帮助，以及相关教程和工具的提供者，恕不表名

如果发现文中有遗留的细节，我会在评论区补充

![](http://image.coolapk.com/feed/2024/0224/19/506153_ce93fc6e_2486_0243_784@1668x2388.jpg.m.jpg)

![](http://image.coolapk.com/feed/2024/0224/19/506153_c56db513_2486_025_190@1668x2388.jpg.m.jpg)

![](http://image.coolapk.com/feed/2024/0224/19/506153_cf8019c6_2486_0258_953@1668x2388.jpg.m.jpg)

![](http://image.coolapk.com/feed/2024/0224/19/506153_25da7488_2486_0263_663@1668x2388.jpg.m.jpg)

[ ![](http://image.coolapk.com/product_logo/2023/0104/16/0_0199_2739_939@320x320.png.t.jpg) 一加11 ](/product/2980)

  - 更多功能，丰富内容，尽在酷安 APP
