---
layout: post
title: Climbing the ruby and rails learning curve
categories: General
old: 1864
blog: andy-mckay
---
Been building a ruby on rails app this week. Like most new technologies, its very feast or famine. I get a road block and get stuck for a while, get over it and get productive for a while, then hit the next road block. Actually probably most development is like that. I've got lots of posts in my head about it and Plone.

General thoughts so far are there are many good things in it, I like the environment separation, creation of unit tests and fixtures so I don't have to write SQL (yet). There are also many bad things in it, the templating is painful, it doesn't create any HTML for you (except through scaffold which isn't usable except for 20 min. screencasts) and waaay to much magic. It feels like Zope 2.

The one that hits me right now is introspection, I'm so used to going up to anything in Python and being able to do: <code>type(something)</code> will always give me a clue as to the type and figure out the api. In theory in ruby <code>something.class</code> should be same. Except it's not, because it doesn't always work. In my rails unit tests I can access one of my fixtures like this: <code>timesheets[:foo]</code> to get the foo fixture. But I can't iterate through it. I also can't do <code>puts timesheets.class</code> I get:

<pre>ArgumentError: wrong number of arguments (0 for 1)</pre>

Even using the ruby debugger (thanks to help from Geoff Davis) gives me:

<pre>
(rdb:1) m timesheets
test/unit/timesheet_test.rb:24:in `__send__':wrong number of arguments (0 for 1)
</pre>

Magic is bad. Not least of which it makes me feel stupid.