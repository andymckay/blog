---
layout: post
title: Triaging WebExtensions Bugs
categories: General
blog: andy-mckay
---

When a bug lands in Bugzilla for WebExtensions a few things can happen to it. This blog outlines the current triage process. This is likely to change, so chances if you read this in 2017, it might be completely different.

Weekly new bug triage
---------------------

We look at all new bugs in an attempt to spot serious bugs, regressions or other issues. We try to give each bug a priority and mark as [triaged] in the whiteboard. The point here is to do an initial triage and catch critical things. We also label bugs that might be good for contributors or need thinking about. The latter are marked [design-decision-needed], but its important to point out that straightforward change or obvious bugs just go through.

Bi-weekly community meeting
---------------------------

We look at a number of bugs marked with [design-decision-needed] every other week, currently we are doing 6 per meeting, which averages us at 5 minutes per bug. Some take longer. The goal here is to see the use case, understand what the bug is for and if it should proceed. If we are still unsure then it will get kicked "up" to the [Advisory Group](http://wiki.mozilla.org/WebExtensions/AdvisoryGroup) for some more help and insight.

Advisory Group meeting
----------------------

Where Mozillians with knowledge and insight beyond our group help out with the toughest bugs. Happens about once a month.

Good first bug meeting
----------------------

If a bug gets marked as [good-first-bug] then we make sure the bug has a mentor, has a decent description and make sense. We hope that contributors will use this to get into Firefox development.

The majority of bugs coming into WebExtensions don't go through this process they hit the first triage and get dealt with. But sometimes bugs are more complicated than that.
