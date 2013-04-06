---
layout: post
title: Plone 3 tiny changes #3
categories: Plone
old: 2005
blog: andy-mckay
---
<img src="http://www.agmweb.ca/files/plone_small_changes_lock.png" style="float:right; padding: 1em" />
<p>This looks like a tiny change in the user interface, but represents a larger change behind the scenes, adding in locking. When you hit the edit page a WebDAV lock is placed on the page. When the browser leaves the page the lock is removed. If the user just closes the browser the lock times out. Having the page locked means it cannot be edited by anyone else.</p>
<img src="http://www.agmweb.ca/files/plone_small_changes_lock_cp.png" style="float:right; padding: 1em" />
<p>The lock is visible in the Zope Control Panel under WebDAV locks. I haven't spotted anywhere else in Plone that shows the locks and allows you to clear them or see what's locked when, if anyone does, let me know.</p>