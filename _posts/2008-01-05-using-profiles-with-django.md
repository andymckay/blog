---
layout: post
title: Using profiles with Django
categories: Django
old: 2037
blog: andy-mckay
---
<p>There's a feature in Django to add in new values to a user record, use a profile. Here's an example: <a href="http://www.b-list.org/weblog/2006/jun/06/django-tips-extending-user-model/">http://www.b-list.org/weblog/2006/jun/06/django-tips-extending-user-model/</a>. So first thing I did was write a unit test for it, which failed.</p>
<p>This got me confused for a minute because I thought that when you created a user, it created the profile for you automatically. Duh! So for the record here's a simple unit test, create a user, set the company (a field on the Profile object), retrieve it and check the company is still there.</p>
<pre>
import unittest
from models import Profile
from django.contrib.auth.models import User
from django.contrib import auth

class TestSecurity(unittest.TestCase):
    def setUp(self):
        user = User.objects.create_user(username="bob",
                                        email="j@j.com",
                                        password="pwd")
        user.save()
        
        profile = Profile.objects.create(user_id=user.id)
        profile.company = "Test"
        profile.save()

    def testProfile(self):
        user = User.objects.get(username="bob")
        assert user.get_profile().company == "Test"
</pre>