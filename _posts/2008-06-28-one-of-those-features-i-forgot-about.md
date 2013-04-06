---
layout: post
title: One of those features I forgot about
categories: Python
old: 2103
blog: andy-mckay
---
<p>Always nice to remember a feature in Python that I haven't used for ages. This happened to me the other day with this... given a list:</p>
<pre>x = ["hair", "brown", "eyes", "blue"]</pre>
<p>How do I get the hair and eye colours easily? One way, the oft forgotten 3rd argument to list slicing:</p>
<pre>
Python 2.5.1 (r251:54869, Apr 18 2007, 22:08:04)
>>> x = ["hair", "brown", "eyes", "blue"]
>>> for z in zip(x[::2], x[1::2]):
...   print z
... 
('hair', 'brown')
('eyes', 'blue')
</pre>