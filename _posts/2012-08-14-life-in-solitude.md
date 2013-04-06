---
layout: post
title: Life in solitude
categories: Mozilla
old: 2345
blog: andy-mckay
---
<p>There's quite a few libraries to integrate PayPal with Django, including <a href="https://github.com/johnboxall/django-paypal">django-paypal</a> and an <a href="https://www.x.com/devzone/articles/getting-started-paypal-django">example from PayPal</a>. We needed a library to integrate with PayPal that uses <a href="https://www.x.com/developers/paypal/documentation-tools/api/preapproval-api-operation">pre-approval</a>. Pre-approval means that payments can be made automatically, without any interaction. To use this a token for the user is stored in the marketplace.</p>
<p>Therein lies some security issues. Tokens and PayPal credentials or keys are being stored on your server., perhaps your database or settings files. Encryption of your database fields will help, but we can do probably do more.</p>
<p><a href="https://github.com/mozilla/solitude">Solitude</a> is a <a href="http://djangoproject.com/">Django</a> project to provide a REST interface to PayPal (and potentially other payment providers). It uses <a href="https://github.com/toastdriven/django-tastypie">TastyPie</a> to provide the API.</p>
<p>Currently the API is focused purely on what the Mozilla Marketplace needed, but it includes the ability to create buyers and sellers, store pre-approvals, do payments, do refunds and check account statuses. It also features a PayPal mock so that you can interact with solitude without having to interact with PayPal at all.</p>
<p>For example to create a buyer account, then create a pre-approval (and then bounce to PayPal) and then save that token you'd do:</p>
<script src="https://gist.github.com/3346503.js"> </script>
<p>Solitude stores the payments and transaction information, but knows absolutely nothing about the buyers and sellers. The calling application just passes id's for those users. Key parts of data, anything that might be personal or a security issue, is encrypted using <a href="http://dev.mysql.com/doc//refman/5.5/en/encryption-functions.html#function_aes-decrypt">MySQL AES encryption</a>.</p>
<p>The primary goal here is <a href="http://en.wikipedia.org/wiki/Defense_in_depth_%28computing%29">defense by depth</a> and solitude ensure that simple attacks such as SQL injections on the marketplace will fail to render anything useful for payments. Not that we'll be invulnerable to attack, it will just be harder to get through to the next layer.</p>
<p>A longer term goal is that solitude provides a payment server for all of Mozilla, not just the marketplace, should that be something we want to use. Solitude is currently in an early version and isn't rolled out yet to production, so take the code for what it's worth.</p>