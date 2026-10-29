---
title: "Posts"
permalink: /posts/
layout: archive
author_profile: true
---

{% for post in site.posts %}
  {% include archive-single.html type="grid" %}
{% endfor %}
