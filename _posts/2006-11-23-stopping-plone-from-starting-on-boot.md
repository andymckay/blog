---
layout: post
title: Stopping Plone from starting on boot
categories: General
old: 1875
blog: andy-mckay
---
I get annoyed by the Plone instance that installed using the OS X installer starting automatically. I'm now at the stage of having 5 Plone instances, 3 Zope versions and they all run ZEO which doesn't start up automatically, leaving Zope wedged. Fortunately I only restart the once a month or so when my MacBook freezes or the next BIOS patch comes in. It's fixed by removing: <em>/Library/StartupItems/Plone-2.5</em>. In fact I found a few other things in there I didn't want and removed too.