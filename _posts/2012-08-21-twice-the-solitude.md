---
layout: post
title: Twice the solitude
categories: Mozilla
old: 2347
blog: andy-mckay
---
<p><a href="http://github.com/andymckay/solitude">Solitude</a> is a server to do payment processing for the <a href="https://marketplace.mozilla.org">Mozilla Marketplace</a>. In my <a href="https://mckay.pub.ca/blog/andy/2345/">last post</a> I blogged about how Solitude seperates itself from the client application to provide a level of defense by depth.</p>
<p>Well Solitude provides yet another layer of defense. It can be run in two modes: as a server or as a server and a proxy. Currently this mode works with PayPal, but is applicable to any third party payment provider. The former looks like this:</p>
<img src="/files/solitude.png">
<p>In this case if a security breach occurs on the Solitude server you'll get access to the credentials to access PayPal and some key tokens to access PayPal with. You'd need to get into both the file system and the database to get that information. But still it's just one server.</p>
<p>In the latter mode, Solitude is run twice, once as server with access to the database and once as a proxy that can access PayPal:</p>
<img src="/files/solitude-two.png">
<p>In this scenario a security breach needs to occur on the Solitude database server and the proxy. You'd need to get into both the file system and the database, but on two seperate machines.</p>
<p>To have the database server talk to a proxy, point to the proxy in the Solitude settings file:</p>
<pre>PAYPAL_PROXY = 'https://addons.mozilla.local/proxy/paypal'</pre>
<p>On you proxy server, run the server with the environment variable:</p>
<pre>SOLITUDE_PROXY='enabled'</pre>
<p>Just make sure you don't do something silly and connect that instance to the database (you should block that at the network level anyway), on the proxy your set:</p>
<pre>DATABASES = {'default': {}}</pre>
<p>Should work. More information on setting this up is in the <a href="http://solitude.readthedocs.org/en/latest/topics/paypal.html#proxy">Solitude docs</a>.</p>