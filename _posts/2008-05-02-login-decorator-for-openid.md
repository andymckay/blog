---
layout: post
title: Login decorator for OpenId
categories: Django
old: 2081
blog: andy-mckay
---
<p>The login decorator for Django looks for a user, as if you'd logged in through the admin interface. That's not what OpenId gives you. For that you'd want something like this:</p>
<pre>
def login_required(fn):
    def new(*args, **kw):
        request = args[0]
        if request.openid is None:
            return HttpResponseRedirect("/login")
        else:
            return fn(*args, **kw)
    return new  
</pre>
<p>Then for any views that require OpenId login on them, slap the following before them just like normal:</p>
<pre>
@login_required
</pre>