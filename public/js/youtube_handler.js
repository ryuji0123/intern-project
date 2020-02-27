let tag = document.createElement('script')
tag.src = 'https://www.youtube.com/iframe_api'

let video_src = 'https://www.youtube.com/watch?v=ZMcD_4w3Wyw'

let YoutubeHandleTag = document.getElementsByTagName('script')[0];

YoutubeHandleTag.parentNode.insertBefore(tag, YoutubeHandleTag);

let videoId = getVideoId(video_src);

function getVideoId(src)
{
	let params = src.split('?').slice(1).toString().split('&');
	for (let i = 0; i < params.length; i++) {
		tmp = params[i].split('=');
		if (tmp[0] == 'v') return tmp[1]; 
	}
	return '';
}

let player;

function onYouTubeIframeAPIReady()
{
	player = new YT.Player('player',
		{
			width: 640,
			height: 390,
			videoId: videoId,
			events: {
				'onReady': onPlayerReady,
				'onStateChange': onPlayerStateChange
			}
		}
	);
}

function onPlayerReady(event) {
	event.target.playVideo();
}


var done = false;
function onPlayerStateChange(event) {
	//if (event.data == YT.PlayerState.PLAYING && !done) {
	//}
}

function stopVideo() {
	player.stopVideo();
}
