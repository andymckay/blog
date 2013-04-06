---
layout: post
title: Django Test Client and OpenID
categories: Django
old: 2192
blog: andy-mckay
---
<p>...or how I used <a href="http://code.google.com/p/django-openid">django-openid</a> all wrong in the first place and I've just gotten it cleaned up.</p>
<p>A while back I dedicated myself to trying to do everything with OpenID since having all these logins all other the place is just awful. With sites dedicated to the technically minded it seems the right way to go. So I grabbed django-openid out and slapped it in. This handles the login and logout for you. When an authenticated request is made a variable is appended to request by its middleware: <code>request.openid</code> which in turn provides account information.</p>
<p>So then it was a simple matter of checking if that request.openid is there and finding the user. In the old version of my site that was very simple, just a decorator to check someone is logged in and I'm done.</p>
<p>In the next revision I need permissions, so I thought I'd use the Django permissions from contrib.auth. No problem... just make the current user model a <a href="http://www.b-list.org/weblog/2006/jun/06/django-tips-extending-user-model/">user profile</a> and I can use permissions. Except this is where it gets sticky. Because I was working around the Django contrib.auth with using openid, things weren't working. This came to the fore when I tried to use the test client to check that I can only view pages when logged in.</p>
<p>To do that you use the <code>login</code> method of the <a href="http://docs.djangoproject.com/en/dev/topics/testing/?from=olddocs">test Client</a>, so here's what I wanted to check:</p>
<pre>from django.test import TestCase                
from django.test.client import Client

class register(TestCase):
    def testLogin(self):
        client = Client()
        client.login(openid="http://some.user.id/")
        res = client.get("/listener/view/2/")
        assert res.status_code == 200

    def testFailLogin(self):
        client = Client()
        res = client.get("/listener/view/2/")
        assert res.status_code == 302
</pre>
<p>However there's a problem. The <code>login</code> code works with the authentication backend, django-openid doesn't define one and neither did I. After trying to bend the Client to my will I realised I was going the wrong way and use the django authentication system that's there. So let's snip out all the messing around in the middle and cut to the chase of what worked.</p>
<p>Firstly, define an authentication backend, so that's a matter of grabbing the <code>openid</code> from the <code>request</code> and then searching in my <code>UserProfile</code>:</p>
<pre>from general.models.user import UserProfile
from django.contrib.auth.models import User

class OpenIDAuthentication:
    def authenticate(self, openid):
        user = UserProfile.objects.get(openid__exact=openid)
        if user:
            return user.user
        
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
</pre>
<p>Then you add in:</p>
<pre>AUTHENTICATION_BACKENDS = (
    'general.authentication.OpenIDAuthentication',
)</pre>
<p>That then handles my authentication. Now in my code i can call:</p>
<pre>authenicate(openid="some id")</pre>
<p>All I had to do then was realise that most of my old login handling and checking methods were wrong and remove them or make them use the contrib.auth ones. Once that was all done, my test cases ran much more smoothly. Going back and looking at django-openid now, this makes much more sense and will hopefully be easier to switch to a more up to date openid version.</p>