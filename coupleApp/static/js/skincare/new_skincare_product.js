async function handleSubmit(event) {
    event.preventDefault(); // Evita el envío por defecto del formulario

    const form = document.getElementById('dataForm'); // ID del formulario
    const formData = new FormData(form); // Recoge los datos del formulario

    try {
      // Enviar datos al servidor mediante fetch
      const response = await fetch(form.action, {
          method: 'POST',
          body: formData,
          headers: {
              'X-Requested-With': 'XMLHttpRequest', // Indica que es una solicitud AJAX
          },
      });
      // Comprobamos si la respuesta es correcta
      if (response.ok) {
          const result = await response.json(); // Asumimos una respuesta en JSON
          showPopup(true, '¡Producto guardado correctamente!'); // Muestra éxito
          setTimeout(() => {
              window.location.href = '/skincare';
          }, 20000); // Espera 2 segundos antes de redirigir
      } else {
          const errorData = await response.json();
          console.error('Error del servidor:', errorData);
          showPopup(false, 'Hubo un error al guardar el producto de skincare. Revisa los datos.');
      }
    }catch(error){
        console.error('Error de conexión:', error);
        showPopup(false, 'No se pudo conectar con el servidor. Inténtalo más tarde.');
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

function closePopup() {
    const popup = document.getElementById('popup');
    popup.style.display = 'none';
    window.location.href = '/skincare';
}