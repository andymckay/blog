---
layout: post
title: Preventing typos with Python mock
categories: General
blog: andy-mckay
---

Python mock is pretty cool, but there's been a recurring problem for me with <a href="https://docs.python.org/3/library/unittest.mock.html#module-unittest.mock">mock</a>
in that if you access any property on a Mock it returns a method which is *truthy*. This means
simple typos can exist in your testing.

As an example, in this library, there's a method <code>from_nonce</code>. If you just mock the object, then you can typo the method and it continues like normal:

<pre>
>>> with mock.patch('braintree.CreditCard') as mocked:
...   assert mocked.from_none
...
</pre>

This has happened to me and I didn't notice when I'd typo'd a mock call, like <code>is_called</code>. The test were wrong, but passed quite happily.

The better way is to pass <a href="https://docs.python.org/3/library/unittest.mock.html#the-mock-class">the object to the Mock call</a> as <code>spec</code>. Then only methods on the object can be called, for example:

<pre>
>>> with mock.patch('braintree.CreditCard', spec=braintree.CreditCard) as mocked:
...   assert mocked.from_none
...
Traceback (most recent call last):
  [..snip]
  File "/Users/andy/.virtualenvs/solitude/lib/python2.7/site-packages/mock.py", line 658, in __getattr__
    raise AttributeError("Mock object has no attribute %r" % name)
AttributeError: Mock object has no attribute 'from_none'
</pre>

Much better.
