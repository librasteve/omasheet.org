---
layout: single
permalink: /getting-started/
author_profile: true
---

{% capture content %}
{% include_relative external/omasheet/README.md %}
{% endcapture %}
{% assign parts = content | split: '## Install' %}
## Install
{{ parts[1] }}
