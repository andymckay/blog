---
layout: post
title: Handling dir in Clouseau
categories: Plone
old: 1853
blog: andy-mckay
---
I was playing with <em>dir</em> in Clouseau today. The problem is that in all tools this useful function returns around 600-900 when run on a Zope object. The reason I thought was acquistion and then I realised it wasn't its just Zope 2's huge inheritance tree. So how can this be more useful?

<ul>
	<li>Integration with DocFinderTab to find say the dir of the top 4-5 or five classes, most of the time you don't need to go too deep.</li>
	<li>Easy introspection of an objects Schema for example:
<pre>
<textarea name="code" class="python">
>>> utils.schema(context)
[ 'setDescription', 'setTitle', 'Title',]
</textarea>
</pre>
        </li>
</ul>

Any other things that are <strong>possible</strong> to do? ie: give me code or sane ideas please