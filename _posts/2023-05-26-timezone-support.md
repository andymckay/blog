---
layout: post
title: Service catalog - Timezone support
categories: general
blog: andy-mckay
---

When you are in an incident that's causing impact to your customers, you'll be looking at data in multiple sources. From events on GitHub, messages on Slack, logs in Splunk, graphs in Datadog and on and on. At the time of an incident there's a lot going on and one thing that always caused a bit more cognitive stress for me was calculating when everything happened. To add to this, you might be working with people who are in diverse time zones. Most services (thank goodness) these days log in UTC and the service catalog is no exception, logging things in UTC.

To make life just that bit easier, the <a href="https://github.com/clearwind-ca/service-catalog/releases/tag/0.1.3">service catalog now allows you to set a timezone</a> and whenever you see a date, you'll see it 3 different ways:
* The time relative to now
* The time in UTC
* The time in your timezone

Here's an example:

<img src="/files/service-catalog-times.png" />

This may seem like a small thing, but this, along with the little <code>copy to clipboard</code> make it easier to communicate and understand what happened. Since the service catalog can capture important arbitrary events, such as deployments, migrations, releases, feature flag changes in catalog events, it's easy to establish a timeline of what happened.

It's been a while since I've done Django and this was a good learning experience through the timezone support which has been added over the years, and as usual was done really well. There's a few things I'm going to highlight that I thought were good, but this document <a href="https://docs.djangoproject.com/en/4.2/topics/i18n/timezones/">covers all the basics</a>.

### Settings

You should have `TIME_ZONE` set to `UTC` and `USE_TZ` set to `True`. I've worked on projects where the timestamp in the database is not in `UTC` and it just made me cry. Just leave this as `UTC` and never change it. There is only one timezone that data should ever be stored and it should always be `UTC`. Just don't change that.

### Letting users pick a timezone

You'll probably have to make a <a href="https://docs.djangoproject.com/en/4.2/topics/auth/customizing/#extending-the-existing-user-model">user profile</a> you ask the user for their timezone and then attach it to the user. The service catalog is tightly coupled to GitHub. In GitHub you also get to specify your timezone, but the <a href="https://docs.github.com/en/rest/users/users?apiVersion=2022-11-28#get-the-authenticated-user">REST API</a> doesn't include this information [^1].

If you are looking for a list of all the timezones, then the <a href="https://docs.python.org/3/library/zoneinfo.html">zoneinfo</apy> package has you covered, no need to use <a href="https://pypi.org/project/pytz/">pytz</a> anymore.

With a model like this:

```python
zones = sorted(zoneinfo.available_timezones())


class Profile(models.Model):
    TIMEZONE_CHOICES = zip(zones, zones)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    timezone = models.CharField(max_length=255, choices=TIMEZONE_CHOICES, default="UTC")
```

You'll quickly have a nice form for the users.

### Using that timezone

Again, as noted in that document, you'll want to activate the timezone for that user as they hit the site.

```python
class TimezoneMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        tzname = request.session.get("tz")
        if not tzname:
            try:
                tzname = request.user.profile.timezone
            except (AttributeError):
                pass

        # You've got settings.TIME_ZONE set to "UTC" right? So that becomes the default.
        tzname = tzname or settings.TIME_ZONE
        timezone.activate(zoneinfo.ZoneInfo(tzname))

        # Stuff into the session for the next request.
        request.session["tz"] = tzname
        return self.get_response(request)
```

This is a pretty simplified middleware that activates the timezone and stuffs it in the session. So what's this going to do?

The date and time will be stored in the database as `UTC` as nature intended. But whenever it's shown to a user, it will be translated into their timezone. When you have a form, users enter the date and time in their timezone and Django stores it as UTC. This is pretty much exactly what you want in a web site.

### Gotchas

To show the date in `UTC` in a template, I used the `utc` filter. You can also use the `{% raw %}{% timezone None %}{% endraw %}` (as <a href="https://docs.djangoproject.com/en/4.2/topics/i18n/timezones/">documented</a>) or `localtime`. Otherwise Django was being smart and trying to convert into the timezone for me.

A model has `default=datetime.now` on it, meaning a HTML form defaulted to showing the time in `UTC`. This was simple to fix in the view, because when the view was being called, the middleware (see above) had been called, allowing us to know the users timezone. So then in the view, I simply switched to the users timezone:

```python
        form = EventForm()
        form.fields["start"].initial = timezone.now()
```

All this is well and good for the web interface, but what about the API? API's should always be in `UTC` and again that's something non-negotiable in my opinion. In the middleware, if the request is coming into an API endpoint (it's using Django Rest Framework) then the timezone just remains as UTC.

### Conclusion

That's it, nothing to revolutionary in this post, but just a pile of stuff that's builtin to Django and just gets it right in my opinion.

[^1]: I couldn't spot it in GraphQL either, sometimes the two aren't in sync so it might be there, couldn't find it though.

