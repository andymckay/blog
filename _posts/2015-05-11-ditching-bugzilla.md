---
layout: post
title: Moving to GitHub issues
categories: General
blog: andy-mckay
---

Mozilla wasn't my first time using Bugzilla. About ten years earlier I worked at ActiveState and spent hours hacking away at Bugzilla with a certain David Ascher to produce an issue tracker for the company.

That was forever ago, when I was a junior who knew nothing and found Bugzilla a bit of a mess. But that was ages ago, software improves and life moves on.

We've used Bugzilla every day at Mozilla for Add-ons and the Marketplace. Actually came to like Bugzilla, sort of. But recently we had an opportunity to move onto a new project - and we decided to move issues to GitHub.

Again I'm going to blame David Ascher who one day asked me "Have you tried putting your issues on GitHub?". I gave a list of reasons why not. Then later on I realised they were mostly bogus and the only real reason had become "Because that's what we've always done."

The biggest reason I could think of is that GitHub is repository based. As an example... suppose there's a bug in Payments, where do I file an issue? The payments-server, the payments-ui, the payments-example repository? It's not project based. So we created a <a href="https://github.com/mozilla/payments">payments</a> repository that's a catch all for issues and documentation. Problem solved.

By moving to GitHub issues we've gained:

* faster performance
* better integration with our code and pull requests
* ability to link-in other tools (e.g. <a href="http://waffle.io">http://waffle.io</a>)
* lose a whole pile of features, settings and flags we never use
* lose getting told off for features that cross products, e.g. the time people removed [perf] off our bugs because that reserved for something in Firefox

So far the things we've lost are:

* ability to file security or Mozilla confidential bugs, but for that we just use Bugzilla

But so far everything is great.

My favourite thing is using <a href="http://waffle.io">waffle.io</a> which provides us with a Kanban flow across <a href="http://waffle.io/mozilla/payments">multiple repos</a> and is pretty awesome.

I tried to use a similar tool with Bugzilla that an intern wrote. But surprise, the tool wasn't maintained, didn't always worked and I ended up maintaining it. I didn't want to do that, I just want good tools that other people maintain so I can ship my project.

Oh the last downside? When GitHub goes down:

<img src="http://i.cubeupload.com/D6bRPx.png" />

If you are still reading this blog post, I strongly encourage you not to think about ditching Bugzilla, but to think about your entire tool chain set and find new tools and improvements when you can. Oh, and read <a href="http://gregoryszorc.com/blog/">Gregory Szorc's blog</a>.
