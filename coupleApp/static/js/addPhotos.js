document.getElementById('uploadButton').addEventListener('click', (event) => {
    event.preventDefault(); // Prevenir recarga de página

    const form = document.getElementById('dataForm');
    const files = document.getElementById('images').files;
    
    const csrfToken = document.querySelector('input[name=csrfmiddlewaretoken]').value;

    const uploadContainer = document.getElementById('uploadProgressContainer');
    uploadContainer.innerHTML = ''; // Limpiar contenedor

    if (!files.length) {
        alert('Por favor, selecciona al menos un archivo.');
        return;
    }

    // Crear la solicitud AJAX
    const xhr = new XMLHttpRequest();
    xhr.open('POST', form.action, true);
    xhr.setRequestHeader('X-CSRFToken', csrfToken);
    
    Array.from(files).forEach((file, index) => {
        // Crear elementos para el progreso
        const progressWrapper = document.createElement('div');
        progressWrapper.className = 'progress-container';

        const fileInfo = document.createElement('div');
        fileInfo.className = 'file-info';
        fileInfo.innerText = file.name;

        const progressBar = document.createElement('div');
        progressBar.className = 'progress-bar';
        const progressSpan = document.createElement('span');
        progressBar.appendChild(progressSpan);

        progressWrapper.appendChild(fileInfo);
        progressWrapper.appendChild(progressBar);
        uploadContainer.appendChild(progressWrapper);

        xhr.upload.addEventListener('progress', (e) => {
            if (e.lengthComputable) {
                const percentComplete = (e.loaded / e.total) * 100;
                progressSpan.style.width = percentComplete + '%';
            }
        });

        xhr.onload = () => {
            progressSpan.style.width = '100%';
            if (xhr.status === 200) {
                const successIcon = document.createElement('span');
                successIcon.textContent = '✔';
                successIcon.className = 'success-icon';
                progressWrapper.appendChild(successIcon);
            } else {
                const errorIcon = document.createElement('span');
                errorIcon.textContent = '✖';
                errorIcon.className = 'error-icon';
                progressWrapper.appendChild(errorIcon);
            }
        };

        // Manejar errores
        xhr.onerror = () => {
            progressSpan.style.width = '100%';
            progressSpan.style.backgroundColor = 'red';
            const errorIcon = document.createElement('span');
            errorIcon.textContent = '✖';
            errorIcon.className = 'error-icon';
            progressWrapper.appendChild(errorIcon);
        };

        uploadContainer.style.display = 'block'
    });

    // Enviar datos
    const formData = new FormData(form);
    formData.append('images', files);
    xhr.send(formData);
});

// async function handleSubmit(event) {
//     event.preventDefault(); // Evita el envío por defecto del formulario

//     const form = document.getElementById('dataForm'); // ID del formulario
//     const formData = new FormData(form); // Recoge los datos del formulario

//     const url = window.location.pathname;
//     const pk = url.split('/')[2];

//     try {
//       // Enviar datos al servidor mediante fetch
//       const response = await fetch(form.action, {
//           method: 'POST',
//           body: formData,
//           headers: {
//               'X-Requested-With': 'XMLHttpRequest', // Indica que es una solicitud AJAX
//           },
//       });
//       // Comprobamos si la respuesta es correcta
//       if (response.ok) {
//           const result = await response.json(); // Asumimos una respuesta en JSON
//           showPopup(true, '¡Foto guardada correctamente!'); // Muestra éxito
//           setTimeout(() => {
//               window.location.href = '/sites/' + pk;
//           }, 20000); // Espera 2 segundos antes de redirigir
//       } else {
//           const errorData = await response.json();
//           console.error('Error del servidor:', errorData);
//           showPopup(false, 'Hubo un error al guardar el sitio. Revisa los datos.');
//       }
//     }catch(error){
//         console.error('Error de conexión:', error);
//         showPopup(false, 'No se pudo conectar con el servidor. Inténtalo más tarde.');
//     }
// }
// // Función para mostrar el popup
// function showPopup(success, message) {
//     const popup = document.getElementById('popup');
//     const popupMessage = document.getElementById('popupMessage');

//     popupMessage.innerText = message;
//     if(success){
//         popup.classList.add('success');
//         popup.classList.remove('error');
//     }else{
//         popup.classList.add('error');
//         popup.classList.remove('success');
//     }

//     popup.style.display = 'block'; // Muestra el pop-up
// }

// // Función para cerrar el pop-up
// function closePopup() {
//     const url = window.location.pathname;
//     const pk = url.split('/')[2];

//     const popup = document.getElementById('popup');
//     popup.style.display = 'none';
//     window.location.href = '/sites/' + pk;
// }