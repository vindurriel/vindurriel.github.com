---
layout: post
title: "forced graph"
date: "2013-07-30"
description: ""
category:
tags:
- d3
- visualization
- physics
- graph
---
下图是用d3中的forced graph画出的post和tag的关联关系。为了区别post和tag，使用了两种颜色，
并且施加了两个力场，把post向左推，tag向右推。

{% highlight js %}
{% raw %}
//准备post和tag的关联数据
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
//数据准备完毕，开始画图
var width = 400,
height = 400;
//两个力场的中心位置
var foci={
    "post":{"x":0,"y":height/2},
    "tag":{"x":width,"y":height/2},
};
var color = d3.scale.category10();
var force = d3.layout.force()
    .linkDistance(100)
    .linkStrength(.3)
    .gravity(0)
.size([width, height]);
var svg = d3.select("#svg").append("svg")
    .attr("width", width)
    .attr("height", height);
force
    .charge(-400)
    .nodes(graph.nodes)
    .links(graph.links)
    .start();
var link = svg.selectAll(".link")
    .data(graph.links)
    .enter().append("line")
    .attr("class", "link");
var node = svg.selectAll(".node")
    .data(graph.nodes)
    .enter().append("circle")
    .attr("class", "node")
    .attr("r",10)
    .on("click",function(d){
        window.open(d.url);
    })
    .style("cursor","pointer")
    .style("fill", function(d) { return color(d.type); })
    .call(force.drag);
node.append("title")
    .text(function(d) { return d.name; });
force.on("tick", function(e) {
    link.attr("x1", function(d) { return d.source.x; })
        .attr("y1", function(d) { return d.source.y; })
        .attr("x2", function(d) { return d.target.x; })
        .attr("y2", function(d) { return d.target.y; });
    //e.alpha是“温度”，粒子的“活性”与之相关，它是一个不断下降的变量，模拟冷却过程。
    var k = .5 * e.alpha;
    //让每个粒子都被力场减速吸向中心，直到温度为0
    //同时每个粒子还受到库仑力(由force.charge定义)，从而彼此不会聚合在一起。
    graph.nodes.forEach(function(o, i) {
        o.y += (foci[o.type].y - o.y) * k;
        o.x += (foci[o.type].x - o.x) * k;
    });
    node.attr("cx", function(d) { return d.x; })
        .attr("cy", function(d) { return d.y; });
});
{% endraw %}
{% endhighlight %}

效果如下：

<div id="svg"></div>
<script type="text/javascript" src="/javascripts/d3.v3.min.js"></script>
<script type="text/javascript" src="/javascripts/forced-graph.js"></script>

参考了下面两个例子：

- [Custom Forces](http://bl.ocks.org/mbostock/1021841)
- [Labeled Force Layout](http://bl.ocks.org/mbostock/950642)