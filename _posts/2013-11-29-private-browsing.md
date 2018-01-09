---
layout: post
title: Default private browsing
categories: Mozilla
blog: andy-mckay
---

Yesterday I found that Firefox was behaving oddly. Sites were behaving oddly, as if the cookies weren't being passed correcly to sites, repeatedly. On reloading old tabs weren't loading. When trying to go into private browsing mode, there was no purple indicator in the top right.

Going to the File menu I noticed that the private browsing link key shortcut had changed to ⌘N instead of shift-⌘P.

<img src="/files/private-before.png">

But that shortcut still worked and seemed to open new non-private windows.

<img src="/files/private-after.png">

What was going on? I tried removing add-ons, cleaning out jetpacks and anything I could change. Finally I went to <code>about:config</code> and searched for "private" and then found this setting:

<pre>browser.privatebrowsing.autostart</pre>

...was set to <code>true</code>. When this is set, all windows and new windows are in private browsing mode. But with no notification or warning of that.

Changed that back to <code>false</code> and it was all good. I'm not sure what toggled that but being able to have normal browsing and private browsing meant I could go back to running my two Google accounts at once, get past newspaper pay-walls and easily test my sites.

I was tempted to file a bug about this, but then realised this was probably all intended. But here's a post that the search engines can find for the future.
