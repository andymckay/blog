---
layout: post
title: Downloading Firefox Marketplace Apps
categories: General
blog: andy-mckay
---

Apps can be freely downloaded from the Marketplace and that's a good thing. Yet every few weeks we get a bug filed along the lines of "you can download apps from the Marketplace without doing..." and we have to close it. This blog post is an explanation of why.

<h2>Hosted apps</h2>

In the beginning there were hosted apps. Hosted apps are completely hosted on the developers site, the manifest for that app is uploaded to the Marketplace and extra data added. In this scenario the Marketplace does not have any of the code for the app.

For this reason, we can't prevent downloading of hosted apps, any of the content or media for the app because the app and its media all exists on the developers site. All we do is point to the developers site.

For this reason, we also cannot prevent the downloading or installing of hosted apps that request a payment before installing. Paid apps can still be directly downloaded and installed from the developers site.

Paid apps do not restrict the installation of an app as a way to enforce payment. Instead we use a <a href="https://wiki.mozilla.org/Apps/WebApplicationReceipt">receipt checking mechanism</a>. When a payment is processed, the app is installed and a receipt is installed for the app. That receipt is added at install time and it's the app developers job to check that receipt.

Using receipts to enforce payment have a couple of advantages: receipts can come from any store that the developer chooses to accept, receipts can be revoked when refunds or other actions occur.

<h2>Packaged apps</h2>

Then enter packaged apps which were primarily added to allow developers to access sensitive APIs on the Firefox OS phone. A packaged app is the contents of the site zipped up and uploaded to the Marketplace.

Since the app contents are on the Marketplace, they can be reviewed for any malicious behaviour and signed. The platform downloads the packaged app and installs it, checking the signature on the way.

Any packaged app can be downloaded once its been made public. We don't restrict downloads, the contents of the packaged app are not secret and not intended to do so.

Similarly paid packaged apps do not restrict the installation of an app as a way to enforce payment. Instead we use the receipt *exactly* the same way as a paid hosted app.

In fact packaged apps are seen as a bit of hack and something Mozilla should not be focusing on long term. There's a rather long <a href="https://www.mail-archive.com/dev-b2g@lists.mozilla.org/msg10022.html">mailing list thread on this subject</a> and it sounds like the next iteration will be "browseable packaged apps" where it signed and hosted by the developer

<h2>Restriction of downloads</h2>

So then people file bugs stating "I can download any packaged app, even paid ones, the Marketplace is broken!". To repeat, downloads of paid apps are allowed, the receipt mechanism is the enforcement of payment. If you are an app developer and upload a paid app and do not check the receipt to prove payment, then that's your problem.

"Shouldn't we be protecting proprietary content in the packaged apps by preventing download?". Really? Should we be doing that? Just think about that for a moment. The developer can protect proprietary content within a packaged app, put it on their server and restrict the download through a mechanism of your choosing [<a href="#1">1</a>].

If we tried to stop this, it would be completely ineffective. All it takes is one person to download the packaged app, unzip it and grab that content and share it with everyone. It will probably be completely ineffective if you did it too, but it's not a promise we are going to make.

Remember this is an open platform and open technology. This is the key difference between the Marketplace and every other app store out there. We don't require you to use our payment system. We don't want any obfuscation or source code protection mechanisms on the platform. We don't try and make it difficult to pull apps off phones. Apps can be re-used on devices and platforms that support the open web.

This is the web, this is Mozilla, it's open. All roads on this approach lead to the rabbit hole that is DRM [<a href="#1">1</a>].

For that reason, currently the Marketplace doesn't restrict download of packaged apps.

[<a name="1">1</a>] Yes I know <a href="https://blog.mozilla.org/blog/2014/05/14/drm-and-the-challenge-of-serving-users/">Mozilla announced this</a> so at least that's a route you can go for protecting your content. Apps don't exist inside that DRM bubble.
