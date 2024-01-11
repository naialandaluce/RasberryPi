#Paso 1 y 2: Instalar las Bibliotecas Necesarias
import gpxpy
import matplotlib.pyplot as plt
import folium
import math

#Paso 3: Parsear los Archivos GPX
# Función para parsear un archivo GPX y extraer las coordenadas
def parse_gpx(file_path):
    with open(file_path, 'r') as gpx_file:
        gpx = gpxpy.parse(gpx_file)
    coords = []
    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                coords.append((point.latitude, point.longitude))
    return coords

# Parsea los dos archivos GPX
coords_1 = parse_gpx('activity_1.gpx')
coords_2 = parse_gpx('activity_2.gpx')
coords_3 = parse_gpx('activity_3.gpx')
coords_4 = parse_gpx('activity_4.gpx')
coords_5 = parse_gpx('activity_5.gpx')
coords_6 = parse_gpx('activity_6.gpx')
coords_7 = parse_gpx('activity_7.gpx')
coords_8 = parse_gpx('activity_8.gpx')


mapa = folium.Map(location=coords_1[0], zoom_start=14)

#Calcular la Distancia de los Recorridos
def calculate_distance(coords):
    total_distance = 0
    for i in range(len(coords) - 1):
        lat1, lon1 = coords[i]
        lat2, lon2 = coords[i + 1]
        radius = 6371  # Radio de la Tierra en kilómetros

        dlat = math.radians(lat2 - lat1)
        dlon = math.radians(lon2 - lon1)
        a = (math.sin(dlat / 2) * math.sin(dlat / 2) +
             math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) *
             math.sin(dlon / 2) * math.sin(dlon / 2))
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        distance = radius * c
        total_distance += distance
    return total_distance

# Calcular la distancia para cada ruta
distance_1 = calculate_distance(coords_1)
distance_2 = calculate_distance(coords_2)
distance_3 = calculate_distance(coords_3)
distance_4 = calculate_distance(coords_4)
distance_5 = calculate_distance(coords_5)
distance_6 = calculate_distance(coords_6)
distance_7 = calculate_distance(coords_7)
distance_8 = calculate_distance(coords_8)


# Añadir la primera ruta con distancia al mapa
route_1 = folium.PolyLine(coords_1, color="red", weight=2.5, opacity=1)
route_1.add_to(mapa)
route_1.add_child(folium.Popup(f'Distancia Recorrido 1: {distance_1:.2f} km'))

# Añadir la segunda ruta con distancia al mapa
route_2 = folium.PolyLine(coords_2, color="blue", weight=2.5, opacity=1)
route_2.add_to(mapa)
route_2.add_child(folium.Popup(f'Distancia Recorrido 2: {distance_2:.2f} km'))

# Añadir la tercera ruta con distancia al mapa
route_3 = folium.PolyLine(coords_3, color="green", weight=2.5, opacity=1)
route_3.add_to(mapa)
route_3.add_child(folium.Popup(f'Distancia Recorrido 3: {distance_3:.2f} km'))
# Añadir la cuarta ruta con distancia al mapa
route_4 = folium.PolyLine(coords_4, color="yellow", weight=2.5, opacity=1)
route_4.add_to(mapa)
route_4.add_child(folium.Popup(f'Distancia Recorrido 1: {distance_4:.2f} km'))

# Añadir la quinta ruta con distancia al mapa
route_5 = folium.PolyLine(coords_5, color="purple", weight=2.5, opacity=1)
route_5.add_to(mapa)
route_5.add_child(folium.Popup(f'Distancia Recorrido 2: {distance_5:.2f} km'))

# Añadir la sexta ruta con distancia al mapa
route_6 = folium.PolyLine(coords_6, color="pink", weight=2.5, opacity=1)
route_6.add_to(mapa)
route_6.add_child(folium.Popup(f'Distancia Recorrido 3: {distance_6:.2f} km'))
# Añadir la septima ruta con distancia al mapa
route_7 = folium.PolyLine(coords_7, color="orange", weight=2.5, opacity=1)
route_7.add_to(mapa)
route_7.add_child(folium.Popup(f'Distancia Recorrido 1: {distance_7:.2f} km'))

# Añadir la octava ruta con distancia al mapa
route_8 = folium.PolyLine(coords_8, color="grey", weight=2.5, opacity=1)
route_8.add_to(mapa)
route_8.add_child(folium.Popup(f'Distancia Recorrido 1: {distance_8:.2f} km'))


# Guardar el mapa en un archivo HTML
mapa.save('mis_rutas.html')