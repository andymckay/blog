---
layout: post
title: Stricter API filtering
categories: General
blog: andy-mckay
---

<a href="http://www.django-rest-framework.org">Django Rest Framework</a> and
Tastypie both provide REST queries and allow looking up lists of objects based
on query parameters. In the former case it allows multiple back-ends, but
defaults to using Django filter.

That's a fine approach with one problem. Consider this:

<pre>
http://example.com/api/products?category=clothing
</pre>

You've got a reasonably good idea of what that will return. How about this one?

<pre>
http://example.com/api/products?categry=clothing
</pre>

What does that return? Everything. Because `category` got typo'd. Meaning that
it was excluded from the filter and you didn't filter on anything at all. Ouch.

Out of the box Django Rest Framework only allows GETs on lists. Even a GET that
goes awry like that is bad. But you can use the
<a href="https://github.com/miki725/django-rest-framework-bulk">bulk library</a>
 to do PATCH, PUT and DELETE.

<pre>
DELETE http://example.com/api/products?categry=clothing
</pre>

That's really going to ruin your day. <a href="https://twitter.com/kumar303/">Kumar</a> rightly
complained about this so I threw in a simple filter to stop that.

{% highlight python %}
from rest_framework.exceptions import ParseError
from rest_framework.filters import DjangoFilterBackend

class StrictQueryFilter(DjangoFilterBackend):

    def filter_queryset(self, request, queryset, view):
        requested = set(request.QUERY_PARAMS.keys())
        allowed = set(getattr(view, 'filter_fields', []))
        difference = requested.difference(allowed)
        if difference:
            raise ParseError(
                detail='Incorrect query parameters: ' + ','.join(difference))

        return (super(self.__class__, self)
                .filter_queryset(request, queryset, view))
{% endhighlight %}

Once it's done alter: `DEFAULT_FILTER_BACKENDS` to point to that and make sure your <a href="http://www.django-rest-framework.org/api-guide/filtering/#api-guide">filter_fields</a> are correct.

Now a typo'd query string will return you a 422 error.
