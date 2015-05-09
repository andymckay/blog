---
layout: post
title: Catching unused mocks
categories: General
blog: andy-mckay
---

It's easy for mocks to get out of hand and I've seen tests that have many mocks and patches. That in itself is bad enough, but I want to make sure that each mock is there for a reason, not just because the test has been copy and pasted, or underlying code has changed meaning mocks are no longer used.

So I added a registration step for mocks. Here's a simplified version:

<pre>
def setUp(self):
    self.mocks = {}

    for name, obj in self.registered_mocks.items():
        self.mocks[name] = OurMock(name, spec=obj)

    self.addCleanup(self.cleanUpMocks)
</pre>

`OurMock` is a special mock that registers all the mocks registered against it. This pattern is pretty specific to the type of object I'm mocking in the tests:

<pre>
class OurMock(mock.Mock):

    def __getattr__(self, name):
        if not name.startswith('_'):
            setattr(self, '_registered', [])
            self._registered.append(name)
        return super(OurMock, self).__getattr__(name)
</pre>

Then on `cleanUp`:

<pre>
def cleanUpMocks(self):
    for k, v in self.mocks.items():
        for call in getattr(v, '_registered', []):
            if not getattr(v, call).called:
                raise MockError('{0}.{1} registered but not called.'
                                .format(self.registered_mocks[k].__name__, call))
</pre>

So a test now reads:

<pre>
class Test(tests.TestCase):
    self.registered_mocks = {'some': object}

    def test_ok(self):
        self.mocks['some'].create.return_value = something()
</pre>

If you run that test without anything else, it will fail because the mock never actually got called.

This has already caught a few errors and let me keep my mocks nice and clean.
