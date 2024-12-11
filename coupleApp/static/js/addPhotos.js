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

        // Crear la solicitud AJAX
        const xhr = new XMLHttpRequest();
        xhr.open('POST', form.action, true);
        xhr.setRequestHeader('X-CSRFToken', csrfToken);

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

        // Enviar datos
        const formData = new FormData();
        formData.append('image', file);
        xhr.send(formData);
    });
});