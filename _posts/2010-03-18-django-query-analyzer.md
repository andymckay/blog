---
layout: post
title: Django query analyzer
categories: Django
old: 2247
blog: andy-mckay
---
<p>One of the things I wanted to work on at the <a href="http://clearwind.ca/djangoski">DjangoSki sprints</a> was a django query analyzer.</p>
<p>The basic premise is that I want to create an easy way for users to experiment with and play with the ORM to produce the queries that they want. If you are new to Django, figuring out the ORM is one the first things you will need to tackle and it can be a little opaque. There's some ways to play with it at the shell, or use the debug toolbar, but these can be a little limited and unhelpful to newbies.</p>
<p>The main interface would ideally be a series of options introspected from the model. Choose a model, choose a query manager, then add in multiple filter queries. This would not be able to capture everything and you'd always need an opt out clause of a text area where you can enter anything you want.</p>
<p>This is pretty similar to the GUI's you'll get with most SQL servers, its just the Django ORM layer on top of it.</p>
<p>Sadly I didn't get much chance apart from some time on Thursday afternoon. But a whole bunch of other people did including Stefan Tjarks, <a href="http://twitter.com/robhudson">Rob Hudson</a> and Nick Fitzgerald. These guys did some great work on the project despite my vague handwaving about what the project should be. Fortunately after the conference I got a chance to do a few hours works and got to this stage:</p>
<img src="/files/django-query-analyzer-part-one.png" />
<p>The introspection code is there, just need to get around to pulling it altogether on the front end so that we've got a nice way. But I think for a newbie this can be a very useful way to play with the ORM and see what comes out and how those little changes to the code can make substantial changes to the SQL.</p>
<p>The code is very rough and has been messed around by me from that original hard work by Rob, Stefan and Nick - but it's at: <a href="http://github.com/andymckay/django-query-analyzer">http://github.com/andymckay/django-query-analyzer</a></p>