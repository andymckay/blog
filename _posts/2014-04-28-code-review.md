---
layout: post
title: Code Review
categories: General
blog: andy-mckay
---

So you've got some code you want reviewed? Awesome. But there's a problem with
code reviews - *they can be disruptive to the person doing the review*.

The reviewer will be interrupting their own development and thought streams, a
review can be quite disruptive. As that reviewer is taking their time
to make your code better, they are doing you a favour, show them the respect
of getting a good pull request in.

The best way to help them and yourself is to make your code review easy to
read. Here's some tips on that.

* Follow your projects code writing guidelines, unless they are silly.
* Keep them small. A small pull request is easy to understand, review and get
  feedback on. The difficulty of reviewing a pull request snowballs quickly
  as it gets bigger.
* Try and keep a pull request to one concept or change at a time.
* Comment sensibly. Comments help people who read your code. Funny that.
* Review your change before you ask for a pull request. You'll catch a few
  errors in there (well I do).
* Make sure you've got a link to the bug if the code review is for a bug.
* Readability of code counts. Small compact complicated code might be clever,
  but making it hard to read makes it hard to review.
* Don't skimp on the description. You can include multiple bullet points
  of text explaining what is going on.
* If your result is visual, include an image in the pull request showing the
  change. We've even had some people include videos, which is pretty cool.
* Once people start reviewing, follow up quickly if possible, so that you can
  have that conversation whilst its in the other person's mind.

Finally - be mindful of other peoples time, they might have a whole pile of
other more important things to do.

And remember code reviews are an async process. Push your code review on to
the stack and then get on with something else. Don't get blocked on waiting.
