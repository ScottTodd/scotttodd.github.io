---
layout: page
title: Home
tagline: My personal page and portfolio.
group: navigation
---
{% include JB/setup %}

This website is home to my portfolio. Check out the navigation links in the banner up above.

<hr>

Featured Projects
-----------------

<div>
  {% for post in site.posts %}
    {% if post.title_images %}
      {% if post.title_images.first %}
        {% capture image %}{{ post.title_images.first }}{% endcapture %}
      {% else %}
        {% capture image %}{{ post.title_images }}{% endcapture %}
      {% endif %}
      <a href="{{ post.url }}"><img src="{{ image }}" class="featured-image" title="{{ post.title }}"></a>
    {% endif %}
  {% endfor %}
</div>
