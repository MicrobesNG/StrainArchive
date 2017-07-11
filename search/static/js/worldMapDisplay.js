
function drawMap(data) {


    console.log(data);

    var margin = {top: 0, right: 0, bottom: 0, left: 0},
        width = 960 - margin.left - margin.right,
        height = 500 - margin.top - margin.bottom;

    var path = d3.geoPath();

    var svg = d3.select("body")
                .append("svg")
                    .attr("width", width)
                    .attr("height", height)
                    .append('g')
                        .attr('class', 'map');

        svg.append("g")
            .attr("class", "countries")
            .selectAll("path")
            .data(data)
            .enter()
                .append("path")
                    .attr("d", path)
                    .style("fill", "#3f3f3f")
                    .style('stroke', 'white')
                    .style('stroke-width', 1.5)
                    .style("opacity",0.8)
                    .style("stroke","white")
                    .style('stroke-width', 0.3)
                    .on('mouseover',function(d){
                        d3.select(this)
                            .style("opacity", 1)
                            .style("stroke","white")
                            .style("stroke-width",3);
                    })
                    .on('mouseout', function(d){
                        d3.select(this)
                            .style("opacity", 0.8)
                            .style("stroke","white")
                            .style("stroke-width",0.3);
                    });

                    svg.append("path")
                        .datum(topojson.mesh(data.objects.countries, function(a, b) {
                            return a.id !== b.id;
                        }))
                        .attr("class", "names")
                        .attr("d", path);
}



$(document).ready(function() {
    drawMap(worldJson);
});