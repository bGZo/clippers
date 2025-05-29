---
created: 2025-05-17T12:59:16
modified: 2025-05-17T12:59:33
source: "https://www.v2ex.com/t/1131883"
tags:
tags-link:
type: "archive-web"
---

## Origin Content
# 起因

提前声明，可能仅仅是社区部分人士行为，和某厂本身关系并不大。

起因是在 Babel 的仓库里看到了一个 issue： [https://github.com/babel/babel/issues/17309](https://github.com/babel/babel/issues/17309)

无 pr ，无实际内容，完全看不懂想干什么。

遂点进了此账号的动态，不看不知道，短时间向各大仓库滥发了 190 多条的 spam： [https://github.com/wshixjrnjr#:~:text=Contribution%20activity](https://github.com/wshixjrnjr#:%7E:text=Contribution%20activity)

格式是：Proposal for OpenHarmony Adaptation of [ .+ ]

---

# 研究

为了搞清楚这些无意义的 issue 到底目的是什么，简单的搜索了下，发现了这样一条 issue： [https://github.com/pillarjs/path-to-regexp/issues/359](https://github.com/pillarjs/path-to-regexp/issues/359)

在这条 issue 中，"Adaptation Plan" 终于有了实际内容，简而言之就是：希望向上游贡献在 HarmonyOS 上使用这个包的方式，以及去适配 OHPM 。

然后，"Test Results" 写了个：

> Based on the OpenHarmony system, we conducted unit tests on the original library test cases of dayjs.

大哥，你看清楚你这包名对的上这仓库吗？

并且在这条 issue 的下面，发现一个回复： [https://github.com/pillarjs/path-to-regexp/issues/359#issuecomment-2838577595](https://github.com/pillarjs/path-to-regexp/issues/359#issuecomment-2838577595)

> Regarding the statement of "OpenHarmony support" mentioned in our initial proposal, it is indeed inaccurate. In fact, since OpenHarmony supports Node.js, the path-to-regexp library can run directly in the OpenHarmony environment without any additional code adaptation work.
>
> As OpenHarmony adopts a new software center repository, [OHPM](https://ohpm.openharmony.cn/#/en/home), the build/packaging process for our JS projects differs from the traditional NPM approach. Previously, we planned to submit the relevant packaging scripts to the path-to-regexp community. However, as you all have pointed out, it might be more appropriate to configure this in GitHub Actions. We fully understand that this operation may bring additional maintenance burden to the path-to-regexp project.
>
> Based on the above considerations, we propose a lighter - weight collaboration solution: We will use our own automated build platform to regularly build path-to-regexp and publish the build artifacts to OHPM. During this process, we will clearly mark path-to-regexp as the upstream project. Meanwhile, we also hope that the path-to-regexp community can add a link to the library on the OHPM platform in the project's README, so that more developers can learn about its application in the OpenHarmony ecosystem.

---

# 所以大概情况是这样的

为了推动生态，某厂社区向一批库发起了一批 pr or issue ，向让仅支持 npm 并仅面向 node.js 生态的库提交一些兼容性的东西，并想在这些库的 README 中加上生态介绍。

仅确定的确有某厂员工参与回复，但 spam 并不确定是否是相关人士行为。

的确后续的 spam 不像大厂水平。

---

# 评价

我理解国产生态起步很难，但这种操作非常欠考量。

1. " 借生态 " 无可厚非，开源社区就是允许这样，但这种应该自己 fork ，而不是去麻烦上游。提 issue 搞得好像发广告一样，毫无诚意的机翻和冗长的介绍，还不带上具体 pr ，给人一个仓库让上游自己看？你到底想要上游做什么？
2. 既然菊厂相关高级员工已经提出了由己方社区去维护，相关生态人士就不应该再发 spam 了，几个 issue 已经被 closed 并表达反感了。收手吧，阿祖！名声都要给你搞坏了。国产起步不易，请不要破坏这份努力。

## Comment

当一家公司把自己和爱国做捆绑之后，就不要期待它以及它的信徒会遵守任何规则了

不支持 = 叛国

你怎么反驳？
