---
layout: post
title: Debugging mod_python
categories: Python
old: 2139
blog: andy-mckay
---
<p>Today I had a small interesting project I didn't quite complete, but should do in the morning
its adding in a python authentication wrapper pulling from our LDAP server so that we can control our SVN and Trac access. We've already sort of got one, but it requires LDAP munging to move people around and instead we are moving that up to Python and so may as well give it a web interface in Django.</p>
<p>Some of the things I learned:</p>
<ul>
<li>mod_python has a very useful handler called <code>PythonAuthenHandler</code> that allows you to just plugin a directive to get a peice of Python to handle authentication - <a href="http://www.modpython.org/live/current/doc-html/dir-handlers-auh.html">documentation is online</a>.</li>
<li>There's a <a href="http://docs.djangoproject.com/en/dev/howto/apache-auth/">sample in the Django docs</a> of using this handing directive.</li>
<li>When it doesn't work you can get to a pdb in mod_python, called PythonEnablePdb, that is <a href="http://www.modpython.org/live/mod_python-3.2.8/doc-html/dir-other-epd.html">documented here</a>.</li>
<li>You will then need to start Apache using <code>-DONE_PROCESS</code> and then you get a pdb and bob is your uncle.</li>
</ul>
<p>Until you realise the LDAP data is dodgy. Tthere I was about to jump ship to mod_wsgi, but got the job done for now (almost)</p>