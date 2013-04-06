---
layout: post
title: TalFlatPages
categories: Django
old: 2038
blog: andy-mckay
---
<p>Django provides <a href="http://www.djangoproject.com/documentation/flatpages/">flatpages</a> but these won't inherit from your page templated pages, only the Django templating language one. Talflatpages is a very simple app that copies completely from flatpages, but changes the default template to be a tal one, using main_template in a macro (I'm sure you can change this to suit your site).</p>
<p>Only a small project so not bothering with a release, grab it from SVN here:</p>
<pre> http://svn.clearwind.ca/public/django/talflatpages/</pre>
<p><b>Update:</b> got the URL for SVN wrong, corrected.</p>