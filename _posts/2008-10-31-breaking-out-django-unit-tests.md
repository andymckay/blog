---
layout: post
title: Breaking out Django unit tests
categories: Django
old: 2148
blog: andy-mckay
---
<p>You can move models.py and views.py into seperate directories called models and views. I also make a directory to stick all my forms in called, excitingly enough, forms. But you can make a tests directory and put your tests in there. Grrr. A bit of Googling didn't get me too far, so a bit of reading of source got me this far.</p>
<p>The key is that Django will look to see if tests.py has a "suite" method, if so it will run it. This allows us to do what we'd like with the test runner.</p>
<p>So, make a directory called tests and put in it your unit tests, make a __init__.py and in that reference each of the modules you'd like to run tests on. Contents of my __init__.py:</p>
<pre>
import unittest       
import browser
import site 

__tests__ = [browser, site]  

def suite():
    suite = unittest.TestSuite()
    tests = []                           
    for test in __tests__:
        tl = unittest.TestLoader().loadTestsFromModule(test)
        tests += tl._tests
    suite._tests = tests
    return suite
</pre>
<p>My tests directory has a browser.py and site.py that contain unit tests. Adjust the imports and the __tests__ lists as you see fit for your instance. When I add a new file, I register it here.</p>
