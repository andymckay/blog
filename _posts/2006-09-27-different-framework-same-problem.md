---
layout: post
title: Different framework same problem
categories: General
old: 1857
blog: andy-mckay
---
One thing I've enjoyed doing the last year is taking a bit of a step away from being blinkered solely on Plone and Zope and take a look around at other things out there. And no surprise -  all these fancy new frameworks out there don't actually solve some problems. The exact same problems and patterns exist out there. All too often in IRC channels or from managers I've heard an answer like "so if move away from Plone we'll fix this problem". Chances are you won't, chances are other framework's have the same problem.

Take for example the "pulling large amount of data from a remote source" situation. I've seen this now in Plone, Zope, Ruby on Rails and heard about it Drupal. The problem is simple, you've got a source that contains a large amount of records, such as a SQL server or and LDAP server. You write code to show the first 20 users and but the rest behind next links. Works with 10, 20, 200 users. Now throw 5 million in there and what happens. It falls over.

It's a pattern that developers (like myself) need to learn and in LDAP's case its a limitation of the tool. OpenLDAP has recently started to support this kind of "give me records 200-300 out of this possible 1,000 records" but no fiddling on the framework is going to change that. I was in a Drupal birds of a feather and I remember hearing them say "oh yeah when our LDAP server has 20,000 users in (number made up) the admin tool for browsing gets really slow". Yep same thing.

Many times Alan Runyan is right, one talk in particular that stuck in head was a talk at the last New Orleans conference. At that he was asking people to focus on reusability, not re-invention (although his point was probably deeper than that). 

And don't get me started on how Django is crippling itself with re-inventing yet another templating language and simultaneously natching defeat from the jaws of victory.

<em>Side note:</em> Just to compound the problem in the Ruby on Rails app was that it was looking for a change on the input box every second and firing off a request to the server, returning a huge recordset every time. There's a reason Google doesn't have this on their home page you know.

Okay rant over, on with the show.

