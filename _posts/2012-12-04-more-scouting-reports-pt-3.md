---
layout: post
title: More scouting reports (pt 3)
categories: Mozilla
old: 2358
blog: andy-mckay
---
<p><em>Following on from <a href="https://mckay.pub/blog/andy/2356/">part one</a> and <a href="https://mckay.pub/blog/andy/2357/">part two</a></em>.</p>
<p>The last post I was looking at fixtures. I haven't fixed up all the fixtures, but as I'm going along I'm fixing them. As it turns out, most of the tests need very few fixtures, but were just pulling in large ones because it's easy. Haven't seen any huge wins on the overall test time yet, but it won't hurt.</p>
<h3>Scouting</h3>
<p>Fixing tests requires information. There are quite a few timing plugins out there, but I didn't find one that did what I wanted, so I wrote one. <a href="https://github.com/andymckay/nose-timing">Nose timing</a> is based on <a href="https://github.com/acdha/nose-congestion">nose congestion</a> and is a basic plugin to output the time of each test setup and each test. It then outputs them in JSON with a file and line number.</p>
<p>Once I've got those big JSON dumps, I run a <a href="https://gist.github.com/4211913">secondary  hack</a>, it sorts the data and then tries to run <code>git blame</code> on each test. The result is the slowest tests in zamboni and the person who wrote them. And the output is <a href="/files/zamboni-test-times.html">available here</a>. From that, I filed some bugs on those tests and so hopefully other people will fix them.</p>
<h3>More timing</h3>
<p>Sending stats to django-statsd is giving us quite a lot of information on the tests. Wanting more, I added in a simple <a href="https://github.com/mozilla/zamboni/commit/e4f69a89856c0a491afe2f9ba8985af9b7071184">timer</a> decorator to the marketplace. In this example I've thrown a timer decorator on to the transformer. Now every time I run the tests with statsd, you'll see how long that method takes:</p>
<pre>
[master] zamboni $ t mkt/api/tests/test_handlers.py --with-statsd
[snip]...
======================================================================
Statsd Keys                            | Number | Avg (ms) | Total (ms)
----------------------------------------------------------------------
[snip...]
cache.memcached.set_many               |   1929 | 0.143079 | 276.000
db.mysql.default.execute               |   7499 | 0.199227 | 1494.000
django.management.command.loaddata     |      9 | 46.555556 | 419.000
[snip...]
timer.addons.models.transformer        |    120 | 23.441667 | 2813.000
</pre>
<p>That added key, <code>timer.addons.models.transformer</code> is pretty useful for quick checking how slow a method is. I'm also looking at one that provides a quick profile decorator that hooks in via <code>sys.settrace</code> which I haven't got as useful yet. But it did yield that <code>apps.amo.utils.patched_load method</code> is being called 19,557 times on one test (although I think this fine based on the internals of PIL).</p>
<h3>Miscellany</h3>
<p>Django has a really slow method for checking if a view returns an a redirect. But it then also goes and calls the resulting URL. Meaning that one request to check you get a redirect results in two requests. That has never been a problem for us and has not resulted in finding any broken code. The redirect targets are tested seperately. What it has done is slowed down our tests by doubling the number of requests. So the most excellent <a href="https://github.com/robhudson">Rob Hudson</a> wrote a simple little replacement <a href="https://github.com/mozilla/zamboni/blob/master/apps/amo/tests/__init__.py#L314">assert3xx</a> that doesn't do the extra request.</p>
<p>There's also a matching assertLogin which just checks that the user is redirected to a login.</p>
<p>Next? Finding some of the stupid things zamboni is doing all the time and stopping that.</p>