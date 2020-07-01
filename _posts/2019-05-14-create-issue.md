---
layout: post
title: Create Issue Extension
categories: General
blog: andy-mckay
---

I needed to find a better way to keep track of my to-do lists. I've tried a few tools, but after a while always forget about them and don't keep them up to date. A to-do list is only any good if you add stuff to it and look at it.

I spend 95% my time in about 5 places these days: Google Calendar, Google Docs, Gmail, Slack and Github. I spend a lot of time on the latter, GitHub. So, of course, to super charge my to-do list I went for a quick browser extension - cue colleagues who laugh and say "of course you did" when I mention this.

[Create issue on GitHub](https://github.com/andymckay/create-issue) is a [stupid simple Firefox Extension](https://addons.mozilla.org/en-US/firefox/addon/create-github-issue/) that lets you highlight a peice of text on a page, then right click to create an issue. It creates the issue in a repository defined on the config page using a personal access token. That's it. 

The beauty of this is that everything is a web page. Emails. Slack messages. Docs. All you do is highlight some text then right click and it creates an issue with the selected text and a URL to the item. Key to this is that's it **fast** to create a simple issue.

<img src="https://user-images.githubusercontent.com/74699/53767875-fac37300-3e8b-11e9-8401-650d0a317f3a.png" />

For this I've setup a private repo ([those are free now](https://github.blog/2019-01-07-new-year-new-github/)). Thanks to all the integrations with GitHub issues, I get a bunch of stuff for free:

* automatic links on other issues and PRs across GitHub back to my to-do item
* notifications in email and Slack
* [stale](https://github.com/marketplace/stale) to automatically clean my list
* [reminders](https://github.com/probot/reminders) to remind me of me of things at set times

So far I've used this more than any to-do list system I've used in the past.

