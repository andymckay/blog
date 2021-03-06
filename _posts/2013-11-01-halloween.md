---
layout: post
title: Halloween
categories: General
blog: andy-mckay
---

It's Halloween time and this year I thought I'd get into the spirit of things and dress up. The only problem with that is I'm remote most of the time and so wearing a costume seemed a little pointless. We do have meetings at Mozilla using video conferencing so I thought I'd do something for that.

Armed with a Darth Vader mask, I wanted to try a few things out. I thought I'd go for a bit of a Star Wars themed background. My first attempt was to get a projector screen and place it behind me. I'd then project Star Wars onto the screen using a project. This turned out not to work too well for a few reasons. The screen had to be really close behind me to cover the range of the webcam and the projector had to be right above my laptop so it shined onto my face. I tried a few different arrangements couldn't get a could configuration.

Next I turned to green screen, but the problem is how to get that fed through to video conferencing solution Vidyo. So I turned to <a href="http://camtwiststudio.com/download/">CamTwist</a>. It takes multiple sources, mashes them together in real time and outputs a stream as a device. A device that Vidyo can then read. I tried to use a white screen, because it was the night before Halloween and I didn't have a green screen available. As it turns out the shiny white surface of the projector screen is really hard to light correctly. You need a very consistent colour to be able to get a consistent <a href="http://en.wikipedia.org/wiki/Chroma_key">chroma key</a>.

After lots of messing I went and bought a few sheets of bright green paper on an errand. A few bits of tape and we've got a green screen:

<img src="http://farm4.staticflickr.com/3719/10618987583_c91548c29e_n.jpg">

Lighting is a real challenge, I had to put some behind me focusing on the screen and some in front focusing on me:

<img src="http://farm8.staticflickr.com/7407/10618746956_d0d23f229f_n.jpg">

Time to fire up CamTwist and see how it looks with the green screen:

<img src="http://farm4.staticflickr.com/3783/10619372506_60a2a4edc2_n.jpg">

The green came out pretty even. CamTwist has lots of buttons and sliders without labels, so setting it can be an experience, but I grabbed a bit of Episode IV altered it in iMovie and stuck it on a loop:

<img src="http://farm8.staticflickr.com/7364/10619608013_6721ebe4f9.jpg">

There's a green halo around me which is a bit annoying, but for a rush job and some fun on Halloween, I could cope with that. If this was a professional video, I would recommend some fancier software. For full marks, of course I'd use HTML 5 to read the camera and process it using <a href="http://seriouslyjs.org">seriouslyjs.org</a>, but I couldn't figure out how to make the output become a device in OS X.

Anyway let's get Vidyo up and reading the CamTwist device and bingo:

<img src="http://farm4.staticflickr.com/3807/10619372046_3db844a6e9_n.jpg">

Now it wouldn't be enough just to video, we need sound. So I grabbed some .wav of the Sith Lord and made a <a href="/files/darth">simple web page</a>. Positioned the speakers near my speaker phone and hovered a finger over the right button. The phrase "Don't be too proud of this technological terror you've constructed." is too good to pass up in a Mozilla meeting.

So there I was on Thursday with everything set up and waiting for that first Vidyo call. But then meeting after meeting got cancelled, leaving me only two brief meetings to try it out. I had to hold it over to Friday, a few more meetings got cancelled, leaving me to inflict it upon a few people in the Apps demo meeting on Friday. Sorry for the distraction, but hey it's almost Halloween.

And I got a great quote from <a href="https://twitter.com/potch">potch</a> remarking on the lack of demo's in the meeting.... "There's a real *darth* of demo's today.".

Worth it. Watch out Halloween next year, I've still got the green card.
