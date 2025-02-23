---
title: 我们找到了Windows电脑续航差的原因-苹果M2深度分析
cover: https://i.ytimg.com/vi/Z0tNtMwYrGA/maxresdefault.jpg
author: 极客湾Geekerwan
created: 2025-01-15T09:32:40

modified: 2025-01-15T09:34:07
published: 2022-07-29T23:21:41
description: 为了真正了解M2芯片的新款MacBook的续航表现，我们建立了一套属于我们自己的续航测试标准，在测试过程中我们发现了Mac和Windows笔记本续航的真正差距，于是我们试着找了找原因......除了续航，我们也做了深入的性能分析，我们引入了SPEC CPU 2017的测试，来看看M系列处理器和x86处理器架构上的差距到底有多少
source: https://www.youtube.com/watch?v=Z0tNtMwYrGA
tags:
  - youtube
tags-link: 
type: video
---

## Source

<iframe src="https://www.youtube.com/embed/Z0tNtMwYrGA" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
<center>via: <a href='https://www.youtube.com/watch?v=Z0tNtMwYrGA' target='_blank' class='external-link'>https://www.youtube.com/watch?v=Z0tNtMwYrGA</a></center>

## Notes 10:00 start

### Software

- Macos => https://github.com/tlkh/asitop
- Windows => HWiNFO, https://www.hwinfo.com/

### Intel
- `BIOS/Platform Configuration (RBSU)` > `Power and Performance Options` > `Intel(R) Turbo Boost Technology`
- via: [Enabling or disabling Intel Turbo Boost Technology (hpe.com)](https://techlibrary.hpe.com/docs/iss/proliant-gen10-uefi/s_enable_intel_boost_tech.html)

### AMD
- PBO / Precision Boost Overdrive
- "Auto" is actually *Disabled*
- via: [How Exactly Do YOu Disable PBO? : AMDHelp (reddit.com)](https://www.reddit.com/r/AMDHelp/comments/es0d4a/how_exactly_do_you_disable_pbo/)
