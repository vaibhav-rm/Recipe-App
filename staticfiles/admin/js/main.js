// myapp/static/js/main.js

function loadPage(url) {
    fetch(url)
        .then(response => response.text())
        .then(html => {
            document.getElementById('app').innerHTML = html;
        })
        .catch(error => console.error('Error:', error));
}

// Example usage
document.addEventListener('DOMContentLoaded', function () {
    // Initial page load
    loadPage('/home/');

    // Example: Handle navigation click
    document.getElementById('nav-home').addEventListener('click', function (event) {
        event.preventDefault();
        loadPage('/home/');
    });

    document.getElementById('nav-about').addEventListener('click', function (event) {
        event.preventDefault();
        loadPage('/about/');
    });
});
