// Inicializar el mapa
var map = L.map('map').setView([40.416775, -3.703790], 3); // Coordenadas iniciales (España)
    
// Añadir capa de OpenStreetMap
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 100,
    attribution: '© OpenStreetMap contributors'
}).addTo(map);

window.addEventListener('resize', function() {
    map.invalidateSize();  // Asegura que el mapa se redimensione
});

// Obtener datos GeoJSON de Django
fetch(geojsonUrl)
.then(response => response.json())
.then(data => {
    L.geoJSON(data, {
        onEachFeature: function(feature, layer) {
            // Popup con información del sitio
            layer.bindPopup(
                `<strong>${feature.properties.name}</strong><br>${feature.properties.description}`
            );
            
            // Mostrar el popup cuando el ratón pase por encima (mouseover)
            layer.on('mouseover', function() {
                layer.openPopup(); // Abrir el popup al pasar el ratón
            });

            // Cerrar el popup cuando el ratón salga (mouseout)
            layer.on('mouseout', function() {
                layer.closePopup(); // Cerrar el popup al salir el ratón
            });
        },
        pointToLayer: function(feature, latlng) {
            // Crear el marcador como un círculo
            var marcador = L.circleMarker(latlng, {
                radius: 4,
                fillColor: "#C71585", // Color de los puntos
                color: "#fff",
                weight: 2,
                opacity: 1,
                fillOpacity: 0.8
            });

            // Evento de clic para redirigir a la página de detalles
            marcador.on('click', function() {
                console.log(feature.properties.pk)
                window.location.href = feature.properties.pk; // Redirigir al usuario
            });

            return marcador;
        }
    }).addTo(map);
});