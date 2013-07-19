---
layout: page
title: vindurriel
tagline: a coding site
---
{% include JB/setup %}
<div>  
  {% assign post = site.posts.first %}
  {% assign content = post.content %}
  {% include post_detail.html %}
</div>