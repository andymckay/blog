---
layout: post
title: Full text searching in Django
categories: Test
old: 2195
blog: andy-mckay
---
<p>I've been looking for a nice full text search index for Postgres. For a while I've used the built in full text search in Postgres and have been pretty impressed in that I've had nothing to fix on it or worry about in over 5 months and I like that.</p>
<p>On the next upgrade of the site I wanted to do full text indexing across multiple models. This made it a little bit more interesting, but I quickly discarded a few plans:
<ul>
<li><a href="http://barryp.org/blog/entries/postgresql-full-text-search-django/">tsvector</a> is the one I was using and is based on providing search for a single model.</li>
<li><a href="http://www.arnebrodowski.de/blog/add-full-text-search-to-your-django-project-with-whoosh.html">Whoosh</a> came up in my twitter feed the other day and I tried it and got it working, but I don't feel too comfortable with whoosh. It's light on the unit tests and features. It's new and made me think the zcatalog and it's indexes from zope might be a better bet. Would like to see some more maturity out of that one.</li>
<li><a href="http://code.google.com/p/django-solr-search/">Django solr</a> seems like a more mature choice, but even the install of solr took over an hour as ubuntu apt-getted the world. After that I got a bit lost on reading solr docs. In the end I just didn't feel too comfortable with another peice of machinery to blow up. It's clearly a good mature product, but I feel at this stage overkill, definitely something I would use for a big project though.</li>
<li><a href="http://www.djangosnippets.org/snippets/1328/">This snippet</a> is very cool, but again only for one model....</li>
</ul>
<p>So all we need to do is hack apart that snippet and use it with the content types framework instead. So here's yet another solution that provides cross model searching. I use the Vector field from the last snippet and use it in a Generic content model.  Then using a bit from the Whoosh example, I apply a signal to listen to every model. When it changes a check to see if the "get_search_fields" method exists. Yes that's hacky but works.</p>
<p>The last hacky part is actually saving the tsvector, that is done through raw sql (as is the snippet). I've tried overriding get_db_prep_save and such (<a href="http://docs.djangoproject.com/en/dev/howto/custom-model-fields/?from=olddocs">as documented</a>) but can only succeed in strings being written in, not tsvectors. So if anyone has any thoughts on that, much appreciated.</p>
<p>So a query returns the search model hits and then access content_object on the result gives you the object for the results page. With pagination that will mean 20 queries, one for each row of my result. Which isn't ideal, but we can optimize by adding more values to the search model if needed to prevent those lookups.</p>
<p>Here's the code:</p>
<pre>from django.db import models
from django.contrib import admin

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.db import connection
from django.db.models import signals

# from http://www.djangosnippets.org/snippets/1328/
class VectorField (models.Field):
    def __init__(self, *args, **kwargs):
        kwargs['null'] = True
        kwargs['editable'] = False
        kwargs['serialize'] = False
        super(VectorField, self).__init__(*args, **kwargs)

    def db_type( self ):
        return 'tsvector'

class Search(models.Model):
    object_id = models.PositiveIntegerField()
    content_type = models.ForeignKey(ContentType)
    content_object = generic.GenericForeignKey()
    
    index = VectorField()

    class Meta:
        app_label = "general"

    @staticmethod
    def query(query):
        query = connection.ops.quote_name(query)
        result = Search.objects.extra(where=["index @@ plainto_tsquery(%s)"], params=[query,])
        return result

# bits from http://www.arnebrodowski.de/blog/add-full-text-search-to-your-django-project-with-whoosh.html
def update_index(sender, instance, created, **kwargs):
    if not hasattr(instance, "get_search_fields"):
        return
        
    catalog = 'pg_catalog.english'
    data = [ str(f) for f in instance.get_search_fields() if f ]
    data = " ".join(data)
    
    content_type = ContentType.objects.get_for_model(instance)
    try:
        search = Search.objects.get(content_type__pk=content_type.id, object_id=instance.id)
    except Search.DoesNotExist:
        search = Search.objects.create(content_object=instance)
        search.save()

    cursor = connection.cursor()
    sql = "update general_search set index = to_tsvector(%s, %s) where id = %s"
    cursor.execute(sql, (catalog, data, search.id))
    cursor.execute("COMMIT;")
    cursor.close()

signals.post_save.connect(update_index)</pre>
<p><b>Update:</b> corrected possible sql injection.</p>