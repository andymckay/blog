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

window.addEventListener('DOMContentLoaded', () => {
    function switchTheme(event) {
        let html = document.getElementsByTagName("html")[0];
        let theme = html.getAttribute("data-bs-theme") === "dark" ? "light" : "dark";
        html.setAttribute("data-bs-theme", theme);
        localStorage.setItem("theme", theme);
        event.preventDefault();
    }


    for (let el of document.getElementsByClassName("theme-switch")) {
        el.addEventListener("click", switchTheme);
    }

    let theme = localStorage.getItem("theme");
    if (!theme) {
        theme = window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
    }
    if (theme) {
        document.getElementsByTagName("html")[0].setAttribute("data-bs-theme", theme);
    }
});