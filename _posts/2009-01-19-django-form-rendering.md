---
layout: post
title: Django form rendering
categories: Django
old: 2173
blog: andy-mckay
---
<p>The other day I was putting on an iPhone skin for Arecibo. Just a HTML and CSS wrapping of the site using <a href="http://code.google.com/p/iui/">IUI</a>. But the form rendering options for forms aren't quite right since IUI is very specific about the HTML is laid out.</p>
<p>There's a simple way to fix that though, add a custom method that outputs it the way I want:</p>
<pre>class Form(forms.Form):
    ....
    def as_iui(self):
        return self._html_output(u"""
        &lt;div class="row"&gt;
            %(label)s
             %(field)s%(help_text)s
        &lt;/div&gt;
        """, u'%s', '', u' %s', True)</pre>
<p>Calling <code>form/as_iui</code> gives us the form rendered just as IUI want's it.</p>