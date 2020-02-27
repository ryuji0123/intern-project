window.onload = function()
{
	$.getJSON('../json/sample.json', function(data) {
		let i = 0;
		$('p#click_handler').click(function() {
			i = (i + 1) % Object.keys(data).length;
			player.seekTo(data[i]);
		});
		
		function parseAndShowJson(data) 
		{
			$.each(data, function(key, val) {
				console.log(key, val);
			});
		}
	});
	
	
};


