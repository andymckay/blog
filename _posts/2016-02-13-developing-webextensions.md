---
layout: post
title: Writing a WebExtension
categories: General
blog: andy-mckay
---

Yesterday I spent 10 minutes throwing together an example WebExtension to show how a few APIs worked. It's not a complicated or sophisticated one by any means, it just shows a pop-up and links to trigger some tab APIs.

<img src="http://www.mckay.pub/files/tabs-tabs-tabs.png">

But when writing an add-on like that, you might notice a few things:

* Thanks to <a href="https://blog.mozilla.org/addons/2015/12/23/loading-temporary-add-ons/">about:debugging</a> you can load the add-on straight from the directory and run it. There is no xpi, zip or compile step. It just works.

* The menu is a html page with some JavaScript on it. That's familiar territory for anyone web developer.

* The HTML and Javascript *reload* each time I make a change. That's refreshingly simple and easy to develop with.

Those factors alone make developing that add-on so much easier than before. We are getting there.
