---
layout: post
title: Docker in development (part 2)
categories: General
blog: andy-mckay
---

Tips for developing with Docker.

Write critical logs outside the container
-----------------------------------------

You are developing an app, so it will go wrong. It will go wrong a lot, that's fine. But at the beginning you will have a cycle that goes like this: container starts up, container starts your app, app fails and exits, container stops. What went wrong with your app? You've got no idea.

Because the container died, you lost the logs and if you start the container up again, the same thing happens.

If you store the critical logs of your app outside your container, then you can see the problems after it exits. If you use a process runner like  <a href="http://supervisord.org/">supervisord</a> then you'll find that <a href="https://docs.docker.com/reference/commandline/cli/#logs">docker logs</a> contains your process runner.

You can do a few things here, like move your logs into the process runner logs, or just write your logs to a location that allows you to save them. There's lots of ways to do that, but since we use supervisord and <a href="https://docs.docker.com/compose/">docker-compose</a>, for us its a matter of making sure supervisord writes its logs out to a <a href="https://docs.docker.com/reference/builder/#volume">volume</a>.

See also <a href="/2015-05-30-docker-in-development-part-1/">part 1</a>.
