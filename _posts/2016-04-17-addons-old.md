---
layout: post
title: The add-ons burden
categories: General
blog: andy-mckay
---

Before I got into working on add-ons I didn't realise the burden that the old style add-ons have created for everyone in the add-on. I do think add-ons are great and what they've done to help Firefox users and Firefox has been excellent. But the more I've understood the ecosystem, the more I'm concerned by it.

This is a negative post, focusing on the problems, but I don't think these are a surprise for people involved in add-ons. No matter how fondly some people might look at add-ons of the past, they have some real problems that haven't been addressed.

## For users

* There is no information what an add-on does beyond the description. It might slow down the browser in various ways. It might mess with the user interface or settings.

* Because an add-on can do pretty well anything, the security can be problematic.

* For most users there is no difference between Firefox and the add-ons. There's no way to tell that an add-on caused problems or wierd behaviour.

## For Firefox developers

* Because there is no layer between many of the XUL and XPCOM internals of Firefox, its really hard for Firefox developers to change things without being hampered by the effect on add-on developers. It's really hard to move Firefox forward when every change might break the experience for an unknown number of users.

* Problems reported in Firefox are harder to diagnose and add-ons are the first line of inquiry.

## For Add-on developers

* Every release of Firefox can break your add-on because Firefox developers are changing the internals and progressing. You might get a notice about it if we can find it (see below).

* The API for what an add-on can do is as about as large the Firefox internals itself. Thats a huge, sporadically documented and continually shifting API. Developers shouldn't have to be Mozilla experts to produce an add-on.

## For the add-ons team

* Every release the add-ons team trawls through bugs and finds things that could cause problems for add-ons. We then alter the addons.mozilla.org validator, run add-ons through them. Squint at the result, see if they sound right and then repeat. Then tell all the add-on developers about them.

* Reviewing add-ons places a security burden upon Mozilla to prevent malicious add-ons going through. Add-ons could be obfuscated or just plain complicated and add-on developers want their add-ons approved. This creates a huge amount of tension between everyone.

People have asked me questions about where WebExtensions will go and I have to refer back to this list and make sure that when we implement that feature we don't fall into the same trap. So to repeat: **what's really important is to look back at the decisions that led to this and stop ourselves repeating these problems**.

WebExtensions and the path forward is looking really good and I know that it will get so much better, I'm genuinely excited by that.
