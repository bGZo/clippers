---
created: 2024-12-28T10:42:35
source: "https://zhangslob.github.io/2019/01/16/Golang%E5%86%99%E7%88%AC%E8%99%AB/"
type: "archive-web"
modified: 2025-01-15T11:38:20
---

发表于 2019-01-16 | 分类于 [Golang](https://zhangslob.github.io/categories/Golang/)

```
这是崔斯特的第八十三篇原创文章
```

新的旅程开始了 (๑• . •๑)

[![](https://ws2.sinaimg.cn/large/006tNc79ly1fz8qeqbn5ej30u00ulq74.jpg)](https://ws2.sinaimg.cn/large/006tNc79ly1fz8qeqbn5ej30u00ulq74.jpg)

---

## 前言

近期有些项目需要用到 Golang，大概花了一周来看语法，然后就开始看爬虫相关的。这里记录下如何使用 Golang 来写爬虫的几个步骤，最终完成的效果如下图

[![](https://ws4.sinaimg.cn/large/006tNc79gy1fz7qipg6aaj31100ls43h.jpg)](https://ws4.sinaimg.cn/large/006tNc79gy1fz7qipg6aaj31100ls43h.jpg)

## 环境

安装比较简单

| ``` 12 ``` | ``` sudo apt-get install golang  # (Linux)brew install go  # (Mac) ``` |
| --- | --- |

安装之后注意 `GOPATH` 和 `GOROOT` 等环境变量设置，IDE 用的是 jetbrains 家的 GoLand。

建议先去看看 Golang 的官方文档，学习基本语法知识。地址：[官方教程中文版](https://tour.go-zh.org/welcome/1)

## 创建文档

新建文件 `crawler.go`，并写入如下代码：

| ``` 1234567 ``` | ``` package mainimport "fmt"func main() {	fmt.Println("Hello, world")} ``` |
| --- | --- |

运行方法：`go run crawler.go`，肉眼可见，编译速度比 JAVA 要快得多。

## 下载网页

这里先从 Golang 原生 http 库开始，直接使用 `net/http` 包内的函数请求

| ``` 123 ``` | ``` import "net/http"...resp, err := http.Get("http://wwww.baidu.com") ``` |
| --- | --- |

所以代码可以这样写

| ``` 12345678910111213141516171819202122 ``` | ``` package mainimport ("fmt""io/ioutil""net/http")func main() {	fmt.Println("Hello, world")	resp, err := http.Get("http://www.baidu.com/")if err != nil {		fmt.Println("http get error", err)return	}	body, err := ioutil.ReadAll(resp.Body)if err != nil {		fmt.Println("read error", err)return	}	fmt.Println(string(body))} ``` |
| --- | --- |

Golang 的错误处理就是这样的，习惯就好。

这里更好的做法是把下载方法封装为函数。

| ``` 1234567891011121314151617181920212223242526272829303132333435 ``` | ``` package mainimport ("fmt""io/ioutil""net/http")func main() {	fmt.Println("Hello, world")	url := "http://www.baidu.com/"	download(url)}func download(url string) {	client := &http.Client{}	req, _ := http.NewRequest("GET", url, nil)// 自定义Header	req.Header.Set("User-Agent", "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)")	resp, err := client.Do(req)if err != nil {		fmt.Println("http get error", err)return	}//函数结束后关闭相关链接defer resp.Body.Close()	body, err := ioutil.ReadAll(resp.Body)if err != nil {		fmt.Println("read error", err)return	}	fmt.Println(string(body))} ``` |
| --- | --- |

## 解析网页

go 常见的解析器 xpath、jquery、正则都有，直接搜索即可，我这里偷懒，直接用别人写好的轮子 `collectlinks`，可以提取网页中所有的链接，下载方法 `go get -u github.com/jackdanger/collectlinks`

| ``` 123456789101112131415161718192021222324252627282930313233 ``` | ``` package mainimport ("fmt""github.com/jackdanger/collectlinks""net/http")func main() {	fmt.Println("Hello, world")	url := "http://www.baidu.com/"	download(url)}func download(url string) {	client := &http.Client{}	req, _ := http.NewRequest("GET", url, nil)// 自定义Header	req.Header.Set("User-Agent", "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)")	resp, err := client.Do(req)if err != nil {		fmt.Println("http get error", err)return	}//函数结束后关闭相关链接defer resp.Body.Close()	links := collectlinks.All(resp.Body)for _, link := range links {		fmt.Println("parse url", link)	}} ``` |
| --- | --- |

## 并发

Golang 使用关键字 `go` 即可开启一个新的 go 程，也叫 `goroutine`，使用 go 语句开启一个新的 goroutine 之后，go 语句之后的函数调用将在新的 goroutine 中执行，而不会阻塞当前的程序执行。所以使用 Golang 可以很容易写成异步 IO。

| ``` 12345678910111213141516171819202122232425262728293031323334353637383940414243 ``` | ``` package mainimport ("fmt""github.com/jackdanger/collectlinks""net/http")func main() {	fmt.Println("Hello, world")	url := "http://www.baidu.com/"	queue := make(chan string)go func() {		queue <- url	}()for uri := range queue {		download(uri, queue)	}}func download(url string, queue chan string) {	client := &http.Client{}	req, _ := http.NewRequest("GET", url, nil)// 自定义Header	req.Header.Set("User-Agent", "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)")	resp, err := client.Do(req)if err != nil {		fmt.Println("http get error", err)return	}//函数结束后关闭相关链接defer resp.Body.Close()	links := collectlinks.All(resp.Body)for _, link := range links {		fmt.Println("parse url", link)go func() {			queue <- link		}()	}} ``` |
| --- | --- |

现在的流程是 main 有一个 for 循环读取来自名为 queue 的通道，download 下载网页和链接解析，将发现的链接放入 main 使用的同一队列中，并再开启一个新的 goroutine 去抓取形成无限循环。

这里对于新手来说真的不好理解，涉及到 Golang 的两个比较重要的东西：goroutine 和 channels，这个我也不大懂，这里也不多讲了，以后有机会细说。

官方：A *goroutine* is a lightweight thread managed by the Go runtime.翻译过来就是：Goroutine 是由 Go 运行时管理的轻量级线程。channels 是连接并发 goroutine 的管道，可以理解为 goroutine 通信的管道。 可以将值从一个 goroutine 发送到通道，并将这些值接收到另一个 goroutine 中。对这部分有兴趣的可以去看文档。

好了，到这里爬虫基本上已经完成了，但是还有两个问题：去重、链接是否有效。

## 链接转为绝对路径

| ``` 1234567891011121314151617181920212223242526272829303132333435363738394041424344454647484950515253545556575859 ``` | ``` package mainimport ("fmt""github.com/jackdanger/collectlinks""net/http""net/url")func main() {	fmt.Println("Hello, world")	url := "http://www.baidu.com/"	queue := make(chan string)go func() {		queue <- url	}()for uri := range queue {		download(uri, queue)	}}func download(url string, queue chan string) {	client := &http.Client{}	req, _ := http.NewRequest("GET", url, nil)// 自定义Header	req.Header.Set("User-Agent", "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)")	resp, err := client.Do(req)if err != nil {		fmt.Println("http get error", err)return	}//函数结束后关闭相关链接defer resp.Body.Close()	links := collectlinks.All(resp.Body)for _, link := range links {		absolute := urlJoin(link, url)if url != " " {			fmt.Println("parse url", absolute)go func() {				queue <- absolute			}()		}	}}func urlJoin(href, base string) string {	uri, err := url.Parse(href)if err != nil {return " "	}	baseUrl, err := url.Parse(base)if err != nil {return " "	}return baseUrl.ResolveReference(uri).String()} ``` |
| --- | --- |

这里新写了一个 `urlJoin` 函数，功能和 Python 中的 `urllib.parse.urljoin` 一样。

## 去重

我们维护一个 map 用来记录，那些是已经访问过的。

| ``` 12345678910111213141516171819202122232425262728293031323334353637383940414243444546474849505152535455565758596061626364 ``` | ``` package mainimport ("fmt""github.com/jackdanger/collectlinks""net/http""net/url")var visited = make(map[string]bool)func main() {	fmt.Println("Hello, world")	url := "http://www.baidu.com/"	queue := make(chan string)go func() {		queue <- url	}()for uri := range queue {		download(uri, queue)	}}func download(url string, queue chan string) {	visited[url] = true	client := &http.Client{}	req, _ := http.NewRequest("GET", url, nil)// 自定义Header	req.Header.Set("User-Agent", "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)")	resp, err := client.Do(req)if err != nil {		fmt.Println("http get error", err)return	}//函数结束后关闭相关链接defer resp.Body.Close()	links := collectlinks.All(resp.Body)for _, link := range links {		absolute := urlJoin(link, url)if url != " " {if !visited[absolute] {				fmt.Println("parse url", absolute)go func() {					queue <- absolute				}()			}		}	}}func urlJoin(href, base string) string {	uri, err := url.Parse(href)if err != nil {return " "	}	baseUrl, err := url.Parse(base)if err != nil {return " "	}return baseUrl.ResolveReference(uri).String()} ``` |
| --- | --- |

好了大功告成，运行程序，会像一张网铺开一直不停的抓下去。

写到这里，我突然觉得我忘了什么，哦，忘记加 timeout 了，必须要为每次请求加上超时，前两天才写了的。完整代码就补贴上来了，[在github中](https://github.com/zhangslob/awesome_crawl/tree/master/Golang_basic_spider)。

运行一段时间后的资源消耗

[![](https://ws2.sinaimg.cn/large/006tNc79gy1fz7qd8qffhj31400u0jv4.jpg)](https://ws2.sinaimg.cn/large/006tNc79gy1fz7qd8qffhj31400u0jv4.jpg)

[![](https://ws3.sinaimg.cn/large/006tNc79gy1fz7qe2sxkej31400u0jv8.jpg)](https://ws3.sinaimg.cn/large/006tNc79gy1fz7qe2sxkej31400u0jv8.jpg)

CPU 使用率并不高，内存因为会保存一张不断增大的 map，所以会一直上涨。如果是用 Python，该怎么写呢？资源消耗和 Golang 比会如何呢？有兴趣的小伙伴可以去试试。

## 后记

都说 Golang 的并发好，体验了下确实如此。Golang 起步晚，但是发展的块。采集还是多学点技能防身吧。我从上周开始学习 Golang 语法，跟着官方文档学习，基本上都可以看懂在做什么，除了那几块难理解的，需要自己多写多用才行。

有兴趣的小伙伴一起入坑啊。
