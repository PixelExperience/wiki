---
sidebar: home_sidebar
title: Information for maintainers
folder: meta
toc: false
permalink: help/developer-information/
---
So, you've decided you want to contribute to the PixelExperience. Awesome! This page provides reference material that may be useful to help you.

## List of links

These are pages you might want to check out for the information you are searching

{% assign sorted_pages = site.pages | sort: 'title' %}

{% for page in sorted_pages %}
{% if page.tags contains "internal" %}
- [{{ page.title }}]({{ page.url | relative_url }})
{% endif %}
{% endfor %}
