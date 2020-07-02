function addLoadEvent(func) {
    var oldonload = window.onload;
    if (typeof window.onload != 'function') {
        window.onload = func;
    }
    else {
        window.onload = function() {
            oldonload();
            func();
        }
    }
}

function randomImage() {
    var head = document.getElementById("topbar");
    var num = Math.floor(Math.random() * 4);
    head.setAttribute("class", "image_" + num);
    head.className = "image_" + num;
}

addLoadEvent(randomImage);
