---
layout: post
title: RSS feed fixed
categories: Django
old: 1972
blog: andy-mckay
---
<p>The RSS feed for this blog has been a bit wonky in Safari for a while. Specifically Safari would randomly pick dates for posts, randomly showing old posts as new ones. I think the problem was I was missing a timestamp on each item. This was as simple as adding in:
</p>
<pre>
    def item_pubdate(self, obj):
        return obj.timestamp
</pre>
<p>...on to my feeds class. Apologies if this has been messing your feed. Safari and Shrook now seem much happier.</p>