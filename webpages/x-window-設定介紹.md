---
created: 2024-01-06T00:00:00
source: https://linux.vbird.org/linux_basic/centos7/0590xwindow.php
type: archive-web
modified: 2025-03-31T21:57:28
---

在 Linux 上頭的圖形介面我們稱之為 X Window System，簡稱為 X 或 X11 囉！ 為何稱之為系統呢？這是因為 X 視窗系統又分為 X server 與 X client ，既然是 Server/Client (主從架構) 這就表示其實 X 視窗系統是可以跨網路且跨平台的！X 視窗系統對於 Linux 來說僅是一個軟體， 只是這個軟體日趨重要喔！因為 Linux 是否能夠在桌上型電腦上面流行，與這個 X 視窗系統有關啦！ 好在，目前的 X 視窗系統整合到 Linux 已經非常優秀了，而且也能夠具有 3D 加速的功能， 只是，我們還是得要瞭解一下 X 視窗系統才好，這樣如果出問題，我們才有辦法處理啊！

### 23.1 什麼是 X Window System

  Unix Like 作業系統不是只能進行伺服器的架設而已，在美編、排版、製圖、多媒體應用上也是有其需要的。 這些需求都需要用到圖形介面 (Graphical User Interface, GUI) 的操作的， 所以後來才有所謂的 X Window System 這玩意兒。那麼為啥圖形視窗介面要稱為 X 呢？因為就英文字母來看 X 是在 W(indow) 後面，因此，人們就戲稱這一版的視窗介面為 X 囉 (有下一版的新視窗之意)！

  事實上， X Window System 是個非常大的架構，他還用到網路功能呢！也就是說，其實 X 視窗系統是能夠跨網路與跨作業系統平台的！ 而鳥哥這個基礎篇是還沒有談到伺服器與網路主從式架構，因此 X 在這裡並不容易理解的。不過，沒關係！ 我們還是談談 X 怎麼來的，然後再來談談這 X 視窗系統的元件有哪些，慢慢來，應該還是能夠理解 X 的啦！

### 23.1.1 X Window 的發展簡史

  X Window 系統最早是由 MIT (Massachusetts Institute of Technology, 麻省理工學院) 在 1984 年發展出來的， 當初 X 就是在 Unix 的 System V 這個作業系統版本上面開發出來的。在開發 X 時，開發者就希望這個視窗介面不要與硬體有強烈的相關性，這是因為如果與硬體的相關性高，那就等於是一個作業系統了， 如此一來的應用性會比較侷限。因此 X 在當初就是以應用程式的概念來開發的，而非以作業系統來開發。

  由於這個 X 希望能夠透過網路進行圖形介面的存取，因此發展出許多的 X 通訊協定，這些網路架構非常的有趣， 所以吸引了很多廠商加入研發，因此 X 的功能一直持續在加強！一直到 1987 年更改 X 版本到 X11 ，這一版 X 取得了明顯的進步， 後來的視窗介面改良都是架構於此一版本，因此後來 X 視窗也被稱為 X11 。這個版本持續在進步當中，到了 1994 年發佈了新版的 X11R6 ，後來的架構都是沿用此一釋出版本，所以後來的版本定義就變成了類似 1995 年的 X11R6.3 之類的樣式。 ([註1](https://linux.vbird.org/linux_basic/centos7/0590xwindow.php#ps1))

  1992 年 XFree86 ([http://www.xfree86.org/](http://www.xfree86.org/)) 計畫順利展開， 該計畫持續在維護 X11R6 的功能性，包括對新硬體的支援以及更多新增的功能等等。當初定名為 XFree86 其實是根據『 X + Free software + x86 硬體 』而來的呢。早期 Linux 所使用的 X Window 的主要核心都是由 XFree86 這個計畫所提供的，因此，我們常常將 X 系統與 XFree86 掛上等號的說。

  不過由於一些授權的問題導致 XFree86 無法繼續提供類似 GPL 的自由軟體，後來 Xorg 基金會就接手 X11R6 的維護！ Xorg ([http://www.x.org/](http://www.x.org/)) 利用當初 MIT 發佈的類似自由軟體的授權， 將 X11R6 拿來進行維護，並且在 2004 年發佈了 X11R6.8 版本，更在 2005 年後發表了 X11R7.x 版。 現在我們 CentOS 7.x 使用的 X 就是 Xorg 提供的 X11R7.X 喔！ 而這個 X11R6/X11R7 的版本是自由軟體，因此很多組織都利用這個架構去設計他們的圖形介面喔！包括 Mac OS X v10.3 也曾利用過這個架構來設計他們的視窗呢！我們的 CentOS 也是利用 Xorg 提供的 X11 啦！

  從上面的說明，我們可以知道的是：

在 Unix Like 上面的圖形使用者介面 (GUI) 被稱為 X 或 X11；

X11 是一個『軟體』而不是一個作業系統；

X11 是利用網路架構來進行圖形介面的執行與繪製；

較著名的 X 版本為 X11R6 這一版，目前大部分的 X 都是這一版演化出來的 (包括 X11R7)；

現在大部分的 distribution 使用的 X 都是由 Xorg 基金會所提供的 X11 軟體；

X11 使用的是 MIT 授權，為類似 GPL 的開放原始碼授權方式。

### 23.1.2 主要元件： X Server/X Client/Window Manager/Display Manager

  如同前面談到的，X Window system 是個利用網路架構的圖形使用者介面軟體，那到底這個架構可以分成多少個元件呢？ 基本上是分成 X Server 與 X Client 兩個元件而已喔！其中 X Server 在管理硬體，而 X Client 則是應用程式。 在運作上，X Client 應用程式會將所想要呈現的畫面告知 X Server ，最終由 X server 來將結果透過他所管理的硬體繪製出來！ 整體的架構我們大約可以使用如下的圖示來作個介紹：([註2](https://linux.vbird.org/linux_basic/centos7/0590xwindow.php#ps2))

  ![X Window System 的架構](assets/2024/x_ser_cli.gif "X Window System 的架構")

  圖 23.1.1、X Window System 的架構

  上面的圖示非常有趣喔！我們在用戶端想要取得來自伺服器的圖形資料時，我們用戶端使用的當然是用戶端的硬體設備啊， 所以，X Server 的重點就是在管理用戶端的硬體，包括接受鍵盤/滑鼠等設備的輸入資訊， 並且將圖形繪製到螢幕上 (請注意上圖的所有元件之間的箭頭指示)。但是到底要繪製個啥東西呢？ 繪圖總是需要一些數據才能繪製吧？此時 X Client (就是 X 應用程式) 就很重要啦！他主要提供的就是告知 X Server 要繪製啥東西。那照這樣的想法來思考，我們是想要取得遠端伺服器的繪圖數據來我們的電腦上面顯示嘛！ 所以囉，遠端伺服器提供的是 X client 軟體啊！

  底下就讓我們來更深入的聊一聊這兩個元件吧！

X Server：硬體管理、螢幕繪製與提供字型功能：

  既然 X Window System 是要顯示圖形介面，因此理所當然的需要一個元件來管理我主機上面的所有硬體設備才行！ 這個任務就是 X Server 所負責的。而我們在 X 發展簡史當中提到的 XFree86 計畫及 Xorg 基金會，主要提供的就是這個 X Server 啦！那麼 X Server 管理的設備主要有哪些呢？其實與輸入/輸出有關喔！包括鍵盤、滑鼠、手寫板、顯示器 (monitor) 、螢幕解析度與色彩深度、顯示卡 (包含驅動程式) 與顯示的字型等等，都是 X Server 管理的。

  咦！顯示卡、螢幕以及鍵盤滑鼠的設定，不是在開機的時候 Linux 系統以 systemd 的相關設定處理好了嗎？ 為何 X Server 還要重新設定啊？這是因為 X Window 在 Linux 裡面僅能算是『一套很棒的軟體』， 所以 X Window 有自己的設定檔，你必須要針對他的設定檔設定妥當才行。也就是說， Linux 的設定與 X Server 的設定不一定要相同的！因此，你在 CentOS 7 的 multi-user.target 想要玩圖形介面時，就得要載入 X Window 需要的驅動程式才行～總之， X Server 的主要功能就是在管理『主機』上面的顯示硬體與驅動程式。

  既然 X Window System 是以透過網路取得圖形介面的一個架構，那麼用戶端是如何取得伺服器端提供的圖形畫面呢？ 由於伺服器與用戶端的硬體不可能完全相同，因此我們用戶端當然不可能使用到伺服器端的硬體顯示功能！ 舉例來說，你的用戶端電腦並沒有 3D 影像加速功能，那麼你的畫面可能呈現出伺服器端提供的 3D 加速嗎？ 當然不可能吧！所以囉 X Server 的目的在管理用戶端的硬體設備！也就是說：『每部用戶端主機都需要安裝 X Server，而伺服器端則是提供 X Client 軟體， 以提供用戶端繪圖所需要的數據資料』。

  X Server / X Client 的互動並非僅有 client --> server，兩者其實有互動的！從上圖 23.1.1 我們也可以發現， X Server 還有一個重要的工作，那就是將來自輸入裝置 (如鍵盤、滑鼠等) 的動作告知 X Client， 你曉得， X Server 既然是管理這些周邊硬體，所以，周邊硬體的動作當然是由 X Server 來管理的， 但是 X Server 本身並不知道周邊設備這些動作會造成什麼顯示上的效果， 因此 X Server 會將周邊設備的這些動作行為告知 X Client ，讓 X Client 去傷腦筋。

X Client：負責 X Server 要求的『事件』之處理：

  前面提到的 X Server 主要是管理顯示介面與在螢幕上繪圖，同時將輸入裝置的行為告知 X Client， 此時 X Client 就會依據這個輸入裝置的行為來開始處理，最後 X Client 會得到『 嗯！這個輸入裝置的行為會產生某個圖示』，然後將這個圖示的顯示資料回傳給 X Server ， X server 再根據 X Client 傳來的繪圖資料將他描圖在自己的螢幕上，來得到顯示的結果。

  也就是說， X Client 最重要的工作就是處理來自 X Server 的動作，將該動作處理成為繪圖資料， 再將這些繪圖資料傳回給 X Server 囉！由於 X Client 的目的在產生繪圖的數據，因此我們也稱呼 X Client 為 X Application (X 應用程式)。而且，每個 X Client 並不知道其他 X Client 的存在， 意思是說，如果有兩個以上的 X client 同時存在時，兩者並不知道對方到底傳了什麼數據給 X Server ， 因此 X Client 的繪圖常常會互相重疊而產生困擾喔！

  舉個例子來說，當我們在 X Window 的畫面中，將滑鼠向右移動，那他是怎麼告知 X Server 與 X Client 的呢？ 首先， X server 會偵測到滑鼠的移動，但是他不知道應該怎麼繪圖啊！此時，他將滑鼠的這個動作告知 X Client， X Client 就會去運算，結果得到，嘿嘿！其實要將滑鼠指標向右移動幾個像素，然後將這個結果告知 X server ， 接下來，您就會看到 X Server 將滑鼠指標向右移動囉～

  這樣做有什麼好處啊？最大的好處是， X Client 不需要知道 X Server 的硬體配備與作業系統！因為 X Client 單純就是在處理繪圖的資料而已，本身是不繪圖的。所以，在用戶端的 X Server 用的是什麼硬體？用的是哪套作業系統？伺服器端的 X Client 根本不需要知道～相當的先進與優秀～對吧！ ^\_^ 整個運作流程可以參考下圖：用戶端用的是什麼作業系統在 Linux 主機端是不在乎的！

  ![X Server 用戶端的作業系統與 X client 的溝通示意](assets/2024/x_client_os.gif "X Server 用戶端的作業系統與 X client 的溝通示意")

  圖 23.1.2、X Server 用戶端的作業系統與 X client 的溝通示意

X Window Manager：特殊的 X Client ，負責管理所有的 X client 軟體

  剛剛前面提到，X Client 的主要工作是將來自 X Server 的資料處理成為繪圖數據，再回傳給 X server 而已， 所以 X client 本身是不知道他在 X Server 當中的位置、大小以及其他相關資訊的。這也是上面我們談到的， X client 彼此不知道對方在螢幕的哪個位置啊！為了克服這個問題，因此就有 Window Manager (WM, 視窗管理員) 的產生了。 視窗管理員也是 X client ，只是他主要在負責全部 X client 的控管，還包括提供某些特殊的功能，例如：

提供許多的控制元素，包括工作列、背景桌面的設定等等；

管理虛擬桌面 (virtual desktop)；

提供視窗控制參數，這包括視窗的大小、視窗的重疊顯示、視窗的移動、視窗的最小化等等。

  我們常常聽到的 KDE, GNOME, XFCE 還有陽春到爆的 twm 等等，都是一些視窗管理員的專案計畫啦！ 這些專案計畫中，每種視窗管理員所用以開發的顯示引擎都不太相同，所著重的方向也不一樣， 因此我們才會說，在 Linux 底下，每套 Window Manager 都是獨特存在的，不是換了桌面與顯示效果而已， 而是連顯示的引擎都不會一樣喔！底下是這些常見的視窗管理員全名與連結：

GNOME (GNU Network Object Model Environment)：[http://www.gnome.org/](http://www.gnome.org/)

KDE (K Desktop Enviroment)：[http://kde.org/](http://kde.org/)

twm (Tab Window Manager)：[http://xwinman.org/vtwm.php](http://xwinman.org/vtwm.php)

XFCE (XForms Common Environment)：[http://www.xfce.org/](http://www.xfce.org/)

  由於 Linux 越來越朝向 Desktop 桌上型電腦使用方向走，因此視窗管理員的角色會越來越重要！ 目前我們 CentOS 預設提供的有 GNOME 與 KDE ，這兩個視窗管理員上面還有提供非常多的 X client 軟體， 包括辦公室生產力軟體 (Open Office) 以及常用的網路功能 (firefox 瀏覽器、 Thunderbird 收發信件軟體) 等。 現在使用者想要接觸 Linux 其實真的越來越簡單了，如果不要架設伺服器，那麼 Linux 桌面的使用與 Windows 系統可以說是一模一樣的！不需要學習也能夠入門哩！ ^\_^

  那麼你知道 X Server / X client / window manager 的關係了嗎？我們舉 CentOS 預設的 GNOME 為例好了， 由於我們要在本機端啟動 X Window system ，因此，在我們的 CentOS 主機上面必須要有 Xorg 的 X server 核心， 這樣才能夠提供螢幕的繪製啊～然後為了讓視窗管理更方便，於是就加裝了 GNOME 這個計畫的 window manager ， 然後為了讓自己的使用更方便，於是就在 GNOME 上面加上更多的視窗應用軟體，包括輸入法等等的， 最後就建構出我們的 X Window System 囉～ ^\_^！所以你也會知道，X server/X client/Window Manager 是同時存在於我們一部 Linux 主機上頭的啦！

Display Manager：提供登入需求

  談完了上述的資料後，我們得要瞭解一下，那麼我如何取得 X Window 的控制？在本機的文字介面底下你可以輸入 startx 來啟動 X 系統，此時由於你已經登入系統了，因此不需要重新登入即可取得 X 環境。但如果是 graphical.target 的環境呢？你會發現在 tty1 或其他 tty 的地方有個可以讓你使用圖形介面登入 (輸入帳號密碼) 的咚咚，那個是啥？ 是 X Server/X client 還是什麼的？其實那是個 Display Manager 啦！這個 display manager 最大的任務就是提供登入的環境， 並且載入使用者選擇的 Window Manager 與語系等資料喔！

  幾乎所有的大型視窗管理員專案計畫都會提供 display manager 的，在 CentOS 上面我們主要利用的是 GNOME 的 GNOME Display Manager (gdm) 這支程式來提供 tty1 的圖形介面登入喔！至於登入後取得的視窗管理員， 則可以在 gdm 上面進行選擇的！我們在 [第四章](https://linux.vbird.org/linux_basic/0160startlinux.php#start_startx) 介紹的登入環境， 那個環境其實就是 gdm 提供的啦！再回去參考看看圖示吧！ ^\_^！所以說，並非 gdm 只能提供 GNOME 的登入而已喔！

### 23.1.3 X Window 的啟動流程

  現在我們知道要啟動 X Window System 時，必須要先啟動管理硬體與繪圖的 X Server ，然後才載入 X Client 。 基本上，目前都是使用 Window Manager 來管理視窗介面風格的。那麼如何取得這樣的視窗系統呢？ 你可以透過登入本機的文字介面後，輸入 startx 來啟動 X 視窗；也能夠透過 display manager (如果有啟動 graphical.target) 提供的登入畫面，輸入你的帳號密碼來登入與取得 X 視窗的！

  問題是，你的 X server 設定檔為何？如何修改解析度與顯示器？你能不能自己設定預設啟動的視窗管理員？ 如何設定預設的使用者環境 (與 X client 有關) 等等的，這些資料都需要透過瞭解 X 的啟動流程才能得知！ 所以，底下我們就來談談如何啟動 X 的流程吧！ ^\_^

在文字介面啟動 X ：透過 startx 指令

  我們都知道 Linux 是個多人多工的作業系統，所以啦，X 視窗也是可以根據不同的使用者而有不同的設定！ 這也就是說，每個用戶啟動 X 時， X server 的解析度、啟動 X client 的相關軟體及 Window Manager 的選擇可能都不一樣！ 但是，如果你是首次登入 X 呢？也就是說，你自己還沒有建立自己的專屬 X 畫面時，系統又是從哪裡給你這個 X 預設畫面呢？而如果你已經設定好相關的資訊，這些資訊又是存放於何處呢？

  事實上，當你在純文字介面且並沒有啟動 X 視窗的情況下來輸入 startx 時，這個 startx 的作用就是在幫你設定好上頭提到的這些動作囉！ startx 其實是一個 shell script ，他是一個比較親和的程式，會主動的幫忙使用者建立起他們的 X 所需要引用的設定檔而已。你可以自行研究一下 startx 這個 script 的內容，鳥哥在這裡僅就 startx 的作用作個介紹。

  startx 最重要的任務就是找出使用者或者是系統預設的 X server 與 X client 的設定檔，而使用者也能夠使用 startx 外接參數來取代設定檔的內容。這個意思是說：startx 可以直接啟動，也能夠外接參數，例如底下格式的啟動方式：

  ```
  [root@study ~]# <span>startx [X client 參數] -- [X server 參數]</span>
  <span># 範例：以色彩深度為 16 bit 啟動 X</span>
  [root@study ~]# <span>startx  --  -depth 16</span>
  ```

  startx 後面接的參數以兩個減號『--』隔開，前面的是 X Client 的設定，後面的是 X Server 的設定。 上面的範例是讓 X server 以色彩深度 16 bit 色 (亦即每一像素佔用 16 bit ，也就是 65536 色) 顯示， 因為色彩深度是與 X Server 有關的，所以參數當然是寫在 -- 後面囉，於是就成了上面的模樣！

  你會發現，鳥哥上面談到的 startx 都是提到如何找出 X server / X client 的設定值而已！ 沒錯，事實上啟動 X 的是 xinit 這支程式， startx 僅是在幫忙找出設定值而已！那麼 startx 找到的設定值可用順序為何呢？基本上是這樣的：

X server 的參數方面：

    1. 使用 startx 後面接的參數；

    2. 若無參數，則找尋使用者家目錄的檔案，亦即 ~/.xserverrc

    3. 若無上述兩者，則以 /etc/X11/xinit/xserverrc

    4. 若無上述三者，則單純執行 /usr/bin/X (此即 X server 執行檔)

X client 的參數方面：

    1. 使用 startx 後面接的參數；

    2. 若無參數，則找尋使用者家目錄的檔案，亦即 ~/.xinitrc

    3. 若無上述兩者，則以 /etc/X11/xinit/xinitrc

    4. 若無上述三者，則單純執行 xterm (此為 X 底下的終端機軟體)

  根據上述的流程找到啟動 X 時所需要的 X server / X client 的參數，接下來 startx 會去呼叫 xinit 這支程式來啟動我們所需要的 X 視窗系統整體喔！接下來當然就是要談談 xinit 囉～

由 startx 呼叫執行的 xinit

  事實上，當 startx 找到需要的設定值後，就呼叫 xinit 實際啟動 X 的。他的語法是：

  ```
  [root@study ~]# <span>xinit [client option] -- [server or display option]</span>
  ```

  那個 client option 與 server option 如何下達呢？其實那兩個咚咚就是由剛剛 startx 去找出來的啦！ 在我們透過 startx 找到適當的 xinitrc 與 xserverrc 後，就交給 xinit 來執行。 在預設的情況下 (使用者尚未有 ~/.xinitrc 等檔案時)，你輸入 startx ， 就等於進行 xinit /etc/X11/xinit/xinitrc -- /etc/X11/xinit/xserverrc 這個指令一般！但由於 xserverrc 也不存在，參考上一小節的參數搜尋順序， 因此實際上的指令是：xinit /etc/X11/xinit/xinitrc -- /usr/bin/X，這樣瞭了嗎？

  那為什麼不要直接執行 xinit 而是使用 startx 來呼叫 xinit 呢？這是因為我們必須要取得一些參數嘛！ startx 可以幫我們快速的找到這些參數而不必手動輸入的。因為單純只是執行 xinit 的時候，系統的預設 X Client 與 X Server 的內容是這樣的：([註3](https://linux.vbird.org/linux_basic/centos7/0590xwindow.php#ps3))

  ```
  <span>xinit xterm  -geometry  +1+1  -n  login  -display  :0 --  X  :0</span>
  ```

  在 X client 方面：那個 xterm 是 X 視窗底下的虛擬終端機，後面接的參數則是這個終端機的位置與登入與否。 最後面會接一個『 -display :0 』表示這個虛擬終端機是啟動在『第 :0 號的 X 顯示介面』的意思。至於 X Server 方面， 而我們啟動的 X server 程式就是 X 啦！其實 X 就是 Xorg 的連結檔，亦即是 X Server 的主程式囉！ 所以我們啟動 X 還挺簡單的～直接執行 X 而已，同時還指定 X 啟動在第 :0 個 X 顯示介面。 如果單純以上面的內容來啟動你的 X 系統時，你就會發現 tty2 以後的終端機有畫面了！只是.....很醜～因為我們還沒有啟動 window manager 啊！

  從上面的說明我們可以知道， xinit 主要在啟動 X server 與載入 X client ，但這個 xinit 所需要的參數則是由 startx 去幫忙找尋的。因此，最重要的當然就是 startx 找到的那些參數啦！ 所以呢，重點當然就是 /etc/X11/xinit/ 目錄下的 xinitrc 與 xserverrc 這兩個檔案的內容是啥囉～ 雖然 xserverrc 預設是不存在的。底下我們就分別來談一談這兩個檔案的主要內容與啟動的方式～

啟動 X server 的檔案： xserverrc

  X 視窗最先需要啟動的就是 X server 啊，那 X server 啟動的腳本與參數是透過 /etc/X11/xinit/ 裡面的 xserverrc 。不過我們的 CentOS 7.x 根本就沒有 xserverrc 這個檔案啊！ 那使用者家目錄目前也沒有 ~/.xserverrc ，這個時候系統會怎麼做呢？其實就是執行 /usr/bin/X 這個指令啊！ 這個指令也是系統最原始的 X server 執行檔囉。

  在啟動 X Server 時，Xorg 會去讀取 /etc/X11/xorg.conf 這個設定檔。針對這個設定檔的內容， 我們會在下個小節介紹。如果一切順利，那麼 X 就會順利的在 tty2 以後終端環境中啟動了 X 。 單純的 X 啟動時，你只會看到畫面一片漆黑，然後中心有個滑鼠的游標而已～

  由前一小節的說明中，你可以發現到其實 X 啟動的時候還可以指定啟動的介面喔！那就是 :0 這個參數，這是啥？ 事實上我們的 Linux 可以『同時啟動多個 X』喔！第一個 X 的畫面會在 :0 亦即是 tty2 ，第二個 X 則是 :1 亦即是 tty3 。 後續還可以有其他的 X 存在的。因此，上一小節我們也有發現， xterm 在載入時，也必須要使用 -display 來說明， 這個 X 應用程式是需要在哪個 X 載入的才行呢！其中比較有趣的是， X server 未註明載入的介面時，預設是使用 :0 ～ 但是 X client 未註明時，則無法執行喔！

  Tips

  ![鳥哥](assets/2024/vbird_face.gif "鳥哥") CentOS 7 的 tty 非常有趣！如果你在 [分析 systemd 的章節中](https://linux.vbird.org/linux_basic/0560daemons.php#systemd_cfg_repeat) 有仔細看的話， 會發現到其實 tty 是有用到才會啟動的，這與之前 CentOS 6 以前的版本預設啟用 6 個 tty 給你是不同的。因此，如果你只有用到 tty1 的話， 那麼啟動 X 就會預設丟到 tty2 ，而 X :1 就會丟到 tty3 這樣～以此類推喔～

  啟動了 X server 後，接下來就是載入 X client 到這個 X server 上面啦！

啟動 X Client 的檔案： xinitrc

  假設你的家目錄並沒有 ~/.xinitrc ，則此時 X Client 會以 /etc/X11/xinit/xinitrc 來作為啟動 X Client 的預設腳本。xinitrc 這個檔案會將很多其他的檔案參數引進來， 包括 /etc/X11/xinit/xinitrc-common 與 /etc/X11/xinit/Xclients 還有 /etc/sysconfig/desktop 。你可以參考 xinitrc 後去搜尋各個檔案來瞭解彼此的關係。

  不過分析到最後，其實最終就是載入 KDE 或者是 GNOME 而已。你也可以發現最終在 XClient 檔案當中會有兩個指令的搜尋， 包括 startkde 與 gnome-session 這兩個，這也是 CentOS 預設會提供的兩個主要的 Window Manager 囉。 而你也可以透過修改 /etc/sysconfig/desktop 內的 DESKTOP=GNOME 或 DESKTOP=KDE 來決定預設使用哪個視窗管理員的。 如果你並沒有安裝這兩個大傢伙，那麼 X 就會去使用陽春的 twm 這個視窗管理員來管理你的環境囉。

  Tips

  ![鳥哥](assets/2024/vbird_face.gif "鳥哥") 不論怎麼說，鳥哥還是希望大家可以透過解析 startx 這個 script 的內容去找到每個檔案， 再根據分析每個檔案來找到您 distributions 上面的 X 相關檔案～ 畢竟每個版本的 Linux 還是有所差異的～

  另外，如果有特殊需求，你當然可以自訂 X client 的參數！這就得要修改你家目錄下的 ~/.xinitrc 這個檔案囉。 不過要注意的是，如果你的 .xinitrc 設定檔裡面有啟動的 x client 很多的時候，千萬注意將除了最後一個 window manager 或 X Client 之外，都放到背景裡面去執行啊！舉例來說，像底下這樣：

  ```
  <span>       xclock -geometry 100x100-5+5 &
       xterm -geometry 80x50-50+150 &
       exec /usr/bin/twm</span>
  ```

  意思就是說，我啟動了 X ，並且同時啟動 xclock / xterm / twm 這三個 X clients 喔！ 如此一來，你的 X 就有這三個咚咚可以使用了！如果忘記加上 & 的符號，那就..... 會讓系統等待啊，而無法一次就登入 X 呢！

X 啟動的埠口

  好了，根據上面的說明，我們知道要在文字介面底下啟動 X 時，直接使用 startx 來找到 X server 與 X client 的參數或設定檔， 然後再呼叫 xinit 來啟動 X 視窗系統。xinit 先載入 X server 到預設的 :0 這個顯示介面，然後再載入 X client 到這個 X 顯示介面上。而 X client 通常就是 GNOME 或 KDE ，這兩個設定也能夠在 /etc/sysconfig/desktop 裡面作好設定。最後我們想要瞭解的是，既然 X 是可以跨網路的，那 X 啟動的埠口是幾號？

  其實，CentOS 由於考慮 X 視窗是在本機上面運作，因此將埠口改為插槽檔 (socket) 了，因此你無法觀察到 X 啟動的埠口的。事實上， X server 應該是要啟動一個 port 6000 來與 X client 進行溝通的！ 由於系統上面也可能有多個 X 存在，因此我們就會有 port 6001, port 6002... 等等。這也就是說：(假設為 multi-user.target 模式， 且用戶僅曾經切換到 tty1 而已)

  <table><tbody><tr><td>X 視窗系統</td><td>顯示介面號碼</td><td>預設終端機</td><td>網路監聽埠口</td></tr><tr><td>第一個 X</td><td>hostname:0</td><td>tty2</td><td>port 6000</td></tr><tr><td>第二個 X</td><td>hostname:1</td><td>tty3</td><td>port 6001</td></tr></tbody></table>
  在 X Window System 的環境下，我們稱 port 6000 為第 0 個顯示介面，亦即為 hostname:0 ， 那個主機名稱通常可以不寫，所以就成了 :0 即可。在預設的情況下，第一個啟動的 X (不論是啟動在第幾個 port number) 是在 tty2 ，亦即按下 \[ctrl\]+\[Alt\]+\[F2\] 那個畫面。 而起動的第二個 X (注意到了吧！可以有多個 X 同時啟動在您的系統上呢) 則預設在 tty3 亦即 \[ctrl\]+\[Alt\]+\[F3\] 那個畫面呢！很神奇吧！ ^\_^
  如前所述，因為主機上的 X 可能有多個同時存在，因此，當我們在啟動 X Server / Client 時， 應該都要註明該 X Server / Client 主要是提供或接受來自哪個 display 的 port number 才行。

### 23.1.4 X 啟動流程測試

  好了，我們可以針對 X Server 與 X client 的架構來做個簡單的測試喔！ 這裡鳥哥假設你的 tty1 是 multi-user.target 的，而且你也曾經在 tty2 測試過相關的指令，所以你的 X :1 將會啟用在 tty3 喔！ 而且，底下的指令都是在 tty1 的地方執行的，至於底下的畫面則是在 tty3 的地方展現。 因此，請自行切換 tty1 下達指令與 tty3 查閱結果囉！

  ```
  <span>1. 先來啟動第一個 X 在 :1 畫面中：</span>
  [dmtsai@study ~]$ <span>X :1 &</span>
  ```

  ![單純啟動 X server的情況](assets/2024/xwin_test_1.gif "單純啟動 X server的情況")

  圖 23.1.3、單純啟動 X server 的情況

  上述的 X 是大寫，那個 :1 是寫在一起的，至於 & 則是放到背景去執行。此時系統會主動的跳到第二個圖形介面終端機，亦即 tty3 上喔！所以如果一切順利的話，你應該可以看到一個 X 的滑鼠游標可以讓你移動了 (如上圖所示)。 該畫面就是 X Server 啟動的畫面囉！醜醜的，而且沒有什麼 client 可以用啊！ 接下來，請按下 \[ctrl\]+\[alt\]+\[F1\] 回到剛剛下達指令的終端機： (若沒有 xterm 請自行 yum 安裝它！)

  ```
  <span>2. 輸入數個可以在 X 當中執行的虛擬終端機</span>
  [dmtsai@study ~]$ <span>xterm -display :1 &</span>
  [dmtsai@study ~]$ <span>xterm -display :1 &</span>
  ```

  ![在 X 上面啟動 xterm 終端機顯示的結果](assets/2024/centos7_xwin_test_2.jpg "在 X 上面啟動 xterm 終端機顯示的結果")

  圖 23.1.4、在 X 上面啟動 xterm 終端機顯示的結果

  那個 xterm 是必須要在 X 底下才能夠執行的終端機介面。加入的參數 -display 則是指出這個 xterm 要在那個 display 使用的。這兩個指令請不要一次下完！先執行一次，然後按下 \[ctrl\]+\[alt\]+\[F3\] 去到 X 畫面中，你會發現多了一個終端機囉～ 不過，可惜的是，你無法看到終端機的標題、也無法移動終端機，當然也無法調整終端機的大小啊！我們回到剛剛的 tty1 然後再次下達 xterm 指令，理論上應該多一個終端機，去到 tty3 查閱一下。唉～沒有多出一個終端機啊？ 這是因為兩個終端機重疊了～我們又無法移動終端機，所以只看到一個。 接下來，請再次回到 tty1 去下達指令吧！(可能需要 yum install xorg-x11-apps 喔！)

  ```
  <span>3. 在輸入不同的 X client 觀察觀察，分別去到 tty3 觀察喔！</span>
  [dmtsai@study ~]$ <span>xclock -display :1 &</span>
  [dmtsai@study ~]$ <span>xeyes -display :1 &</span>
  ```

  ![分別啟動 xclock 時鐘與 xeyes 眼睛的結果](assets/2024/centos7_xwin_test_3.jpg "分別啟動 xclock 時鐘與 xeyes 眼睛的結果")

  圖 23.1.5、分別啟動 xclock 時鐘與 xeyes 眼睛的結果

  跟前面一樣的，我們又多執行了兩個 X client ，其中 xclock 會顯示時鐘，而 xeyes 則是會出現一雙大眼睛來盯著游標！ 你可以移動一下游標就可以發現眼睛的焦聚會跑啊 ^\_^！不過，目前的四個 X client 通通不能夠移動與放大縮小！ 如此一來，你怎麼在 xterm 底下下達指令啊？當然就很困擾～所以讓我們來載入最陽春的視窗管理員吧！

  ```
  <span>4. 輸入可以管理的 window manager，我們這邊先以 root 來安裝 twm 喔！</span>
  [root@study ~]# <span>yum install http://ftp.ksu.edu.tw/FTP/CentOS/6/os/x86_64/\</span>
  > <span>Packages/xorg-x11-twm-1.0.3-5.1.el6.x86_64.rpm</span>
  <span># 真要命！CentOS 7 說 twm 已經沒有在維護，所以沒有提供這玩意兒了！鳥哥只好拿舊版的 twm 來安裝！
  # 請您自行到相關的網站上找尋這個 twm 囉！因為版本可能會不一樣！</span>
  [root@study ~]# <span>yum install xorg-x11-fonts-{100dpi,75dpi,Type1}</span>
  <span>5. 接下來就可以開始用 dmtsai 的身份來玩一下這玩意兒了！</span>
  [dmtsai@study ~]$ <span>twm -display :1 &</span>
  ```

  ![視窗管理員 twm 的功能顯示](assets/2024/centos7_xwin_test_4.jpg "視窗管理員 twm 的功能顯示")

  圖 23.1.6、視窗管理員 twm 的功能顯示

  回到 tty1 後，用最簡單的 twm 這個視窗管理員來管理我們的 X 吧！輸入之後，去到 tty3 看看，用滑鼠移動一下終端機看看？可以移動了吧？也可以縮小放大視窗囉～同時也出現了標題提示囉～也看到兩個終端機啦！ 現在終於知道視窗管理員的重要性了吧？ ^\_^！在黑螢幕地方按下滑鼠右鍵，就會出現類似上面畫面最右邊的選單， 你就可以進行額外的管理囉～玩玩看先！

  ```
  <span>6. 將所有剛剛建立的 X 相關工作全部殺掉！</span>
  [dmtsai@study ~]# <span>kill %6 %5 %4 %3 %2 %1</span>
  ```

  很有趣的一個小實驗吧～透過這個實驗，你應該會對 X server 與 Window manager 及 tty3 以後的終端介面使用方式有比較清楚的瞭解～加油！

### 23.1.5 我是否需要啟用 X Window System

  談了這麼多 X 視窗系統方面的資訊後，再來聊聊，那麼你的 Linux 主機是否需要預設就啟動 X 視窗呢？ 一般來說，如果你的 Linux 主機定位為網路伺服器的話，那麼由於 Linux 裡面的主要服務的設定檔都是純文字的格式檔案， 相當的容易設定的，所以啊，根本就是不需要 X Window 存在呢！因為 X Window 僅是 Linux 系統內的一個軟體而已啊！

  但是萬一你的 Linux 主機是用來作為你的桌上電腦用的，那麼 X Window 對你而言，就是相當重要的一個咚咚了！因為我們日常使用的辦公室軟體，都需要使用到 X Window 圖形的功能呢！此外，以鳥哥的例子來說，俺之前接觸到的數值分析模式，需要利用圖形處理軟體來將資料讀取出來， 所以在那部 Linux 主機上面，我一定需要 X Window 的。

  由於目前的主機系統配備已經很不錯，除非你使用的是單版電腦，否則桌上型電腦、筆記型電腦的系統配備要拿來跑 X window 大概都不是問題！ 所以，是否預設要啟用你的 X window 系統，完全掌握在你的伺服器用途考量上囉！！

### 23.2 X Server 設定檔解析與設定

  從前面的說明來看，我們知道一個 X 視窗系統能不能成功啟動，其實與 X Server 有很大的關係的。因為 X Server 負責的是整個畫面的描繪，所以沒有成功啟動 X Server 的話，即使有啟動 X Client 也無法將圖樣顯示出來啊。所以，底下我們就針對 X Server 的設定檔來做個簡單的說明，好讓大家可以成功的啟動 X Window System 啊。

  基本上， X Server 管理的是顯示卡、螢幕解析度、滑鼠按鍵對應等等，尤其是顯示卡晶片的認識，真是重要啊。 此外，還有顯示的字體也是 X Server 管理的一環。基本上，X server 的設定檔都是預設放置在 /etc/X11 目錄下，而相關的顯示模組或上面提到的總總模組，則主要放置在 /usr/lib64/xorg/modules 底下。比較重要的是字型檔與晶片組，她們主要放置在:

提供的螢幕字型: /usr/share/X11/fonts/

顯示卡的晶片組: /usr/lib64/xorg/modules/drivers/

  在 CentOS 底下，這些都要透過一個統一的設定檔來規範，那就是 X server 的設定檔啦。這個設定檔的檔名就是 /etc/X11/xorg.conf 喔！

### 23.2.1 解析 xorg.conf 設定

  如同前幾個小節談到的，在 Xorg 基金會裡面的 X11 版本為 X11R7.N ，那如果你想要知道到底你用的 X Server 版本是第幾版，可以使用 X 指令來檢查喔！(你必須以 root 的身分執行下列指令)

  ```
  [root@study ~]# <span>X -version</span>
  X.Org X Server <span>1.15.0</span>
  Release Date: 2013-12-27
  <span>X Protocol Version 11, Revision 0</span>
  Build Operating System:  2.6.32-220.17.1.el6.x86_64
  Current Operating System: Linux study.centos.vbird 3.10.0-229.el7.x86_64 #1 SMP Fri Mar
  6 11:36:42 UTC 2015 x86_64
  Kernel command line: BOOT_IMAGE=/vmlinuz-3.10.0-229.el7.x86_64 root=/dev/mapper/centos-
  root ro rd.lvm.lv=centos/root rd.lvm.lv=centos/swap crashkernel=auto rhgb quiet
  Build Date: 10 April 2015  11:44:42AM
  Build ID: xorg-x11-server 1.15.0-33.el7_1
  Current version of pixman: 0.32.4
        Before reporting problems, check <span>http://wiki.x.org</span>
        to make sure that you have the latest version.
  ```

  由上面的幾個關鍵字我們可以知道，目前鳥哥的這部測試機使用的 X server 是 Xorg 計畫所提供的 X11 版， 不過看起來 Xorg 已經將所謂的 X11R7 那個 R7 的版次移除，使用的是 Xorg 自己的版次了！所以是 Xorg 1.15.0 版本！ 此外，若有問題則可以到 http://wiki.x.org 去查詢～因為是 Xorg 這個 X server ，因此我們的設定檔檔名為 /etc/X11/xorg.conf 這一個哩。所以，理解這個檔案的內容對於 X server 的功能來說，是很重要的。

  比較需要留意的是，從 CentOS 6 以後 (當然包含 CentOS 7)，X server 在每次啟動的時候都會自行偵測系統上面的顯示晶片、螢幕類型等等， 然後自行搭配最佳化的驅動程式載入。因此，這個 /etc/X11/xorg.conf 已經不再被需要了。不過，如果你不喜歡 X 系統自行偵測的設定值， 那也可以自行建置 xorg.conf 就是了。

  此外，如果你只想要加入或者是修改部份的設定，並不是每個元件都要自行設定的話，那麼可以在 /etc/X11/xorg.conf.d/ 這個目錄下建立檔名為 .conf 的檔案， 將你需要的額外項目加進去即可喔！那就不會每個設定都以你的 xorg.conf 為主了！瞭解乎？

  Tips

  ![鳥哥](assets/2024/vbird_face.gif "鳥哥") 那我怎麼知道系統用的是哪一個設定呢？可以參考 /var/log/Xorg.0.log 的內容，該檔案前幾行會告訴你使用的設定檔案是來自於哪裡的喔！

  注意一下，在修改這個檔案之前，務必將這個檔案給它備份下來，免的改錯了甚麼東西導致連 X server 都無法啟動的問題啊。這個檔案的內容是分成數個段落的，每個段落以 Section 開始，以 EndSection 結束， 裡面含有該 Section (段落) 的相關設定值，例如:

  ```
  <span>Section  "section name"
  …… <span><== 與這個 section name 有關的設定項目</span>
  ……
  EndSection</span>
  ```

  至於常見的 section name 主要有:

  1. Module: 被載入到 X Server 當中的模組 (某些功能的驅動程式)；
  2. InputDevice: 包括輸入的 1. 鍵盤的格式 2. 滑鼠的格式，以及其他相關輸入設備；
  3. Files: 設定字型所在的目錄位置等；
  4. Monitor: 監視器的格式， 主要是設定水平、垂直的更新頻率，與硬體有關；
  5. Device: 這個重要，就是顯示卡晶片組的相關設定了；
  6. Screen: 這個是在螢幕上顯示的相關解析度與色彩深度的設定項目，與顯示的行為有關；
  7. ServerLayout: 上述的每個項目都可以重覆設定，這裡則是此一 X server 要取用的哪個項目值的設定囉。
  前面說了，xorg.conf 這個檔案已經不存在，那我們怎麼學習呢？沒關係，Xorg 有提供一個簡單的方式可以讓我們來重建這個 xorg.conf 檔案！ 同時，這可能也是 X 自行偵測 GPU 所產生的最佳化設定喔！怎麼處理呢？假設你是在 multi-user.target 的環境下，那就可以這樣作來產生 xorg.conf 喔！

  ```
  [root@study ~]# <span>Xorg -configure</span>
  <span>.....(前面省略).....</span>
  Markers: (--) probed, (**) from config file, (==) default setting,
        (++) from command line, (!!) notice, (II) informational,
        (WW) warning, (EE) error, (NI) not implemented, (??) unknown.
  (==) Log file: "/var/log/Xorg.0.log", Time: Wed Sep 16 10:13:57 2015
  List of video drivers:   <span># 這裡在說明目前這個系統上面有的顯示卡晶片組的驅動程式有哪些的意思</span>
        qxl
        vmware
        v4l
        ati
        radeon
        intel
        nouveau
        dummy
        modesetting
        fbdev
        vesa
  (++) Using config file: "/root/xorg.conf.new"        <span># 使用的設定檔</span>
  (==) Using config directory: "/etc/X11/xorg.conf.d"  <span># 額外設定項目的位置</span>
  (==) Using system config directory "/usr/share/X11/xorg.conf.d"
  (II) [KMS] Kernel modesetting enabled.
  <span>.....(中間省略).....</span>
  Your xorg.conf file is /root/xorg.conf.new           <span># 最終新的檔案出現了！</span>
  To test the server, run 'X -config /root/xorg.conf.new' <span># 測試手段！</span>
  ```

  這樣就在你的 root 家目錄產生一個新的 xorg.conf.new 囉！好了，直接來看看這個檔案的內容吧！這個檔案預設的情況是取消很多設定值的， 所以你的設定檔可能不會看到這麼多的設定項目。不要緊的，後續的章節會交代如何設定這些項目的喔！

  ```
  [root@study ~]# <span>vim xorg.conf.new</span>
  Section "ServerLayout"                             <span># 目前 X 決定使用的設定項目</span>
        Identifier     "X.org Configured"
        <span>Screen      0  "Screen0" 0 0</span>               <span># 使用的螢幕為 Screen0 這一個 (後面會解釋)</span>
        InputDevice    "Mouse0" "CorePointer"      <span># 使用的滑鼠設定為 Mouse0</span>
        InputDevice    "Keyboard0" "CoreKeyboard"  <span># 使用的鍵盤設定為 Keyboard0</span>
  EndSection
  <span># 系統可能有多組的設定值，包括多種不同的鍵盤、滑鼠、顯示晶片等等，而最終 X 使用的設定，
  # 就是在這個 ServerLayout 項目中來處理的！因此，你還得要去底下找出 Screen0 是啥</span>
  Section "Files"
        ModulePath   "/usr/lib64/xorg/modules"
        FontPath     "catalogue:/etc/X11/fontpath.d"
        FontPath     "built-ins"
  EndSection
  <span># 我們的 X Server 很重要的一點就是必須要提供字型，這個 Files 的項目就是在設定字型，
  # 當然啦，你的主機必須要有字型檔才行。一般字型檔案在：/usr/share/X11/fonts/ 目錄中。
  # 但是 Xorg 會去讀取的則是在 /etc/X11/fontpath.d 目錄下的設定喔！</span>
  Section "Module"
        Load  "glx"
  EndSection
  <span># 上面這些模組是 X Server 啟動時，希望能夠額外獲得的相關支援的模組。
  # 關於更多模組可以搜尋一下 /usr/lib64/xorg/modules/extensions/ 這個目錄</span>
  Section "InputDevice"
        Identifier  "Keyboard0"
        Driver      "kbd"
  EndSection
  <span># 就是鍵盤，在 ServerLayout 項目中有出現這個 Keyboard0 吧！主要是設定驅動程式！</span>
  Section "InputDevice"
        Identifier  "Mouse0"
        Driver      "mouse"
        Option      "Protocol" "auto"
        Option      "Device" "/dev/input/mice"
        Option      "ZAxisMapping" "4 5 6 7"   <span># 支援滾輪功能！</span>
  EndSection
  <span># 這個則主要在設定滑鼠功能，重點在那個 Protocol 項目，
  # 那個是可以指定滑鼠介面的設定值，我這裡使用的是自動偵測！不論是 USB/PS2。</span>
  Section "Monitor"
        Identifier   "Monitor0"
        VendorName   "Monitor Vendor"
        ModelName    "Monitor Model"
  EndSection
  <span># 螢幕監視器的設定僅有一個地方要注意，那就是垂直與水平的更新頻率，常見設定如下：
  #       HorizSync    30.0 - 80.0
  #       VertRefresh  50.0 - 100.0
  # 在上面的 HorizSync 與 VerRefresh 的設定上，要注意，不要設定太高，
  # 這個玩意兒與實際的監視器功能有關，請查詢你的監視器手冊說明來設定吧！
  # 傳統 CRT 螢幕設定太高的話，據說會讓 monitor 燒毀呢，要很注意啊。</span>
  Section "Device"     <span># 顯示卡晶片 (GPU) 的驅動程式！很重要的設定！</span>
        Identifier  "Card0"
        Driver      "qxl"        <span># 實際使用的顯示卡驅動程式！</span>
        BusID       "PCI:0:2:0"
  EndSection
  <span># 這地方重要了，這就是顯示卡的晶片模組載入的設定區域。由於鳥哥使用 Linux KVM
  # 模擬器模擬這個測試機，因此這個地方顯示的驅動程式為 qxl 模組。
  # 更多的顯示晶片模組可以參考 /usr/lib64/xorg/modules/drivers/</span>
  Section "Screen"                <span># 與顯示的畫面有關，解析度與色彩深度</span>
        Identifier "Screen0"    <span># 就是 ServerLayout 裡面用到的那個螢幕設定</span>
        Device     "Card0"      <span># 使用哪一個顯示卡的意思！</span>
        Monitor    "Monitor0"   <span># 使用哪一個螢幕的意思！</span>
        SubSection "Display"    <span># 此階段的附屬設定項目</span>
                Viewport   0 0
                Depth     1     <span># 就是色彩深度的意思！</span>
        EndSubSection
        SubSection "Display"
                Viewport   0 0
                Depth     16
        EndSubSection
        SubSection "Display"
                Viewport   0 0
                Depth     24
        EndSubSection
  EndSection
  <span># Monitor 與實際的顯示器有關，而 Screen 則是與顯示的畫面解析度、色彩深度有關。
  # 我們可以設定多個解析度，實際應用時可以讓使用者自行選擇想要的解析度來呈現，設定如下：
  #Modes    "1024x768" "800x600" "640x480" <span><==解析度</span>
  # 上述的 Modes 是在 "Display" 底下的子設定。
  # 不過，為了避免困擾，鳥哥通常只指定一到兩個解析度而已。</span>
  ```

  上面設定完畢之後，就等於將整個 X Server 設定妥當了，很簡單吧。如果你想要更新其他的例如顯示晶片的模組的話，就得要去硬體開發商的網站下載原始檔來編譯才行。 設定完畢之後，你就可以啟動 X Server 試看看囉。然後，請將 xorg.conf.new 更名成類似 00-vbird.conf 之類的檔名， 再將該檔案移動到 /etc/X11/xorg.conf.d/ 裡面去，這樣就 OK 了！

  ```
  <span># 測試 X server 的設定檔是否正常：</span>
  [root@study ~]# <span>startx  </span>  <span><==直接在 multi-user.target 啟動 X 看看</span>
  [root@study ~]# <span>Xorg :1 </span>  <span><==在 tty3 單獨啟動 X server 看看</span>
  ```

  當然，你也可以利用 systemctl isolate graphical.target 這個指令直接切換到圖形介面的登入來試看看囉。

  Tips

  ![鳥哥](assets/2024/vbird_face.gif "鳥哥") 經由討論區網友的說明，如果你發現明明有捉到顯示卡驅動程式卻老是無法順利啟動 X 的話，可以嘗試去官網取得驅動程式來安裝， 也能夠將『Device』階段的『Driver』修改成預設的『Driver "vesa"』，使用該驅動程式來暫時啟動 X 內的顯示卡喔！

### 23.2.2 字型管理

  我們 Xorg 所使用的字型大部分都是放置於底下的目錄中：

/usr/share/X11/fonts/

/usr/share/fonts/

  不過 Xorg 預設會載入的字型則是記錄於 /etc/X11/fontpath.d/ 目錄中，使用連結檔的模式來進行連結的動作而已。 你應該還記得 xorg.conf 裡面有個『 Flies 』的設定項目吧？該項目裡面就有指定到『 FontPath "catalogue:/etc/X11/fontpath.d" 』 對吧！也就是說，我們預設的 Xorg 使用的字型就是取自於 /etc/X11/fontpath.d 囉！

  鳥哥查了一下 CentOS 7 針對中文字型 (chinese) 來說，有楷書與明體，明體預設安裝了，不過楷書卻沒有安裝耶～ 那我們能不能安裝了楷書之後，將楷書也列為預設的字型之一呢？來瞧一瞧我們怎麼作的好了：

  ```
  <span># 1. 檢查中文字型，並且安裝中文字型與檢驗有沒有放置到 fontpath.d 目錄中！</span>
  [root@study ~]# <span>ll -d /usr/share/fonts/cjk*</span>
  drwxr-xr-x. 2 root root 22 May  4 17:54 /usr/share/fonts/cjkuni-uming
  [root@study ~]# <span>yum install cjkuni-ukai-fonts</span>
  [root@study ~]# <span>ll -d /usr/share/fonts/cjk*</span>
  drwxr-xr-x. 2 root root 21 Sep 16 11:48 /usr/share/fonts/cjkuni-ukai  <span># 這就是楷書！</span>
  drwxr-xr-x. 2 root root 22 May  4 17:54 /usr/share/fonts/cjkuni-uming
  [root@study ~]# <span>ll /etc/X11/fontpath.d/</span><span>
  lrwxrwxrwx. 1 root root 29 Sep 16 11:48 cjkuni-ukai-fonts -> /usr/share/fonts/cjkuni-ukai/
  lrwxrwxrwx. 1 root root 30 May  4 17:54 cjkuni-uming-fonts -> /usr/share/fonts/cjkuni-uming/
  lrwxrwxrwx. 1 root root 36 May  4 17:52 default-ghostscript -> /usr/share/fonts/default/ghostscript
  lrwxrwxrwx. 1 root root 30 May  4 17:52 fonts-default -> /usr/share/fonts/default/Type1
  lrwxrwxrwx. 1 root root 27 May  4 17:51 liberation-fonts -> /usr/share/fonts/liberation
  lrwxrwxrwx. 1 root root 27 Sep 15 17:10 xorg-x11-fonts-100dpi:unscaled:pri=30 -> /usr/share/X11/fonts/100dpi
  lrwxrwxrwx. 1 root root 26 Sep 15 17:10 xorg-x11-fonts-75dpi:unscaled:pri=20 -> /usr/share/X11/fonts/75dpi
  lrwxrwxrwx. 1 root root 26 May  4 17:52 xorg-x11-fonts-Type1 -> /usr/share/X11/fonts/Type1</span>
  <span># 竟然會自動的將該字型加入到 fontpath.d 當中！太好了！ ^_^</span>
  <span># 2. 建立該字型的字型快取資料，並檢查是否真的取用了？</span>
  [root@study ~]# <span>fc-cache -v | grep ukai</span>
  /usr/share/fonts/cjkuni-ukai: skipping, existing cache is valid: 4 fonts, 0 dirs
  [root@study ~]# <span>fc-list | grep ukai</span>
  /usr/share/fonts/cjkuni-ukai/ukai.ttc: AR PL UKai TW:style=Book
  /usr/share/fonts/cjkuni-ukai/ukai.ttc: AR PL UKai HK:style=Book
  /usr/share/fonts/cjkuni-ukai/ukai.ttc: AR PL UKai CN:style=Book
  /usr/share/fonts/cjkuni-ukai/ukai.ttc: AR PL UKai TW MBE:style=Book
  <span># 3. 重新啟動 Xorg，或者是強制重新進入 graphical.target</span>
  [root@study ~]# <span>systemctl isolate multi-user.target; systemctl isolate graphical.target</span>
  ```

  如果上述的動作沒有問題的話，現在你可以在圖形界面底下，透過『應用程式』 --> 『公用程式』 --> 『字型檢視程式』當中找到一個名為 『AR PL UKai CN, Book』字樣的字型，點下去就會看到如下的圖示，那就代表該字型已經可以被使用了。不過某些程式可能還得要額外的加工就是了～

  ![安裝楷書字型的結果](assets/2024/centos7_font_1.jpg "安裝楷書字型的結果")

  圖 23.2.1、安裝楷書字型的結果

  鳥哥比較好奇的是，這個字型的開發者怎麼這麼有趣！列出來的示意字型竟然是吃了玻璃會身體頭好壯壯～這...會不會教壞小孩啊？呵呵呵呵～

讓視窗管理員可以使用額外的字型

  如果想要使用額外的字型的話，你可以自行取得某些字型來處理的。鳥哥這邊從 Windows 微軟正黑體、Times new Romans 兩種字型加上粗、斜體等共六個檔案來處理字型的安裝～ 這邊得註明一下是純粹的測試，測試完畢後檔案就給它拿掉了，並沒有持續使用喔！並沒有想要違法的意思啦～大家參考看看就好了。 那就來看看如何增加字型吧！(假設上述的字體檔是放置在 /root/font 中)

  ```
  <span># 1. 將字型檔案放置到系統設定目錄，亦即底下的目錄中：</span>
  [root@study ~]# <span>cd /usr/share/fonts/</span>
  [root@study ~]# <span>mkdir windows</span>
  [root@study ~]# <span>cp /root/font/*.ttf /usr/share/fonts/windows/</span>
  <span># 2. 使用 fc-cache 將上述的檔案加入字型的支援中：</span>
  [root@study ~]# <span>fc-cache -f -v</span>
  <span>....(前面省略)....</span>
  /usr/share/fonts/windows: caching, new cache contents: 6 fonts, 0 dirs
  <span>....(後面省略)....</span>
  <span># -v 僅是列出目前的字型資料， -f 則是強制重新建立字型快取！</span>
  <span># 3. 透過 fc-list 列出已經被使用的檔案看看：</span>
  [root@study ~]# <span>fc-list : file | grep window</span>  <span><==找出被快取住的檔名</span>
  /usr/share/fonts/windows/timesbi.ttf:
  /usr/share/fonts/windows/timesi.ttf:
  /usr/share/fonts/windows/msjh.ttf:
  /usr/share/fonts/windows/times.ttf:
  /usr/share/fonts/windows/msjhbd.ttf:
  /usr/share/fonts/windows/timesbd.ttf:
  ```

  之後在字型檢視器裡面就會發現有多了『Microsoft JhengHei, Times New Roman』等等的字型可以用囉！

### 23.2.3 顯示器參數微調

  有些朋友偶而會這樣問：『我的顯示器明明還不錯，但是螢幕解析度卻永遠只能達到 800x600 而已， 這該如何處理？』，螢幕的解析度應該與顯示卡相關性不高，而是與顯示器的更新頻率有關！

  所謂的更新頻率，指的是在一段時間內螢幕重新繪製畫面的速度。舉例來說， 60Hz 的更新頻率， 指的是每秒鐘畫面更新 60 次的意思。那麼關於顯示器的更新頻率該如何調整呢？ 你得先去找到你的顯示器的使用說明書 (或者是網站會有規格介紹)，取得最高的更新率後，接下來選擇你想要的解析度， 然後透過這個 gtf 的指令功能來調整：

  Tips

  ![鳥哥](assets/2024/vbird_face.gif "鳥哥") 基本上，現在新的 Linux distribution 的 X server 大多使用自行偵測方式來處理所有的設定了，因此， 除非你的螢幕特別新或者是特別怪，否則應該不太需要使用到 gtf 的功能囉！

  ```
  <span># 1. 先來測試一下你目前的螢幕搭配顯卡所能夠處理的解析度與更新頻率 (須在 X 環境下)</span>
  [root@study ~]# <span>xrandr</span>
  Screen 0: minimum 320 x 200, current 1440 x 900, maximum 8192 x 8192
  Virtual-0 connected primary 1440x900+0+0 0mm x 0mm
   1024x768       59.9 +
   1920x1200      59.9
   1920x1080      60.0
   1600x1200      59.9
   1680x1050      60.0
   1400x1050      60.0
   1280x1024      59.9
   1440x900       59.9*
   1280x960       59.9
   1280x854       59.9
   1280x800       59.8
   1280x720       59.9
   1152x768       59.8
   800x600        59.9
   848x480        59.7
   720x480        59.7
   640x480        59.4
  <span># 上面顯示現在的環境中，測試過最高解析度大概是 1920x1200 ，但目前是 1440x900 (*)
  # 若需要調整成 1280*800 的話，可以使用底下的方式來調整喔！</span>
  [root@study ~]# <span>xrandr -s 1280x800</span>
  <span># 2. 若想強迫 X server 更改螢幕的解析度與更新頻率，則需要修訂 xorg.conf 的設定。先來偵測：</span>
  [root@study ~]# <span>gtf 水平像素 垂直像素 更新頻率 [-xv]</span>
  <span>選項與參數：
  水平像素：就是解析度的 X 軸
  垂直像素：就是解析度的 Y 軸
  更新頻率：與顯示器有關，一般可以選擇 60, 75, 80, 85 等頻率
  -x      ：使用 Xorg 設定檔的模式輸出，這是預設值
  -v      ：顯示偵測的過程</span>
  <span># 1. 使用 1024x768 的解析度，75 Hz 的更新頻率來取得顯示器內容</span>
  [root@study ~]# <span>gtf 1024 768 75 -x</span>
  # 1024x768 @ 75.00 Hz (GTF) hsync: 60.15 kHz; pclk: 81.80 MHz
  Modeline "1024x768_75.00"  81.80  1024 1080 1192 1360  768 769 772 802  -HSync +Vsync
  <span># 重點是 Modeline 那一行！那行給他抄下來</span>
  <span># 2. 將上述的資料輸入 xorg.conf.d/*.conf 內的 Monitor 項目中：</span>
  [root@study ~]# <span>vim /etc/X11/xorg.conf.d/00-vbird.conf</span>
  Section "Monitor"
    Identifier   "Monitor0"
    VendorName   "Monitor Vendor"
    ModelName    "Monitor Model"
    <span>Modeline "1024x768_75.00"  81.80  1024 1080 1192 1360  768 769 772 802  -HSync +Vsync</span>
  EndSection
  <span># 就是新增上述的那行特殊字體部分到 Monitor 的項目中即可。</span>
  ```

  然後重新啟動你的 X ，這樣就能夠選擇新的解析度囉！那如何重新啟動 X 呢？兩個方法， 一個是『 systemctl isolate multi-user.target; systemctl isolate graphical.target 』從文字模式與圖形模式的執行等級去切換，另一個比較簡單， 如果原本就是 graphical.target 的話，那麼在 X 的畫面中按下『 \[alt\] + \[ctrl\] + \[backspace\] 』三個組合按鍵， 就能夠重新啟動 X 視窗囉！

### 23.3 顯示卡驅動程式安裝範例

  雖然你的 X 視窗系統已經順利的啟動了，也調整到你想要的解析度了，不過在某些場合底下，你想要使用顯示卡提供的 3D 加速功能時，卻發現 X 提供的預設的驅動程式並不支援！此時真是欲哭無淚啊～那該如何是好？沒關係，安裝官方網站提供的驅動程式即可！ 目前 (2015) 世界上針對 x86 提供顯示卡的廠商最大的應該是 Nvidia / AMD (ATI) / Intel 這三家 (沒有照市佔率排列)， 所以底下鳥哥就針對這三家的顯示卡驅動程式安裝，作個簡單的介紹吧！

  由於硬體驅動程式與核心有關，因此你想要安裝這個驅動程式之前，請務必先參考 [第二十一章](https://linux.vbird.org/linux_basic/0520source_code_and_tarball.php) 與 [第二十二章](https://linux.vbird.org/linux_basic/0520rpm_and_srpm.php) 的介紹，才能夠順利的編譯出顯示卡驅動程式喔！ 建議可以直接使用 yum 去安裝『 Development Tools 』這個軟體群組以及 kernel-devel 這個軟體即可。

  Tips

  ![鳥哥](assets/2024/vbird_face.gif "鳥哥") 因為你得要有實際的硬體才辦法安裝這些驅動程式，因此底下鳥哥使用的則是實體機器上面裝有個別的顯示卡的設備，就不是使用虛擬機器了喔！

### 23.3.1 NVidia

  雖然 Xorg 已經針對 NVidia 公司的顯示卡驅動程式提供了 "nouveau" 這個模組，不過這個模組無法提供很多額外的功能。 因此，如果你想要使用新的顯示卡功能時，就得要額外安裝 NVidia 提供的給 Linux 的驅動程式才行。

  至於 NVidai 雖然有提供驅動程式給大家使用，不過他們並沒有完全釋出，因此自由軟體圈不能直接拿人家的東西來重新開發！ 不過還是有很多好心人士有提供相關的軟體庫給大家使用啦！你可以自行 google 查閱相關的軟體庫 (比較可惜的是，EPEL 裡面並沒有 NVidia 官網釋出的驅動程式就是了！) 所以，底下我們還是使用傳統的從 NVidia 官網上面下載相關的軟體來安裝的方式喔！

查詢硬體與下載驅動程式

  你得要先確認你的硬體為何才可以下載到正確的驅動程式啊！簡單查詢的方法可以使用 lspci 喔！還不需要拆主機機殼啦！

  ```
  [root@study ~]# <span>lspci | grep -Ei '(vga|display)'</span>
  00:02.0 Display controller: Intel Corporation Xeon E3-1200 v3/4th Gen Core Processor Integrated
        Graphics Controller (rev 06)
  01:00.0 VGA compatible controller: NVIDIA Corporation GF119 [GeForce GT 610] (rev a1)
  <span># 鳥哥選的這部實體機器測試中，其實有內建 Intel 顯卡以及 NVidia GeForece GT610 這兩張卡！
  # 螢幕則是接在 NVidia 顯卡上面喔！</span>
  ```

  建議你可以到 NVidia 的官網 ([http://www.nvidia.com.tw](http://www.nvidia.com.tw/)) 自行去下載最新的驅動程式，你也可以到底下的連結直接查閱給 Linux 用的驅動程式：

[http://www.nvidia.com.tw/object/unix\_tw.html](http://www.nvidia.com.tw/object/unix_tw.html)

  請自行選擇與你的系統相關的環境。現在 CentOS 7 都僅有 64 位元啊！所以不要懷疑，就是選擇 Linux x86\_64/AMD64/EM64T 的版本就對了！ 不過還是得要注意你的 GPU 是舊的還是新的喔～像鳥哥剛剛查到上面使用的是 GT610 的顯卡，那使用最新長期穩定版就可以了！ 鳥哥下載的版本檔名有點像： NVIDIA-Linux-x86\_64-352.41.run，我將這檔名放置在 /root 底下喔！接下來就是這樣作：

系統升級與取消 nouveau 模組的載入

  因為這部系統是新安裝的，所以沒有我們虛擬機裡面已經安裝好所有需要的環境了。因此，我們建議你最好是做好系統升級的動作， 然後安裝所需要的編譯環境，最後還得要將 nouveau 模組排除使用！因為強迫系統不要使用 nouveau 這個驅動，這樣才能夠完整的讓 nvidia 的驅動程式運作！ 那就來瞧瞧怎麼作囉！

  ```
  <span># 1. 先來全系統升級與安裝所需要的編譯程式與環境；</span>
  [root@study ~]# <span>yum update</span>
  [root@study ~]# <span>yum groupinstall "Development Tools"</span>
  [root@study ~]# <span>yum install kernel-devel kernel-headers</span>
  <span># 2. 開始處理不許載入 nouveau 模組的動作！</span>
  [root@study ~]# <span>vim /etc/modprobe.d/blacklist.conf</span>  <span># 這檔案預設應該不存在</span>
  <span>blacklist nouveau
  options nouveau modeset=0</span>
  [root@study ~]# <span>vim /etc/default/grub</span>
  GRUB_CMDLINE_LINUX="vconsole.keymap=us crashkernel=auto  vconsole.font=latarcyrheb-sun16
  rhgb quiet <span>rd.driver.blacklist=nouveau nouveau.modeset=0</span>"
  <span># 在 GRUB_CMDLINE_LINUX 設定裡面加上 rd.driver.blacklist=nouveau nouveau.modeset=0 的意思！</span>
  [root@study ~]# <span>grub2-mkconfig -o /boot/grub2/grub.cfg</span>
  [root@study ~]# <span>reboot</span>
  [root@study ~]# <span>lsmod | grep nouveau</span>
  <span># 最後要沒有出現任何模組才是對的！</span>
  ```

安裝驅動程式

  要完成上述的動作之後才能夠處理底下的行為喔！(檔名依照你的環境去下載與執行)：

  ```
  [root@study ~]# <span>systemctl isolate multi-user.target</span>
  [root@study ~]# <span>sh NVIDIA-Linux-x86_64-352.41.run</span>
  <span># 接下來會出現底下的資料，請自行參閱圖示內容處理囉！</span>
  ```

  ![Nvidia 官網驅動程式相關設定畫面示意](assets/2024/centos7_nvidia_1.jpg "Nvidia 官網驅動程式相關設定畫面示意")

  圖 23.3.1-1、Nvidia 官網驅動程式相關設定畫面示意

  上面說的是授權，你必須要接受 (Accept) 才能繼續。

  ![Nvidia 官網驅動程式相關設定畫面示意](assets/2024/centos7_nvidia_2.jpg "Nvidia 官網驅動程式相關設定畫面示意")

  圖 23.3.1-2、Nvidia 官網驅動程式相關設定畫面示意

  要不要安裝 32 位元相容的函式庫，鳥哥個人是認為還是裝一下比較好啦！

  ![Nvidia 官網驅動程式相關設定畫面示意](assets/2024/centos7_nvidia_3.jpg "Nvidia 官網驅動程式相關設定畫面示意")

  圖 23.3.1-3、Nvidia 官網驅動程式相關設定畫面示意

  讓這支安裝程式主動的去修改 xorg.conf 吧！比較輕鬆愉快！就按下 Yes 即可。

  最後按下 OK 就結束安裝囉！這個時候如果你去查閱一下 /etc/X11/xorg.conf 的內容，會發現 Device 的 Driver 設定會成為 nvidia 喔！這樣就搞定囉！很簡單吧！ 而且這個時候你的 /usr/lib64/xorg/modules/drivers 目錄內，會多出一個 nvidia\_drv.so 的驅動程式檔案囉！ 同時這個軟體還提供了一支很有用的程式來幫助我們進行驅動程式升級喔！

  ```
  [root@study ~]# <span>nvidia-installer --update</span>
  <span># 可以進行驅動程式的升級檢查喔！</span>
  ```

  好囉，那你就趕緊試看看新的顯示卡晶片的功能吧。而如果有什麼疑問的話，查閱一下 /var/log/nvidia\* 開頭的登錄檔看看吧！ ^\_^

### 23.3.2 AMD (ATI)

  AMD 的顯卡 (ATI) 型號也很多，不過因為 AMD 的顯卡有提供成為 Open Source ，目前有個名為 ELrepo 的網站有主動提供 AMD 的顯卡驅動喔！ 而且是針對我們 CentOS 7 耶～好像還不賴～其實 ELrepo 也提供了 NVidia 的驅動程式啦！只是型號太多，所以鳥哥還是使用 NVidia 官網的資料來教學而已。

  那如何取得 ELrepo 呢？這個網站家目錄在底下，你可以自己瞧一瞧，至於安裝 ELrepo 的 yum 設定檔方式如下：

[http://elrepo.org](http://elrepo.org/)

  ```
  [root@study ~]# <span>rpm --import https://www.elrepo.org/RPM-GPG-KEY-elrepo.org</span>
  [root@study ~]# <span>rpm -Uvh http://www.elrepo.org/elrepo-release-7.0-2.el7.elrepo.noarch.rpm</span>
  [root@study ~]# <span>yum clean all</span>
  [root@study ~]# <span>yum --enablerepo elrepo-testing search fglrx</span>
  kmod-fglrx.x86_64 : fglrx kernel module(s)
  fglrx-x11-drv.x86_64 : AMD's proprietary driver for ATI graphic cards <span># 這就對了！</span>
  fglrx-x11-drv-32bit.x86_64 : Compatibility 32-bit files for the 64-bit Proprietary AMD driver
  fglrx-x11-drv-devel.x86_64 : Development files for AMD OpenGL X11 display driver.
  [root@study ~]# <span>yum --enablerepo elrepo-testing install fglrx-x11-drv</span>
  <span># 很快的！這樣就安裝好了 AMD 的顯示卡驅動程式了耶！超開心的吧！</span>
  ```

  安裝完畢後，系統就會在 /usr/lib64/xorg/modules/drivers/ 裡面出現 fglrx\_drv.so 這個新的驅動程式啦！ 與 Nvidia 相同的， ATI 也提供一支名為 aticonfig 的指令來幫忙設定 xorg.conf ，你可以直接輸入『 aticonfig -v 』來看看處理的方式即可。然後你就可以重新啟動 X 來看看新的驅動程式功能囉！非常簡單吧！

### 23.3.3 Intel

  老實說，由於 Intel 針對 Linux 的圖形介面驅動程式已經開放成為 Open source 了，所以理論上你不需要重新安裝 Intel 的顯示卡驅動程式的。除非你想要使用比預設的更新的驅動程式，那麼才需要重新安裝底下的驅動程式。 Intel 對 Linux 的顯示卡驅動程式已經有獨立的網站在運作，如下的連結就是安裝的說明網頁：

[https://01.org/zh/linuxgraphics](https://01.org/zh/linuxgraphics)

  其實 Intel 的顯示卡用的地方非常的多喔！因為只要是整合型主機板晶片組，用的是 Intel 的晶片時， 通常都整合了 Intel 的顯示卡囉～鳥哥使用的一組 cluster 用的就是 Intel 的晶片，所以囉～ 這傢伙也是用的到的啦！

  一般來說， Intel 的顯示卡都常常會使用 i910 等驅動程式，而不是這個較新的 intel 驅動程式！ 你可以察看一下你系統是否有存在這些檔案：

  ```
  [root@study ~]# <span>locate libdrm</span>
  /usr/lib64/libdrm.so.2
  /usr/lib64/libdrm.so.2.4.0
  /usr/lib64/libdrm_intel.so.1      <span># 就是這幾個怪東西！</span>
  /usr/lib64/libdrm_intel.so.1.0.0
  <span>.....(底下省略).....</span>
  [root@study ~]# <span>locate intel | grep xorg</span>
  /usr/lib64/xorg/modules/drivers/intel_drv.so
  <span># 上面這個就是 Intel 的顯示卡驅動程式了！</span>
  ```

  呼呼！我們的 CentOS 有提供新的 Intel 顯示卡驅動程式啦！所以不需要重新安裝說～ 只是可能需要修改 xorg.conf 這個設定檔的內容。基本上，要修改的地方有：

  ```
  [root@study ~]# <span>vi /etc/X11/xorg.conf</span>
  Section "Device"
        Identifier  "Videocard0"
        <span>Driver      "intel"</span>  <span><==原本可能會是使用 i91x 喔</span>
  EndSection
  Section "Module"
        <span>....(中間省略)....</span>
        <span>Load  "glx"    <span><==這兩個很重要！務必要載入！</span>
        Load  "dri"</span>
        <span>....(中間省略)....</span>
  EndSection
  <span>Section "DRI"          <span><==這三行是新增的！讓大家都能使用 DRI</span>
       Mode 0666       <span><==基本上，就是權限的設定</span>
  EndSection</span>
  ```

  如果一切順利的話，接下來就是重新啟動 X 囉～使用新的 Intel 驅動程式吧！加油囉！

  Tips

  ![鳥哥](assets/2024/vbird_face.gif "鳥哥") 老實說，CentOS 7 的 Xorg 自動偵測程式作的其實還不錯，在鳥哥這次測試實體機器的系統上面安裝的圖形界面時，幾乎 Xorg 都可以正確的抓到驅動程式， 連雙螢幕功能也都可以順利的啟用沒問題。所以除非必要，否則您應該不需要重新設定 xorg.conf 喔！ ^\_^

### 23.5 本章習題

  ( 要看答案請將滑鼠移動到『答：』底下的空白處，按下左鍵圈選空白處即可察看 )

在 X 設定沒問題的情況下，你在 Linux 主機如何取得視窗介面？

    如果是在 multi-user.target 模式下，可以使用 startx 進入，至於 graphical.target ，則直接進入 tty1 即可使用 display manager 登入 X Window 系統。

利用 startx 可以在 multi-user.target 的環境下進入 X Window 系統。請問 startx 的主要功能？

    整個 X 視窗系統的重點在啟動 X server 並載入 X client ，而執行 X server/X client 呼叫的任務為 xinit ，startx 只是一個較為親和的腳本程式，可以搜尋系統上面的 X server / X client 設定值， 以提供 xinit 來執行而已。

如何知道你系統當中 X 系統的版本與計畫？

    最簡單可以利用 root 的身份下達 X -version 或 Xorg -version 即可知道！

要瞭解為何 X 系統可以允許不同硬體、主機、作業系統之間的溝通，需要知道 X server / X client 的相關知識。 請問 X Server / X client / Window manager 的主要用途功能？

    X Server 主要負責螢幕的繪製，以及周邊輸入裝置如滑鼠、鍵盤等資料的收集，並回報給 X Client ； X Client 主要負責資料的運算，收到來自 X Server 的資料後，加以運算得到圖形的數據，並回傳給 X Server， 讓 X server 自行繪製圖形。至於 Window manager 是一個比較特殊的 X Client ，他可以管理更多控制元素， 最重要的地方還是在於視窗的大小、重疊、移動等等的功能。

如何重新啟動 X

  - 最簡單在 X Window System 下，直接按下 \[alt\]+\[ctrl\]+\[backspace<--\] 即可
  - 也可以 systemctl isolate multi-usertarget 再 systemctl isolate graphical.target
  - 也可以關閉 X 後，再 startx 啟動等等。

試說明 ~/.xinitrc 這個檔案的用途？

    當我們要啟動 X 時，必須要啟動 X Client 軟體端。這個 ~/.xinitrc 即是在客制化自己的 X Client ， 你可以在這個檔案內輸入你自己的 X Client 。若無此檔案，則預設以 /etc/X11/xinit/xinitrc 替代。

我在 CentOS 的系統中，預設使用 GNOME 登入 X 。但我想要改以 KDE 登入，該怎麼辦？

  - 首先你必須要已經安裝 KDE 環境 (參考前一章的 yum grouplist 功能)，
  - 然後可以藉由修改 /etc/sysconfig/desktop 內的設定值即可。
  - 但如果你不是 root 無法修訂該檔案時，亦可以在自己的家目錄參考 /etc/X11/xinit/xinitrc 的內容自行製作 ~/.xinitrc 檔案來修改！

X Server 的 port 預設開放在？

    目前預設並不會啟動 TCP 埠口。不過如果經過設定，則 X port 預設開放在 port 6000 ，而且稱此一顯示為 :0

Linux 主機是否可以有兩個以上的 X

    是的！可以！第一個 X 通常在 tty1 ，第二個在 tty2 以後，依序類推。 第幾個是以啟動的順序來定義，並非 :0 , :1 的意思～

X Server 的設定檔是 xorg.conf，在該檔案中， Section Files 幹嘛用的？

    相當重要！是設定顯示字型用的。而字型一般放置目錄在 /usr/share/X11/fonts/ 及 /usr/share/fonts/ 當中。

我發現我的 X 系統鍵盤所輸入的字母老是打不出我所需要的單字，可能原因該如何修訂？

    應該是鍵盤符號對應表跑掉了。可以修改 xorg.conf 檔案內， 關於 Keyboard 的 Option XkbLayout 項目，將他改為 us 即可！

當我的系統內有安裝 GNOME 及 KDE 兩個 X Widnow Manager ，我原本是以 KDE 為預設的 WM， 若想改為 GNOME 時，應該如何修改？

    修改 /etc/sysconfig/desktop 內部，成為 GNOME 即可！
