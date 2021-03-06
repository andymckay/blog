---
layout: post
title: Web presentations
categories: Web 2.0
old: 1793
blog: andy-mckay
---
Jon Udell posts on <a href="http://weblog.infoworld.com/udell/2006/05/23.html#a1453">web presentations</a>, pointing to <a href="http://www.meyerweb.com/eric/tools/s5/">S5</a> and<a href="http://www.w3.org/Talks/Tools/Slidy/"> HTML Slidy</a>. Both of these are excellent systems and I think the time has truly come to seperate the world from their PowerPoint dependencies.

<blockquote>There's an option in HTML Slidy to make each slide's title the HTML doctitle, and of course I turned that on because I'm always looking for ways to make my stuff more coherent and useful in search results contexts. But to no avail.</blockquote>

Good question, as I'm doing quite a bit of plotting and planning around presentations right now. The simplest solution is a <em>publish</em> process to publish pages individually.

In a slightly different arena, this problem has also cropped up at <a href="http://www.enfoldsystems.com">Enfold</a> recently where I've been addressing a complete Ajax front end for <a href="http://www.plone.org">Plone</a>. In this scenario Enfold Entransit writes out a complete set of xml to the filesystem, it screams Ajax to pull it together. But then how do bots index the site? No idea.

But then this does beg the question, how valuable to a search engine is a multi page view of a topic? Does that truly represent how the data should be presented? I would argue its not that important. For me the breaking down of a slide into multiple pages is an act of logical planning through my topic. Individually each slide taken out of context, is only partially useful in comparison to the whole.

Breaking down of the talk into slides is purely a representation of the time frame for the talk and the limit of only being able to fit one set of things onto a screen. The fact that all that content can be shown in one HTML page (as below) is to me good enough.

For the record a couple of interesting things. I've been using S5 for about 2 years and its great. I added S5 support to Plone then, mainly out of frustration dealing with Powerpoint and OpenOffice. It's really nice to be able to write a presentation in any format Plone can handle: Structured text, Restructured text, HTML via Kupu or Epoz gui editors or just plain HTML. Then its output as a presentation, for example:

Plain page: <a href="http://www.enfoldsystems.com/About/Talks/overview">http://www.enfoldsystems.com/About/Talks/overview</a>

S5 presentation: <a href="http://www.enfoldsystems.com/About/Talks/overview/s5_document">http://www.enfoldsystems.com/About/Talks/overview/s5_document
</a>

Aas with many things, it was Jon Udell who started me down this path about 5 years ago by complaining to me about having to open one of my presentations in PowerPoint.