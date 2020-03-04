const SAMPLE_IMG_BASE_PATH = './img/';
const number_of_sample_images = 16;

window.onload = function()
{
	$.getJSON('../json/sample.json', function(data) {
		createSliderElement($('div#img-slider-container'), data);
		$('div.slide').click(function() {
			let time_to_seek = $(this).attr('data-seek-time');
			if (time_to_seek === undefined) {
				return;
			}
			player.seekTo(time_to_seek);
			console.log(time_to_seek);
		});
		
		function parseAndShowJson(data) 
		{
			$.each(data, function(key, val) {
				console.log(key, val);
			});
		}

		function createSliderElement(parent_div, data)
		{
			for (let i = 0; i < number_of_sample_images; i++) {
				let current_img_path = SAMPLE_IMG_BASE_PATH + 'sample' + i + '.png';
				$("<div class='slide' data-seek-time=" + data[i] + "><img src=" + current_img_path  + "></div>").appendTo(parent_div);
			}
		}
	});
	
	
};


