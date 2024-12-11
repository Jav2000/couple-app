async function handleSubmit(event) {
    event.preventDefault(); // Evita el envío por defecto del formulario

    const form = document.getElementById('dataForm'); // ID del formulario
    const formData = new FormData(form); // Recoge los datos del formulario

    console.log(formData)
    
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
          showPopup(true, '¡Sitio guardado correctamente!'); // Muestra éxito
          setTimeout(() => {
              window.location.href = '/sites/';
          }, 20000); // Espera 2 segundos antes de redirigir
      } else {
          const errorData = await response.json();
          console.error('Error del servidor:', errorData);
          showPopup(false, 'Hubo un error al guardar el sitio. Revisa los datos.');
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

// Función para cerrar el pop-up
function closePopup() {
    const popup = document.getElementById('popup');
    popup.style.display = 'none';
    window.location.href = '/sites';
}

const nameInput = document.querySelector("input[name='name']");
const suggestionsList = document.getElementById("autocompleteSuggestions");

nameInput.addEventListener("input", () => {
    const query = nameInput.value;

    if (query.length > 2) { // Evitar demasiadas consultas para cadenas cortas
        fetchSuggestions(query);
    } else {
        suggestionsList.innerHTML = "";
        suggestionsList.style.display= 'none';
    }
});

function fetchSuggestions(query) {
    // Configurar la solicitud para la API Places de Google
    const service = new google.maps.places.AutocompleteService();

    service.getPlacePredictions(
        { input: query },
        (predictions, status) => {
            if (status === google.maps.places.PlacesServiceStatus.OK && predictions) {
                displaySuggestions(predictions);
            } else {
                suggestionsList.innerHTML = "";
                suggestionsList.style.display= 'none';
            }
        }
    );
}

function displaySuggestions(predictions) {
    suggestionsList.innerHTML = ""; // Limpiar las sugerencias anteriores

    predictions.forEach((prediction) => {
        const suggestionItem = document.createElement("li");
        suggestionItem.textContent = prediction.description;
        suggestionItem.classList.add("suggestion-item");

        suggestionItem.addEventListener("click", () => {
            nameInput.value = prediction.description; // Actualizar el campo con la selección
            suggestionsList.innerHTML = ""; // Limpiar las sugerencias
            fetchPlaceDetails(prediction.place_id); // Obtener coordenadas del lugar seleccionado
        });

        suggestionsList.appendChild(suggestionItem);
    });
    suggestionsList.style.display= 'block';
}

function fetchPlaceDetails(placeId) {
    const service = new google.maps.places.PlacesService(document.createElement("div"));

    service.getDetails({ placeId }, (place, status) => {
        if (status === google.maps.places.PlacesServiceStatus.OK && place.geometry) {
            // Rellenar los campos de latitud y longitud
            document.querySelector("input[name='latitude']").value = place.geometry.location.lat();
            document.querySelector("input[name='longitude']").value = place.geometry.location.lng();
        }
    });
}