---
layout: post
title: Why you should use PhoneGap
categories: General
old: 2248
blog: andy-mckay
---
<p><a href="http://phonegap.com/">PhoneGap</a> is a library for building out mobile phone applications. It does it by giving you a browser embedded in an application and letting you build the application using HTML and JS. There's lots of arguments for and against tools like PhoneGap (other libraries are available). But the one I keep arguing is something <a href="http://docs.google.com/fileview?id=0B29qXMz8reouYzJhMjhhZDMtOTQ5MC00NjY3LWIxM2EtY2U3ZmI2NzQzYjk3&hl=en">Zach</a> said to me at DjangoSki.</p>

<p>Simply put, building apps with PhoneGap allows you to re-use existing skill sets without having to learn new stuff.</p>

<p>Many years ago at Enfold we were building an installer. We started using Inno installer which is a fine little installer and can be extended using Pascal. That was great fun to do, for a while. As the installer grew and took on more features, the ability to interact more with Windows got more complicated. The installer is quite complicated and requires configuring of IIS and interaction with Active Directory, fun stuff indeed. At some point we had to stop trying to build all this in Pascal and move to Python.</p>

<p>So the installer moved to a two step process, Inno installs Python and other dependencies and <a href="http://www.enfoldsystems.com/developer/software/spats">spats</a>. That's a little process that fires up a local window with a browser window embedded pointing to a Python process, running a simple HTTP that serves back HTML from Page Templates. The user interacts with a browser that looks reasonably native and we process and do all the remaining work in Python.</p>

<p>A year or two later out came <a href="http://www.adobe.com/products/air/">Adobe Air</a> which is a similar plan (although quite a bit more sophisticated). These days there a few of these different tools (eg <a href="http://www.appcelerator.com/products/titanium-cross-platform-application-development/">Titanium</a>).</p>

<p>The result was using Python and HTML allowed us to have a product that was easily maintained and updated by anyone developer in the company.</p>

<h3>Re-use tools</h3>

<p>Using the same technologies for building websites, mobile applications and desktop applications is incredibly helpful. You get to use the same tool chain throughout. That means you can move developers between projects quickly and tools that developers are already familiar with can be used. That makes your developers far more productive.</p>

<p>Got a common JavaScript library that you use for all your websites? Re-use it. Unless its jQuery.</p>

<h3>Re-use skills</h3>

<p>Your developers are quickly building up skills becoming Javascript and HTML 5 rock stars. Re-use that skill and let's face it in terms of cost, you can't get much cheaper and more ubiquitous than these skills. Well except for maybe PHP developers. Good Objective C developers are expensive and hard to find and for the vast majority of iPhone apps, just not needed.</p>

<h3>Keep learning, the right bits</h3>

<p>I didn't have any problem with re-learning Pascal for the installer. It was quite good fun. Learning stuff happens all day, every day, it's an essential part of our careers. However I think it's important to learn and move forward on the right bits. Time and brain space is limited and there's an almost limitless amount of things that can be learnt. Focusing on things that can give the maximum return is crucial.</p>

<p>So that's why I think PhoneGap is useful, not the cross platform stuff, but because it let's you re-use existing resources in your organization. It allows you to focus time on learning new ways to be awesome within your current realm. Or as Zach said over a beer (paraphrasing) "I could get our web developers up and running on it in no time".</p>