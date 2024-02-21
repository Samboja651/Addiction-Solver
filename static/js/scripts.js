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


    function searchResources(query) {
        const searchRegex = new RegExp(query.trim(), "i");

        articles.forEach(article => {
            const articleContent = article.textContent.toLowerCase();
            if (searchRegex.test(articleContent)) {
                article.style.display = "block";
            } else {
                article.style.display = "none";
            }
        });

        videos.forEach(video => {
            const videoContent = video.textContent.toLowerCase();
            if (searchRegex.test(videoContent)) {
                video.style.display = "block";
            } else {
                video.style.display = "none";
            }
        });
    }

    // Event listener for search button
    const searchButton = document.getElementById("search-button");
    searchButton.addEventListener("click", function() {
        const searchInput = document.getElementById("search-input").value;
        searchResources(searchInput);
    });

    // Optional: Trigger search on pressing Enter key
    const searchInput = document.getElementById("search-input");
    searchInput.addEventListener("keyup", function(event) {
        if (event.key === "Enter") {
            const searchInputValue = searchInput.value;
            searchResources(searchInputValue);
        }
    });
});
