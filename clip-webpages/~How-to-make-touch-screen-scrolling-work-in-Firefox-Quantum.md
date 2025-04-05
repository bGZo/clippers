---
title: "How to make touch-screen scrolling work in Firefox Quantum?"
created: 2025-04-05T17:31:16
modified: 2025-04-05T17:31:16
description: "Using Firefox quantum 57 and Ubuntu 17.10, I am unable to scroll a web page by touching the screen and sliding the page.  However this works in Chrome browser.How to make touch-screen scrolling w..."
source: "https://askubuntu.com/questions/978226/how-to-make-touch-screen-scrolling-work-in-firefox-quantum"
tags:
tags-link:
type: "archive-web"
---
The same solution for Firefox 50 and Ubuntu 16.xx still works for Firefox Quantum 57 and Ubuntu 17.10: [Ubuntu 16 and touchscreen scrolling in FireFox](https://askubuntu.com/questions/853910/ubuntu-16-and-touchscreen-scrolling-in-firefox)

The solution is to launch firefox using:

```
env MOZ_USE_XINPUT2=1 firefox
```

You can make this permanent by modifying the launcher using the following:

```
sudo sed -i "s|Exec=|Exec=env MOZ_USE_XINPUT2=1 |g" /usr/share/applications/firefox.desktop
```

To undo this change, use:

```
sudo sed -i "s|Exec=env MOZ_USE_XINPUT2=1 |Exec=|g" /usr/share/applications/firefox.desktop
```

EDIT: Per @poomerang's comment below, if you are using the Snap version of Firefox, the path in the above commands should be `/var/lib/snapd/desktop/applications/firefox_firefox.desktop`

Comparing touch scrolling in Firefox Quantum, using this solution. with touch scrolling in Chrome:

- Scrolling is one finger only; two finger scrolling causes the web page to zoom. This is different from Chrome, where you can scroll using two fingers, but still pinch to zoom or un-zoom.
- You can only scroll vertically or horizontally, depending on which direction your initial motion is in; this is different from Chrome, where you can scroll horizontally or vertically (or in circles) without lifting your finger(s).