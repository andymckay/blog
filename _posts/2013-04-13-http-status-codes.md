---
layout: post
title: HTTP status codes
categories: General
blog: andy-mckay
---
For the <a href="https://marketplace.firefox.com/">Firefox Marketplace</a> we
are building out a REST API. We have had one for a while for app submission and it
is now growing to provide an API for fireplace, an app that will go onto
Firefox OS phones.

When writing a REST API you have an opportunity to be more expressive than just
returning web pages and a few normal statuses like 200, 302, 403 and 500. A HTTP status
can tell the client quickly and succinctly what happened. Most client libraries assume
that a status with a range either means a success or failure. So returning a status
code 202 over 200, will work in pretty much every library and convey more information.

Some of the HTTP status codes we are using:

* <a href="http://httpstatus.es/201">201 Created</a>: we have created the new resource (e.g.: app).
* <a href="http://httpstatus.es/202">202 Accepted</a>: we haven't processed yet, but we will do. Normally this means we've pushed the request off to a <a href="http://www.celeryproject.org/">Celery</a> queue.
* <a href="http://httpstatus.es/402">402 Payment Required</a>: you tried to install an app without paying for it.
* <a href="http://httpstatus.es/409">409 Conflict</a>: this would generate a conflict in the state of the resource. For example you tried to POST something instead of a PUT or PATCH.
* <a href="http://httpstatus.es/429">429 Too Many Requests</a>: you've made too many requests and we've throttled you.
* <a href="http://ttp://tools.ietf.org/html/draft-tbray-http-legally-restricted-status-00">451 Unavailable for Legal Reasons</a>: the app is unavailable for legal reasons, perhaps due to region or content restrictions.

Unfortunately some of these status codes are a little less well defined. For code 451 there are currently at least 3 proposed meanings: <a href="http://msdn.microsoft.com/en-us/library/gg651019">something about users mailboxes</a> and <a href="https://tools.ietf.org/html/rfc2326#page-42">something RTSP</a> along with the <a href="http://ttp://tools.ietf.org/html/draft-tbray-http-legally-restricted-status-00">legal restriction</a>. But hopefully users of our API will realise we aren't using Exchange or RTSP and maybe even <a href="https://zamboni.readthedocs.org/en/latest/topics/api/submission.html#get--api-v1-apps-app-%28int-id%29|%28string-slug%29-">read the docs</a> to find out what this means.

Using HTTP statuses is simple and descriptive. I like that.
