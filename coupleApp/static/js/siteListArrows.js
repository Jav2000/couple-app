const container = document.querySelector('.sites-container');

document.getElementById('left').addEventListener('click', function() {
    container.scrollLeft -= 290; // Ajusta el valor según el desplazamiento deseado
});

document.getElementById('right').addEventListener('click', function() {
    container.scrollLeft += 290; // Ajusta el valor según el desplazamiento deseado
});