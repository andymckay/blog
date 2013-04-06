---
layout: post
title: Accessing JSON from Adobe Air
categories: Air
old: 2243
blog: andy-mckay
---
<p>So you have a REST style API on a server that returns JSON that you'd like to access from Adobe Air app (using Javascript). Seems simple right? There's a few tricks in there.</p>
<p>Firstly cross domain. Once you've set up your <a href="http://help.adobe.com/en_US/AIR/1.5/devappshtml/WS5b3ccc516d4fbf351e63e3d118666ade46-7cb1.html#WS5b3ccc516d4fbf351e63e3d118666ade46-7ca9">URLLoader</a> and made your request, you'll get a response back. The only problem is that you can't access the data in it. In the Air Introspector:</p>
<pre>event.target</pre>
<p>Will show you there's a data element and the data contains your JSON. But no matter what, you can't access it:</p>
<pre>event.target.data</pre>
<p>Will always return "undefined", not "You can't access this due to cross domain policy" or something useful. So go to your server and add in the following at the URL <code>/crossdomain.xml</code>:</p>
<pre>&lt;?xml version="1.0"?&gt;
&lt;!DOCTYPE cross-domain-policy SYSTEM "http://www.macromedia.com/xml/dtds/cross-domain-policy.dtd"&gt;
&lt;cross-domain-policy&gt;
&lt;allow-access-from domain="*" /&gt;
&lt;/cross-domain-policy&gt;
</pre>
<p>Now you've got your JSON. So you could just eval it? Fortunately Adobe blocked that, eval is nasty anyway. How about using <a href="http://api.jquery.com/jQuery.parseJSON/">jQuery.parseJSON</a>? Nope:</p>
<pre>Adobe AIR runtime security violation for JavaScript code in the application security sandbox</pre>
<p>So I grabbed <a href="http://www.json.org/js.html">json2.js</a> and did:</p>
<pre>JSON.parse(event.target.data)</pre>
<p>...and then we've got the JSON.</p>