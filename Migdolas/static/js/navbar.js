document.addEventListener('DOMContentLoaded', function() {
    const searchContainer = document.querySelector('.search-container');
    const searchToggle = document.querySelector('.search-toggle');
    const searchInput = document.querySelector('.search-input');
    
    // Toggle search visibility
    searchToggle.addEventListener('click', function(e) {
        e.preventDefault();
        searchContainer.classList.add('active');
        searchInput.focus();
    });
    
    // Close when clicking outside
    document.addEventListener('click', function(e) {
        if (!searchContainer.contains(e.target)) {
            searchContainer.classList.remove('active');
        }
    });
    
    // Close on Escape key
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape') {
            searchContainer.classList.remove('active');
        }
    });
});