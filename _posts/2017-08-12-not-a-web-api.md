---
layout: post
title: Not a WebAPI
categories: Mozilla
blog: andy-mckay
---

As we've been working on WebExtensions we've been adding in more functionality and APIs to the framework. I repeatedly see concerns from developers about new APIs and how we plan to expose them, so I wanted to address those.

When you add in a new web API into a browser you basically set up for support of that API for a long time. It's really hard to determine what websites are using an API. If you can determine that, you've then got to get those websites to actually change their code... but old versions of browsers exist.

Backward compatibility of web sites is impressive, websites written in HTML from the very beginning still work in browsers. Compatibility of Web APIs is hard and Mozilla, along with other browser vendors, has the scars to attest to that. We have a most excellent team at Mozilla dedicated just to compatibility.

However, with WebExtensions we don't mean we have to be as conservative about what code or APIs we implement as we do with web APIs for a few reasons.

1. We already implement all of the community group specification (there's a bug to track any differences). The specification is a basic core.

2. We (Mozilla) have a copy of every single extension that runs in Firefox thanks to extension signing. We know how many extensions use every API and can contact all the authors of those extensions.

3. Through extension compatibility we can enforce what extensions run in what edition of the browser.

So when a new request for an API comes in, we evaluate it for security, privacy, UX, performance, internal seperation and other concerns. One of those concerns is to check that the API is high level and see if it could possibly be implemented by other browsers.

But implementation by other browsers isn't a blocker and we aren't going to wait for them. If, through the community group, other browsers pick it up that will be great. If we need to change or deprecate the API, that should be pretty easy. We have a deprecation plan for that, tools to do it and the team to make it happen.

WebExtensions at their core are compatible with other browsers, but extensions and their power have been a strength of Firefox and we'll need to play to that strength.
