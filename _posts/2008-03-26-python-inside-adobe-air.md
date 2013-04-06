---
layout: post
title: Python inside Adobe Air
categories: Air
old: 2066
blog: andy-mckay
---
<p>Adobe Air is nice, but I have to say, moving onto the next steps has stalled me because I don't have a set of libraries to play with. Consider these two toy quick apps:</p>
<ul>
<li>SVN proxy that monitors all your SVN traffic, allowing you to log exactly what you logged when (useful with multiple SVN servers) and show statistics, including automatic timesheet hint generation.</li>
<li>IMAP statistics tool that tells when and where your email traffic is coming from and going to.</li>
</ul>
<p>Both of these would be simple to do in Python and matter of calling out to say HTTPServer, urllib, imaplib for the various protocols to setup proxies or query IMAP servers. However how do I do that. I've got access to javascript and Flex. I'm stuck with: clunky system calls to another language, passing things off to the cloud (not sure thats possible or desire-able) or looking for SWF libraries.</p>
<p>There is a C compatibility layer which gives the prospect of being able to access Python, but still no news.</p>
<p>There were a few red herrings, <a href="http://www.adobe.com/devnet/flex/articles/flex_ui_03.html">this article</a> by Bruce Eckel covers calling Python for XML-RPC. Another red herring was this project in <a href="http://pypi.python.org/pypi?name=pyAIR&version=1.0&:action=display">PyPI</a>, thankfully I found a download URL that got me around the site that it's hosted on that requires registration and makes no sense. In the end it turns it out its Windows only and comes as an Air APP and a py2exe app. A quick rummage through the source of the .exe reveals it contains links to XMLRPCServer, so I'm guessing its just an implementation of Bruce's ideas. I must admit I was incensed that sort of thing gets into PyPI, but I know there's no policing of that.</p>
<p>Those examples both ship an Air app and a "frozen" python instance. My wife wouldn't be able to run that, it's not user friendly and fraught with problems (one is running the other isn't etc). So currently I'm stuck, I can't see how I can easily extend Adobe Air to do anything beyond interact with what I get. Surely there must be a way forward and I'm missing the big picture.</p> 