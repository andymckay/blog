---
layout: post
title: Plone File Uploader first release
categories: Plone
old: 2059
blog: andy-mckay
---
<img src="http://www.agmweb.ca/files/plone-file-upload-picture.png" style="float:right; padding: 1em" />
<p>The Plone File Uploader is a little experimental product I wrote using Adobe Air. It's designed to all you to just easily drag and drop multiple files into your Plone site. After installing, tell it where you want files to go and then just drag and drop files in, it queues them up and sends them to your server as HTTP PUT's (with all the problems that involves in Plone).</p>
<p>It's in it's beta stages and done more for fun than anything else. It doesn't recurse folders - if it you drag in a folder it just grabs the files from that folder and uploads them. It ignores sub folders, shortcuts etc. If you want a super duper upload tool, go look at <a href="http://www.enfoldsystems.com">Enfold Desktop</a>.</p>
<p><b>Note:</b> A few people tried it on Windows and Plone 3 including Kaell in irc (thanks) and we got differing responses, including <a href="https://bugs.launchpad.net/zope2/+bug/143780">this bug</a>. So it looks like some Plone or Zope combo's might need patching to allow PUT's.</p>
<dl>
<dt>Requires</dt>
<dd><a href="http://get.adobe.com/air/">Adobe Air</a> installed on your computer and access to a Plone site.</dd>
<dt>Tested on</dt>
<dd>Plone 2.5, OS X.</dd>
<dt>Download</dt>
<dd><a href="http://www.agmweb.ca/files/uploader.0.2.2.air">uploader.0.2.2.air</a></dd>
</dl>
