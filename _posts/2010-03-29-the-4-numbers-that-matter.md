---
layout: post
title: The 4 numbers that matter
categories: General
old: 2252
blog: andy-mckay
---
<img src="http://farm5.static.flickr.com/4028/4326156938_47ec1b9ab0_m.jpg" class="photo" />

<p>A while ago I had a conversation with a project manager who was trying to specify a project. Every time we discussed relationships between entities I kept asking the same question about how many of X is related to Y. In the end I got down to a simple set of rules.</p>

<p><b>Zero:</b> there's no relationship at all between X and Y.</p>

<p><b>One:</b> there's one of them, in terms of data structures, this has a specific meaning.</p>

<p><b>Some:</b> more than one. If this was Django for example, "one" might be a OneToOneField where as some would be a "ForeignKey". A car has some wheels on it but only one steering wheel.</p>

<p><b>Crap loads:</b> lots and lots of them. This is important to differentiate from "some" because it has clear performance implications. This normally means more than a few hundred thousand.</p> 

<p>As a project manager you can then guess the implications of changes in your specification. The amount of time to make the change will be affected by the change between these levels, the latter being the most costly.</p>

<p>To change from 0 to 1, is a bit of a pain. To change 1 to some, you might need to add in a new relationship and migrate data around. But once you are at "some", you don't really care if there's 4 wheels on a car or 36, that's likely easy. The tricky one is when you hit "crap loads", that's when performance and other things will start to impact the application.</p>

<p>Once we'd got this sorted out things went much smoother.</p>