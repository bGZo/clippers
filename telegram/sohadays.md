
## 2023-09-19 14:17:10

![](assets/sohadays/20250320_123500_617280.jpg) 

WSL 2 终于也有更舒适的网络体验了！就像 WSL 1 一样，新增的 mirrored 网络模式可以直接使用 Windows 的 IP 连入连出，也可以直接使用 127.0.0.1 或 ::1 访问 Windows 的服务。
目前只在 Insider 任意 channel 有效，只需要在 Windows 用户目录下 .wslconfig 的 [experimental] 部分下加入 networkingMode=mirrored 即可。
更多更新内容：https://devblogs.microsoft.com/commandline/windows-subsystem-for-linux-september-2023-update/
https://t.me/sohadays/4889
