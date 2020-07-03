---
layout: post
title: Ajax services
categories: Plone
old: 1837
blog: andy-mckay
---
A while back I posted on <a href="https://mckay.pub.ca/blog/index.php?p=39">the end of web services</a>. In this post I was proposing that Web Services as traditionally represented are dead and a new batch of Ajax based web services will arise.

The thing is most people don't actually do "Web services". Most of the time it's used to improve the UI experience locally for users and the idea of consuming remote data doesn't happen. This is because of a technical problem. A client can't make a request to a remote server in Ajax. 

There are many ways around this on the client, including using form posts and some toolkits Dojo abstract that out. There is a way to do this at the server as well, using say Apache's Proxy pass. That allows the request to still appear in the local domain, but behind the scenes Apache is doing the forwarding for you. 

Once you've got this done you are opened up to the world of web services. Any server that provides a datasource or interaction via Ajax or XML is open to be used on your client. For example:

<ul>
	<li>Want to show an RSS feed in your site? Well if you don't want to actually parse the data on the server, why not parse it on the client, using an Ajax RSS reader (<a href="http://ajax.phpmagazine.net/2005/11/ajax_rss_reader_step_by_step_t.html">example</a>)</li>
	<li>Want to show the weather on your site? You don't want to store that on the server, you just want a pretty graphic, pull it using one of these (<a href="http://blogs.pathf.com/agileajax/2006/07/bjax_with_greas.html">example 1</a>, <a href="http://saratoga-weather.org/scripts-WD-AJAX.php">example 2</a>)</li>
        <li>Want a spell checker in Plone, but don't want to install the spell checking libraries on your server because its a pain? Then get the spell checker from <a href="http://www.clearwind.ca/software/clearspell">ClearWind.</a></li>
</ul>

This approach is more akin to the Web services of old, it abstracts away services into other servers and allows you to re-use both ends of the equation. Clients for displaying widgets can be used in multiple places and the servers can be re-used in a service model. That's why I'm calling it <strong>Ajax Services</strong>.

An Ajax Service is a:

<ul>
	<li>An Ajax based client that can be re-used in multiple different sites.</li>
	<li>A server side service that can be consumed by an web site using the client, not just the local site the site was intended for. The service uses REST for incoming requests and XML for responses, allowing easy Ajax integration in a client.</li>
</ul>

One example is the Ajax Proxy for Plone. This is a server side proxy that lives inside Plone. It takes incoming requests from the client and proxies them on. There are a few nice things this gives you: caching, security, transformations and load balancing to name a few. Once you've got a generic proxy for your server you can load up your client with services pointing to multiple places and get true web services back to your client.

Here's an example:

<ul>
	<li>The browser fires off the Ajax request, normally a GET or other HTTP verb.</li>
	<li>The request comes into your local server (for example Plone) on the same domain.</li>
	<li>The local server does some processing of the payload (for example caching) and figure's out where to send it on to.</li>
	<li>The local server forwards the request on to the remote server and waits for a response.</li>
        <li>The response is received and processed.</li>
        <li>The response is then passed back upstream to the browser and the user gets the data.</li>
</ul>

Apologies for the ramble, I'll try to be more coherent and release more code soon. For the moment here's two releases: <em>AjaxProxy</em> is a tool for Plone that acts as a generic Ajax proxy allowing you to proxy any request on through Plone. <em>ClearSpell</em> is a spelling tool for Plone that provides spell checking on any input or textarea. Unlike previous spell checking, there is no dependencies other than AjaxProxy, the ClearWind spell checking service provides the spell checking libraries. 

More to come...