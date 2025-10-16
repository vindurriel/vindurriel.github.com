---
date: "2013-07-19T00:00:00Z"
tags:
- gem
- ruby
title: 为gem install 提速
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
