---
layout: post
title: The end of Web Services?
categories: Web 2.0
old: 1827
blog: andy-mckay
---
So in the Plone, Zope and Python communities, there are a large number of people putting together web sites. In a total of 6 years I've done one Web Service <em>and that was for a company trying to be an expert in Web Services</em>. So lets just clarify term's here...

I've always been annoyed by the term web services because I often get into my rant that a web service is something on the web that returns a service. Be it via XML-RPC, REST or any other thing you can mention. In this case I'm referring to that bundle of technology that is (usually) SOAP, over HTTP with WSDL and all that jazz behind it.

There are a few modules for <a href="http://pywebsvcs.sourceforge.net/">web services for Python</a> and Ben Saller even worked one for Plone. From what I can see they aren't used that much and from where I sit the whole thing has slipped into obscurity? Why?

<ul>
	<li>It's pretty darn complicated. Getting into the WSDL specification is not for the faint of heart.</li>
	<li>SOAP will if I can paraphrase a talk Paul gave... "SOAP is a terrible acronym. It's not simple, it's sort of about objects, it has no access control and its not a protocol."</li>
	<li>There are a few high level tools.</li>
</ul>

Perhaps things are changing slowly, but from where I sit for the last 5 years it's dying. Look at these Google trends ("<a href="http://www.google.com/trends?q=web+services%2C+ajax">web services, ajax</a>",  and just to be sure "<a href="http://www.google.com/trends?q=apples%2C+oranges">apples, oranges</a>"). 

Where's the future here? Well I'm betting that Ajax will provide a huge boost to the Web Services model of having remote services handling transactions and outputting XML. Not some big fancy model, but just some XML. Once people start to pull these things in through Ajax, you can pull them in anything. Ajax will be the driving force and it will start to pull services up out of the dust. And it will be spotty, unspecified, <a href="http://www.google.com/trends?q=j2ee%2C+php">quick hacks</a> that just work ignoring all the formalisation of what was Web Services.

Perhaps I've listened to <a href="http://www.prescod.net/">Paul Prescod</a> a little to much.