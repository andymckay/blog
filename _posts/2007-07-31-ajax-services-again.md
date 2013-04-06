---
layout: post
title: Ajax services again
categories: Ajax services
old: 1984
blog: andy-mckay
---
<p>I am doing some work in PHP at the moment, not a huge amount, connecting things up. I got back to how much I like doing simple things at the Ajax level. One example is I needed to normalise a string, from unicode to plain text, much like Plone currently does. For example turning:</p>
<pre>Pdi manjar de veire, me nafrari pas</pre>
<p>Into:</p>
<pre>podi-manjar-de-veire-me-nafraria-pas</pre>
<p>An English ASCII approximation. My first thought was "hey, that's what Plone does". So I grabbed my highly unsophisticated mod_python services framework and wrapped the Plone API from PloneTool.py (which means yes its under GPL) and threw together a quick file (about 20 lines) so that the above comes back as:</p>
<pre>
&lt;?xml version="1.0" ?>
&lt;response>
&lt;info author="Andy McKay, ClearWind Consulting" 
     end="Tue Jul 31 14:28:53 2007"
     length="0.00110411643982" 
     start="Tue Jul 31 14:28:53 2007" version="1.0"/>
&lt;result>podi-manjar-de-veire-me-nafraria-pas&lt;/result>
&lt;/response>
</pre>
<p>Weee, it's a simple manner of now writing Ajax to pull that out and bingo I can do that in Rails, Plone, mod_python and PHP. Assuming the server stays up. The pattern of doing lots of little bits at the browser level is something I really like, having the discipline of using lots of languages forces a different solution. Web services at last.</p>
<p>Service available at: <a href="http://www.clearwind.ca/software/normalize/">http://www.clearwind.ca/software/normalize/</a></p>