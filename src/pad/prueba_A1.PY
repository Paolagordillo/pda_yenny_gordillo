import os
import requests
import json



class Actividad_1:
    def __init__(self):
        self.ruta_json = "src/pad/static/json"

    def leer_api(self, url):
        response = requests.get(url)
        return response.json()

    def escribir_json(self, ruta, data):
        # Escribir datos JSON en un archivo
        with open(ruta, 'w') as f:
            json.dump(data, f, indent=4)

# Crear una instancia de la clase
ingestion = Actividad_1()

# Leer datos de la API
datos_json = ingestion.leer_api("https://api.thecatapi.com/v1/images/search?limit=10")

# Mostrar los datos obtenidos
print("Datos JSON:", datos_json)

# Guardar los datos en un archivo JSON
ruta_archivo = ingestion.ruta_json + "datos.json"  # Combinar ruta estática con el nombre del archivo
ingestion.escribir_json(ruta_archivo, datos_json)
print(f"Datos guardados en: {ruta_archivo}")
