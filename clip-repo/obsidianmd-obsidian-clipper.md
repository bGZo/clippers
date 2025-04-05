---
title: obsidianmd/obsidian-clipper
aliases:
  - obsidian-clipper
created: 2025-03-09T10:52:10
modified: 2025-04-05T11:23:07
description: Highlight and capture the web in your favorite browser. The official Web Clipper extension for Obsidian.
source: https://github.com/obsidianmd/obsidian-clipper
tags:
  - star
tags-link:
  - "[[obsidian]]"
type: repo
---

## Repo Meta

![](https://img.shields.io/github/stars/obsidianmd/obsidian-clipper?style=for-the-badge&label=stars) ![](https://img.shields.io/github/repo-size/obsidianmd/obsidian-clipper?style=for-the-badge&label=size) ![](https://img.shields.io/github/created-at/obsidianmd/obsidian-clipper?style=for-the-badge&label=since)

[![](https://github-readme-stats.vercel.app/api/pin/?username=obsidianmd&repo=obsidian-clipper&bg_color=00000000)](https://github.com/obsidianmd/obsidian-clipper)

## Template ^1f4ed6

### Webpages

```json
{
  "schemaVersion": "0.1.0",
  "name": "Webpage",
  "behavior": "create",
  "noteContentFormat": "{{content}}",
  "properties": [
    {
      "name": "title",
      "value": "{{title}}",
      "type": "text"
    },
    {
      "name": "aliases",
      "value": "{{title}}",
      "type": "text"
    },
    {
      "name": "created",
      "value": "{{date|date:YYYY-MM-DDTHH:mm:ss}}",
      "type": "datetime"
    },
    {
      "name": "modified",
      "value": "{{date|date:YYYY-MM-DDTHH:mm:ss}}",
      "type": "datetime"
    },
    {
      "name": "description",
      "value": "{{description}}",
      "type": "text"
    },
    {
      "name": "source",
      "value": "{{url}}",
      "type": "text"
    },
    {
      "name": "tags",
      "value": "",
      "type": "multitext"
    },
    {
      "name": "tags-link",
      "value": "",
      "type": "text"
    },
    {
      "name": "type",
      "value": "archive-web",
      "type": "text"
    }
  ],
  "triggers": [],
  "noteNameFormat": "~{{title|safe_name|replace:\"_哔哩哔哩_bilibili\":\"\"|replace:\"- 知乎\":\" \"|replace:\"「ONE · 一个」\":\" \"|replace:\" Linux区\":\" \"|replace:\"‘\":\" \"|replace:\"’\":\" \"|replace:\"；\":\" \"|replace:\"。\":\" \"|replace:\"…\":\" \"|replace:\"：\":\" \"|replace:\".\":\" \"|replace:\"？\":\" \"|replace:\"，\":\" \"|replace:\"！\":\" \"|replace:\"｜\":\" \"|replace:\"【\":\" \"|replace:\"】\":\" \"|replace:\"[\":\" \"|replace:\"]\":\" \"|replace:\"!\":\" \"|replace:\"“\":\" \"|replace:\"”\":\" \"|replace:\"《\":\" \"|replace:\"》\":\" \"|trim|replace:\"  \":\" \"|replace:\" \":\"-\"}}",
  "path": "archives/clip-webpages"
}
```

### Webpage: V2EX

```json
{
  "schemaVersion": "0.1.0",
  "name": "Webpage:V2EX",
  "behavior": "create",
  "noteContentFormat": "## Origin Content\n\n{{description}}\n\n## Comment\n\n{{content}}\n\n",
  "properties": [
    {
      "name": "title",
      "value": "{{meta:property:og:title}}",
      "type": "text"
    },
    {
      "name": "aliases",
      "value": "{{meta:property:og:title}}",
      "type": "text"
    },
    {
      "name": "created",
      "value": "{{date|date:YYYY-MM-DDTHH:mm:ss}}",
      "type": "datetime"
    },
    {
      "name": "modified",
      "value": "{{date|date:YYYY-MM-DDTHH:mm:ss}}",
      "type": "datetime"
    },
    {
      "name": "source",
      "value": "{{url}}",
      "type": "text"
    },
    {
      "name": "tags",
      "value": "",
      "type": "multitext"
    },
    {
      "name": "tags-link",
      "value": "",
      "type": "text"
    },
    {
      "name": "type",
      "value": "archive-web",
      "type": "text"
    }
  ],
  "triggers": [
    "/https:\\/\\/.*\\.v2ex\\.com/",
    "https://v2ex.com/",
    "https://origin.v2ex.com/"
  ],
  "noteNameFormat": "~{{meta:property:og:title|safe_name|replace:\"- V2EX\":\" \"|replace:\"‘\":\" \"|replace:\"’\":\" \"|replace:\"；\":\" \"|replace:\"。\":\" \"|replace:\"…\":\" \"|replace:\"：\":\" \"|replace:\".\":\" \"|replace:\"？\":\" \"|replace:\"，\":\" \"|replace:\"！\":\" \"|replace:\"｜\":\" \"|replace:\"【\":\" \"|replace:\"】\":\" \"|replace:\"[\":\" \"|replace:\"]\":\" \"|replace:\"!\":\" \"|replace:\"“\":\" \"|replace:\"”\":\" \"|replace:\"《\":\" \"|replace:\"》\":\" \"|trim|replace:\"  \":\" \"|replace:\" \":\"-\"}}",
  "path": "archives/clip-webpages"
}
```

### Github:repo

```json
{
  "schemaVersion": "0.1.0",
  "name": "Github:repo",
  "behavior": "create",
  "noteContentFormat": "## Repo Meta\n\n![](https://img.shields.io/github/stars/{{url|replace:'/.*github.com/([^&]+)/([^&]+).*/g':'$1/$2'}}?style=for-the-badge&label=stars) ![](https://img.shields.io/github/repo-size/{{url|replace:'/.*github.com/([^&]+)/([^&]+).*/g':'$1/$2'}}?style=for-the-badge&label=size) ![](https://img.shields.io/github/created-at/{{url|replace:'/.*github.com/([^&]+)/([^&]+).*/g':'$1/$2'}}?style=for-the-badge&label=since)\n\n[![](https://github-readme-stats.vercel.app/api/pin/?{{url|replace:'/.*github.com/([^&]+)/([^&]+).*/g':'username=$1&repo=$2'}}&bg_color=00000000)](https://github.com/{{url|replace:'/.*github.com/([^&]+)/([^&]+).*/g':'$1/$2'}})\n\n## Notes\n\n",
  "properties": [
    {
      "name": "title",
      "value": "{{url|replace:'/.*github.com/([^&]+)/([^&]+).*/g':'$1/$2'}}",
      "type": "text"
    },
    {
      "name": "aliases",
      "value": "{{url|replace:'/.*github.com/([^&]+)/([^&]+).*/g':'$2'}}",
      "type": "text"
    },
    {
      "name": "created",
      "value": "{{date|date:YYYY-MM-DDTHH:mm:ss}}",
      "type": "datetime"
    },
    {
      "name": "modified",
      "value": "{{date|date:YYYY-MM-DDTHH:mm:ss}}",
      "type": "datetime"
    },
    {
      "name": "description",
      "value": "{{title|replace:'/.*/.*\\: /g':''}}",
      "type": "text"
    },
    {
      "name": "source",
      "value": "{{url}}",
      "type": "text"
    },
    {
      "name": "tags",
      "value": "star",
      "type": "multitext"
    },
    {
      "name": "tags-link",
      "value": "",
      "type": "text"
    },
    {
      "name": "type",
      "value": "repo",
      "type": "text"
    }
  ],
  "triggers": [
    "https://github.com/"
  ],
  "noteNameFormat": "{{url|replace:'/.*github.com/([^&]+)/([^&]+).*/g':'$1-$2'}}",
  "path": "archives/clip-repo"
}
```

### Douban:movies

```json
{
  "schemaVersion": "0.1.0",
  "name": "Douban:movies",
  "behavior": "create",
  "noteContentFormat": "\n## Comments\n\n## References\n",
  "properties": [
    {
      "name": "title",
      "value": "{{schema:@Movie:name}}",
      "type": "text"
    },
    {
      "name": "cover",
      "value": "{{schema:@Movie:image}}",
      "type": "text"
    },
    {
      "name": "alias",
      "value": "{{schema:@Movie:name}}",
      "type": "text"
    },
    {
      "name": "author",
      "value": "{{author}}",
      "type": "multitext"
    },
    {
      "name": "created",
      "value": "{{date|date:YYYY-MM-DDTHH:mm:ss}}",
      "type": "datetime"
    },
    {
      "name": "modified",
      "value": "{{date|date:YYYY-MM-DDTHH:mm:ss}}",
      "type": "datetime"
    },
    {
      "name": "published",
      "value": "{{published}}",
      "type": "datetime"
    },
    {
      "name": "description",
      "value": "{{schema:@Movie:description}}",
      "type": "text"
    },
    {
      "name": "tags",
      "value": "douban",
      "type": "multitext"
    },
    {
      "name": "type",
      "value": "movie",
      "type": "text"
    },
    {
      "name": "douban",
      "value": "{{url}}",
      "type": "text"
    },
    {
      "name": "imdb",
      "value": "https://www.imdb.com/title/",
      "type": "text"
    }
  ],
  "triggers": [
    "https://movie.douban.com/subject/"
  ],
  "noteNameFormat": "~{{title|uncamel|safe_name|replace:\"_哔哩哔哩_bilibili\":\"\"|replace:\"-\":\" \"|replace:\"…\":\" \"|replace:\"：\":\" \"|replace:\".\":\" \"|replace:\"？\":\" \"|replace:\"，\":\" \"|replace:\"！\":\" \"|replace:\"｜\":\" \"|replace:\"【\":\" \"|replace:\"】\":\" \"|replace:\"[\":\" \"|replace:\"]\":\" \"|replace:\"!\":\" \"|replace:\"“\":\" \"|replace:\"”\":\" \"|replace:\"《\":\" \"|replace:\"》\":\" \"|trim|replace:\"/[ ]+/g\":\" \"|replace:\" \":\"-\"}}",
  "path": "archives/clip-douban"
}
```

### Douban:books

```json
{
  "schemaVersion": "0.1.0",
  "name": "Douban:books",
  "behavior": "create",
  "noteContentFormat": "\n## Comments\n\n\n\n## Contents\n\n\n\n## References\n\n\n",
  "properties": [
    {
      "name": "alias",
      "value": "{{title}}",
      "type": "text"
    },
    {
      "name": "title",
      "value": "{{title}}",
      "type": "text"
    },
    {
      "name": "author",
      "value": "{{author}}",
      "type": "multitext"
    },
    {
      "name": "created",
      "value": "{{date|date:YYYY-MM-DDTHH:mm:ss}}",
      "type": "datetime"
    },
    {
      "name": "modified",
      "value": "{{date|date:YYYY-MM-DDTHH:mm:ss}}",
      "type": "datetime"
    },
    {
      "name": "published",
      "value": "{{meta:name:keywords|replace:\\\"/.*?(\\d{4}.*?),.*/g\\\":\\\"$1\\\"}}",
      "type": "datetime"
    },
    {
      "name": "description",
      "value": "{{meta:property:og:description}}",
      "type": "text"
    },
    {
      "name": "cover",
      "value": "{{image}}",
      "type": "text"
    },
    {
      "name": "douban",
      "value": "{{url}}",
      "type": "text"
    },
    {
      "name": "isbn",
      "value": "{{schema:@Book:isbn}}",
      "type": "text"
    },
    {
      "name": "rating",
      "value": "⭐⭐⭐⭐⭐",
      "type": "text"
    },
    {
      "name": "status",
      "value": "book/reading",
      "type": "text"
    },
    {
      "name": "tags",
      "value": "douban",
      "type": "multitext"
    },
    {
      "name": "type",
      "value": "book",
      "type": "text"
    },
    {
      "name": "weread",
      "value": "https://weread.qq.com/web/bookDetail/",
      "type": "text"
    },
    {
      "name": "weread-link",
      "value": "",
      "type": "text"
    }
  ],
  "triggers": [
    "https://book.douban.com/subject/"
  ],
  "noteNameFormat": "~{{title|uncamel|safe_name|replace:\"_哔哩哔哩_bilibili\":\"\"|replace:\"-\":\" \"|replace:\"…\":\" \"|replace:\"：\":\" \"|replace:\".\":\" \"|replace:\"？\":\" \"|replace:\"，\":\" \"|replace:\"！\":\" \"|replace:\"｜\":\" \"|replace:\"【\":\" \"|replace:\"】\":\" \"|replace:\"[\":\" \"|replace:\"]\":\" \"|replace:\"!\":\" \"|replace:\"“\":\" \"|replace:\"”\":\" \"|replace:\"《\":\" \"|replace:\"》\":\" \"|trim|replace:\"/[ ]+/g\":\" \"|replace:\" \":\"-\"}}",
  "path": "archives/clip-books"
}
```

### Bilibili

```json
{
  "schemaVersion": "0.1.0",
  "name": "Bilibili",
  "behavior": "create",
  "noteContentFormat": "## Source\n\n<iframe src='https://player.bilibili.com/player.html?isOutside=true&bvid={{url|replace:'/.*video/([^&]+).*//g':'$1'}}&p=1&autoplay=false' style='height:40vh;width:100%' class='iframe-radius' allow='fullscreen'></iframe>\n<center>via: <a href='https://www.bilibili.com/video/{{url|replace:'/.*video/([^&]+).*//g':'$1'}}' target='_blank' class='external-link'>https://www.bilibili.com/video/{{url|replace:'/.*video/([^&]+).*//g':'$1'}}</a></center>\n\n\n## Notes\n\n",
  "properties": [
    {
      "name": "title",
      "value": "{{title|safe_name|replace:\\\"_哔哩哔哩_bilibili\\\":\\\"\\\"|replace:\\\"…\\\":\\\" \\\"|replace:\\\"：\\\":\\\" \\\"|replace:\\\".\\\":\\\" \\\"|replace:\\\"？\\\":\\\" \\\"|replace:\\\"，\\\":\\\" \\\"|replace:\\\"！\\\":\\\" \\\"|replace:\\\"｜\\\":\\\" \\\"|replace:\\\"【\\\":\\\" \\\"|replace:\\\"】\\\":\\\" \\\"|replace:\\\"[\\\":\\\" \\\"|replace:\\\"]\\\":\\\" \\\"|replace:\\\"!\\\":\\\" \\\"|replace:\\\"“\\\":\\\" \\\"|replace:\\\"”\\\":\\\" \\\"|replace:\\\"《\\\":\\\" \\\"|replace:\\\"》\\\":\\\" \\\"|trim|replace:\\\"  \\\":\\\" \\\"|replace:\\\" \\\":\\\"-\\\"}}",
      "type": "text"
    },
    {
      "name": "aliases",
      "value": "{{title|safe_name|replace:\\\"_哔哩哔哩_bilibili\\\":\\\"\\\"|replace:\\\"…\\\":\\\" \\\"|replace:\\\"：\\\":\\\" \\\"|replace:\\\".\\\":\\\" \\\"|replace:\\\"？\\\":\\\" \\\"|replace:\\\"，\\\":\\\" \\\"|replace:\\\"！\\\":\\\" \\\"|replace:\\\"｜\\\":\\\" \\\"|replace:\\\"【\\\":\\\" \\\"|replace:\\\"】\\\":\\\" \\\"|replace:\\\"[\\\":\\\" \\\"|replace:\\\"]\\\":\\\" \\\"|replace:\\\"!\\\":\\\" \\\"|replace:\\\"“\\\":\\\" \\\"|replace:\\\"”\\\":\\\" \\\"|replace:\\\"《\\\":\\\" \\\"|replace:\\\"》\\\":\\\" \\\"|trim|replace:\\\"  \\\":\\\" \\\"|replace:\\\" \\\":\\\"-\\\"}}",
      "type": "text"
    },
    {
      "name": "cover",
      "value": "{{schema:thumbnailUrl|slice:0}}",
      "type": "text"
    },
    {
      "name": "author",
      "value": "{{author}}",
      "type": "multitext"
    },
    {
      "name": "created",
      "value": "{{date|date:YYYY-MM-DDTHH:mm:ss}}",
      "type": "datetime"
    },
    {
      "name": "modified",
      "value": "{{date|date:YYYY-MM-DDTHH:mm:ss}}",
      "type": "datetime"
    },
    {
      "name": "published",
      "value": "{{schema:uploadDate|date:YYYY-MM-DDTHH:mm:ss}}",
      "type": "datetime"
    },
    {
      "name": "description",
      "value": "{{description|replace: \\\"/(.*), 视频播放量.*/g\\\":\\\"$1\\\"}}",
      "type": "text"
    },
    {
      "name": "source",
      "value": "{{url}}",
      "type": "text"
    },
    {
      "name": "tags",
      "value": "bilibili",
      "type": "multitext"
    },
    {
      "name": "tags-link",
      "value": "",
      "type": "text"
    },
    {
      "name": "type",
      "value": "video",
      "type": "text"
    }
  ],
  "triggers": [
    "https://www.bilibili.com/video/"
  ],
  "noteNameFormat": "~{{url|replace:'/.*video/(\\w+).*[/]*/g':'$1'}}-{{title|safe_name|replace:\"_哔哩哔哩_bilibili\":\"\"|replace:\"…\":\" \"|replace:\"：\":\" \"|replace:\".\":\" \"|replace:\"？\":\" \"|replace:\"，\":\" \"|replace:\"！\":\" \"|replace:\"｜\":\" \"|replace:\"【\":\" \"|replace:\"】\":\" \"|replace:\"[\":\" \"|replace:\"]\":\" \"|replace:\"!\":\" \"|replace:\"“\":\" \"|replace:\"”\":\" \"|replace:\"《\":\" \"|replace:\"》\":\" \"|trim|replace:\"  \":\" \"|replace:\" \":\"-\"}}",
  "path": "archives/clip-bilibili"
}
```

### YouTube

```json
{
  "schemaVersion": "0.1.0",
  "name": "YouTube",
  "behavior": "create",
  "noteContentFormat": "## Source\n\n<iframe src=\"https://www.youtube.com/embed/{{url|replace:'/.*v=([^&]+).*/g':'$1'}}\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\" referrerpolicy=\"strict-origin-when-cross-origin\" allowfullscreen></iframe>\n<center>via: <a href='https://www.youtube.com/watch?v={{url|replace:'/.*v=([^&]+).*/g':'$1'}}' target='_blank' class='external-link'>https://www.youtube.com/watch?v={{url|replace:'/.*v=([^&]+).*/g':'$1'}}</a></center>\n\n## Notes\n\n",
  "properties": [
    {
      "name": "title",
      "value": "{{schema:name|safe_name|replace:\\\"_哔哩哔哩_bilibili\\\":\\\"\\\"|replace:\\\"…\\\":\\\" \\\"|replace:\\\"：\\\":\\\" \\\"|replace:\\\".\\\":\\\" \\\"|replace:\\\"？\\\":\\\" \\\"|replace:\\\"，\\\":\\\" \\\"|replace:\\\"！\\\":\\\" \\\"|replace:\\\"｜\\\":\\\" \\\"|replace:\\\"【\\\":\\\" \\\"|replace:\\\"】\\\":\\\" \\\"|replace:\\\"[\\\":\\\" \\\"|replace:\\\"]\\\":\\\" \\\"|replace:\\\"!\\\":\\\" \\\"|replace:\\\"“\\\":\\\" \\\"|replace:\\\"”\\\":\\\" \\\"|replace:\\\"《\\\":\\\" \\\"|replace:\\\"》\\\":\\\" \\\"|trim|replace:\\\"  \\\":\\\" \\\"|replace:\\\" \\\":\\\"-\\\"}}",
      "type": "text"
    },
    {
      "name": "aliases",
      "value": "{{schema:name|safe_name|replace:\\\"_哔哩哔哩_bilibili\\\":\\\"\\\"|replace:\\\"…\\\":\\\" \\\"|replace:\\\"：\\\":\\\" \\\"|replace:\\\".\\\":\\\" \\\"|replace:\\\"？\\\":\\\" \\\"|replace:\\\"，\\\":\\\" \\\"|replace:\\\"！\\\":\\\" \\\"|replace:\\\"｜\\\":\\\" \\\"|replace:\\\"【\\\":\\\" \\\"|replace:\\\"】\\\":\\\" \\\"|replace:\\\"[\\\":\\\" \\\"|replace:\\\"]\\\":\\\" \\\"|replace:\\\"!\\\":\\\" \\\"|replace:\\\"“\\\":\\\" \\\"|replace:\\\"”\\\":\\\" \\\"|replace:\\\"《\\\":\\\" \\\"|replace:\\\"》\\\":\\\" \\\"|trim|replace:\\\"  \\\":\\\" \\\"|replace:\\\" \\\":\\\"-\\\"}}",
      "type": "text"
    },
    {
      "name": "cover",
      "value": "{{schema:thumbnailUrl|slice:0}}",
      "type": "text"
    },
    {
      "name": "author",
      "value": "{{schema:author}}",
      "type": "multitext"
    },
    {
      "name": "created",
      "value": "{{date|date:YYYY-MM-DDTHH:mm:ss}}",
      "type": "datetime"
    },
    {
      "name": "modified",
      "value": "{{date|date:YYYY-MM-DDTHH:mm:ss}}",
      "type": "datetime"
    },
    {
      "name": "published",
      "value": "{{schema:uploadDate|date:YYYY-MM-DDTHH:mm:ss}}",
      "type": "datetime"
    },
    {
      "name": "description",
      "value": "{{description}}",
      "type": "text"
    },
    {
      "name": "source",
      "value": "{{url}}",
      "type": "text"
    },
    {
      "name": "tags",
      "value": "youtube",
      "type": "multitext"
    },
    {
      "name": "tags-link",
      "value": "",
      "type": "text"
    },
    {
      "name": "type",
      "value": "video",
      "type": "text"
    }
  ],
  "triggers": [
    "https://www.youtube.com/watch?v="
  ],
  "noteNameFormat": "{{url|replace:'/.*v=([^&]+).*/g':'$1'}}-{{schema:name|safe_name|replace:\"_哔哩哔哩_bilibili\":\"\"|replace:\"…\":\" \"|replace:\"：\":\" \"|replace:\".\":\" \"|replace:\"？\":\" \"|replace:\"，\":\" \"|replace:\"！\":\" \"|replace:\"｜\":\" \"|replace:\"【\":\" \"|replace:\"】\":\" \"|replace:\"[\":\" \"|replace:\"]\":\" \"|replace:\"!\":\" \"|replace:\"“\":\" \"|replace:\"”\":\" \"|replace:\"《\":\" \"|replace:\"》\":\" \"|trim|replace:\"  \":\" \"|replace:\" \":\"-\"}}",
  "path": "archives/clip-youtube"
}
```

### Javlibary

```json
{
  "schemaVersion": "0.1.0",
  "name": "Javlibary",
  "behavior": "create",
  "noteContentFormat": "## Preview\n\n![Jav Cover](http:{{image}})\n\n![DMM Cover](https://pics.dmm.co.jp/mono/movie/adult/{{title|replace:'/(.*?) .*/g':'$1'|lower|replace:'-':''}}/{{title|replace:'/(.*?) .*/g':'$1'|lower|replace:'-':''}}pl.jpg)\n\n<iframe src='https://jable.tv/videos/{{title|replace:'/(.*?) .*/g':'$1'}}/' style='height:40vh;width:100%' class='iframe-radius' allow='fullscreen'></iframe>\n<center>via: <a href='https://jable.tv/videos/{{title|replace:'/(.*?) .*/g':'$1'}}/' target='_blank' class='external-link'>https://jable.tv/videos/{{title|replace:'/(.*?) .*/g':'$1'}}/</a></center>\n\n<iframe src='https://123av.com/zh/dm2/v/{{title|replace:'/(.*?) .*/g':'$1'}}/' style='height:40vh;width:100%' class='iframe-radius' allow='fullscreen'></iframe>\n<center>via: <a href='https://123av.com/zh/dm2/v/{{title|replace:'/(.*?) .*/g':'$1'}}/' target='_blank' class='external-link'>https://123av.com/zh/dm2/v/{{title|replace:'/(.*?) .*/g':'$1'}}/</a></center>\n\n## Notes\n\n",
  "properties": [
    {
      "name": "title",
      "value": "{{title|replace:' - JAVLibrary':''}}",
      "type": "text"
    },
    {
      "name": "cover",
      "value": "https://pics.dmm.co.jp/mono/movie/adult/{{title|replace:'/(.*?) .*/g':'$1'|lower|replace:'-':''}}/{{title|replace:'/(.*?) .*/g':'$1'|lower|replace:'-':''}}pl.jpg",
      "type": "text"
    },
    {
      "name": "author",
      "value": "{{title|replace:\\\"/.* (.*?) - JAVLibrary/g\\\":\\\"$1\\\"}}",
      "type": "multitext"
    },
    {
      "name": "created",
      "value": "{{date|date:YYYY-MM-DDTHH:mm:ss}}",
      "type": "datetime"
    },
    {
      "name": "modified",
      "value": "{{date|date:YYYY-MM-DDTHH:mm:ss}}",
      "type": "datetime"
    },
    {
      "name": "published",
      "value": "{{schema:uploadDate|date:YYYY-MM-DDTHH:mm:ss}}",
      "type": "datetime"
    },
    {
      "name": "description",
      "value": "",
      "type": "text"
    },
    {
      "name": "tags",
      "value": "NSFW",
      "type": "multitext"
    },
    {
      "name": "type",
      "value": "video",
      "type": "text"
    },
    {
      "name": "javlibrary",
      "value": "{{url}}",
      "type": "text"
    },
    {
      "name": "telegram",
      "value": "https://t.me/bgzosex/",
      "type": "text"
    }
  ],
  "triggers": [
    "https://www.javlibrary.com/"
  ],
  "noteNameFormat": "~{{title|replace:'/(.*?) .*/g':'$1'}}",
  "path": "archives/clip-javs"
}
```
