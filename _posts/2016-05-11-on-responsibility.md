---
layout: post
title: Developer responsibility
categories: General
blog: andy-mckay
---

There are many traits that I value in developers, one I keep reiterating to anyone who will listen is developer responsibility. What does that mean?

So you write a peice of code based on a bug report or a feature request. You get it past code review, merge it and move to the next bug. Does that mean your responsibility ends there? No.

If you are working on something that is being deployed to a server, did you make sure it actually landed in on the production server? Did you do a quick check that it actually worked in production? Did it need in any metrics? Did you look at any logs to see if it threw some errors? Did something come up a few days later, a bug report maybe? Did you follow up on that?

Most of those questions and checks shouldn't take long to do, if they do then that's a problem.

But just throwing out code and then ignoring it afterward isn't ok. I've seen that happen and then been shocked to find that the developer never actually checked even very quickly that the feature went out. It created bugs or in some cases didn't even work because settings hadn't been flipped. That's not cool. It's your code, it's your responsibility.

...and by the way everyone on my team at the time of writing this is awesome at this.
