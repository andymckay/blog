---
layout: post
title: Easy RSS Widgets
categories: Django
old: 2191
blog: andy-mckay
---
<p>One thing that I looked at a while back, but didn't have chance to play with was <a href="http://code.google.com/apis/ajaxfeeds/">Google Ajax Feeds</a>. These give you an interface to easily read RSS feeds in Javascript.</p>
<p>A few years ago I tried this in Javascript using ClearRSS for Plone. The only problem with that was that I used a generic server side proxy (now redundant thanks to JSONP) and found myself hitting all the inconsistencies with feeds and programming that in Javascript. This API removes the first problem and solves the second by normalising all the data so that it is accessible consistently.</p>
<p>The result is that it's easy to read feeds in Javascript. As an example I just created a widget for Cleartrain, so that all trainings can be easily embedded on a page. For example all the Django training can be pulled using this:</p>
<pre>&lt;div id="cleartrain-feed" /&gt;
&lt;script type="text/javascript" src="https://www.google.com/jsapi"&gt;&lt;/script&gt;
&lt;script type="text/javascript" src="http://media.cleartrain.ca/widget/cleartrain.js"&gt;&lt;/script&gt;	
&lt;script type="text/javascript"&gt;
    cleartrain.url = "http://cleartrain.ca/atom/topics/4/";
    cleartrain.content = false;
&lt;/script&gt;</pre>
<div id="cleartrain-feed"></div>
<script type="text/javascript" src="https://www.google.com/jsapi"></script>
<script type="text/javascript" src="http://media.cleartrain.ca/widget/cleartrain.js"></script>	
<script type="text/javascript">
    cleartrain.url = "http://cleartrain.ca/atom/topics/4/";
    cleartrain.content = false;
</script>
<p>Cleartrain is itself a Django site and required no modification above and beyond having RSS feeds for everything. The Javascript to allow this to be embedable is really easy, all we do is read the Ajax API, loop through the entries and then add into the innerHTML. The source for that is here: <a href="http://media.cleartrain.ca/widget/cleartrain.js">http://media.cleartrain.ca/widget/cleartrain.js</a>.</p>
<p>Definitely a neat API from Google and a very quick and easy way to create an RSS widget.</p>