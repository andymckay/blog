---
layout: post
title: How many Chrome Extensions run in Firefox?
categories: General
blog: andy-mckay
---

This question gets asked quite a lot around Mozilla now that we've been working on [WebExtensions](https://developer.mozilla.org/en-US/Add-ons/WebExtensions) for a while. We've been aiming for some sort of [Chrome parity](https://blog.mozilla.org/addons/2016/09/13/webextensions-and-parity-with-chrome/). A while back I wrote a script that I used on [arewewebextensionsyet.com](http://arewewebextensionsyet.com/). That produced a percentage of WebExtensions, but I always felt nervous about talking about it because there so many caveats it never felt accurate.

One of the major caveats was that the sample size of extensions I had from the Chrome store of 10,000 felt too small (that sample is the one used on [arewewebextensionsyet.com](http://arewewebextensionsyet.com/) currently). This week I used [this project](https://github.com/mdamien/chrome-extensions-archive) to parse the sitemap on the Chrome store and get 100,000 extensions and apps. A much more satisfying amount.

After stripping out apps, I then ran some scripts over those extensions to see how many would work in Firefox Nightly. Here's the output:

<table>
<tr><th></th><td>Number</td><td>Percentage</td></tr>
<tr><th style="text-align:right">Extensions</th><td>71,551</td><td></td></tr>
<tr><th style="text-align:right">Missing one or more permission</th><td>5,463</td><td>7.64%</td></tr>
<tr><th style="text-align:right">Missing one or more API</th><td>6,542</td><td>9.14%</td></tr>
<tr><th style="text-align:right">Easily convertable</th><td>62,792</td><td><b>87.76%</b></td></tr>
</table>

And here is an explanation of the long list of caveats and why I still am very cautious about this number.

<b>Caveats</b>

<ul>
<li>This doesn't mean they can run out of the box, it means they are </b>easily convertable</b>. Possibly the most obvious reason is that some of these extensions contain deprecated methods. Firefox hasn't implemented those deprecate methods. But if the developer updates their extension to use the new methods it will work in both Firefox and Chrome.</li>
<li>This method filters out apps, or extensions which use apps API, which can be a little heavy handed and hard for extension users to spot.</li>
<li>This method just looks at APIs and permissions. Which means that features that are required beyond those two methods are not covered. Web APIs for example aren't tested.</li>
<li>Whilst we've got many APIs, some of them may not be implemented exactly the same as Chrome. Or have bugs. That can cause some extensions to have some problems.</li>
<li>A grep of chrome.* for APIs reveals domains, typos, comments and some just wierd strings. If you ignore those there would probably be even more that work.</li>
</ul>

The result of these caveats is a list of variables which you can see in [the code](https://github.com/andymckay/examine-chrome-extensions). A more perfect scenario would be to download the extension, try loading it into Firefox and then seeing the result. But automating and building it all out would take more than one hour or two of hacking. If anyone wants to try to do that for 100,000 extensions let me know.

So what can you take from the number 87.76%? Some comfort that its probably somewhere around that number. I can say with a lot of confidence that over 75% of extensions are easily convertable to Firefox. A bit less confidence that over 85% are.

That sounds pretty good to me though and a credit to the hard work the team has put in this year.
