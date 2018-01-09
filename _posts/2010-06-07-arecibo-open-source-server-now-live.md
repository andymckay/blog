---
layout: post
title: Arecibo open source server now live
categories: Arecibo
old: 2263
blog: andy-mckay
---
<p>We've now updated <a href="http://areciboapp.com">Arecibo</a> so that the open source server is now live and the free hosted version is now turned off. It's time to get that App Engine version of Arecibo up and running and start pushing your errors to that. Hopefully the DNS will have updated in your area by the time this post goes live.</p>

<img src="/files/arecibo-new.png" class="clear" title="Arecibo server on App Engine"/>

<p>In the process we've had to update a few of the clients as well so that they work with a Arecibo server specified by the user. So instead of all of them hard coding in the URL, this is now part of the library. We've moved the documentation into sphinx, so you can find some <a href="http://areciboapp.com/docs">docs online</a>.</p>

<p>Along the way we've put the <a href="http://pypi.python.org/pypi/arecibo/0.1.1dev">Python Arecibo client</a> and <a href="http://pypi.python.org/pypi/django_arecibo/">Django Arecibo client</a> in PyPi so they will work easily with Python package management.</p>

<p>I'm actually quite excited about this version of Arecibo, it allows me to focus on features and not worry about maintenance. Plus, being open source, hopefully this project will start grow that bit bigger.</p>