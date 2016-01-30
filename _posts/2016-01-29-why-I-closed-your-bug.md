---
layout: post
title: Why I closed your bug
categories: General
blog: andy-mckay
---

Because I'm mean. Well not really, but I understand how it can feel that way.

Web sites at Mozilla have a unique advantage in that they are open source. That is great for development and contributions. Although the number of contributions tends to be lower than for Firefox and other projects [1].

Just like Firefox anyone can file a bug and anyone can send in a patch. Which is truly awesome and for the last 10+ years AMO has had some excellent contributors as well as paid staff help it out. Except for a few basic problems:

* There are always new features, new edge cases, new problems to be solved.

* Each new feature spawns new bugs.

* Each new feature interacts with other features to become more and more complex.

* The number of bugs on the site grows to overwhelming proportions given time.

* The maintenance burden grows and grows until no new features can be added without getting more resources.

This is probably a familiar cycle to many. In open source projects you can fork and take your project off in a different direction. In the case of <a href="https://addons.mozilla.org">AMO</a> though you really can't in that there's only one such site for Firefox.

And there in we get to the dilemma. At Mozilla we've gone through various phases of support for AMO from paid contributors: from lots of developers, to none, to one, to lots of developers.

The one continual theme in all of them, the number of features and bugs just keeps growing and to get more done we need more and more people.

So let's return to that bug you've filed asking for something on AMO. We'll think quite unsurprisingly of things like:

* Will it add complexity or remove it?

* What are the long term maintenance and security issues?

* Will it be used?

...that shouldn't be too much of a surprise. But that might mean that we won't take that bug, or pull request, and then you'll think we are mean.

In the past I've seen bugs triaged to be "P5 Enhancement" (or maybe even "good first bug" or "patches welcome"), this is just a cop out. Basically we don't want to work on this so we are going to ignore it, we know that you don't really want to work on the feature either and it sits in limbo. I'd rather be up front and close it.

The only way we can make a site like AMO maintainable is by keeping the complexity and feature set down. After all, there's a lot of work to be done around add-ons, the more we can keep the complex things simple, the more we can do.

[1] Citation needed.
