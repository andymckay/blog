---
layout: post
title: Grouping in Django URL's
categories: Django
old: 2178
blog: andy-mckay
---
<p>I wanted to include a regular expression in my Django URL's, but I didn't want to that be passed as an argument to the view. The answer is in the Python <a href="http://docs.python.org/library/re.html#module-re">regular expression</a> documentation:</p>
<blockquote>(?:...)
A non-grouping version of regular parentheses</blockquote>
<p>So in my case a URL like:</p>
<pre>r'^(?:site/[0-9]+/)view/(?P&lt;id&gt;.*)/$</pre>
<p>Would match the URL:</p>
<pre>/site/1/view/2/</pre>
<p>But by using (?: only the <code>id</code> is passed to the view.</p>