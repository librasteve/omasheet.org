---
title: "Posts"
permalink: /posts/
layout: base
excerpt: "Notes on building Omasheet: why, how, and what you can do with it."
---
<main class="page wide">
  <div class="page-head">
    <h1>Posts</h1>
    <p class="lede">Notes on building Omasheet: why, how, and what you can do with it.</p>
  </div>
  <div class="postlist">
  {% for post in site.posts %}
    <a class="postcard{% unless post.header.teaser %} noimg{% endunless %} rise" href="{{ post.url }}">
      <div>
        <div class="kicker">{{ post.date | date: "%-d %B %Y" }}</div>
        <h2>{{ post.title }}</h2>
        <p>{{ post.excerpt | strip_html | strip }}</p>
      </div>
      {% if post.header.teaser %}<div class="thumb"><img src="{{ post.header.teaser }}" alt="" loading="lazy"></div>{% endif %}
    </a>
  {% endfor %}
  </div>
</main>
