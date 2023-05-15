---
layout: post
title: Service catalog
categories: general
blog: andy-mckay
---

When I joined the on-call rotation at GitHub as we [launched GitHub Actions](https://docs.github.com/en/actions), being on-call was something that was pretty new to me. I learnt a lot and had some amazing experienced colleagues who taught me a lot and there's still so much to learn.

At one point we can probably estimate GitHub had about 800 developers working [^1] on the site and all the parts, spread out across the globe. It also interacted with teams at other companies, such as Microsoft and the Azure teams.

Navigating and understanding your services, teams and dashboards in an organization is hard, it was at GitHub. Repeatedly I've spoken to organizations building tooling to solve this internally.

Some of the problems you might have in your engineering organization 👇

## Navigating your engineering services

As the size, speed and scale of your organization grows just navigating the teams grows harder. New people who join the company can struggle to find who does what and what's important. Veterans struggle to keep up with changes.

What do those teams do? Who's on the teams? Where do they hang out and communicate? What dashboards do they have?

If your answer is a document somewhere, a wiki, or so-on, I bet it's not up to date. The moment those documents land (I've written a few), they are out of date.

## Quality of your services

So you've got a series of services that make up your product. Those will be spread out across the organisation with different ideas and leaders. Spreading ideas and information out across those services and teams is hard.

Tools like Datadog, Splunk etc, are available to crunch all the run time information and provide you with good information about how users are using your service.

But there are other metrics and measurements within an organisation that you need to make sure are kept up to date. How many security issues are there on the service? Are they being dealt with quickly? Are legal requirements satisified? Has the team got on-call rotation setup? And so on.

In a large organization you want to ensure that teams are ready to deal with problems before its too late.

## How do we fix a problem?

Most of the time when something went wrong at GitHub we'd go through a progression that looked like this, in roughly this order:
* What just got deployed?
* What got migrated or transitioned?
* What just got turned on or off?
* What external services we depend on are having problems?
* What are users doing to the site?

In an incident your time to mitigate is really important and you need concise and clear information as soon as you can. Cognitive overload, lack of clarity in an incident slows everything down and causes stress and anxiety.

Even just knowing the key deployments and releases over the last hour and then the right teams to contact about those changes reduces the time to mitigate incidents the majority of the time.

## Service catalog release

Over the last while I've been building a tool to do this. The service catalog is tightly integrated into GitHub and GitHub Actions. Best of all it's free, open source and available for anyone to us straightaway.

Check it out here 👉 https://github.com/clearwind-ca/service-catalog

<img src="files/catalog-services-may-15.png" width="500px">

Watch this space for some more articles about it and if you are interested in using this, [drop me a line](https://clearwind.ca/).

[^1]: This is an estimate, I don't have the numbers and can't remember the exact number 🤷‍♂