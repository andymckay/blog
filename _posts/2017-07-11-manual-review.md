---
layout: post
title: Manual review of add-ons
categories: Mozilla
blog: andy-mckay
---

As we start to expand WebExtension APIs beyond parity with Chrome, a common theme is appearing in bug comments when proposing new APIs. When an API violates reasonable security, privacy or performance concerns, then usually someone will say "we'll have to give add-ons using that API a special manual review".

Put simply, that's not happening. We should be doing anything we can to avoid manual review process for specific WebExtension APIs.

Manual review has quite a few problems but simply, it costs Mozillians resources and upsets developers.

On the cost side, we've had to put an awful lot of developer and reviewer (both paid and volunteer) time into reviewing extensions. There are tools and sites supported by Mozilla to support the review process.

But more than that, loud and clear developers have told us they dislike the review process and complain about it. It causes delays and developers get upset when people (many of whom are volunteer) aren't able to turn around reviews within reasonable time scales.

Further, this makes it harder for developers because it forces developers to upload unobfuscated sources. Something that its getting harder and harder as webpack, browserify and other tools gain in popularity.

And finally manual review isn't perfect. It's hard to review code, look for all the possible security and policy problems and ensure that the question API didn't do something we felt uncomfortable with.

Manual review has its place in Mozilla, but one thing we shouldn't be do is placing more burdens on the process. We should be aiming to streamline review and ease the burden on reviewers and developers.

The result is we've got to either deny the API or find a way to make the API work within reasonable security, privacy or performance guidelines.
