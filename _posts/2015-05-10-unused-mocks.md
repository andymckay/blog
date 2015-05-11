---
layout: post
title: Catching unused Python mocks
categories: General
blog: andy-mckay
---

It's easy for mocks to get out of hand and I've seen tests that have many mocks and patches. That in itself is bad enough, but I want to make sure that each mock is there for a reason. Over time tests get been copy and pasted or underlying code has changes - meaning mocks exist but are no longer used.

You can do this my asserting that each mock is called in the test. I've seen tests with that end up being 4 lines of mocks, a call, then 4 lines of checking the mocks are being called. Clearly, something was going wrong with those tests in the first place.

Anyway, I wanted to keep my tests clean in the future, so I added a registration step for mocks. Here's a simplified version:

{% highlight python %}
def setUp(self):
    self.mocks = {}

    for name, obj in self.registered_mocks.items():
        self.mocks[name] = OurMock(name, spec=obj)

    self.addCleanup(self.cleanUpMocks)
{% endhighlight %}

`OurMock` is a special mock that registers all the mocks registered against it. This pattern is pretty specific to the type of object I'm mocking in the tests:

{% highlight python %}
class OurMock(mock.Mock):

    def __getattr__(self, name):
        if not name.startswith('_'):
            setattr(self, '_registered', [])
            self._registered.append(name)
        return super(OurMock, self).__getattr__(name)
{% endhighlight %}

Then on `cleanUp`:

{% highlight python %}
def cleanUpMocks(self):
    for k, v in self.mocks.items():
        for call in getattr(v, '_registered', []):
            if not getattr(v, call).called:
                raise MockError('{0}.{1} registered but not called.'
                                .format(self.registered_mocks[k].__name__, call))
{% endhighlight %}

So a test now reads:

{% highlight python %}
class Test(tests.TestCase):
    self.registered_mocks = {'some': object}

    def test_ok(self):
        self.mocks['some'].create.return_value = something()
{% endhighlight %}

In this example: *create* is in the list of *_registered* on the Mock. When the test completes we check it got called. If you run that test without anything else, it will fail because the mock never actually got called.

If what is passed to the mock is important, all the usual methods like *assert_called_with* can be called.

This has already caught a few errors in my tests.
