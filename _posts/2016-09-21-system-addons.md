---
layout: post
title: System Add-ons
categories: General
blog: andy-mckay
---

System add-ons are a new kind of add-on in Firefox, you might also know them as <a href="https://wiki.mozilla.org/Firefox/Go_Faster">Go Faster add-ons</a>.

These are interesting add-ons, they allow Firefox developers to ship code faster by writing the code in an add-on and then allow that to be developed and shipped independently of the main Firefox code.

Mostly these are not using <a href="https://wiki.mozilla.org/WebExtensions">WebExtensions</a> and there is some questions if they should. I've been thinking about this one for a while and here are my thoughts at the moment - they aren't more than thoughts at this time.

System add-ons are really "internal" pieces of code that would otherwise be shipped in mozilla-central, blessed by the module owner and generally approved. They are maintained by someone who is active involved in their code (usually but not always a Mozilla employee). They have gone through security and privacy reviews. They are tested against Firefox code in the test infrastructure on each release. They sometimes do things that no other add-on should be allowed to do.

This is all in contrast to third party add-ons that you'll find on AMO. When you look through all the reasoning behind WebExtensions, you'll find that a lot of the reasons involve things like "hard to maintain", "security problems" and so on. Please see my <a href="https://mckay.pub/2016-04-17-addons-old/">earlier posts for more on this</a>. I would say that these reasons don't apply to system add-ons.

So do system add-ons need to be WebExtensions? Maybe they don't. In fact I think if we try and push them into being system add-ons we'll create a scenario where WebExtensions become the blocker. 

System add-ons will want to do things that don't exist, so APIs will need to be added to WebExtensions. Some of the things that system add-ons will want to do are things that third party add-ons should not be allowed to do. Then we need to add in another permissions layer to say some add-on developers can use those APIs and others can't. 

Already there is a distinction between what can and cannot land in Firefox and that's made by the module owners and people who work on Firefox. 

If a system add-on does something unusual, do you end up in a scenario where you write a WebExtension API that only one add-on uses? The maintenance burden of creating an API for one part of Firefox that only one add-on can use doesn't seem worth it. It also makes WebExtensions the blocker and slows system add-on development down.

It feels to me like there isn't a compelling reason to make system add-ons to be WebExtensions. Instead we should encourage them to be so if it makes sense and let them be regular bootstrapped add-ons otherwise.
