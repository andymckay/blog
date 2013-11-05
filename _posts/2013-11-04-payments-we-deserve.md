---
layout: post
title: Payments the world needs
categories: Mozilla
blog: andy-mckay
---

At the about this time last year we started working on payments for the Firefox Marketplace. For a long time we focused on how that would work with all the privacy, security, identity and integration issues. When the Firefox OS phones came out this year payments rolled out with them.

For us on the payments team its time to take a look around and see where things are going and its clear to me that there's one thing we need to do more. **Make payments on the web better**. We tried to do this at the same time as the marketplace, but the need to support Firefox OS overrode all the other stuff.

Mozilla has a unique position in the payments space. Raising money through a payment system is not our goal. Creating user or developer lock in is not our goal. We don't need to propose or promote one system for monetary gain. We can focus on security and privacy for users and developers.

Payments already work on the web, so what can we improve? Here's some ideas:

* *Choice*: do users want the ability to pay with any payment provider quickly and easily? Would this increase purchasing on the web?

* *Security*: can we enhance security beyond SSL? Can we provide some measure of trust about the person paying or the person receiving payment. Perhaps some vendors are more trustworthy than others. Perhaps APIs can be given that mark certain interactions as more trustworthy than others (the <a href="https://bugzilla.mozilla.org/show_bug.cgi?id=794999">Trusted UI</a> is an example of that).

* *Device APIs*: there's some proposals to give support for particular APIs that payments needs to communicate with the device. For example to perform carrier billing, the phone needs access to the device <a href="https://bugzilla.mozilla.org/show_bug.cgi?id=794999">MCC and MNC</a> info. Web APIs to give access to NFC would also help.

* *Data*: entering all your billing and shipping information over and over boring? How about all that credit card information? Would it be possible for the browser to store that in a manner that is secure and protects privacy, maybe <a href="http://www.chromium.org/developers/using-requestautocomplete">requestAutocomplete</a>?

* *Privacy*: is there a need to actually give all your personal information to a vendor. Could the client act as a broker to prevent the passing of personal information?

* *Transparency*: can there be an improvement in the transparency of where your personal information is going, how the payment is going to be split up and what happens afterwards in terms of refunds?

* *Alternatives*: there's a lot of alternative payment systems outside of Western economies that are used by millions of people all the time (for example <a href="http://en.wikipedia.org/wiki/M-Pesa">M-Pesa</a>), can we do anything to help and support those?

There's lots of opportunities here. But it's important to mention some things that we shouldn't be setting up a payment processing system or some form of a bank. Rather we should be doing our best to work with other companies. Doing so is not our area of expertise, puts in competition with people we should be working with and changes the nature of our relationship. Let's use the unique position that Mozilla entertains in this market and help make it better for everyone.

So what is next? I think there is an opportunity to start an informal working group at Mozilla and start collecting ideas and form a set of real goals. At this point I'm really looking for feedback at Mozilla about this idea. Should we pursue this? What things could we improve? Drop me a line and let me know, or write on your blog.

I think we have a chance to make <a href="https://air.mozilla.org/nature-of-mozilla/">payments system the world needs</a>.
