#!/bin/env python
# -*- coding: utf-8 -*-
import os
import markdown2
import re

def md_to_html(ifile,ofile):
    tpl=u'''
    <html>
	<head>
	    <meta charset="utf-8">
	    <meta name="viewport" content="width=device-width">
            <link rel="stylesheet" href="./{css}">
            <link rel="stylesheet" href="./{code_css}">
            <title>{title}</title>
	</head>
	<body class="publisher">
            <div class="container">
                <article id="preview-contents">
	        {body} 
                </article>
            </div>
	</body>
    </html>
    '''
    css='agroup.css'
    code_css='github.css'
    title=''
    reg=re.compile(r'^#\s*([^#]+)')
    m=reg.search(file(ifile,'r').read())
    if m:
        title=m.group(1).decode('utf8')
    body=markdown2.markdown_path(ifile,extras=[
        "fenced-code-blocks",
        "tables",
        "toc",
    ])
    html=tpl.format(**locals())
    file(ofile,'w').write(html.encode('utf8'))
if __name__=='__main__':
    md_path='./md'
    html_path='../'
    (_,_,fnames)=os.walk(md_path).next()
    for fname in fnames:
        if '.md' not in fname:
            continue
        base=os.path.splitext(fname)[0]
        ifile=os.path.join(md_path,fname)
        ofile=os.path.join(html_path,base+'.html')
        md_to_html(ifile,ofile)
