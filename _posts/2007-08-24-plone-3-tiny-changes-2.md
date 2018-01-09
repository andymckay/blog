---
layout: post
title: Plone 3 tiny changes #2
categories: Plone
old: 2004
blog: andy-mckay
---
<img src="/files/plone_small_things_message.png" style="padding:1em; float:right" />
<p>Quite often in applications I've wanted to show just a warning or some information back to the user. In older Plone's there was one choice, that bright orange box that screamed "idiot!". Now you can give your status message a level and there will a suitably bold message.</p>
<code>
addStatusMessage(_(u"Changes saved."), type='info')
</code>
<p>Choices are: <code>info</code>, <code>warning</code> or <code>error</code>.</p>