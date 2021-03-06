---
layout: post
title: Speeding up Arecibo
categories: Arecibo
old: 2169
blog: andy-mckay
---
<p>Since I managed to move from mod_python to mod_wsgi I thought I'd spend a few minutes tweaking the site up a little. The <a href="https://addons.mozilla.org/en-US/firefox/addon/5369">YSlow Firefox</a> extension is excellent for this. Unfortunately at this point I don't use a CDN so no points for that.</p>
<p>However I was able to tweak the Apache Expires and got caught by rules I'd set up:</p>
<pre>ExpiresByType image/jpg "access plus 5 day"</pre>
<p>Didn't do anything, should be:</p>
<pre>ExpiresByType image/jpeg "access plus 5 day"</pre>
<p>Funnily enough an expires set at "access plus 1 day" wasn't enough for YSlow to trigger that it's an expires far in the future. Setting it for 5 days is and that gives me enough leeway to change the images without having to change the URL's.</p>
<p>The thing that drags down the scores is Google Analytics and Blip.tv, neither of which set Expires or other headers that would improve the score.</p>

