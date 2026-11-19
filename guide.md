---
layout: docs
permalink: /guide/
title: "Guide"
wide: true
---

{% capture content %}
{% include_relative external/omasheet/docs/format.md %}

{% include_relative external/omasheet/docs/expressions.md %}

{% include_relative external/omasheet/docs/app.md %}

{% include_relative external/omasheet/docs/interop.md %}
{% endcapture %}
{{ content | remove: "Copyright (c) 2026 Stephen Roe. MIT licence." }}

---

Copyright (c) 2026 Stephen Roe. MIT licence.
