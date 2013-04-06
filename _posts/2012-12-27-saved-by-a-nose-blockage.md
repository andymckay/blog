---
layout: post
title: Saved by a nose-blockage
categories: Django
old: 2359
blog: andy-mckay
---
<p>Was slightly pleased to see today that nose-blockage saved our test suite. A change in the <a href="https://github.com/mozilla/django-browserid">django-browserid</a> library meant that on each call to login in our test suite, it was going to make a HTTP request to <code>verifier.login.persona.org</code>.</p>
<p>Fortunately <a href="https://github.com/andymckay/nose-blockage">nose-blockage</a> stops that request and 1,012 tests failed. If we didn't have that blockage in place, out test suite would have made over 1,012 HTTP requests to the persona.org server on each test run. That would have made our test suite slower and dependent on an external service. Not a big issue to fix, but this is a really good example of why nose-blockage can be useful to save you from libraries that change. Example failure:</p>
<pre>
-------------------- >> begin captured logging << --------------------
django_browserid.base: INFO: Verification URL: https://verifier.login.persona.org/verify
requests.packages.urllib3.connectionpool: INFO: Starting new HTTPS connection (1): verifier.login.persona.org
blockage.plugins: WARNING: Denied HTTP connection to: verifier.login.persona.org
--------------------- >> end captured logging << ---------------------
</pre>