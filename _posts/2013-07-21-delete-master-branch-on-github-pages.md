---
layout: post
title: 删除github pages的master分支
description: ""
tags:
- github pages
---

github pages默认使用两个分支：master和gh-pages。 在两个分支间切换很不方便：在gh-pages写了一些blog， 然后切回master进行一次push，才能让服务器重新build。

<del>但是可以删除master。 首先到github.com的repo设置里面把默认分支设为gh-pages，然后删除master分支，最后回到本地，用 `git branch -D master` 删除master分支。</del>

但是删除master后，发现远端页面更新非常缓慢，而且页面状态不稳定（有的页面更新了，有的则没有）。因此后来恢复了用两个分支。[有文章](http://lea.verou.me/2011/10/easily-keep-gh-pages-in-sync-with-master/)介绍可以用post commit hook来保持两个分支的一致性。