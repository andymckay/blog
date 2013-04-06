---
layout: post
title: Why I prefer Poi to Trac
categories: General
old: 1883
blog: andy-mckay
---
If I had the choice, I'd use <a href="http://plone.org/products/poi">Poi</a> over <a href="http://trac.edgewall.org/">Trac</a> and that's because Trac does not support multiple sites very easily. Almost every company I've run or worked at over the last few years has been primarily a consulting company.  I spend my day dealing with multiple projects, sometimes an insanely high number.

Simply put, Trac does not do this. From the <a href="http://trac.edgewall.org/wiki/TracFaq#can-i-manage-multiple-projects-from-a-single-installation-of-trac">Trac wiki</a>:
<blockquote>Right now there is no support for sharing information between projects.

The rationale for this is that the scope of Trac (1.0) is to manage a single project, and do it well. Support for larger multi-project management adds a lot of complexity, but is planned for post-1.0 development, probably as a separate framework around Trac.</blockquote>
But in a world where all I have is multiple projects, this is a problem. Poi allows me to:
<ul>
	<li>Have multiple bug trackers, the permissions on each individual tracker is configurable, so different clients can have different trackers and can't view each others.</li>
	<li>As a developer, or project manager, I can have one page that lists all bugs assigned to me, across all the collectors. Such a summary page is invaluable to me.</li>
</ul>
Trac also provides a Wiki. A wiki is not useful to a developer of CMS's. In fact the problem in some organisations is that you can't find the damn data because it could be in SVN, Plone, Trac's wiki or Bootcamp. Ouch.

Not that Trac is bad, there are some nice features in there. The viewed source for SVN, checkin messages that are interlinked, closing bugs from checkin messages and so on are all cool.

The only real downside is that Poi does need a bit of work and cleaning on an install, something that raises the bar a little. But that's only if you are being a perfectionist about it.

<p><b>Update Wed Jan 3rd, 2.53pm</b>: Calvin wrote to tell me that with some mod_python you can make global lists pulling from multiple databases. Unfortunately he hasn't got any examples yet, but sounds like I might have to give this a go.</p>