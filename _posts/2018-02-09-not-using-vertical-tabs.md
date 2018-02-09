---
layout: post
title: Alternatives to vertical tabs
categories: General
blog: andy-mckay
---

For the longest time I've used vertical tabs in Firefox and I still find it odd that people don't use it more. It's a simple fact that a horizontal tab strip doesn't scale too well when you get lots of tabs.

Of course, for most users this isn't a problem, most users do not have a lot of tabs open according to [Firefox telemetry](https://telemetry.mozilla.org/new-pipeline/dist.html#!cumulative=0&end_date=2018-02-08&keys=__none__!__none__!__none__&max_channel_version=nightly%252F60&measure=TAB_COUNT&min_channel_version=null&processType=*&product=Firefox&sanitize=1&sort_keys=submissions&start_date=2018-01-22&table=0&trim=1&use_submission_date=0):

<a href="https://telemetry.mozilla.org/new-pipeline/dist.html#!cumulative=0&end_date=2018-02-08&keys=__none__!__none__!__none__&max_channel_version=nightly%252F60&measure=TAB_COUNT&min_channel_version=null&processType=*&product=Firefox&sanitize=1&sort_keys=submissions&start_date=2018-01-22&table=0&trim=1&use_submission_date=0"><img src="/files/tab-count.png"></a>

But if you have a few the title just gets squished and squished till it becomes a scroll bar. Vertical tabs look great for this giving you lots of title space on a wide monitor:

<img src="/files/tab-list-vertical.png">

Firefox is *way better* at this than Chrome. I sat next to someone who had nothing but triangles as their tab bar in Chrome. How did they cope?

<img src="/files/tab-chrome.png">

With the landing of the tab hiding API in WebExtensions in Firefox 59, I wanted to try and understand what the many people who were clamouring for this API wanted to do. So I wrote a [quick extension that's pretty terrible](https://addons.mozilla.org/en-US/firefox/addon/tab-hider/). It provided a "Hide this tab" context menu item on the tab to hide the tab. I then through together a quick management page to list all the hidden pages.

<img src="/files/tab-hidden-list.png">

That was ok, but clicking that menu item was tedious. So then I set it to just perform some actions for me. I've now got it set up to *hide* a tab if it hasn't been looked it for an hour. Then five hours after that, if I haven't opened it again, the extension just closes the tab.

I tried that for a week and found it pretty useful. Tabs that are hidden still show up in the awesome bar and as soon as I click on them, they come back instantly. Eventually they'll get closed and are still in the awesome bar and I can bring them back, just in a slower manner.

If I find myself saying "where was that tab..." I just go to the management view and its got all the ones there.

This extension isn't perfect, but its enabled me to stop using vertical tabs most of the time and now I'm torn which workflow is better. Maybe some combination.

