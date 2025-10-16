//数据准备完毕，开始画图
var width = window.innerWidth/2;
height = 400;
//两个力场的中心位置
var foci={
    "post":{"x":0,"y":height/2},
    "tag":{"x":width,"y":height/2},
};
var color = d3.scale.category10();
var force = d3.layout.force()
    .linkDistance(100)
    .linkStrength(.3)
    .gravity(0)
.size([width, height]);
var svg = d3.select("#svg").append("svg")
    .attr("width", width)
    .attr("height", height);
force
    .charge(-400)
    .nodes(graph.nodes)
    .links(graph.links)
    .start();
var link = svg.selectAll(".link")
    .data(graph.links)
    .enter().append("line")
    .attr("class", "link");
var node = svg.selectAll(".node")
    .data(graph.nodes)
    .enter().append("circle")
    .attr("class", "node")
    .attr("r",10)
    .on("click",function(d){
        window.open(d.url);
    })
    .style("cursor","pointer")
    .style("fill", function(d) { return color(d.type); })
    .call(force.drag);
node.append("title")
    .text(function(d) { return d.name; });
force.on("tick", function(e) {
    link.attr("x1", function(d) { return d.source.x; })
        .attr("y1", function(d) { return d.source.y; })
        .attr("x2", function(d) { return d.target.x; })
        .attr("y2", function(d) { return d.target.y; });
    //e.alpha是“温度”，粒子的“活性”与之相关，它是一个不断下降的变量，模拟冷却过程。
    var k = .5 * e.alpha;
    //让每个粒子都被力场减速吸向中心，直到温度为0
    //同时每个粒子还受到库仑力(由force.charge定义)，从而彼此不会聚合在一起。
    graph.nodes.forEach(function(o, i) {
        o.y += (foci[o.type].y - o.y) * k;
        o.x += (foci[o.type].x - o.x) * k;
    });
    node.attr("cx", function(d) { return d.x; })
        .attr("cy", function(d) { return d.y; });
});