---
layout: post
title: mod_python to mod_wsgi
categories: Django
old: 2168
blog: andy-mckay
---
<p>These last few days I've been doing some <a href="http://www.areciboapp.com/blog/5/">upgrades to Arecibo</a>. These include adding in new fields and converting times into a users local timezones - figuring out when an error occurred is now just that little bit easier.</p>
<p>I also moved from mod_python to mod_wsgi. I still have to tune those settings but it looks like a great win in terms of performance and mirrors what other people have been saying about mod_wsgi. There were helpful docs <a href="http://ericholscher.com/blog/2008/jul/8/setting-django-and-mod_wsgi/">here</a> and <a href="http://code.google.com/p/modwsgi/wiki/IntegrationWithDjango">here</a>. Was very easy to setup too, worked first time.</p>
<p>Also did some quick benchmarking with CoralCDN and just to confirm, its stated goal is to make a website available, but <i>not fast</i>. My site was way slower with CoralCDN, probably more available, but slower.</p>