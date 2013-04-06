---
layout: post
title: Don't use properties
categories: Plone
old: 1813
blog: andy-mckay
---
Was helping a person on irc the other day. The problem was they were including a string into a template. The string was coming from a property on an object, that property was being acquired through acquisition. The code was something like this:

<textarea name="code" class="xml">tal:content="context/getSectionText"</textarea>

So the what's the problem here?

<ul>
	<li>What's the chance you will remember in 6 months what getSectionText is? Go away for a day then try to remember (ok, perhaps I'm just getting old). But you'll never remember that is a property on an object and there is no easy way of finding that out.</li>
	<li>There is no easy way to change it.</li>
	<li>There is no easy way to list them all - short of waking up every object and examining it.</li>
	<li>You could conceivably get hit by security when someone workflows the object with the property for you (admittedly perhaps less of a concern).</li>
</ul>

In this case I prefer a Python script that searches the objects location and returns a value. Here's an example that I pulled from Enfold Systems that displays a different image on the top of every folder.
<pre>
<textarea name="code" class="python">
# add in new images here
images = {
  "desktop":"enfoldsystems/sections/desktop.jpg",
  "server":"enfoldsystems/sections/server.jpg",
}
url = context.portal_url.getRelativeContentPath(context)
img = None
# in this case we are looking for url's like
# products/server or products/proxy
if len(url) > 1:
  # look up the images
  if url[0].lower()=="products":
    product = url[1].lower()
    img = products.get(product, None)
# set the default
if img is None:
  img = "sections/homepage.jpg"
return img
</textarea>
</pre>

Next we add this into the skin. In this case this is called getSectionImage and the template reads:

<textarea name="code" class="xml">tal:attributes="src string:$portal_url/${context/getSectionImage}"</textarea>

Not the worlds most sophisticated peice of code but...
<ul>
	<li>It's easy to remember, when looking in our templates and I spot the line getSectionImage, its easy for me to look in the skin and remember there is a script called getSectionImage even now two years later.</li>

	<li>I can easily see what all the images are and alter them.</li>
	<li>Never any security to worry about.</li>
</ul>
The only real problem you have is that for complicated requirements, that script can get complicated, but that's true of properties too.

