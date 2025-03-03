import json
import requests


class Ingestiones:
    def __init__(self):
        self.ruta_static = "src/pad/static/"

    def leer_api(self, url):
        response = requests.get(url)
        return response.json()

    def escribir_json(self, ruta, data):
        # Escribir datos JSON en un archivo
        with open(ruta, 'w') as f:
            json.dump(data, f, indent=4)


# Crear una instancia de la clase
ingestion = Ingestiones()

# Leer datos de la API
datos_json = ingestion.leer_api("https://api.thecatapi.com/v1/images/search?limit=10")

# Opción 1: Guardar en una ruta personalizada
ruta_personalizada = "src/pad/static/json/actividad_1.json"
ingestion.escribir_json(ruta_personalizada, datos_json)
print(f"Datos guardados en: {ruta_personalizada}")


