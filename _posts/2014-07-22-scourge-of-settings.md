---
layout: post
title: The scourge of settings files
categories: General
blog: andy-mckay
---

When zamboni started on Django, many years ago we started writing settings files. These python files are used by Django to determine site behaviour. It started off optimistically, developers would have have a local settings file, the production servers would have a slightly different one and that's that.

Except then tests get run and tests might need different settings, so a setting file was created for that. Then multiple staging servers got added, so multiple settings file were added for that. Then we split the site into two sites (AMO and Marketplace) so another settings file was added. That meant we could refactor some settings into a base file (my fault).

Each time a new feature was added emails were sent saying how to adjust your settings file locally. Then a settings change log was added that detailed what you needed to change in your settings file.

By now settings files were hundreds of lines long. When new developers joined, they were just sent a copy of someone else's settings file and that got them up and running.

I started thinking about how to make a virtual machine for the <a href="https://marketplace.firefox.com">Marketplace</a> and was start to think about tools for manipulating settings files, like Puppet. That's when I realised I was looking at the problem all wrong, the problem was that there was a need for a settings file at all. That was the root cause that needed to be fixed.

So we set down a new path. Since all the settings for production servers are in source control, the default should be that the settings value has a sane default and works without custom changes out of the box. Production servers can then override them.

Looking at the settings files, we found:

* Values that needed to be the same, but were set differently in three different projects. Those were cleaned up.
* Values that had to be overridden in the local settings files because they were based upon the value of an earlier setting. Those were moved into a lookup method in code.
* Values that were set because of security concerns, e.g.: SECRET_KEY. Those were set to default values. A check method was added to startup to raise an error if those were not altered on production servers.
* Values that were just never used. Those were deleted.

We then looked at the settings and grouped them into two values:

* Settings that are likely to be changed.
* Settings that might be changed locally for development or testing, but it's pretty unusual.

For the former, we used environment variables instead of settings files. This has the advantage of meaning that the environment variables are shared across the projects. We've currently got only <a href="https://marketplace.readthedocs.org">five of those</a> and they cover databases and urls. Those default to sane values, so even those are optional.

Finally we re-ordered the settings files into three categories:

* Environment setting: paths, hostnames that sort of thing.
* Django specific settings: which don't really need documentation.
* Application specific settings: which are commented well.
* Each of those categories is alphabetized, unless something needs to go before another.

The end result is that marketplace can be installed and run without any custom settings files. That's quicker, easier and saner to setup and maintain.
