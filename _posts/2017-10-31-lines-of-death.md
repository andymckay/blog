---
layout: post
title: Lines of death in Firefox
categories: General
blog: andy-mckay
---

There is an interesting blog post about the <a href="https://textslashplain.com/2017/01/14/the-line-of-death/">"line of death" and Chrome</a>. It refers to the area of a browser that a user can "trust". There are some parts of the browser that a user can trust because they come from a browser. The rest comes from the content and has a different level of trust. This blog post is musing about this with extensions.

That's why in Firefox popups that are part of the browser overlap into the "trusted" area. The trusted area is above the dotted line:

<image src="/files/line-of-death/line.png" style="width: 600px">

Examples of prompts that cross the line are things like permission prompts or in this case an add-on installation prompt. That cannot be faked by a web site because the page cannot reach outside its content area. That little chevron (shown below) is the difference between what a web site can do and what a browser can do:

<image src="/files/line-of-death/chevron.png" style="width: 600px">

At this point the concerns are similar to the <a href="ttps://textslashplain.com/2017/01/14/the-line-of-death/">other blog post</a>. Except along come extensions. As an aside, please note I'm talking about WebExtensions in Firefox, legacy extensions could do *almost anything* and that is a problem.

Here's a screenshot of some of the things that an extension can do.

<image src="/files/line-of-death/html-area.png" style="width: 600px">

We can set a pop-up button that crosses the browser and content area (this example is a <a href="https://developer.mozilla.org/en-US/Add-ons/WebExtensions/API/browserAction">browserAction</a>, a <a href="https://developer.mozilla.org/en-US/Add-ons/WebExtensions/API/pageAction">pageAction</a> is also available). An extension can specify certain <a href="https://developer.mozilla.org/en-US/Add-ons/WebExtensions/API/menus">context menu items</a> in certain contexts. It can specify some HTML for a <a href="https://developer.mozilla.org/en-US/Add-ons/WebExtensions/API/sidebarAction">sidebar</a> and HTML in the dev tools (<a href="https://developer.mozilla.org/en-US/Add-ons/WebExtensions/API/devtools.panels">panels</a> can also be specified). You'll note a few things about these elements:

* the contents of the elements can be HTML only
* they can't overflow their alloted area
* there is a visual convention tying the element back to the add-on (the header in the sidebar, the browserAction icon etc)

An extension can change the content area, because they can use content scripts to alter the content and that's an interesting problem then of how much a user can trust the content area. However, users have to give explicit permission to a content script being run on a domain. As an aside, perhaps we should warn users when they visit that domain later?

There are other cases, for example you can't change the awesome bar but you can insert entries into the results:

<image src="/files/line-of-death/omnibox-api.png" style="width: 600px">

Some APIs do not have clear user interface implications such as the <a href="https://developer.mozilla.org/en-US/Add-ons/WebExtensions/API/webRequest">webRequest</a> API, these are not covered in this post.

That's where we are now (October 2017) and there's some things that we hope a user can trust as part of the browser. They can trust some parts of the browser: for example the URL bar can't be edited, the SSL icon and info cannot be edited.

In the old days on legacy extensions, because an extension could change any part of the browser, there's only a limited amount that a user could trust part of the UI. It could be Firefox, it could have been an extension [<a href="#footnote">footnote</a>].

Now we've got a new start with extensions, I think its time to think clearly about what extensions should be able to do and how trust with the user can be maintained. For example what do we do when:

* an extension alters part of the browser that isn't obviously extension or content related?
* what does it look like when an extension insert browser elements over content areas?

Maintaining a level of simplicity, understanding and security for the users is something we can't ignore.

<hr class="florished">

<a id="footnote">§</a> If your answer is "the extension is part of the browser" and "its the users responsibility to understand all the code in an extension before installing" that you go and have a hard think about what a web browser is, who uses it and what could wrong. And <a href="/2017-07-11-manual-review/">no manual code review</a> is not the answer.
