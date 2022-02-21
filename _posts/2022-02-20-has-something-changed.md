---
layout: post
title: Using GitHub Actions to spot changes
categories: General
blog: andy-mckay
---

One pattern that has become quite common at GitHub, for me, is using Actions to spot if something has changed. I use this to track changes in project boards, or changes in JSON payloads, changes in websites... basically anything out there.

The basic anatomy is:
* Have a workflow file that runs on a [schedule](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#schedule)
* Create a data file in your repository to store the data, for example in JSON or CSV.

When run:
* The workflow loads the data file from the previous time.
* Loads the data from the source, probably with a bit of massaging to get it just right.
* Compare the two.
* Send any changes to a [slack channel](https://github.com/marketplace/actions/slack-messenger).
* Save the data file.
* Commit the data file.

Then next time it runs, it just repeats the process. I wrote one recently to notify GitHub staff internally when a job gets posted to our external job board and its 85 lines of Python that we whipped up in an hour.

**Please note:** there is an [Acceptable Use](https://docs.github.com/en/github/site-policy/github-acceptable-use-policies#3-conduct-restrictions) policy for GitHub and if you do this alot you might hit that.