---
layout: post
title: Announcing Arecibo
categories: clearwind
old: 2128
blog: andy-mckay
---
<img src="http://media.areciboapp.com/img/pictures/pic02.png" style="float: right; padding: 1em" width="200px" />
<p>One of the problems I find annoying in web development is the bug reports from users. It could be your application has gone live, or it's still going through testing. But feedback tends to be vague "I clicked this and it didn't work" or some such.</p>
<p>There often follows a few emails with questions like "what browser did you use" or "did you get an error message". Those emails are time consuming and expensive. They also have an air of unprofessionalism about them. Why can't you figure this out for yourself?</p>

<p>In some applications like Plone or Django the error handling is well developed. But in others (e.g. Rails) it's not as good. Plus, we rarely have the luxury of living in an isolated world. One application I developed a while back had an Apache front end to Moodle (PHP), Django (Python), Rails (Ruby) and Plone (Python). When an error occurred, looking through all the different possible logs was not easy.</p>

<p>For this reason I'm announcing the <a href="http://www.areciboapp.com">beta of Arecibo</a>. It's a hosted service that listens for errors on your websites. When an error occurs a HTTP post or email containing the details can be whisked off to Arecibo, allowing you the developer to view the error and all its details. Arecibo can send out notifications if you wish via Twitter, email, RSS feeds and the like.</p>

<p>Currently there are implementations to allow you to send issues to Arecibo from JavaScript, Python, PHP, Ruby and more detailed ones for Django and Plone. The JavaScript one is really nice because in just a few lines of JavaScript, you can have servers like Apache send your errors to a centralised repository.</p>
<p>It's currently in beta and available at <a href="http://www.areciboapp.com">http://www.areciboapp.com</a>, there's currently no limit on signing up, but if it's popular I might lock it down. Give it a try, kick the tires, tell me the bugs (well the ones Arecibo didn't catch).</p>                 