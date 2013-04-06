---
layout: post
title: Tidying Page Templates
categories: Django
old: 2084
blog: andy-mckay
---
<p>I know this is old hat, but I still get a fact that I can still run HTML Tidy over my Page Templates and fix up indenting and a few other things. Perhaps it's just because I've seen some horrible Rails templates that are a badly indented and hard to read. Well I've seen a few Page Templates like that, but hey at least I can clean them in one simple bash script:</p>
<pre>tidy -i -m -xml $1</pre>