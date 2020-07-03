---
layout: default
title: The archives
permalink: /archives/
date: 2002-09-09
---
<div class="meta">{{ page.date | date: "%b %d, %Y"  }}</div>

##[{{ page.title }}]({{ page.url }})

<ul class="archives">
{% for post in site.posts %}
<li><time>{{ post.date | date: "%b %d, %Y" }}</time>
    {% if post.categories[0] %}
      <span class="spacer">&mdash;</span> {{ post.categories[0] }}
    {% endif %}
    <span class="spacer">&mdash;</span> <a href="{{ post.url }}">{{ post.title }}</a></li>
{% endfor %}
</ul>
