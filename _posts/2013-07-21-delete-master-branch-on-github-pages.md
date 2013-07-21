---
layout: post
title: 删除github pages的master分支
description: ""
tags: 
- github pages
---

github pages默认使用两个分支：master和gh-pages。 在两个分支间切换很不方便：在gh-pages写了一些blog，然后切回master进行一次push，才能让服务器重新build。

但是可以删除master。 首先到github.com的repo设置里面把默认分支设为gh-pages，然后删除master分支，最后回到本地，用 `git branch -D master` 删除master分支。
