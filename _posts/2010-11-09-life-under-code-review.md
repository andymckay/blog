---
layout: post
title: Life under code review
categories: Mozilla
old: 2288
blog: andy-mckay
---
<p>There were a few things that hit me in the first few weeks of working at Mozilla. There were the obvious things about how smart everyone is, how fun they are and how I felt at home quickly. But there were two techie things that really slowed me down: git and code reviews.</p>
<p>I've used git before, but not this amount of branching and rebasing. After some frustrating days I've found my peace with git and a nice workflow that works pretty well. (I'm sure I have just cursed myself and will have days of hell with git now.)</p>
<p>As for code reviews, I haven't faced code reviews to this level before. Sure, I've committed code on an open source project and people have looked at it and politely (most of the time) pointed out problems. A few places I've worked in have commented that they would do code review and even set the things in place, but never done it, so I've never faced code review to this level before.</p>
<p>What level is it? I don't know, but as the new guy it seemed tough. There's a strict adherence to <a href="http://www.python.org/dev/peps/pep-0008/">PEP 8</a> down to trailing commas, 79 char lines (and not using \), comments as proper sentences and so on. No more using " and ' interchangeably.</p>
<p>I was warned the first checkin or two would get me beaten up a bit. Actually it turned out to be not too bad, but I know people were taking it easy on me. Now the checkins are getting easier, I'm thinking more before I push to code review and the style is in my head. I can really see this paying off.</p>
<p>So if you are starting on a code review process and feeling a bit down, remember it's for a good reason. It's making you better for a few reasons:</p>
<ul>
<li>You start reviewing your own code (or in my case look at it several times with a healthy dose of paranoia).</li>
<li>Code gets better for everyone and with a style guide, code becomes easier to read.</li>
<li>It's a good opportunity to learn new styles and new API's that otherwise you might not see.</li>
<li>It will get you used to criticism and feedback from your peers, who are way smarter than you.</li>
</ul>
<p>The one thing I do find a challenge, is taking the code review in the bigger picture and not just focusing on the syntax, that's easy to spot. And now <a href="http://www.osnews.com/story/19266/WTFs_m">the obligatory code review cartoon</a>.</p>