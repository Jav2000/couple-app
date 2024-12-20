// Menú móvil desplegable
document.querySelector('.menu-toggle').addEventListener('click', function () {
    const categories = document.querySelector('.makeup-mobile-menu .categories');
    categories.style.display = categories.style.display === 'block' ? 'none' : 'block';
});

document.querySelectorAll('.makeup-mobile-menu .category span').forEach(category => {
    category.addEventListener('click', function () {
        const subcategories = this.nextElementSibling;
        subcategories.style.display = subcategories.style.display === 'block' ? 'none' : 'block';
    });
});