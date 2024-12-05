let images = [];
let currentIndex = 0;

function openModal(imageUrl, index) {
    const modal = document.getElementById('photo-modal');
    const modalImage = document.getElementById('modal-image');

    images = Array.from(document.querySelectorAll('.photo-card img')).map(img => img.src);
    currentIndex = index;

    modal.style.display = 'flex';
    modalImage.src = imageUrl;
}

function closeModal() {
    const modal = document.getElementById('photo-modal');
    modal.style.display = 'none'; // Ocultar el modal
}

function navigateModal(direction) {
    const modalImage = document.getElementById('modal-image');
    
    currentIndex += direction;
    if (currentIndex < 0) {
        currentIndex = images.length - 1; 
    } else if (currentIndex >= images.length) {
        currentIndex = 0; 
    }
    modalImage.src = images[currentIndex];
}

document.querySelectorAll('.photo-card img').forEach((img, index) => {
    img.addEventListener('click', () => openModal(img.src, index));
});