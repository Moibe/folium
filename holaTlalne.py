import folium

# Definimos la latitud y longitud del centro del mapa
centro = (19.44, -99.13)

# Creamos un objeto de tipo Map con el centro y el zoom inicial
mapa = folium.Map(location=centro, zoom_start=4)

# Agregamos un marcador al mapa
marcador = folium.Marker(location=centro, popup="¡Hola desde Tlalnepantla!")
mapa.add_element(marcador)

# Guardamos el mapa como un archivo HTML
mapa.save("mapa_basico.html")
