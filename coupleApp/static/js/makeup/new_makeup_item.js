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
              window.location.href = '/makeup';
          }, 20000); // Espera 2 segundos antes de redirigir
      } else {
          const errorData = await response.json();
          console.error('Error del servidor:', errorData);
          showPopup(false, 'Hubo un error al guardar el producto de maquillaje. Revisa los datos.');
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
    window.location.href = '/makeup';
}

function updateSubcategories() {
    const subcategories = {
        Rostro: [
            { value: "bases_maquillaje", label: "Bases de maquillaje" },
            { value: "colorete", label: "Colorete" },
            { value: "bronceadores", label: "Bronceadores y contouring" },
            { value: "correctores", label: "Correctores" },
            { value: "iluminadores", label: "Iluminadores" },
            { value: "fijadores", label: "Fijadores" },
            { value: "polvos", label: "Polvos" },
            { value: "prebases_rostro", label: "Prebases" },
        ],
        Ojos: [
            { value: "mascaras", label: "Máscaras" },
            { value: "sombras", label: "Sombras de ojos" },
            { value: "lapices", label: "Lápices de ojos" },
            { value: "cejas", label: "Cejas" },
            { value: "delineadores", label: "Delineadores" },
            { value: "prebases_ojos", label: "Prebases para ojos" },
        ],
        Labios: [
            { value: "labiales", label: "Labiales" },
            { value: "brillos_labios", label: "Brillos de labios" },
            { value: "lapices_contorno", label: "Lápices contorno" },
            { value: "prebases_labios", label: "Prebases para labios" },
        ],
        Manos: [
            { value: "esmaltes", label: "Esmaltes" },
            { value: "cuidado_unas", label: "Cuidado de las uñas" },
            { value: "manicura_francesa", label: "Manicura francesa" },
            { value: "quitaesmaltes", label: "Quitaesmaltes" },
            { value: "fijadores_esmalte", label: "Fijadores de esmalte de uñas" },
        ],
        Paletas: [
            { value: "paletas_rostro", label: "Paletas para rostro" },
            { value: "paletas_ojos", label: "Paletas para ojos" },
        ],
    };

    const categoryField = document.querySelector('select[name="category"]');
    const subcategoryField = document.querySelector('select[name="subcategory"]');
    const selectedCategory = categoryField.value;

    subcategoryField.innerHTML = '';

    if (subcategories[selectedCategory]) {
        subcategories[selectedCategory].forEach(sub => {
            const option = document.createElement('option');
            option.value = sub.value;
            option.textContent = sub.label;
            subcategoryField.appendChild(option);
        });
    }
}