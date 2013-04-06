---
layout: post
title: Vancouver 2010 website
categories: General
old: 1820
blog: andy-mckay
---
Attended a talk at <a href="http://cmprofessionals.org/">cmprofessionals.org</a> last night. Who knew there was such an organisation, and they might be in your city. Apparently they have been going for about a year and talk every couple of months, so I'll hopefully be going again. It's a different group from the Python or Plone groups, I naturally sat down and got out my laptop to take notes.... only one there with a laptop.

The talk was on the <a href="http://vancouver2010.com">Vancouver 2010</a> website. It's built using <a href="http://thelevel.com">The Level</a>'s software. They are a content management start up in Vancouver. It's rumoured their main contract is a big project for Google (was confirmed last night that they do something for them).

Before the Torino cames they had to get the content out of the old web site and get a new site up and running with a new design in the new CMS. The organising committee (Vanoc) has got their sponsor Bell Canada to do the site which then used The Level. There was a team of 6 people building the site over 3 months, with 3 content editors plugging in the content. There's probably many more involved in the auxilary, but that seemed to be the core group.

The lady doing the talking (who's name unfortunately I did not write down), showed us a demo of editing content. Being one of the few techy people in the audience I was curious to get a quick preview of the editing interface. Basically it's an in place editing system, most of the template is fixed with a few areas you can edit. Common to editing systems a little button pops up so you can edit the post, which takes you to a new page. That pages is just like a Plone edit page, but out of context... enter the data in a few fields and the text into a simple wysiwyg editor.

From a few comments made it seems clear that the system has some sort of relational or xml database backend. Content is pulled out and transformed on the way using XSLT. Spotted a few things in there like versioning and staging but nothing really stunning. Ah I'm such a cynic, but c'mon I thing automatic RSS feeds, css for mobile users and so on are standard these days (although I'm sure people say similar things about Plone with different topics).

My two questions: localisation and accessibility were answered deftly. They even did focus groups for accessiblity prior to launch, good for them! Didn't get into specifics about the traffic, would be curious. From here the site is fast and I can imagine during Turino there was quite a peak of interest. A quick ab gave me:

Requests per second:    22.73 [#/sec] (mean)

However I did it for 50 requests and got a server timeout. Eek, better not run benchmarks on other people's servers :)

Moving to the games is going to be an interesting transition, the site needs for getting all the data from the games out is a different challenge, something I'd like to see more talks on.
