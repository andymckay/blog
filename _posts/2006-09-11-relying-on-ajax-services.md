---
layout: post
title: Relying on Ajax services
categories: Ajax services
old: 1847
blog: andy-mckay
---
<img src="http://www.thisisbroken.com/photos/uncategorized/exit.gif" style="float: right; margin 2em" alt="Broken" width="400" />
There's been lots of chatter on Slashdot and digg about Ajax services. Mostly thanks to the questionable linking to COWS which has ganered press for some reason. One of the main responses went along the lines of "I wouldn't trust some external web site for that part of my site, what if it goes out etc...". That's a fair question, but it's focused on the wrong line of thinking...

Yes, running your multi-million dollar website with a dependency on my ClearWind service is a mistake. I have no resources to monitor or maintain it and I might change it on a whim to start charging you for all your traffic. However I would say that services from Google, Yahoo, Flickr, Apple, eBay will all likely put more resources into keeping their site up and running than any site I will be rolling out over the next few years. So, pick a trusted server for your service.

Bear in mind the Plone AjaxProxy does caching, another advantage of running through a local proxy. If the destination server goes out temporarily the cache might be catching that.

The main use case for Ajax services harks back to a scenario I had at Enfold. In a scenario when you have 20 Plone sites with your software installed and you want to roll out a new service to them - you have a choice, install new software on every client or run a service and have all the servers consume it. Yes, the latter does involve installing software on each installed, but it's an easier install.

Take the scenario for image manipulation, you normally have a library that can do a series of manipulations on an image. This then means installing PIL, ImageMagick or so on a server. It's also something that occurs rarely, you do a few manipulations and save it. With an Ajax service, you install the client part of the image manipulation, the Ajax onto the Plone site. You install the libraries on the server. That's a much easier install.

You can then test and maintain the Image manipulation service on the server. The advantages are the usual one's you'll get from a service oriented architectures:

- each service has a clear API and division from the rest of the software

- each service is easily testable

- each service is easily supportable and maintainable

- each service is cross application

- software is easier to install on the client

The dependence is on your software and services, not on other people.