# Couple-App v1.0

Couple-App es una aplicación diseñada para capturar y gestionar los recuerdos de los viajes de pareja. Con esta herramienta, podrás visualizar, organizar y personalizar toda la información sobre los lugares que has visitado, incluyendo fotografías. A continuación, se describen las funcionalidades disponibles en esta primera versión.

---

## 🚀 Funcionalidades

### 1. Lista de los sitios a los que hemos viajado
- Visualiza una lista completa de los destinos visitados.
- Cada sitio muestra información clave como:
  - Nombre del lugar.
  - Descripción.
  - Fechas de inicio y fin del viaje.

### 2. Mapa con puntos en los sitios que hemos estado
- Un mapa interactivo que marca con pines todos los lugares visitados.
- Haciendo clic en un punto, puedes acceder a los detalles del sitio correspondiente.

### 3. Añadir un nuevo sitio
- Agrega información sobre nuevos destinos:
  - Nombre.
  - Descripción.
  - Ubicación (coordenadas de latitud y longitud).
  - Fechas del viaje.
- Validación para asegurarse de que las fechas de inicio y fin sean coherentes.

### 4. Editar sitio
- Actualiza los detalles de un lugar ya registrado:
  - Modifica información como nombre, descripción, fechas, o ubicación.

### 5. Eliminar sitio
- Borra un destino de la lista.
- Se elimina también toda la información asociada, incluidas las fotos del lugar.

### 6. Visualizar las fotos de cada sitio
- Explora una galería de imágenes para cada destino.
- Al hacer clic en una foto:
  - Se abre un modal con la imagen en tamaño grande.
  - Se pueden navegar las fotos del sitio en la misma ventana.

### 7. Añadir fotos a sitios
- Sube imágenes directamente desde tu dispositivo para cualquier destino.
- Organización automática en carpetas según fecha y lugar.

### 8. Eliminar foto
- Elimina imágenes no deseadas desde la galería de un sitio.
- El archivo correspondiente también se elimina físicamente del servidor.

### 9. Descargar foto en el dispositivo
- Descarga tus fotos favoritas directamente desde la galería.
- Botón de descarga accesible desde el modal al visualizar una imagen.

---

## 💻 Tecnologías Usadas

- **Frontend**: HTML, CSS, JavaScript (con integración de Font Awesome para íconos).
- **Backend**: Django (framework principal).
- **Base de Datos**: SQLite (para el almacenamiento de información).
- **Media**: Gestión de fotos mediante la carpeta `media/`.

---

## 🌟 Próximos Pasos

- Implementación de filtros y categorías para organizar sitios.
- Función de compartir fotos y sitios a través de enlaces.
- Versión móvil para facilitar el acceso desde cualquier dispositivo.

---

Couple-App es el compañero perfecto para preservar los recuerdos de tus viajes. ¡Explora, gestiona y revive cada aventura con facilidad!