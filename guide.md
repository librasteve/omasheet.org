---
layout: single
permalink: /guide/
author_profile: true
---

{% capture content %}
{% include_relative external/omasheet/docs/format.md %}

{% include_relative external/omasheet/docs/expressions.md %}

{% include_relative external/omasheet/docs/app.md %}

{% include_relative external/omasheet/docs/interop.md %}
{% endcapture %}
{{ content }}
