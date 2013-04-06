---
layout: post
title: syncdb and Django
categories: Django
old: 2154
blog: andy-mckay
---
<p>This has cropped up a couple of times on irc, so here's a recipe I have for restarting my Django instance during development. I'm not the sort of person who takes a long time to think it all through and can write a model and call it done, I iterate quickly and often. For the quickest way to do that during the initial development, I drop the db, re run syncdb and import my fixtures regularly.</p>
<p>Once a production version is out and running I then get rid of this script and do migrations.</p>
<p>There's no easy way from the command line to create a user neither <code>syncdb --noinput</code> or <code>createsuperuser --noinput</code> accept a password. Leaving lazy people like me wanting. I used to use <a href="http://www.djangosnippets.org/snippets/111/">pexpect</a> but I find just creating a user object nice and easy. So for a project called collector, the following works well for me:</p>
<pre>
#!/usr/local/bin/python
import os
os.environ["DJANGO_SETTINGS_MODULE"] = "settings"

# dump the data to fixtures
os.system('python manage.py dumpdata collector --indent=2 &gt; collector/models/fixtures/data.json')
# drop and recreate the db (this is for postgres)
os.system('dropdb authy')
os.system('createdb authy --encoding=UTF-8')
# sync the db
os.system('python manage.py syncdb --noinput')

# create a super user
from django.contrib.auth.models import User
u = User.objects.create(
    username='xxx',
    first_name='',
    last_name='',
    email='amckay@bluefountain.com',
    is_superuser=True,
    is_staff=True,
    is_active=True
)
u.set_password('xxx')
u.save()
print "User account created"

# load the fixtures back in
os.system('python manage.py loaddata data.json')
# run the server
os.system('python manage.py runserver')
</pre>
<p>I can then quickly get in the cycle of creating a model, entering data in admin interface, dumping it to a fixture and then writing unit tests.</p> 