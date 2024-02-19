document.addEventListener("DOMContentLoaded", function() {
    const articles = document.querySelectorAll(".article");
    const videos = document.querySelectorAll(".video");

    // Function to show/hide articles based on category
    function filterArticles(category) {
        articles.forEach(article => {
            const articleCategory = article.dataset.category.toLowerCase();
            if (category === "all" || articleCategory === category) {
                article.style.display = "block";
            } else {
                article.style.display = "none";
            }
        });
    }

    // Function to show/hide videos based on category
    function filterVideos(category) {
        videos.forEach(video => {
            const videoCategory = video.dataset.category.toLowerCase();
            if (category === "all" || videoCategory === category) {
                video.style.display = "block";
            } else {
                video.style.display = "none";
            }
        });
    }

    // Event listener for filter buttons
    const filterButtons = document.querySelectorAll(".filter-btn");
    filterButtons.forEach(btn => {
        btn.addEventListener("click", function() {
            const category = this.dataset.category.toLowerCase();
            filterArticles(category);
            filterVideos(category);
        });
    });
});
