---
layout: post
title: Scaling Rails
categories: Rails
old: 1955
blog: andy-mckay
---
<p>An interview with one of the Twitter developers.</p>
<blockquote>
Once you hit a certain threshold of
traffic, either you need to strip out all the costly neat stuff that
Rails does for you (RJS, ActiveRecord, ActiveSupport, etc.) or move
the slow parts of your application out of Rails, or both.</blockquote>
<blockquote> If you're looking to deploy a big web application
and you're language-agnostic, realize that the same operation in Ruby
will take less time in Python. All of us working on Twitter are big
Ruby fans, but I think it's worth being frank that this isnt one of
those relativistic language issues. Ruby is slow.</blockquote>
<cite><a href="http://www.radicalbehavior.com/5-question-interview-with-twitter-developer-alex-payne/">Link</a></cite>
<p>Scaling anything is hard and this seems to be a common payoff, you can get to a good size quickly, but scaling past that is hard - or slow to get there and scale well. I would always, always rather be faced with the former problem.</p>