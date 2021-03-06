---
layout: post
title: Google Web Apps, first look
categories: Python
old: 2072
blog: andy-mckay
---
<p>With some fanfare <a href="http://code.google.com/appengine/">Google Web Apps</a> have been launched. This is great because its using Python and Django, how much more perfect can it get. This morning I've been having a play and I'm just waiting for my account so I can upload something.</p>
<p>Would be nice to take my (as yet unreleased) Plone to Django conversion script, plonk the result on Google Web Apps and then link up a nice little Adobe Air app. Anyway two things that irked me (of course I'm going to complain): 1) the example Python all has two spaces as the indent and 2) it uses Django templating.</p>
<p>Fortunately it says:</p>
<blockquote>You can bundle a framework of your choosing with your application code by copying its code into your application directory</blockquote>
<p>And looking at later comments, it's not going to block a module like simpletemplates, which I use for templating in Django. So. lets alter <code>helloworld.py</code> a bit (<a href="http://code.google.com/appengine/docs/gettingstarted/usingwebapp.html">original</a>):</p>
<pre>
from simpletemplate.google import DjangoSimpleTAL
</pre>
<p>And change the MainPage class to read (only changed last two lines):</p>
<pre>
class MainPage(webapp.RequestHandler):
    def get(self):
        greetings = Greeting.all().order('-date')

        if users.get_current_user():
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Logout'
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'

        template_values = {
          'greetings': greetings,
          'url': url,
          'url_linktext': url_linktext,
          }

        path = os.path.join(os.path.dirname(__file__), 'index.html')  
        template = DjangoSimpleTAL(path)
        self.response.out.write(template.render(template_values)
</pre>
<p>And finally lets change <code>index.html</code> to read:</p>
<pre>
&lt;html&gt;
    &lt;body&gt;
        &lt;tal:loop repeat="greeting greetings"&gt;
            &lt;tal:block condition="greeting/author|none"&gt;
                &lt;b tal:condition="python:greeting.author.nickname"&gt;Author&lt;/b&gt; wrote:
            &lt;/tal:block&gt;
            &lt;tal:block condition="not:greeting/author|none"&gt;
                An anonymous person wrote:
            &lt;/tal:block&gt;
            &lt;blockquote tal:content="greeting/content"&gt;Comment&lt;/blockquote&gt;
        &lt;/tal:loop&gt;

        &lt;form action="/sign" method="post"&gt;
            &lt;div&gt;&lt;textarea name="content" rows="3" cols="60"&gt;&lt;/textarea&gt;&lt;/div&gt;
            &lt;div&gt;&lt;input type="submit" value="Sign Guestbook"&gt;&lt;/div&gt;
        &lt;/form&gt;

        &lt;a tal:attributes="href url" tal:content="url_linktext"&gt;Login&lt;/a&gt;
  &lt;/body&gt;
&lt;/html&gt;
</pre>
<p>And things seem to work just dandy. For those who do use simpletemplate, the google module isn't in SVN yet, and needs a bit of work, but just a quick refactoring of the simpletemplate code to be friendly with the new imports that the Google app server uses.</p>
<p><b>Update:</b> by the time my blog post was done, my account was activated. Unfortunately I have to work today though.</p>