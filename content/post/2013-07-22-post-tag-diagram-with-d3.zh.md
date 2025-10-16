---
date: "2013-07-22T00:00:00Z"
tags:
- d3
- visualization
title: 用d3.js来呈现post-tag的多对多关系
---

最近想用更好的方式呈现blog和tag之间的关系，也就是重写本博客的[标签页面](/tags)。

blog和tag之间是多对多的关系，就是说一篇blog可以有多个tag，一个tag可以包含多篇blog。适合表现这种映射关系的图表叫做平行集（Parallel Set）。

平行集是反应两组或以上数据集之间映射关系的图表。


[d3](https://github.com/mbostock/d3/wiki/Gallery)是一个用javascript的库，主要用途是用svg做数据可视化。 

d3非常强大，基本上能想到的图表都可以实现。而对于平行集，d3有一个插件[d3.parsets](https://github.com/jasondavies/d3-parsets)。

需要添加如下css和js：

- d3.parsets.css
- d3.v3.min.js
- d3.parsets.js

然后在tags.html里写一些javascript。

先构造出所有post和tag的对应数据。[d3.parsets](https://github.com/jasondavies/d3-parsets)使用csv格式，所以要先生成一个csv格式的字符串。在这里，列名就是`post,tag`。
比如本篇blog对应两个tag：`d3`和`visualization`，那么要在csv里添加两行:

```text
{{ page.title }},d3
{{ page.title }},visualization
```

相关代码如下：

```js
var csv="post,tag";
{% for post in site.posts %}
	{% for tag in post.tags %}
		csv+="\n{{post.title}},{{tag}}";
	{% endfor %}
{% endfor %}
```

接着实例化一个chart，再把数据给它：

```js
var chart = d3.parsets()
	  .tension(0.8)
	  .width("800")
	  .height("480")
      .dimensions(["tag","post"]);
var vis = d3.select("#vis").append("svg")
    .attr("width", chart.width())
    .attr("height", chart.height());
var parsed_csv=d3.csv.parse(csv);
vis.datum(parsed_csv).call(chart);
```

我还想实现这样一个功能：点击图中的博客时可以跳转到博客页面。

```js
var posts={};
{% for post in site.posts %}
	posts["{{post.title}}"]={
		"url":"{{post.url}}",
	};
{% endfor %}
vis.selectAll(".category text").on("click",function(d){
	if(!(d.name in posts)) return;
	window.open(posts[d.name].url);
});
```

d3虽然可以看到很多jQuery的影子， 但在data和view的生成方式上很独特，非常地描述化。
[这篇文章](http://bost.ocks.org/mike/join/)是作者自己总结的d3处理数据上的一种模式，也就是所谓的`join`。