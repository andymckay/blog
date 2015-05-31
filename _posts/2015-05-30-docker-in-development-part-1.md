---
layout: post
title: Docker in development (part 1)
categories: General
blog: andy-mckay
---

There's lots of blog posts explaining how to use Docker in production. Those posts are filled with things like: don't run ssh, put only one thing in your container and so on. That's all cool. At the moment however, Mozilla is the opposite way around, we aren't using Docker in production. But, we are using it development. I'd like to use Docker in production for our sites and hope I can work with our operations and security to make that happen.

So here's some blog posts on how we (the Mozilla Payments team) use Docker in development. After all, pushing to production starts with development.

Credit here to <a href="http://github.com/muffinresearch/">Stuart</a> and <a href="https://github.com/jaredkerim/">Jared</a> who got me started on Docker and solved a few of these things.

Use a process manager
---------------------

This is often recommended against, the idea being that a container should do one things and one thing well.

At the end of a Dockerfile there is a <a href="https://docs.docker.com/reference/builder/#cmd">CMD</a> instruction. If that command ever terminates, the container is killed.

Assuming that you are developing on a server that reloads automatically (and why wouldn't you) *you will* break your server. Syntax errors, configuration errors, logic errors - you name it. All part of a days work. When that happens, *if the reload kills the process then your container exits*.

Each stopping of a container slows down your development. So don't do that.

Instead use a process manager like <a href="http://smarden.org/runit/">runit</a> or <a href="http://supervisord.org/">supervisord</a> to run your process. When you process dies (and it will because that's development) your container won't die with it. Once you've fixed your issue you can kick start your server again with <code>supervisord start [servicename]</code>, in the case of supervisord.
