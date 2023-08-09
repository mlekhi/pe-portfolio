<script>
    const carouselContainer = document.querySelector('.carousel-container');
    const slides = document.querySelectorAll('.carousel-slide');
    let currentIndex = 0;

    function showSlide(index) {
    if (index < 0) {
    currentIndex = slides.length - 1;
} else if (index >= slides.length) {
    currentIndex = 0;
}
    carouselContainer.style.transform = `translateX(-${currentIndex * 100}%)`;
}

    setInterval(() => {
    currentIndex++;
    showSlide(currentIndex);
}, 5000); // Change slide every 5 seconds
</script>
