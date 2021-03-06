---
layout: post
title: Django miscellany
categories: Django
old: 2078
blog: andy-mckay
---
<p>My colleagues got hit by <a href="http://blog.cottee.org/2008/04/django-settings-file.html">this issue the other day</a>. It's a definite annoyance, and just for the record here's my version, just on the off chance that <code>os.curdir</code> is different.</p>
<pre>
import os
this = os.path.dirname(os.path.abspath(__file__))

TEMPLATE_DIRS = (
    "%s/jobs/templates" % this,
)
</pre>
<p>On other things I integrated django-openid the other day into a Django site and its really nice. It worked really well, although I do have to find a way of altering the templates to go nicely into my Page Templated site. I do have to put in some work to the login screen. I have to explain the OpenId login, without making it too daunting and provide an easy way to create an account.</p>
<p>Finally I had a quick play with Google maps. Want to show a map based on a UK postcode? How about:</p>
<pre>
          var postcode = "L7 9NJ";
          if (postcode != "") {
              if (GBrowserIsCompatible()) {
                var map = new GMap2(mapnode);
                var lookup = new GClientGeocoder();
                lookup.setBaseCountryCode('uk');            
                map.addControl(new GSmallMapControl());                
                lookup.getLatLng(postcode, function(point){
                    map.setCenter(point, 12);
                });
              }
          }
</pre>
<p>Yay. Not the encoding has to done with setBaseCountryCode as <code>UK</code>, not <code>.co.uk</code> or <code>gb</code>. Otherwise it centres on Germany, not Liverpool. </p>