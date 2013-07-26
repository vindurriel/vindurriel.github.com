---
---
var docs = 
[ 
{% for post in site.posts%}
	{
		"id"    : {{ forloop.index() }},
		"url": "{{site.production_url}}{{ post.url }}",
		"title"   : "{{ post.title }}",
		"content" : "{{ post.content | strip_html | strip_newlines | remove:'"'  }}"
	},
{% endfor %}
];
// init lunr
var idx = lunr(function () {
	this.field('title', 10);
	this.field('content');
})
// add each document to be index
for(var index in docs) {
	idx.add(docs[index]);
}

$(function() {
  $("#search .btn").click(function() {
    search();
  });
  $("#search input").keypress(function(e) {
    if(e.which == 13) {
      e.preventDefault();
      search();
    }
  });
})

function search() {
  var result = idx.search($("#search input").val());
  $("#myModal .modal-body").empty();
  if(result && result.length > 0) {
  	for(var i=0;i< result.length;i++){
  		var x= docs[parseInt(result[i].ref)-1].title;
    	$("#myModal .modal-body").append("<p>"+x+"</p>");
  	}
  } else {

  }
}