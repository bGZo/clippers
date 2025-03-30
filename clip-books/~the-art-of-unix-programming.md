---
aliases: books/unix编程艺术
author: Eric S·Raymond
publisher: 电子工业出版社
published: 20060200
source: https://book.douban.com/subject/1467587, https://weread.qq.com/web/reader/f1f32dd072021a42f1fbdefkc81322c012c81e728d9d180
---


- UNIX 的特点：
  - __Everything (including hardware) is a file__.
    所有的事物（甚至硬件本身）都是一个的文件。
  - __Configuration data stored in text__.
    以文本形式储存配置数据。
  - __Small, single-purpose program.__
    程序尽量朝向小而单一的目标设计。
  - __Avoid captive user interfaces.__
    避免过于复杂花哨的界面。
  - __Ability to chain program together to perform complex tasks.__
    将几个程序连结起来，处理大而复杂的工作。
- Doug McIlroy（UNIX 管道的发明人、UNIX 传统的奠基人之一） 认为 UNIX 的哲学是这样的：
  - __Write programs that do one thing and do it well.__
    写一次只做一件事，并能把这件事做好的程序。
  - __Write programs to work together.__
    写互相协作（调用）的程序。
  - __Write programs to handle text streams, because that is a universal interface.__
    写处理文件流的程序。因为这（处理文件流）是一个通用接口。
- 《The Art of Unix Programming》 总结了下面这些哲学：
  - __Rule of Modularity: Write simple parts connected by clean interfaces.__
    模块化原则：写简单的，能够用清晰的接口连接的代码。
  - __Rule of Clarity: Clarity is better than cleverness.__
    清晰化原则：清晰的代码要好过“聪明”的代码。
  - __Rule of Composition: Design programs to be connected to other programs.__
    组件化原则：设计可以互相关联（拆分）的程序。
  - __Rule of Separation: Separate policy from mechanism; separate interfaces from engines.__
    隔离原则：策略和机制分离，接口和引擎分离。
  - __Rule of Simplicity: Design for simplicity; add complexity only where you must.__
    简洁原则：设计力求简洁，直到无法更简洁。
  - __Rule of Parsimony: Write a big program only when it is clear by demonstration that nothing else will do.__
    小巧原则：不要写大的程序（模块、方法）。除非很明显的，没有别的办法可以完成。
  - __Rule of Transparency: Design for visibility to make inspection and debugging easier.__
    透明原则：为可见性设计，使检查和调试更容易。
  - __Rule of Robustness: Robustness is the child of transparency and simplicity.__
    健壮性原则：健壮性是透明和简单的孩子。
  - __Rule of Representation: Fold knowledge into data so program logic can be stupid and robust.__
    陈述性原则：将认知转化为数据。所以，程序的逻辑可以是愚蠢（简单易懂）的，健壮的。
  - __Rule of Least Surprise: In interface design, always do the least surprising thing.__
    最少的惊讶原则：在界面设计中，少做令人惊讶的设计。（不要标新立异）
  - __Rule of Silence: When a program has nothing surprising to say, it should say nothing.__
    沉默原则：如果一个程序没有什么特别的东西要说（输出），那就什么都别说。
  - __Rule of Repair: When you must fail, fail noisily and as soon as possible.__
    修复原则：如果必须失败，那就尽早。
  - __Rule of Economy: Programmer time is expensive; conserve it in preference to machine time.__
    节约原则：程序员的时间是非常宝贵的。程序员的时间（编程时间）优于机器时间。
  - __Rule of Generation: Avoid hand-hacking; write programs to write programs when you can.__
    生产原则：避免手工编程。如果可以的话，编写可以编写程序的代码。
  - __Rule of Optimization: Prototype before polishing. Get it working before you optimize it.__
    优化原则：建立原型后再去修正。当它能正常工作后，再去优化它。
  - __Rule of Diversity: Distrust all claims for “one true way”.__
    多样性原则：怀疑所有所谓的“不二法门”。
  - __Rule of Extensibility: Design for the future, because it will be here sooner than you think.__
    扩展原则：为未来设计，因为未来来的比你想象的要早。
- **Mike Gancarz** （X Windows 的设计者）给出了下面九条哲学思想：
  - __Small is beautiful.__
    小即是美。
  - __Make each program do one thing well.__
    让每个程序（方法）只做一件事情，并把它做好。
  - __Build a prototype as soon as possible.__
    尽早建立原型。
  - __Choose portability over efficiency.__
    注重可移植性，而非效率。
  - __Store data in flat text files.__
    将数据存储在存文本文件中。
  - __Use software leverage to your advantage.__
    利用软件来发挥你的优势。
  - __Use shell scripts to increase leverage and portability.__
    使用Shell脚本提高编程的手段和程序的可移植性。
  - __Avoid captive user interfaces.__
    避免过于复杂花哨的界面。
  - __Make every program a filter.__
    使每个程序（方法）称为一个过滤器（筛选器）
## refs
  - [关于Unix哲学 - 阮一峰的网络日志](https://www.ruanyifeng.com/blog/2009/06/unix_philosophy.html)
  - [Unix编程艺术集萃 | Shenlvmeng's Blog](https://shenlvmeng.github.io/blog/2021/01/29/zen-of-unix/)
  - [《Unix编程艺术》读书笔记 - 山丘](https://xiezg247.xyz/2020/02/26/Unix%E7%BC%96%E7%A8%8B%E8%89%BA%E6%9C%AF-%E8%AF%BB%E4%B9%A6%E7%AC%94%E8%AE%B0/)
  -