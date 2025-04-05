---
title: "How does .desktop file EXEC field work?"
created: 2025-04-05T16:37:03
modified: 2025-04-05T16:37:03
description: "It's been several months I'm having this horrible problem. I'm currently using Unity 2D, and I manage my menu entries by using .desktop files, which is tiring. Is there a better way to manage them?"
source: "https://askubuntu.com/questions/174968/how-does-desktop-file-exec-field-work"
tags:
tags-link:
type: "archive-web"
---
If you use shell features you need to use `sh -c "the command"`. Also, with Wine you need to set the current directory for some stuff. `man wine`