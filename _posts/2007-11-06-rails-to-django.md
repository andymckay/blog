---
layout: post
title: Rails to Django
categories: Django
old: 2023
blog: andy-mckay
---
<p>Yesterday saw the beginning of the end of our Rails applications as we started moving them over to Django. A simple one was our timesheet application (yes we have one internally) that was in Rails.</p>
<p>The rails application was around 1000+ lines of code (just in the app directory) of which I imagine a lot was the boiler plate scaffold. It used a plugin we developed called Toffee which did the user interface and then one for pretty user interface. It had quite a few bugs, took 2 days to write (which I still find hard to believe).</p>
<p>The django application (with the following exception) took 1 hour to write and had about 80+ lines of code (mostly because I write with lost of new lines). No bugs so far. The tricky bit that took me 2 hours is a) changing django to trust REMOTE_USER sent from our Apache which does LDAP auth and b) figuring out how to set this user on the timesheet model. I'm still not happy with the solution to the latter and need to research, I think it should be a manipulator so the admin interface uses that.</p>
<p>Today we worked on moving an old Zope application to Django, looking good so far.</p>