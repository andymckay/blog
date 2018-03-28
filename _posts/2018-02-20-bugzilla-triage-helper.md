---
layout: post
title: Bugzilla Triage Helper
categories: General
blog: andy-mckay
---

In the process of shipping Firefox 57, we found a couple of things out about bugs and Bugzilla. 

<img src="https://addons.cdn.mozilla.net/user-media/previews/full/197/197451.png?modified=1518215572" style="float:right"> 

There are an awful lot of bugs filed against Firefox and all it's components in the course of a release. Keeping on top of that is hard and some teams have adopted some policies to help with that (for example see: design-decision-needed).

Having a consistent approach to bugs across the organisation makes it a little easier for everyone to get a feel for what's going. 

Sometimes the burden of setting all the right values can be tiring and prone to error. For example: setting a bug to P1 could involve the following:

* changing the priority
* setting the right flag for Firefox version
* changing the status
* turning off the cc flag
* setting a whiteboard value

In Austin, we had a chat about this and it was suggested we make a tool to provide a consistent approach to this. A few weeks later I threw Bugzilla Triage Helper onto [Github](https://github.com/andymckay/bugzilla-triage-helper) and [addons.mozilla.org](https://addons.mozilla.org/en-US/firefox/addon/bugzilla-triage-helper/). This tool is a content script that inserts an overlay onto Bugzilla.

This gives you a simple button (or keyboard shortcut) that does all of the above. It will even submit the bug for you so you can get on to the next bug.

Of course, it turns out that everyone's workflow is slightly different. So I recently added the ability to add "additional" actions. These are dynamically looked by the product and component. They are specified in JS in the repo, so triage owners who want a slightly different wrinkle on the flow can alter that on github.

Some examples: 

* one team sets a blocking bug number of each bug that blocks release, so they've extended P1 to do that.
* one team has 5 or 6 common replies asking for more information and informing the user on how to get that information. So they've extended the "Canned" response option to select those.

The extension is a content script that alters the DOM, which means its full of icky DOM code to manipulate the UI. I could do this through the API, but there's a couple of reasons I do it in the UI:

* I really don't want to build a new UI to Bugzilla
* most people triaging are looking at the bug in the UI
* a user might want to add more to the bug not captured in the tool in ad hoc process
* Bugzilla has lots of things like mid-air collision detection, recursive blocking and so on that are surfaced in the UI
* see the first point again

At this point I'm starting to use it in some triages and I hope others will too and give me some feedback or even better some patches.