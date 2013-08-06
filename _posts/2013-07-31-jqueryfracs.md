---
layout: post
title: "jquery.fracs"
description: ""
category: 
tags:
- jquery
---
[jquery.fracs](http://larsjung.de/fracs/)是一个jquery插件，可用于网站大纲视图的显示，用来替代滚动条。

{%raw%}
```javascript
var graph={
    "nodes":[],
    "links":[],
};
var hash_tag={};
var post_id=0,tag_id=0;
{% for post in site.posts %}
    graph.nodes.push({
        "name": "{{ post.title }}",
        "url":"{{post.url}}",
        "type":"post", 
    });
    post_id=graph.nodes.length-1;
    {% for tag in post.tags %}
        if(hash_tag["{{tag}}"]===undefined){
            graph.nodes.push({
                "name": "{{ tag }}",
                "url":"/tags.html",
                "type":"tag",
            });
            tag_id=graph.nodes.length-1;
            hash_tag["{{tag}}"]=tag_id;
        } else {
            tag_id=hash_tag["{{tag}}"];
        }
        graph.links.push({
            "source":post_id,
            "target":tag_id,
            "value":1    
        });
    {% endfor %}
{% endfor %}
```
{%endraw%}
