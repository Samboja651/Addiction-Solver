document.addEventListener("DOMContentLoaded", function() {
    const articles = document.querySelectorAll(".article");
    const videos = document.querySelectorAll(".video");

    // Function to show/hide articles based on category
    function filterArticles(category) {
        articles.forEach(article => {
            if (category === "all" || article.dataset.category === category) {
                article.style.display = "block";
            } else {
                article.style.display = "none";
            }
        });
    }

    // Event listener for filter buttons
    const filterButtons = document.querySelectorAll(".filter-btn");
    filterButtons.forEach(btn => {
        btn.addEventListener("click", function() {
            const category = this.dataset.category;
            filterArticles(category);
        });
    });
});
