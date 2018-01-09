---
layout: post
title: Clouseau 0.3 released
categories: Plone
old: 1854
blog: andy-mckay
---
<a href="/files/clouseau-context.png"><img src="/files/clouseau-context.png" width="200" style="float: right"></a>
Now features context sensitive Python prompt. Not sure about the API of an object? Just click the little Clouseau button and a Python prompt will appear with <em>context</em> mapped to the actual object you are looking at.

Other changes:

<ul>
	<li>Add in utils library, for things like utils.commit()</li>
        <li>Cleaned up tooltips, no longer raise an error</li>
        <li>New tooltips code from pyShell</li>
        <li>Changed icons</li>
</ul>

<b>Note:</b> because I have no Windows computers anymore this is <b>not</b> tested on IE. May work, help needed for that.

<b>Upgrades:</b> do an install and uninstall from the add/remove products section of the Plone control panel to get the context sensitive help.

<b>Download:</b> <a href="http://plone.org/products/clouseau/releases/0.3/Clouseau.0.3.zip">Clouseau.0.3.zip</a>