---
title: "ios 开发这么离谱的吗 - V2EX"
created: 2025-05-04T19:53:42
modified: 2025-05-04T19:54:14
source: "https://www.v2ex.com/t/1129398#reply84"
tags:
tags-link:
type: "archive-web"
---

## Origin Content

我的 mac book 版本是 14.7.4 (23H420) Sonoma

我安装了 xcode 16.2 ， 想开发 ios 16.0 的版本（因为我的 iphone 是这个版本

但是 xcode16.2 内置的 ios sdk 是 18.2

于是我又下载了一个 xcode 14.0.1 （内置 ios sdk 16.0 ）， 但是 Sonoma 不支持这个版本的 xocde

我又把 xcode 14.0.1 内置 的 ios sdk 16.0 复制到 xcode 16.2 中， 还是不能使用 16.0 的 ios sdk

```bash
❯ xcrun --sdk ios --show-sdk-version
2025-05-02 14:42:44.267 xcodebuild[40697:13592334] [MT] DVTSDK: Skipped SDK /Applications/Xcode16.2.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS16.0.sdk; its version (16.0) is below required minimum (18.2) for the iphoneos platform.
2025-05-02 14:42:44.430 xcodebuild[40697:13592334] Writing error result bundle to /var/folders/pr/vrpq9jvn4jgff8c5jmlm12mm0000gp/T/ResultBundle_2025-02-05_14-42-0044.xcresult
xcodebuild: error: SDK "ios" cannot be located.
2025-05-02 14:42:45.664 xcodebuild[40699:13592356] [MT] DVTSDK: Skipped SDK /Applications/Xcode16.2.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS16.0.sdk; its version (16.0) is below required minimum (18.2) for the iphoneos platform.
2025-05-02 14:42:45.837 xcodebuild[40699:13592356] Writing error result bundle to /var/folders/pr/vrpq9jvn4jgff8c5jmlm12mm0000gp/T/ResultBundle_2025-02-05_14-42-0045.xcresult
xcodebuild: error: SDK "ios" cannot be located.
xcrun: error: Failed to open property list '/Users/hbb/source/repos/rn/AwesomeProject/ios/SDKSettings.plist'
2025-05-02 14:42:47.075 xcodebuild[40700:13592367] [MT] DVTSDK: Skipped SDK /Applications/Xcode16.2.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS16.0.sdk; its version (16.0) is below required minimum (18.2) for the iphoneos platform.
2025-05-02 14:42:47.241 xcodebuild[40700:13592367] Writing error result bundle to /var/folders/pr/vrpq9jvn4jgff8c5jmlm12mm0000gp/T/ResultBundle_2025-02-05_14-42-0047.xcresult
xcodebuild: error: SDK "ios" cannot be located.
xcrun: error: unable to lookup item 'SDKVersion' in SDK 'ios'

```

各位佬都怎么设备 开发环境的，如果要支持旧环境的话， 不然要装旧的操作系统吧

## Comment

1.这就是为什么苹果可以做到让旧版本系统迅速退场，Xcode 是与 macOS 系统版本绑定的 虽然有办法高版本系统跨大版本运行旧的 Xcode ，但是会造成一些奇怪的问题
2.现在安装特定版本模拟器的方法是去官网下载对应的 simulator 版本然后跑指令安装进去就完事了
3.iOS simulator runtime 里面其实分为 sdk 和 simulator ，两个用处并不一样，sdk 用来编译的，你不装新的只装旧的的操作闻所未闻
4.Xcode 有做过一些调整，你现在的操作只有旧版本 Xcode 能这么干
5.手机是 16.0 的那还装啥模拟器，一般这么复杂的整模拟器就是因为老版本系统手机手里没有，但是线上又出了问题需要排查
6.实际上你折腾半天也依然是用的 iOS18 的 sdk 去编译的 编译 sdk 与 Xcode 有关系 这也是为啥你必须要有个对应的新版本系统的 simulator runtime 才能编译
7.你不求甚解就开始说什么 iOS 开发傲慢，正是因为你不懂，所以你在做一个“很新的”事情，一般 iOS 开发根本不需要你这种神秘操作，因此别人才说你的操作离谱
8.接 7 其实你的需求我完全没看懂？手机是 iOS16 的？所以呢？你把 target version 改掉的时候其实就已经自动标记了 iOS17/18 的 API ，你用到的时候会提示的。同 6 ，不同 sdk 编出来的包其实表现是有差异的，反而你不做骚操作的话大部分情况下不同 iOS 系统的 API 表现是一致的，而且苹果对于 App Store 的 sdk 有限制需要用最新的，所以正常开发不会有用旧版 sdk 的事情
