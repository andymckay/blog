---
layout: post
title: Manual review of add-ons
categories: Mozilla
blog: andy-mckay
---

As we start to expand WebExtension APIs beyond parity with Chrome, a common theme is appearing in bug comments when proposing new APIs. That theme is something like "we'll have to give add-ons using that API a special manual review".

Put simply, that's not happening. Either we feel comfortable with an API and everyone can use it, or we don't implement it. There won't be any special manual review process for WebExtensions for specific APIs.

Manual review has quite a few problems but bluntly, it costs Mozillians resources and time and upsets developers.

On the cost side, we've had to put an awful lot of developer and reviewer (both paid and volunteer) time into reviewing extensions. There's tools and sites supported by Mozilla to support the review process.

But more than that, loud and clear developers have told us they dislike the review process and complain about it. It causes delays and developers get upset when people (many of whom are volunteer) aren't able to turn around reviews within reasonable time scales.

Further, this makes it harder for developers because it forces developers to upload unobfuscated sources. Something that its getting harder and harder as webpack, browserify and other tools gain in popularity.

And finally manual review isn't perfect. It's hard to review code, look for all the possible security and policy problems and ensure that questionable API didn't do something we felt uncomfortable with.

Manual review has its place in Mozilla, but one thing we shouldn't be do is placing more burdens on the process. We should be aiming to streamline review and ease the burden on reviewers and developers.

The result is we've got to either say no to the API or find a way to make everyone comfortable with the API.
