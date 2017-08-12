---
layout: post
title: The beginning of the next chapter
categories: Mozilla
blog: andy-mckay
---

This week we limited Firefox Nightly so that by default legacy extensions won't run.

Over the next two releases, this limit will occur on Firefox Beta and then finally Firefox release 57, which goes to the public in November.

It represents a huge amount of work from the last two years by a dedicated team at Mozilla. It's not been an easy journey, we know it's a controversial decision that upset people. Some of those people have voiced their opposition again and again in mailing lists, email and other channels.

Since WebExtensions started we've:

* fixed <a href="https://bugzilla.mozilla.org/buglist.cgi?bug_status=RESOLVED&bug_status=VERIFIED&bug_status=CLOSED&component=WebExtensions%3A%20Android&component=WebExtensions%3A%20Compatibility&component=WebExtensions%3A%20Developer%20Tools&component=WebExtensions%3A%20Experiments&component=WebExtensions%3A%20Frontend&component=WebExtensions%3A%20General&component=WebExtensions%3A%20Request%20Handling&component=WebExtensions%3A%20Untriaged&list_id=13723645&product=Toolkit&query_format=advanced&resolution=FIXED&order=assigned_to%20DESC%2Cbug_status%2Cpriority%2Cbug_id&limit=0">1,083 bugs</a> in Bugzilla
* triaged a further <a href="https://bugzilla.mozilla.org/buglist.cgi?component=WebExtensions%3A%20Android&component=WebExtensions%3A%20Compatibility&component=WebExtensions%3A%20Developer%20Tools&component=WebExtensions%3A%20Experiments&component=WebExtensions%3A%20Frontend&component=WebExtensions%3A%20General&component=WebExtensions%3A%20Request%20Handling&component=WebExtensions%3A%20Untriaged&list_id=13723650&product=Toolkit&query_format=advanced&order=assigned_to%20DESC%2Cbug_status%2Cpriority%2Cbug_id&limit=0">3,086 bugs</a> in Bugzilla
* fixed <a href="https://github.com/mozilla/addons-server/issues">3,688 issues</a> on Github [<a href="https://github.com/mozilla/addons-server/issues">1</a>, <a href="https://github.com/mozilla/addons-linter/issues">2</a>, <a href="https://github.com/mozilla/web-ext/issues">3</a>, <a href="https://github.com/mozilla/addons-frontend/issues">4</a>]
* written over <a href="https://developer.mozilla.org/en-US/Add-ons/WebExtensions">200 documentation pages</a>
* participated in <a href="https://browserext.github.io/browserext/">one standard</a>
* helped shepherd add-ons through Firefox going to more than <a href="https://wiki.mozilla.org/Electrolysis">one process</a> to multiple processes
* completely <a href="https://github.com/mozilla/web-ext">rewritten the command line tools</a> and provided some kick-ass APIs
* re-written the validator for add-ons into JavaScript and its now mirroring the rules from Firefox
* written 11 blog posts(<a href="<a href="https://blog.mozilla.org/addons/2015/12/21/webextensions-in-firefox-45-2/">Firefox 45</a> to <a href="https://blog.mozilla.org/addons/2017/08/10/webextensions-firefox-56/">Firefox 56</a>) on WebExtensions status
* built 2 new services to assist in add-on development
* done 3 work weeks
* worked with a bunch of awesome contributors

... there's a ton of things I've missed, apologies to everyone. And <b>we aren't done</b>, we've got 6 weeks till the cut off for 57 and then another month or two as it rolls out to release.

What's more important is the possibilities for the future, this:

* releases the shackles around Firefox developers that extensions caused
* improves the security and performance for our users
* allows add-on developers to develop faster and easier than ever before
* everyone can be more confident that things don't break every release

This is the beginning of the next chapters for extensions and Firefox. Exciting times.
