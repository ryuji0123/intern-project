$.getJSON('../json/sample.json', function(data) {
	var items = [];
	parseAndShowJson(data);
});

function parseAndShowJson(data) 
{
	$.each(data, function(key, val) {
		console.log(key, val);
	});
}
