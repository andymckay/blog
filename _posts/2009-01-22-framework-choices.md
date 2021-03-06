---
layout: post
title: Framework choices
categories: Django
old: 2175
blog: andy-mckay
---
<p>There was an interesting post on <a href="http://almaer.com/blog/why-i-often-prefer-prototype-too">Dion's blog about using Prototype</a>. I have to throw my hat in the ring there too, I often prefer prototype and fluctuate between that and jQuery.</p>
<p>One application I'm working on revolves around an interface built in Ajax. It started off as complicated, but is rapidly getting simpler - but I moved from jQuery to Prototype. I found that while jQuery was good there were times when I just couldn't get it to co-operate. I was bind a DOM element to an event and then changing the DOM and no matter what I did could no rebind that event to the DOM.</p>
<p>I read the FAQ's, I asked in #jquery but couldn't get anywhere. That magical $ function which is so handy was just swallowing everything. I plopped back into Prototype and find it an easy switch that involved less documentation reading and odd errors. For a while. But I certainly found that Prototype has a place.</p>
<p>With some serendipity <a href="http://superjared.com/entry/rails-versus-django/">this post appeared</a>. A while ago we made this decision at <a href="http://www.bluefountain.com">Blue Fountain</a>, well let's rephrase, I made this decision. As it turned out, it made absolutely no difference, but the key reasons at the time running through my head were:</p>
<ol>
<li>All the Ruby and Ruby on Rails developers have moved on leaving Python developers</li>
<li>We do Plone and there is more opportunity for an overlap between Django and Plone than Rails and Plone</li>
<li>Clients don't really care either way</li>
</ol>
<p>The other issues like Django is faster and easier to develop and has great features like the admin interface, were there. But the above made it a slam dunk.</p>
<p>When tool or programming choices are made, they are rarely made for the reasons that you think. All the big comparison charts can be made, but in the end the reasons people pick A over B can be the oddest ones of all: "We've already paid for an Oracle license" for example.</p>
<p>Want a reason, for Django, <a href="http://bit.ly/Pa55">here's a good one</a>.</p>