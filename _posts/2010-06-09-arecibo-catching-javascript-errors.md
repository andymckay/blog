---
layout: post
title: Arecibo catching Javascript errors
categories: Arecibo
old: 2265
blog: andy-mckay
---
<p>Thanks to a push from <a href="http://github.com/acdha">Chris Adams</a>, the Javascript library in the trunk now catches JavaScript errors.</p>
<p>So if you have some JavaScript that throws an error, for example:</p>
<pre>
            function foo() {
                alert("About to fail!");
                bar();
            }
</pre>
<p>In this case there is no "bar()" defined. This will be caught and passed to Arecibo, so that you have a track of the error and the browser.</p>
<img src="/files/arecibo-client-side.png" />
<p>Unfortunately at the moment this only works in Firefox and Chrome. Thanks Chris!.</p>