---
layout: post
title: Timezones in Rails
categories: Rails
old: 1874
blog: andy-mckay
---
Are a bit of a mess. If you want an easy life assume that your app is only going to be ever run in one timezone and go to <em>environment.rb</em> and set:  ENV[&#39;TZ&#39;] = &#39;GMT&#39;&nbsp; <div><br /></div><div>The problem I had is that it seems rails is doing a cast of the date. I set a date as GMT, put into the database, a <em>timestamp with time zone</em> field. Then when you get it out it casts into my local timezone:  </div>
<pre>
>> sa = Thingy.new
>> sa.datepoint = Time.gm(2006,12,13) => Wed Dec 13 00:00:00 UTC 2006
>> sa.save ..
>> zz = Thingy.find(:all)[1]
>> zz.datepoint => Wed Dec 13 00:00:00 PST 2006
</pre>
<div>If you are having similar problems try trawling through the following posts on this issue. <a href="http://dev.rubyonrails.org/ticket/2282" target="_blank"></a></div><div><a href="http://dev.rubyonrails.org/ticket/2282" target="_blank">http://dev.rubyonrails.org/ticket/2282</a></div><div> <a href="http://dev.rubyonrails.org/ticket/4492" target="_blank">http://dev.rubyonrails.org/ticket/4492</a></div><div> <a href="http://dev.rubyonrails.org/ticket/4551" target="_blank">http://dev.rubyonrails.org/ticket/4551</a></div><div> <a href="http://blog.segment7.net/articles/2006/07/03/timezones-1-rails-0" target="_blank">http://blog.segment7.net/articles/2006/07/03/timezones-1-rails-0</a>&nbsp; </div><div><br /></div><div>On a light note, got Plone 3.0 up and running and made a first completely useless check-in on it. Yay.</div>