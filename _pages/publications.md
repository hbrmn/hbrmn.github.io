---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

This page lists selected publications. Open an article to find its details and, where available, a downloadable manuscript. For a more complete and current list, see my linked researcher profiles.

{% if site.author.googlescholar %}
  You can also find my articles on <u><a href="{{site.author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
