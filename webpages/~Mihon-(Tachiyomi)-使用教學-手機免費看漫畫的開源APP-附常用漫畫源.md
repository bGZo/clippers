---
title: ~Mihon-(Tachiyomi)-使用教學-手機免費看漫畫的開源APP-附常用漫畫源
aliases: []
created: 2025-04-13T23:34:30
modified: 2025-04-25T20:19:47
source: https://freehands.cc/posts/mihon-manga-reader/
tags: 
tags-link: 
type: archive-web
---

這是一款讓你自由看線上漫畫的好用 APP「Mihon」，完全免費，無廣告。![](https://freehands.cc/posts/mihon-manga-reader/images/title.webp)

Mihon 特色如下：

- 閱讀各大網站的漫畫，例如嗶咔漫畫、拷貝漫畫、動漫之家、漫畫人、E-hentai、Pixiv、Danbooru、Webtoon、騰訊漫畫、Toomics、Bilibili 漫畫…等等數不清的網站。
- 支援下載漫畫離線閱讀
- 跨平台，有 Android、iOS、Linux、Windows、macOS、網頁版等各種版本
- 開放原始碼，自由軟體。只要從官方來源下載就不會有任何病毒。
- 有非常多的分支版 APP，針對不同網站優化。
- 可搭配 MyAnimeList、Bangumi 等網站紀錄漫畫閱讀歷程。

本文解說 Mihon 的設計理念，以及安裝方法、加入漫畫擴充套件的作法。

## 1\. Mihon 怎麼用

首先簡述一下 Mihon 的設計理念，這是一款高度模組化的 APP。

使用者要先下載「Mihon 主程式」。主程式開啟預設是什麼都沒有的，只能讀本機漫畫圖檔，類似 Perfect Viewer 那樣。

要看線上漫畫的話，你要加入「擴充套件儲存庫」，再安裝「漫畫擴充套件」，才可以瀏覽各大漫畫網站的資源。這裡面的漫畫網站有的是正版。

漫畫你可以線上閱讀，也可以下載到本機離線閱讀。

Mihon 提供了一個整合性的界面，方便你存取各大漫畫網站的資源。

另外，Mihon 主程式不只官方原版一種，有很多種分支版。如果你覺得原版功能不敷需求，再去試試那些分支版吧！

## 2\. 下載 Mihon 主程式

注意：Mihon 並未在 Google Play 和 App Store 上架，請到 Github 下載。

### 2.1. 官方版 Mihon

目前官方版 Mihon 僅支援 Android 系統。如果你要在其他系統使用，請看下面「分支版 Mihon」一節。

Mihon 以前叫做 Tachiyomi，最早是 Inorichi 在 2014 年發起的專案，APP 名字來自日文，意思是「在書店站著看免費漫畫」![](https://freehands.cc/posts/mihon-manga-reader/images/tachiyomi.png)

然而 2024 年，開發者 [收到韓國Kakao公司的版權警告](https://tachiyomi.org/news/2024-01-13-goodbye)，說要起訴所有參與該專案的人士，導致他們不再積極維護程式，也把漫畫擴充套件的儲存庫給刪了。

所幸開源社群馬上有人接手，「Mihon」是 Tachiyomi 開發者另外發起的專案，功能一模一樣，只是名字改了而已，可說是 Tachiyomi 的正統繼承者。同時，漫畫擴充套件的儲存庫也換其他開發者維護了。

Mihon 這個 APP 名字同樣很有趣，日文意思是「漫畫試閱本」。![](https://freehands.cc/posts/mihon-manga-reader/images/mihon.png)

你可以在 [Github](https://github.com/mihonapp/mihon/releases) 取得最新 Android 版的 Mihon APK。需要 Android 7 以上系統才能安裝。![](https://freehands.cc/posts/mihon-manga-reader/images/Screenshot_20240225_222527.webp)

### 2.2. 分支版 Mihon

分支版 (fork) 是 Mihon 社群的一大特色，許多開發者嫌原版 Mihon 功能太少，便推出了自己的修改版。

雖然分支版功能各異，但有些漫畫擴充套件是通用的，你可以安裝幾個比較後再決定要用哪個當主客戶端。

現在比較活躍的分支版 Mihon 有以下幾個，點選連結下載：

| 名稱 | 支援系統 | 說明 |
| --- | --- | --- |
| [Aniyomi](https://freehands.cc/posts/android-aniyomi/) | Android | 除了漫畫以外，還整合了免費線上動畫來源。 |
| [Dantotsu](https://freehands.cc/posts/android-aniyomi/) | Android | 強化版 Aniyomi，重新設計過的追番界面，相容 Aniyomi 擴充套件。 |
| [Tachidesk Sorayomi](https://freehands.cc/posts/suwayomi-tachidesk/) | Android，iOS，Linux，Windows，macOS，網頁 | 跨平台的客戶端，遠端閱讀漫畫，必須搭配 Suwayomi 伺服器使用。 |
| [Mangayomi](https://github.com/kodjodevf/mangayomi) | Android，iOS，Linux，Windows，macOS | Flutter 改寫的跨平台 Mihon 複製品，可閱讀漫畫和播放動漫。不過 Mangayomi 有自己的套件庫，並不完全相容 Mihon 的擴充套件。 |
| [TachiyomiSY](https://github.com/jobobby04/TachiyomiSY) | Android | 針對 E-hentai 網站特化的版本，基於 Tachiyomi AZ 開發。 |
| [TachiyomiJ2K](https://github.com/Jays2Kings/tachiyomiJ2K) | Android | 針對平板電腦最佳化的分支版，支援雙頁模式閱讀、MyAnimeList 追蹤閱讀清單。 |
| [Tachimanga](https://apps.apple.com/us/app/tachimanga/id6447486175) | iOS | App Store 上的非官方 iOS 版 Mihon，支援安裝擴充套件。似乎沒有開放原始碼，且內含廣告。 |
| [LNreader](https://github.com/LNReader/lnreader) | Android | 針對輕小說特化的版本。 |

## 3\. 安裝漫畫擴充套件來源

1. 初次開啟 APP，Mihon 會要求你設定檔案儲存位置，我個人是把檔案放在 `Pictures/Mihon` 資料夾（若該資料夾不存在請自行新增）

![](https://freehands.cc/posts/mihon-manga-reader/images/Screenshot_20240225-145828.webp)

1. 在 Tachiyomi 開發者收到版權警告後，原本的漫畫擴充套件儲存庫由 [keiyoushi](https://github.com/keiyoushi/extensions-source) 接手維護。
2. 點選 APP 的探索 → 擴充套件，點選右上角擴充套件儲存庫

![](https://freehands.cc/posts/mihon-manga-reader/images/Screenshot_20240225-145854.webp)

1. 加入 [keiyoushi](https://github.com/keiyoushi/extensions) 的儲存庫網址：

```bash
https://raw.githubusercontent.com/keiyoushi/extensions/repo/index.min.json
```

如果擴充功能有問題，請到 [keiyoushi維護者的儲存庫](https://github.com/keiyoushi/extensions-source/issues) 回報。

1. 回到擴充套件頁面，下拉重新整理，就能下載漫畫網站的擴充套件了。點選右上角「篩選」開啟所有語言的網站。

![](https://freehands.cc/posts/mihon-manga-reader/images/Screenshot_20240225-222903.webp)

盜版中文漫畫來源：動漫之家 (DMZJ)、漫畫人、包子漫畫、無限動漫

正版中文漫畫來源：Webtoon、Toomics、騰訊動漫、愛奇藝叭嗒、Bilibili 漫畫

1. 為確保安全，Mihon 會要求你手動「信任」擴充套件才可以使用

![](https://freehands.cc/posts/mihon-manga-reader/images/Screenshot_20240225-145902.webp)

1. 重啟 APP 後，你就可以在「來源」頁面點選網站圖示，瀏覽該網站的漫畫了。注意有的網站會要求登入，此時請點選右上角設定操作。

![](https://freehands.cc/posts/mihon-manga-reader/images/0240225-212931.webp)

## 4\. 管理下載的漫畫

閱讀漫畫的時候你可以點選「加入收藏」將其加到私人書櫃。

![](https://freehands.cc/posts/mihon-manga-reader/images/Screenshot_20240225-224044.webp)

「歷程」是類似讀書紀錄的功能，請自行登入對應網站的帳號，授權 Mihon 存取你的帳號。

點選「下載漫畫」的話，漫畫圖檔就會下載到 Mihon 資料所在路徑下的 `downloads` 資料夾。

Mihon 預設會以.cbz 格式封裝下載的漫畫，如果你要圖片檔，請到 Mihon 設定 → 下載，取消打勾「以 CBZ 封存檔格式儲存」。

由於漫畫檔都是一張一張圖片明碼儲存的，沒有加密，你可以用其他漫畫 APP 閱讀 Mihon 所下載的漫畫。

## 5\. 備份與還原資料

點選 Mihon 設定 → 資料儲存空間，點選建立備份檔。

注意 Mihon 只能備份你的閱讀紀錄，無法備份下載的漫畫檔案。

不同分支版之間的備份檔格式可能也不相通，還原備份的時候需要特別注意。
