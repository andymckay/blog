---
layout: post
title: Adobe Air vs Spats
categories: Air
old: 2051
blog: andy-mckay
---
<img src="http://www.agmweb.ca/files/spats.png" style="float: right; padding: 1em" />
<p>Alright comparing spats (Simple Page Template Server) to Adobe Air is like comparing ZServer to Plone. Air is a very big complex package that does a huge amount of stuff. By comparison spats does very little, but I'd like to keep interest in it up.</p>
<p>Spats is a program I worked on at Enfold to solve a problem we had (example file browser in piccy). We needed to a client side GUI that would do basic installer or controller like things, running as a powerful user able to delete directories, install services and the like. Spats provides a web control embedded in a window, so it looks like a normal program. Behind the scenes you are writing Page Templates (yay) and running Python.</p>
<p>Air is a big complicated program released by Adobe that provides a HTML, Flash or Flex  in a window. Air has full menu support, local database, drag and drop and a whole host of true native program like features. So far I've produced Hello World from it. I've probably under stated what Air does here.</p>
<p>But in the end I still like spats for a few reasons:</p>
<ul>
<li>I can write Python to do what I want, not Javascript. You'll pry Python from my cold dead arthritic hands. In Air I have to write Javascript all the way. Ugh.</li>
<li>Page Templates rock, at this point there isn't anything in Air for doing templating.</li>
<li>I like writing unit tests for my Python.</li>
<li>It's open source and can easily come with your Plone install.</li>
</ul>
<p>What would I chose to write my next client side project in? Adobe Air probably because it has about 8 gazillion features that spats does not. But don't discount spats, its neat and at Enfold made installers and controllers easy to write in familiar technologies that were the same. Plus it makes me think that 3 years ago when I wrote spats, I knew where things were going. For once. Maybe.</p> 
<ul>
<li><a href="https://svn.enfoldsystems.com/public/spats">Spats</a></li>
<li><a href="https://svn.enfoldsystems.com/public/spats-projects">Spats projects</a></li>
<li><a href="http://www.adobe.com/products/air">Adobe Air</a></li>
</ul>