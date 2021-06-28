---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

To download a pre-print version of each article, click on the article's title and see below.

{% if site.author.googlescholar %}
  You can also find my articles on <u><a href="{{site.author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
