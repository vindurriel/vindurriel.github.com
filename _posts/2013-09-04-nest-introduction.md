---
layout: post
title: "nest介绍之音乐地图"
description: "一个节点(node)表示一个元素或者元素的某个属性，节点之间的连线(link)表示元素之间的关系。<br/>元素和关系的类型、属性都可以是任意定制的。<br/>传统的展示元素和关系的视觉组件有列表、树等，但是所能展示的拓扑关系必须是有向无环图(DAG)，通俗的比喻，张三的儿子的儿子不可能是他爹。<br/>[](/images/nest/2.png)<br/>* 左键拖拽： 空白处平移，节点上调整节点位置。<br/>* 左键双击节点： 扩展该节点，即添加与该节点有关系的新节点。<br/>* alt+左键单击节点： 将该节点设为根节点。<br/>[](/images/nest/3.png)"
category: ""
banner: "/images/nest/1.png"
tags:
- visualization
- graph
- d3
---

nest([https://github.com/vindurriel/nest](https://github.com/vindurriel/nest))是一个视觉组件，它用图(graph)来展示元素之间的关系。一个节点(node)表示一个元素或者元素的某个属性，节点之间的连线(link)表示元素之间的关系。 元素和关系的类型、属性都可以是任意定制的。使用者可以和图进行交互， 允许的操作包括拖拽、添加、删除、聚焦、平移和放缩。
节点的颜色由数据实体的`type`属性决定，不同type即颜色之间的节点，使用一种特殊type的节点连接，这种节点的type是relationship(关系)。

##为什么要做

传统的展示元素和关系的视觉组件有列表、树等，但是所能展示的拓扑关系必须是有向无环图(DAG)，通俗的比喻，张三的儿子的儿子不可能是他爹。现实生活中很多元素间的关系满足DAG， 但是不满足例子也很多，比如朋友关系，张三的朋友的朋友可能也是张三的朋友，这在关系上就形成了一个环，不满足DAG。而图可以表示非DAG的拓扑关系，也就是所谓的网络。

nest是为了展示图而生的视觉组件，它能在二维平面展示复杂的元素关系，并且用户可以实时地修改图的布局、增删节点。

nest可以作为脑图使用，也可以作为更一般意义上的关系展示图，参见下面的[例子](http://nest.ap01.aws.af.cm/model/artist_23401?theme=light)。

##例子

音乐地图([http://nest.ap01.aws.af.cm/model/python?theme=light](http://nest.ap01.aws.af.cm/model/artist_23401?theme=light))是一个探索音乐元素之间关系的动态地图，展示歌曲、艺术家、专辑和精选集之间的关系。数据抓取自[虾米网](http://www.xiami.com)。

![](/images/nest/2.png)

使用方法如下：

* 搜索框中可搜索音乐。

* 点击`see all`可查看其他用户已经探索过的音乐地图。

* `保存`按钮可以上传当前音乐地图。

* `?`按钮中可显示图例。 

* 左键单击节点： 选中该节点，可能会弹出可供扩展的关系节点（如选中歌曲节点，弹出歌曲所在的专辑和歌手）

* 左键拖拽： 空白处平移，节点上调整节点位置。

* 左键双击节点： 扩展该节点，即添加与该节点有关系的新节点。支持svg动画的浏览器上(chrome、firefox、<del>IE</del>)该节点会振动，并弹出同类型的新节点。

* ctrl+左键单击节点： 同左键双击节点。

* shift+左键单击节点： 删除该节点，同时一并删除**只与**该节点有连线的所有节点

* alt+左键单击节点： 将该节点设为根节点。图本身无所谓根节点，根节点的唯一目的在于以该节点的id来存储图。

* 地址栏中可修改theme参数,支持light和dark。

![](/images/nest/3.png)

##技术

nest在前台采用了[d3.js](https://github.com/mbostock/d3/wiki)，而d3.js采用了svg。 后台是[web.py](http://webpy.org)。 前后台通信采用了ajax和json。

源代码在github [https://github.com/vindurriel/nest](https://github.com/vindurriel/nest)。

##开发计划

1. 将nest组件化， 允许嵌入到任意的html网页中

2. 固化二次开发的接口， 提供SDK