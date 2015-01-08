---
layout: post
title: Developers First
categories: General
blog: andy-mckay
---

A while back we developed Marketplace Payments. The first version of those was for Firefox OS and it was tough. There were lots of thing happening at once: building out a custom API with a payment provide, a backend to talk to our payment provider through multiple security hoops, integrating the relatively new Persona, working on the Trusted UI and mozPay and so on.

At the moment we are prototyping and shipping desktop payments as part of our final steps in Marketplace Payments. One thing that came clear a while ago was that desktop payments are much, much, much easier to use, test and debug.

Desktop payments are easier for *the developers who work on payments*. That means they are easier to get team members working on, easier to demo, easier to record, easier to debug, easier to test and so on. That dramatically decreases the development time.

In the meantime we've also built out things that make this much easier: a Docker development environment that sets things up correctly and a fake backend so you don't need to process money to test things out.

Hindsight is wonderful thing, but at the time we were actively discouraged from doing desktop development. "Mobile first" and "Don't slow down mobile development".

But inadvertently we slowed down mobile development by not being *developer first*.
