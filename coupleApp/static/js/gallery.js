let images = [];
let currentIndex = 0;

function openModal(imageUrl, index, photoId) {
    const modal = document.getElementById('photo-modal');
    const modalImage = document.getElementById('modal-image');

    images = Array.from(document.querySelectorAll('.photo-card img')).map(img => img.src);
    currentIndex = index;

    modal.style.display = 'flex';
    modalImage.src = imageUrl;

    modalImage.setAttribute('data-id', photoId);
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

function downloadImage() {
    const modalImage = document.getElementById('modal-image');
    const link = document.createElement('a');
    link.href = modalImage.src;
    link.download = modalImage.src.split('/').pop(); // Usamos el nombre de la imagen como nombre del archivo
    link.click();
}

function deleteImage(tripId) {
    const modalImage = document.getElementById('modal-image');
    const photoId = modalImage.getAttribute('data-id');

    if (confirm("¿Estás seguro de que deseas eliminar esta imagen?")) {
        // Enviar solicitud AJAX al servidor para eliminar la imagen
        fetch(`/trips/delete-photo/${photoId}/`, {
            method: 'DELETE',
            headers: {
                'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
            },
        })
        .then(async response => {
            if (response.ok) {
                const result = await response.json(); // Asumimos una respuesta en JSON
                showPopup(true, '¡Sitio guardado correctamente!'); // Muestra éxito
                setTimeout(() => {
                    window.location.href = `/trips/${tripId}/`;
                }, 20000); // Espera 2 segundos antes de redirigir
            } else {
                const errorData = await response.json();
                console.error('Error del servidor:', errorData);
                showPopup(false, 'Hubo un error al guardar el sitio. Revisa los datos.');
            }
        })
        .catch(error => {
            console.error('Error al eliminar la foto:', error);
            alert('Error al eliminar la foto');
        });
    }
}

function showPopup(success, message) {
    const popup = document.getElementById('popup');
    const popupMessage = document.getElementById('popupMessage');

    popupMessage.innerText = message;
    if(success){
        popup.classList.add('success');
        popup.classList.remove('error');
    }else{
        popup.classList.add('error');
        popup.classList.remove('success');
    }

    popup.style.display = 'block'; // Muestra el pop-up
}

function closePopup(tripId) {
    const popup = document.getElementById('popup');
    popup.style.display = 'none';
    window.location.href = `/trips/${tripId}/`;
}