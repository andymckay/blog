---
layout: post
title: Sometimes Ruby is annoying
categories: Rails
old: 1937
blog: andy-mckay
---
<p>Well its annoying a lot of the time to me since it's so magical. Yes I got bitten by the difference between single quoted strings (') and double quoted strings ("). In the previous there are very few escape sequences, in the latter there are more. What got me was a good old newline: <code>\n</code></p>
<pre>
Python 2.4.4 (#1, Feb 18 2007, 22:11:27) 
>>> '\n' == "\n"
True
</pre>
<p>And now in Ruby:</p>
<pre>
~ $ irb
irb(main):001:0> '\n' == "\n"
=> false
</pre>
<p>This isn't hidden, it's documented (<a href="http://www.rubycentral.com/book/tut_stdtypes.html#S2">for example</a>), but to me it's a strange language decision. For a Python programmer it's certainly a gotcha.</p>
