---
layout: post
title: "为gem install 提速"
description: "```<br/>:bulk_threshold: 1000<br/>:backtrace: false<br/>gemcutter_key: XXXXX<br/>gem: --no-ri --no-rdoc<br/>:benchmark: false<br/>:verbose: true<br/>:update_sources: true<br/>:sources: <br/>- http://gems.rubyforge.org/<br/>- http://gems.opscode.com<br/>```<br/>主要起作用的是`gem: --no-ri --no-rdoc`,少下载了很多文档。"
tags: 
- gem
- ruby
---

编辑`.gemrc`，内容如下：

```
:bulk_threshold: 1000
:backtrace: false
gemcutter_key: XXXXX
gem: --no-ri --no-rdoc
:benchmark: false
:verbose: true
:update_sources: true
:sources: 
- http://gems.rubyforge.org/
- http://gems.opscode.com
```
主要起作用的是`gem: --no-ri --no-rdoc`,少下载了很多文档。
