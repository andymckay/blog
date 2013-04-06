---
layout: post
title: Moving to Sentry
categories: Django
old: 2341
blog: andy-mckay
---
<p>Back in the mists of time I worked at company that had lots of projects and lots of errors, but no unified way to find the errors. Instead  we relied on the users to find them, this sucked. So I wrote <a href="http://areciboapp.com">Arecibo</a> to track them. It went through many iterations, I even tried to make a business out of it at one point.</p>
<p>But alas it didn't happen and I moved it to open source a while back. If there was any value in the project someone could move it along. I've rewritten it from a multi-home app to a single home App Engine app and then back away from App Engine. A while back we turned it on for Mozilla and hooked up a few projects to it.</p>
<p>The only real problem is that I lost interest in working on it a while ago. I've really only been maintaining it and hoping someone else would pick it up.</p>
<p>A few years ago David Cramer started <a href="https://www.getsentry.com/welcome/">Sentry</a>.  It's now surpassed passed Arecibo in terms of functionality. The real winner for us was the addition of UDP support, we don't really care about storing every single error and having something non-blocking is crucial. So we've started to shift away from Arecibo towards to Sentry at Mozilla web development.</p>
<p>A few weeks ago we switched <a href="https://addons.mozilla.org">Add-ons</a> to Sentry. By a happy coincidence, last week we had a bot that hit an error and we generated 379,000 errors in about 24 hours. Sentry trundled along quite happily. Of course Arecibo isn't dead, it's open source, it's there if you need it. And being open source, may the best project win - and that's Sentry.</p>
<p>There, that's one more project I don't have to feel guilty about not maintaining.</p>