---
layout: post
title: Your own AMO
categories: General
blog: andy-mckay
---

Back when I started on <a href="https://addons.mozilla.org">addons.mozilla.org</a> (AMO) there was a suggestion lurking in the background... "what if I wanted to run my own copy of addons.mozilla.org"?

I'm never been quite sure if that would be something someone would actually want to do, but people kept mentioning it. I think for a while for some associated Mozilla projects might have tried it, but in the six years of the project I've seen zero bugs about anyone *actually* doing it. Just some talk of "well if you wanted to do it...".

I think we can finally lay to rest that while AMO is an open source project (and long may it stay it that way) and running your own version is technically possible, it's not something Mozilla should worry about or support.

This decision is bolstered by a couple of things that happened in the add-ons community recently: add-on signing, which means that Mozilla can be the only one to sign add-ons for Firefox and the use of Firefox Accounts for authentication.

These are things you can work around or re-purpose, but in the end you'll probably find that these things are not worth the effort when it comes down to it.

From a contribution point of view AMO is <a href="http://addons-server.readthedocs.io/en/latest/topics/install/docker.html">very easy to set up and install these days</a>. Pull down the docker containers, run them and you are going. You'll have a setup that is really similar to production in a few minutes. As an aside: development and production actually use slightly different docker containers, but that will be merged in the future.  

From a development point of view, knowing that AMO is only ever deployed in one way makes life so very much easier. We don't have to support multiple OS's, environments or combinations that will never happen in production.

Recently we've started to move to API driven site and that means that all the data in AMO is now exposed through an API. So if you want to do something with AMO data, the best thing to do is start <a href="http://addons-server.readthedocs.io/en/latest/topics/api/index.html">playing with the API</a> to grab some data and remix that add-on data as much as you'd like (<a href="https://github.com/andymckay/addons-server-mirror">example).

So AMO is still open source and remain so, it just won't support every single option in its development and I think that's a good thing.