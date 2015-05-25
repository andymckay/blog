---
layout: post
title: Accept Header
categories: General
blog: andy-mckay
---

Recently I used an endpoint that had the following <a href="http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html">HTTP Accept Header</a>:

<pre>
*/*; q=0.5, application/xml
</pre>

This server is saying it will accept "application/xml", but if that's not available, then it will accept anything. The "q" indicates that "application/xml" is preferred.

The assumption is that if you send a piece of content, you will send an appropriate HTTP Content-Type Header. Then the server will know how to parse it.

This server wanted a token, just some string, echoed back to it. Given the HTTP headers, it seemed perfectly for me to send:

<pre>
Content-Type: application/json
"some token"
</pre>

Or even [<a href="#xml">1</a>]:

<pre>
Content-Type: application/xml
&lt;?xml version="1.0" encoding="UTF-8"?&gt;&lt;token&gt;some token&lt;/token&gt;
</pre>

As it turned out, it only accepted one thing and thats "test/plain" so something like:

<pre>
Content-Type: text/plain
some token
</pre>

This endpoint was hit using web interface, which was hitting a remote server, so took a little time to debug. But here's the thing, I think accepting `*/*` is a little unusual, unless you are you really going to accept anything, really anything? Will you accept `text/csv`, how about `audio/ogg` or `video/ogg`? Here's <a href="http://www.freeformatter.com/mime-types-list.html">one list</a> of types [<a href="#types">2</a>].

The advantage of using a limited Accept header is that the server and client in question can figure things out without you having to do extra code. If the server explicitly declares what kinds of responses it can accept, then the client can check it can actually return the data encoded in that manner.

If your endpoint sends a `*/*` Accept header and someone sends you something you don't know how to parse, hopefully you'll send them back a <a href="http://httpstatus.es/406">406</a> response back. To tell the caller that you don't Accept that kind of response.

In this example, I've been talking about a server API. But of course this is for anything in the HTTP world, for example my browser sends the following: `text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8`. It would much rather rather have HTML or XHTML, but will Accept anything and then do its best to render it. That seems reasonable for a browser.

But for an API that only accepts JSON or XML? Maybe we should make an effort to tighten up our Accept values on our APIs [<a href="#yes">3</a>].

<p><b>Footnotes</b></p>

<ol>
<li><a id="xml"></a>Although it was never stated what the syntax for the XML was, so who knows.</li>
<li><a id="types"></a>There isn't really a definitive list.</li>
<li><a id="yes"></a>Yes, that includes some APIs I've written.</li>
</ol>
