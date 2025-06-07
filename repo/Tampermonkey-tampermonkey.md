---
title: Tampermonkey/tampermonkey
aliases: tampermonkey
created: 2023-12-24T00:00:00
modified: 2025-06-07T16:13:09
description: Tampermonkey is the most popular userscript manager, with over 10 million users. It's available for Chrome, Microsoft Edge, Safari, Opera Next, and Firefox.
source: https://github.com/Tampermonkey/tampermonkey
tags:
  - star
tags-link: 
type: tool
document: 
status: tool/star
---

## Repo Meta

![](https://img.shields.io/github/stars/Tampermonkey/tampermonkey?style=for-the-badge&label=stars) ![](https://img.shields.io/github/repo-size/Tampermonkey/tampermonkey?style=for-the-badge&label=size) ![](https://img.shields.io/github/created-at/Tampermonkey/tampermonkey?style=for-the-badge&label=since)

[![](https://github-readme-stats.vercel.app/api/pin/?username=Tampermonkey&repo=tampermonkey&bg_color=00000000)](https://github.com/Tampermonkey/tampermonkey)

## Notes

  - [Documentation | Tampermonkey](https://www.tampermonkey.net/documentation.php)
    - 用户脚本标题
      - @name
      - @namespace
      - @copyright
      - @version
      - @description
      - @icon, @iconURL, @defaulticon
      - @icon64, @icon64URL
      - @grant
      - @author
      - @homepage, @homepageURL, @website, @source
      - @antifeature
      - @require
      - @resource
      - @include
      - @match
      - @exclude
      - @run-at
      - @sandbox
      - @connect
      - @noframes
      - @updateURL
      - @downloadURL
      - @supportURL
      - @webRequest
      - @unwrap
    - 应用程序接口
      - unsafeWindow
      - Subresource Integrity
      - GM_addElement(tag_name, attributes), GM_addElement(parent_node, tag_name, attributes)
      - GM_addStyle(css)
      - GM_download(details), GM_download(url, name)
      - GM_getResourceText(name)
      - GM_getResourceURL(name)
      - GM_info
      - GM_log(message)
      - GM_notification(details, ondone), GM_notification(text, title, image, onclick)
      - GM_openInTab(url, options), GM_openInTab(url, loadInBackground)
      - GM_registerMenuCommand(name, callback, accessKey)
      - GM_unregisterMenuCommand(menuCmdId)
      - GM_setClipboard(data, info)
      - GM_getTab(callback)
      - GM_saveTab(tab)
      - GM_getTabs(callback)
      - GM_setValue(key, value)
      - GM_getValue(key, defaultValue)
      - GM_deleteValue(key)
      - GM_listValues()
      - GM_addValueChangeListener(key, (key, old_value, new_value, remote) => void)
      - GM_removeValueChangeListener(listenerId)
      - GM_xmlhttpRequest(details)
      - GM_webRequest(rules, listener)
      - GM_cookie.list(details[, callback])
      - GM_cookie.set(details[, callback])
      - GM_cookie.delete(details, callback)
      - window.onurlchange
      - window.close
      - window.focus
      - <><![CDATA[...]]></>
