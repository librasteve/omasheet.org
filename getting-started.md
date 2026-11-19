---
layout: docs
permalink: /getting-started/
title: "Getting started"
---

{% capture content %}
{% include_relative external/omasheet/README.md %}
{% endcapture %}
{% assign parts = content | split: '## Install' %}
## Install
{{ parts[1] }}
