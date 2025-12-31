window.addEventListener("load", (event) => {
    const carouselElement = document.getElementById("carousel");
    if (0) { //carouselElement) {
        const carousel = new bootstrap.Carousel(carouselElement, {
            interval: 5000,
            wrap: true,
            touch: true,
            keyboard: true,
            ride: 'carousel',
        });
    }
    for (let el of document.getElementsByClassName("strava-explanation")) {
        el.style.display = "none";
    }

    function changeScreen(event) {
        let carouselElement = event.target.parentNode.parentNode;
        carouselElement.classList.toggle("modal-fullscreen");
        if (event.target.text == "Bigger") {
            event.target.text = "Smaller";
        } else {
            event.target.text = "Bigger";
        }
        //event.preventDefault();
    }

    for (let el of document.getElementsByClassName("carousel-enlarge")) {
        for (let a of el.getElementsByTagName("a")) {
            a.addEventListener("click", changeScreen);
        }
    }
});