window.addEventListener("load", (event) => {
    const carouselElement = document.getElementById("carousel");
    if (carouselElement) {
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
});