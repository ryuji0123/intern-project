const SAMPLE_IMG_BASE_PATH = './img/';

$.getJSON('../json/length.json', function(data)
{
	const number_of_sample_images = data['length'];

	window.onload = function()
	{
		$.getJSON('../json/sample.json', function(data)
		{
			createSliderElement($('div#img-slider-container'), data);
			$('div.slide').click(function() {
				let time_to_seek = $(this).attr('data-seek-time');
				if (time_to_seek === undefined || time_to_seek === 'empty') {
					return;
				}
				player.seekTo(time_to_seek);
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
					let child_div = $("<div class='slide' data-seek-time=" + data[i] + "><img src=" + current_img_path  + "></div>")
					if (data.length <= i) {
						child_div.attr('data-seek-time', 'empty');
					}
					child_div.appendTo(parent_div);
				}
			}

			let slide_index = 1;
	    	showSlides();
	    	$('a.prev').click(function() {
	    		plusSlides(-1)
			});
			$('a.next').click(function() {
				plusSlides(1)
			});


			document.onkeydown= function (e) {
				e = e || window.event;
				if (e.keyCode === 37) {
					plusSlides(-1);
				} else if (e.keyCode === 39) {
					plusSlides(1);
				}
			}


	    	function showSlides() {
	    	    let i;
	    	    let slides = document.getElementsByClassName('slide');
	    	    if (slide_index > slides.length) {
	    	        slide_index = 1;
	    	    }
	    	    if (slide_index < 1) {
	    	        slide_index = slides.length;
	    	    }

	    	    for (i = 0; i < slides.length; i++) {
	    	        slides[i].style.display = 'none';
	    	    }

	    	    slides[slide_index - 1].style.display = 'block';
	    	}

			function currentSlide(n)
			{
				showSlides();
			}

			function plusSlides(n)
			{
				slide_index += n
				showSlides();
			}

		});
	};
})
