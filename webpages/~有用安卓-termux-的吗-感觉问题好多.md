---
created: 2025-06-07T15:41:22
modified: 2025-06-07T15:42:26
source: "https://v2ex.com/t/741093#"
tags:
tags-link:
type: "archive-web"
---

## Origin Content
1. root 搞不定，明明手机 root 了，但安装 pkg install tsu 后提示没 root 。直接输入 su 命令可以获取 root 权限，但 termux 自带的命令基本都用不了了。
2. 外置 sd 卡权限无法获取，据说本来就没办法获取。内置 sd 卡似乎也有很多权限问题，不知道 root 后会不会好点，有时候莫名其妙提示权限问题，chmod 也失败。其他程序就基本没见过权限问题，另一个 app“终端模拟器”就能直接获取 root 权限，另外也没见过其他权限问题。
3. tasker 调用方面也没试，看了下有个 termux-tasker 的 app 好像是收费的，付费后也不知道能不能成功使用。
4. 很多问题在英文网站也有一些遇到同样的情况的，但大都不了了之。主要是想用 termux 里面的 python，感觉 python 很多包都可以直接 pip 安装，挺不错的，之前用 qpython 就很多包都用不了。

## Comment

通过添加环境变量的办法非常好用，非常感谢 。

只要添加环境变量之后就可以完全无视 termux 了，termux 自带的一些 linux 命令（没有的命令也可以安装）以及 python 都可以直接去“终端模拟器”或者 tasker 中运行了，并且 termux 不需要后台运行。

▃▃▃▃

只是安卓目前只能临时添加环境命令，每次启动终端都需要设置一下环境变量，暂时没找到永久的办法。

目前这样操作，在根目录 /新建一个 path 的文件，输入下面的两行内容：

export PATH=/data/data/com.termux/files/usr/bin:/data/data/com.termux/files/usr/bin/applets:$PATH

export LD\_LIBRARY\_PATH=/data/data/com.termux/files/usr/lib

▃▃▃▃

以后只需要在 root 权限下在终端中输入. /path 就可以直接添加环境变量了，注意有个点以及一个空格，代表执行根目录下的 path 文件。“终端模拟器”也可以设置启动时自动执行. /path，这样只要一启动就默认添加上环境变量了，直接输入 python 之类的命令就可以运行 python 了。

▃▃▃▃

①tasker 调用：添加任务，选择代码 -- 运行外壳（勾选使用 root ），输入类似下面的代码就可以执行 python 文件：

. /path #添加环境变量

python [test.py](http://test.py/) #运行名为 [test.py](http://test.py/) 的 python 脚本

▃▃▃▃

②tasker 中不使用 py 文件的情况下直接运行多行 python 代码：添加任务，选择代码 -- 运行外壳（勾选使用 root，可选择将输出保存到变量），在三引号内输入类似下面的代码就可以直接执行多行 python 代码：

. /path

python -c '''

a=1

b=2

c=a+b

print(c)

'''

▃▃▃▃

③像上面那样直接写对于偶尔调用下比较方便，if 或复杂的循环逻辑都可以写到里面，只是比较容易出错。我刚 windows 输入后粘贴过去就报错，可能是换行符的问题，手动输入就没问题。
