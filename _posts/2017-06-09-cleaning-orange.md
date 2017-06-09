---
layout: post
title: Cleaning up intermittents
categories: Mozilla
blog: andy-mckay
---

<a href="https://wiki.mozilla.org/Auto-tools/Projects/OrangeFactor>Orange Factor</a> robot creates bugs in Bugzilla components when it detects intermittents in the Firefox test suite. Unfortunately it never cleans up after itself. Trying to keep the bug count in a component manageable is something that really helps me understand whats going on and the orange factor bugs that never get closed don't help.

I found that as I was triaging through I found a common pattern, which is basically go look on Brasstacks and see if it occured in a while. From that came a simple script that looks for intermittents and checks to see if it occurred on Brasstacks in the last 180 days, if not then close it.

Both Brasstacks and Bugzilla have REST APIs, but last week or so Brasstacks went behind Mozilla internal authentication. To get around that, you need to pass the session cookie and user agent through any requests.

The resulting script is on <a href="https://github.com/andymckay/bugzilla-scripts/blob/master/intermittent.py">Github</a> and closes out a couple of bugs for us each week.

For this script to work, you need a bunch of environment variables: the brasstacks session, the brasstacks user agent, the bugzilla API key and bugzilla API token. But this script is written for me, not for your project, you'll probably want to do something different anyway.
