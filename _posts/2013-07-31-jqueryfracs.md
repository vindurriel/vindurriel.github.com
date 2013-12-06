---
layout: post
title: "jquery.fracs"
description: "- d3.parsets.css<br/>- d3.v3.min.js<br/>- d3.parsets.js<br/>{% highlight text %}<br/>{{ page.title }},d3<br/>{{ page.title }},visualization<br/>{% endhighlight %}<br/>{% highlight javascript %}<br/>{%raw%}<br/>var csv=&quot;post,tag&quot;;<br/>{% for post in site.posts %}<br/>	{% for tag in post.tags %}<br/>		csv+=&quot;
{{post.title}},{{tag}}&quot;;<br/>	{% endfor %}<br/>{% endfor %}<br/>{%endraw%}<br/>{% endhighlight %}<br/>{% highlight javascript %}<br/>var chart = d3.parsets()<br/>	  .tension(0.8)<br/>	  .width(&quot;800&quot;)<br/>	  .height(&quot;480&quot;)<br/>      .dimensions([&quot;tag&quot;,&quot;post&quot;]);<br/>var vis = d3.select(&quot;#vis&quot;).append(&quot;svg&quot;)<br/>    .attr(&quot;width&quot;, chart.width())<br/>    .attr(&quot;height&quot;, chart.height());<br/>var parsed_csv=d3.csv.parse(csv);<br/>vis.datum(parsed_csv).call(chart);<br/>{% endhighlight %}<br/>{% highlight javascript %}<br/>{%raw%}<br/>var posts={};<br/>{% for post in site.posts %}<br/>	posts[&quot;{{post.title}}&quot;]={<br/>		&quot;url&quot;:&quot;{{post.url}}&quot;,<br/>	};<br/>{% endfor %}<br/>vis.selectAll(&quot;.category text&quot;).on(&quot;click&quot;,function(d){<br/>	if(!"
category: 
tags:
- jquery
- visualization
---
[jquery.fracs](http://larsjung.de/fracs/)是一个jquery插件，可用于网站大纲视图的显示，用来替代滚动条。
