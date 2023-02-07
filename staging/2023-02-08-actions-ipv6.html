---
layout: post
title: Actions, IPv6 and Fly.io
categories: general
blog: andy-mckay
---

I stood up a service on fly.io as a subdomain of an existing site. You can do this by adding a CNAME record to your DNS pointing to the fly.io instance. In this case [clearwind.ca](https://clearwind.ca) is managed on Google Domains and currently points to GitHub pages site. Then [notifications.clearwind.ca](https://notifications.clearwind.ca) is a fly.io instance. 

When you do this on the dashboard, you'll get a page that looks like this:

<img src="/files/2flyio-ipv6.png">

Added it all in, waited for DNS to update and it all worked. However, when I tried to hit using `wget` or `curl` in GitHub Action, I kept hitting: 

```
Connecting to notifications.clearwind.ca (notifications.clearwind.ca)|2a09:8280:1::db06|:443... failed: Network is unreachable.
```

It's correctly resolved the IPv6 domain, so I wasn't quite sure what the problem was. I couldn't spot anything in the Actions documentation. In the end it was simple as adding in the IPv4 address for the domain. That isn't shown on the fly.io dashboard, but you can find it in the `Dashboard` > `Overview` > `Application` > `IP addresses` section.

In my case adding in an A name to that IP address fixed the issue and `curl` and `wget` worked as expected. Why fly.io is doing this is [covered here](https://community.fly.io/t/announcement-shared-anycast-ipv4/9384).