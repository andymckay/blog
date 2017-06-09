---
layout: post
title: Running WebExtensions only
categories: Mozilla
blog: andy-mckay
---

I've decided in the last few days that its time to move my extensions in Firefox to be WebExtensions only. For about a year I've been running a combination of some legacy extensions and some WebExtensions. Now its time for me to go WebExtensions only.

My needs for must have Extensions are actually pretty small:

* <a href="https://addons.mozilla.org/en-US/firefox/addons/triage-with-me">Triage with me</a> is used to run triages at Mozilla.
* The <a href="https://addons.mozilla.org/en-US/firefox/addon/show-labels-on-trello/">Trello categories</a> content script makes trello usable for me.
* Tabs on the side.
* A good ad-blocker.

Those last two just became possible. For tabs on the side I wrote <a href="http://github.com/andymckay/sidebar-tabs">sidebar tabs</a> once the <a href="https://bugzilla.mozilla.org/show_bug.cgi?id=1208596">sidebar API</a> landed. I'll write a more detailed blog post on that extension, it's in flux, I'm playing around with it and mostly using it for dogfood at the moment.

<img src="http://mckay.pub/files/sidebar-tabs.png" height="400">

The more observant of you will notice that it still has tabs across the top. Currently we <a href="https://bugzilla.mozilla.org/show_bug.cgi?id=1332447">can't hide those</a>.

I've used uBlock Origin for a while and with the landing of the <a href="https://bugzilla.mozilla.org/show_bug.cgi?id=1312802">privacy API</a> and <a href="https://bugzilla.mozilla.org/show_bug.cgi?id=1190687">webNavigation.onCreatedTarget</a>, we can now run uBlock Origin. Actually its been working for a while, but these are the last big bugs on it. The uBlock developers having been putting out WebExtensions builds for a <a href="https://bugzilla.mozilla.org/show_bug.cgi?id=1309926#c5">while now</a> and <a href="https://github.com/gorhill/uBlock/releases">you can get them on github</a>.

These last two add-ons aren't signed, so I'm running them in Nightly where I've turned <a href="https://wiki.mozilla.org/Add-ons/Extension_Signing">signing off</a> in Firefox.

This means I've now got <a href="https://wiki.mozilla.org/Electrolysis">multi process Firefox</a> running and will benefit once extensions also start using their <a href="https://wiki.mozilla.org/WebExtensions/Implementing_APIs_out-of-process">own process</a>. Having this setup is a couple of releases out for some people, but enables me to dogfood WebExtensions and provide some feedback.
