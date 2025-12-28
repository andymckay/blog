window.addEventListener("load", (event) => {
    const carouselElement = document.getElementById("carousel");
    if (carouselElement) {
        const carousel = new bootstrap.Carousel(carouselElement, {
            interval: 20000,
            wrap: true,
            touch: true,
            ride: 'carousel',
        });
    }
    for (let el of document.getElementsByClassName("strava-explanation")) {
        el.style.display = "none";
    }
});