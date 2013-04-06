---
layout: post
title: Mixing string endings in python
categories: Python
old: 1981
blog: andy-mckay
---
<p>This one confused me for a minute when a colleague asked me:</p>
<pre>"some string"""</pre>
<p>My first thought was that should be a syntax error, but it's not. It is infact two strings, the first contains the text <code>"some string"</code>, the second is empty <code>""</code>. If you output that you'll get:
<pre>'some string'</pre>
<p>It's the same output as:</p>
<pre>"some ""string"</pre>
<p>It's actually a pattern we've all used for a long time, if a string is long and splits over a line you can append multiple strings together. Useful when you want to break the text up, but not embed spaces and new lines, like a triple quoted string would. For example:</p>
<pre>    "This is a long message "\
    " that goes over two lines"</pre>
