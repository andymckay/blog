document.onreadystatechange = function () {
	var links = document.getElementsByTagName('a');
	var audio = document.getElementsByTagName('audio')[0];
	function clicky(e) {
		audio.src = '/files/darth/wavs/' + this.dataset.wav;
		audio.play();
		e.stopPropogation();
	}
	for (var i = 0; i < links.length; i++) {
		links[i].addEventListener('click', clicky);
	}
};
