---
layout: post
title: Presentacular
categories: General
old: 1879
blog: andy-mckay
---
<p><a href="http://labs.cavorite.com/presentacular/">Presentacular</a> allows you to add in all the script.aculo.us visual effects to your slideshow. I've already got a script that executes on showing a S5 presentation so it was a simple matter of adding in a class to say all my h1's. Now my headings smoothly fade in.</p>
<pre>function addEffects() {
    var elements = document.getElementsByTagName('h1');   
    for (var k = 0; k < elements.length; k++) {      
       var element = elements[k];      
       element.className = element.className + " appear";
    }
  }</pre>