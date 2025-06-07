---
created: 2025-01-12T02:17:53
modified: 2025-03-30T09:48:07
comments: false
---

![](https://img.shields.io/github/stars/bGZo/clippers?style=for-the-badge&label=stars) ![](https://img.shields.io/github/repo-size/bGZo/clippers?style=for-the-badge&label=size) ![](https://img.shields.io/github/created-at/bGZo/clippers?style=for-the-badge&label=since)

What we ignored is, the web is week, one research[^web-page-research] published in 2024, said 38% of webpages that existed in 2013 are no longer accessible a decade later.

You might think why this matters. So why 10 years? That's the upper limit you could renewal the domain.

It happened more fast in China cause censor. Maybe the article post 10 years ago is matter with current events matters, which would be disappeared as well.

Luckily, you could go http://web.archive.org to look what has gone (personal blog). And look around you what remains today (business content).

> [!note]
> If something illegal you think there is, please notice me, I would remove it immediately.

Something I repost and share here, which is not goods, ideology, hatred.

We could not be so smart.

## Roadmap: why choose this way?

### SingleFile + Raindrop.io

I used use https://github.com/gildas-lormeau/SingleFile and some kind of highlight tool to archive webpages I read. They would be stored as `html` and keep the most style of origin webpage. That's awesome.

But they depend on browser, once leave the pc and browser, they would be unreadable. I prefer to `Markdown`.

### Read on Notes
#### Logseq

I used to use https://github.com/sawhney17/logseq-web-parser to convert link to article and then read on logseq, high light something and store it.

But the cross with logseq sucks, I cannot do this type thing on phone or tablet. Once I leave PC, I have nothing to do.

And the most annoying thing is, the readable of logseq markdown is still ugly, which depend on their design core: outliner software.

#### Obsididn

Now I use the Web Clipper on Mac / iPad / iPhone, they keep the same with cross devices. I clip them in specific folder and notes on them.

They keep the best readable markdown file and most reachable way to access them. That would be a long journals with it.

## Alternativs

### More custom projects

- https://archivebox.io

### More creative way

Using the Github Action, Github Webhook and Telegram Bot to archive content with Markdown. They should from:

- Repo: we could use submodule import it.
- Blog: we could use rss fetch it every day.
- Social Media: in bluesky or mastodon, we still could use rss. Whereas towards traditional services, we only could use custom method to get content(anti-crawling)

## How to work with [[telegram-message-sync-bot]]

```shell
rsync -avz --progress --delete bgzo@192.168.31.20:/home/bgzo/workspaces/telegram-message-sync/archives/channel/ "/Users/bgzo/Library/Mobile Documents/iCloud~md~obsidian/Documents/wiki/archives/clip-telegram/"
```

## What I interested in and archive:

- Github repo tutorials
    - https://github.com/nakanomikuorg/arch-guide ![](https://img.shields.io/github/repo-size/nakanomikuorg/arch-guide)
    - https://github.com/collabnix/dockerlabs ![](https://img.shields.io/github/repo-size/collabnix/dockerlabs)
- Die people/website
    - https://shuziyiming.org
- Individual blog
    - https://www.hecaitou.com/
    - https://www.hecaitou.info/
    - yitianshijie
    - one
- ? Telegram Channel
- ? News
    - solidot

[^web-page-research]: https://www.pewresearch.org/data-labs/2024/05/17/when-online-content-disappears, https://www.reddit.com/r/ExperiencedDevs/comments/129faxx/running_a_website_after_you_die/
