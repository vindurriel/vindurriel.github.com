---
layout: post
title: "github pages 配置"
tags: 
- jekyll
- github pages
- setup
description: ""
---

首先去github pages申请一个页面，默认的域名是`http://USERNAME.github.io`，其中`USERNAME`是你的github用户名。

github使用jekyll做解析引擎。可以直接克隆一个别人写好的jekyll，然后把上传路径改成自己的，像这样：

```
git clone https://github.com/plusjade/jekyll-bootstrap.git USERNAME.github.com
cd USERNAME.github.com
git remote set-url origin git@github.com:USERNAME/USERNAME.github.com.git
git push origin master
```

这个例子中使用的是[jekyll-bootstrap]("https://github.com/plusjade/jekyll-bootstrap")。

###写文章

如果装了ruby的话，直接在文件夹下执行

	rake post title="a new post"

就可以新建一篇文章。内容支持markdown。

其实就是在_post目录下新建了一个md文件，文件名格式为`年-月-日-标题.md`。 文件开始是一些元信息，比如本文的md文件开头是这样的：

```
---
layout: post
title: "github pages 配置"
description: ""
category: misc
tags: [jekyll,github pages,setup]
---
```
写好了内容部分，直接`git commit`然后`git push`到master分支就可以了。

###评论

jekyll-bootstrap本身不提供评论功能，而是通过配置文件引入第三方评论插件， 比如[disqus](http://disqus.com/)。 

配置集中在`_config.yml`中，与评论功能有关的配置可以这样写：

	comments :
	    provider : disqus
	    disqus :
	      short_name : YOUR_DISQUS_SITE_NAME
	      
你需要去disqus.com注册一个用户，然后在dashboard中新建一个站点，注意把`short_name`设置为配置文件中的那个`YOUR_DISQUS_SITE_NAME`。

disqus插件的语言可以切换为中文，需要在disqus.com登陆后进入admin->settings，也就是 [http://USERNAME.disqus.com/admin/settings/](http://USERNAME.disqus.com/admin/settings/)，里面可以设置language。

###分享

jekyll-bootstrap的分享功能还没写好， 所以我找了个国内比较成熟的社会化分享平台： [加网](http://www.jiathis.com/getcode/icon)。把js粘到模板里就行。

###中文编码问题
windows下本jekyll在解析中文的页面时会报编码错误。如果使用cmd的话，需要把代码页改成utf-8：

	$ CHCP 65001

如果是在git bash中的话，需要设置如下环境变量： 
	
	export LC_ALL = enUS.UTF-8
	export LANG   = enUS.UTF-8

然后就可以 `jekyll serve --watch`了。

###代码高亮

默认使用pygments.rb。 版本高于0.5.0在windows和ruby1.9.3下显示不出来，需要安装0.5.0，即

	gem uninstall pygments.rb --version ">0.5.0"
	gem install pygments.rb --version "=0.5.0"

还需要一个代码高亮的css的文件，google `pygments css style`可以找到好多。