---
layout: post
title: Wysiwyg editor for code
categories: Web 2.0
old: 2187
blog: andy-mckay
---
<p>Anyone got a recommendation for a wysiwyg editor that allows you to add code? Basically I have an application that developers will write snippets of code in text areas. No it's not to ever execute, it's for a bug tracker and pasting code in is very common.</p>
<p>But no wysiwyg editor's seem to support this, adding in a pre or code tag seems hard. In all except Plone and Kupu that is. Sadly I'm not using Plone and support in non-Plone kupu land seems to be dead these days - and I think (please tell me if I'm wrong) that getting Kupu working from nothing is a challenge. So I've looked at:</p>
<ul>
<li>jwysiwyg: doesn't work in a lightbox in Firefox, no pre, but it looks like it could be added</li>
<li>tinymce: no pre or code and nightmare to add (from what I here in the forums)</li>
<li>fckeditor: no pre or code, could be addable, but seems to hate me for wanting to serve html and js off a different domain</li>
<li>yui: reading api now</li>
</ul>
<p>Perhaps this why so many bug trackers just use mark up text instead of a wysiwyg.</p>