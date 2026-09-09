---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

Selected publications on NMR methods, glass structure, and functional materials. Open a title for a short summary, citation, and available manuscript.

{% if site.author.googlescholar %}
  For a broader list, visit <a href="{{ site.author.googlescholar }}">my Google Scholar profile</a>.
{% endif %}

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
