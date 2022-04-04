---
layout: post
title: Triage with me update
categories: Mozilla
blog: andy-mckay
---

<a href="https://mckay.pub/2013-09-06-triage/">Triage with me</a> is a tool I wrote a while ago at Mozilla. Mostly when Bugzilla bug numbers rolled over to 7 digits and reading out bug numbers in a meeting became just ridiculous.

As a person leading the triage, as you click on bug links, they are sent to a server and then to every person watching the triage page. All you do is turn on the add-on and continue as usual. Over the past year or so I've found triage with me an invaluable tool and find triages without it really, really hard to do.

This release adds in a few updates:

* bugzilla.mozilla.org and github.com URLs are now covered
* it differentiates between a bugzilla bug, a github pull request and a github issue
* you can choose the destination server in addon settings, which means that you can stand up your own server
* people in the triage get a notification on each URL
* the toggle triaging menu item actually shows a check mark when its enabled (yay)

<img src="/files/triage-with-me-0.3.1.png">

As it turned out, monitoring github URLs was hard because it doesn't do page loads for every page, instead using push state to alter the state of the page. That means the tabs <a href="https://developer.mozilla.org/en-US/Add-ons/SDK/High-Level_APIs/tabs">SDK</a> doesn't quite work. I tried <a href="https://twitter.com/andymckay/status/574108927853400064">several work arounds</a>, in the end settling for just a <a href="https://developer.mozilla.org/en-US/Add-ons/SDK/High-Level_APIs/timers">setInterval</a> and watching for URL changes. Its crude and some titles are going in wrong. Hope to fix those bugs soon.

Version <a href="/files/triage-with-me-0.3.1.xpi">0.3.1 is now available</a> or <a href="https://addons.mozilla.org/en-US/firefox/addon/triage-with-me/">AMO</a>.

