---
layout: post
title: Django and Bleach
categories: Django
old: 2291
blog: andy-mckay
---
<p><a href="https://github.com/jsocol/bleach">Bleach</a> is a HTML whitelist and sanitizer library written by <a href="http://coffeeonthekeyboard.com/bleach-html-sanitizer-and-auto-linker-for-django-344/">James Socol</a>. At mozilla we use it on the <a href="http://addons.mozilla.org">addons</a> and <a href="http://support.mozilla.com">support</a> sites. Chances are you'll need it on pretty much any site that accepts user input, ensuring that the HTML you are outputting is nice and safe.</p>
<p>Under the hood bleach uses the <a href="http://code.google.com/p/html5lib/">html5lib</a>. As an aside, I've been running html5lib sanitisation using a homegrown library on App Engine for a while now and it's been great.</p>
<p>Installing bleach is as simple as:</p>
<pre>pip install bleach</pre>
<p>The place to do user validation is a form, so let's take a simple model and form combination:</p>
<pre>
from django.db import models

class Todo(models.Model):
    text = models.CharField(max_length=255)
</pre>
<pre>
from django.forms import ModelForm
from bleach import Bleach
from todo.models import Todo

bleach = Bleach()

class TodoForm(ModelForm):
    def clean_text(self):
        return bleach.clean(self.cleaned_data.get('text', ''))

    class Meta:
        model = Todo
</pre>
<p>And that's it, our Todo model is now going to be nicely sanitised (assuming you use a django form for validating all user input, which you should do).</p>
<p>So here's a quick test:</p>
<pre>
import unittest
from todo.forms import TodoForm

class TestBleach(unittest.TestCase):
    def test_todo(self):
        data = "&lt;b&gt;bold&lt;/b&gt; &lt;script&gt;alert('hello')&lt;/script&gt; "
        expect = "&lt;b&gt;bold&lt;/b&gt; &amp;lt;script&amp;gt;alert('hello')&amp;lt;/script&amp;gt;"
        form = TodoForm({'text':data})
        assert form.is_valid()
        assert form.cleaned_data['text'] == expect
</pre>
<p>We can see that the nice bold tag is not escaped. But the very nasty script tag is. On the way you also get tag balancing:</p>
<pre>
>>> bleach.clean('bar&lt;/a&gt;')
u'bar'
>>> bleach.clean('&lt;a&gt;bar')
u'&lt;a&gt;bar&lt;/a&gt;'
</pre>
<p>For more information including notes on the link creation function see the <a href="https://github.com/jsocol/bleach/blob/master/README.rst">readme</a>. Probably my favourite part of bleach is the <a href="https://github.com/jsocol/bleach/blob/master/bleach/tests/test_security.py">tests</a>.</p>
<p>Check out <a href="https://github.com/jsocol/bleach">bleach on github</a> and give it a spin for your next Django project.</p> 