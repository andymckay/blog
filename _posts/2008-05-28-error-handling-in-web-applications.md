---
layout: post
title: Error handling in web applications
categories: Python
old: 2091
blog: andy-mckay
---
<p>In recent memory I've had to fight this a couple of times with project managers. When it happens next time, hoping there isn't I'll have this blog post to go back to.</p>
<p>In a web application there's essentially two kinds of errors that can occur, there's an error from user input, or there's an error from infrastructure. The errors from user input, the most frequent ones are easy to handle we'll discuss those simply now: user submits form, form comes back with an error. Everyone knows this one so discussion is over.</p>
<p>The harder one is the unforseen error, the error that occurs in an application because something unexpected happens. I build sites in Python when I can, in Ruby on Rails when god decides I need punishing. Both Python and Ruby have exceptions and exception handling. Anywhere in code you can raise and error and it will bubble up the application until something catches it. Normally the catcher is the main server loop which will format it back to the user in a nice message. Simple.</p>
<p>Being able to raise exceptions is crucial to programming. In a 
<p>For example I will sprinkle my code liberally with asserts and checks. I don't really trust much of anything to work most of the time and a few asserts will give me a fighting chance. I've found a lot of Rails code use the save method in ActiveRecord eg:</p>
<pre>
person.save
</pre>
<p>If anything goes wrong with this, <code>False</code> is returned. If you don't check that code, you don't know if it's worked. Instead:</p>
<pre>
person.save!
</pre>
<p>Will raise an error.</p>