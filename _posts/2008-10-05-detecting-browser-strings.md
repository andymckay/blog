---
layout: post
title: Detecting browser strings
categories: Ajax services
old: 2130
blog: andy-mckay
---
<p>One thing that I needed to do in <a href="http://www.areciboapp.com">Arecibo</a> was detect user agent strings. I finally found a library to do that. This weekend I spent a few minutes wrapping it and adding it in to my <a href="http://clearwind-labs.appspot.com/">clearwind-labs</a> site, running on Google App Engine. Given a user agent string it returns a JSON or JSONP data structure containing hopefully useful information.</p>
<p>Example: <a href="http://clearwind-labs.appspot.com/useragent">http://clearwind-labs.appspot.com/useragent</a>.</p>