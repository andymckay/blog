---
layout: post
title: A WebExtensions scratch pad
categories: General
blog: andy-mckay
---

<a href="https://github.com/andymckay/every-event">Every Event</a> is a daft little WebExtension I wrote a while ago to try and capture the events that WebExtensions APIs fires. It tries to listen to every possible event that is generated. I've found this pretty useful in past for asking questions like "What tab events fire when I move tabs between windows?" or "What events fire when I bookmark something?".

To use Every Event, <a href="https://addons.mozilla.org/en-US/firefox/addon/every-event/">install it from addons.mozilla.org</a>. To open, click the alarm icon on the menu bar.

<img src="/files/web-ext-events.png">

If you turn on every event for everything, you get an awful lot of traffic to the console. You might want to limit that down. So to test what happens when you bookmark something, click "All off", then click "bookmarks". Then click "Turn on". Then open the "Browser Console".

Each time you bookmark something, you'll see the event and the contents of the API as shown below:

<img src="/files/web-ext-bookmark-event.png">

That's also thanks to the Firefox Developer Tools which are great for inspecting objects.

But there's one other advantage to having Every Event around. Because it requests every single permission, it has access to every API. So that means if you go to *about:debugging* and then click on *Debug* for Every Event, you can play around with all the APIs and get nice autocomplete:

<img src="/files/web-ext-auto-complete-one.png">

All you have to do is enter "browser." at the browser console and there's all the WebExtension APIs autocompletable.

Let's add in our own custom handler for *browser.bookmarks.onRemoved.addListener* and see what happens when I remove a bookmark...

<img src="/files/web-ext-auto-complete-two.png">

Finally, I keep a checkout of Every Event near by on all my machines. All I have to do is enter the Every Event directory and start <a href="https://developer.mozilla.org/en-US/Add-ons/WebExtensions/Getting_started_with_web-ext">web-ext</a>:

   <pre>web-ext run --firefox /Applications/FirefoxNightly.app/Contents/MacOS/firefox --verbose --start-url about:debugging</pre>

That's aliased to a nice short command on my Mac and gives me a clean profile with the relevant console *just one click away*...
