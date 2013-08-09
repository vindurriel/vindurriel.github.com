(function($){
	$(document).ready(function(){
	$("#outline").fracs("outline", {
		crop: true,
		styles: [{
			selector: 'p',
			fillStyle: '#fff'
		},{
			selector: '.mybtn',
			fillStyle: 'rgb(104,169,255)'
		},{
			selector: 'h1',
			fillStyle: '#888',
		},{
			selector: 'h2,h3',
			fillStyle: '#aaa',
		},{
			selector:".next-page",
			fillStyle:"#eee"
		},{
			selector:"pre,svg,img",
			fillStyle:"#eee"
		}],
		viewportStyle: {
			fillStyle: 'rgba(104,169,255,0.1)',
		},
		viewportDragStyle: {
			fillStyle: 'rgba(104,169,255,0.3)'
		}
	});
	$("#btn_share").click(function(){
		$("#share").toggle();
	})
	$("#btn_comment").click(function(){
		$("#comment").toggle();
	})
});
})(jQuery);