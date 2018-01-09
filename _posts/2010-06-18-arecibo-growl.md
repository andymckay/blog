---
layout: post
title: Arecibo Growl
categories: Arecibo
old: 2267
blog: andy-mckay
---
<p>Ever wanted to see your website errors pop up in Growl? Well now you can. I just put back in the JSON feed for Arecibo. Which means you can get a nice JSON pull by just going to yoursite/feed/private_key/json. JSON isn't needed to do a Growl client, but its easier.</p>
<p>So anyway, <a href="http://github.com/andymckay/arecibo/tree/master/clients/">grab the client from github</a>. It requires Python 2.6 and the <a href="http://growl.info/source.php">Growl python library</a> installed. Run it and it will poll every 30 seconds and you'll get a nice pop up.</p>
<img src="/files/arecibo-growl.png" />
<p>You can configure what feed to parse and by default it makes priority 1 errors sticky and the rest not. Now if I can just find a way to put a clickable URL in there...</p>