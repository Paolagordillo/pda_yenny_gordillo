import os
import requests
import json

# 📌 URL de la API (reemplázala con la que necesites)
API_URL = "https://jsonplaceholder.typicode.com/posts"

# 📁 Carpeta donde se guardará la respuesta
OUTPUT_FOLDER = "datos_api"
OUTPUT_FILE = "respuesta.json"

def obtener_datos_api(url):
    """Hace una petición GET a la API y devuelve los datos en JSON."""
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/posts")
        response.raise_for_status()  # Lanza un error si hay un problema con la solicitud
        return response.json()  # Retorna la respuesta en formato JSON
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener los datos: {e}")
        return None

def guardar_datos(datos, carpeta, archivo):
    """Guarda los datos en un archivo dentro de una carpeta."""
    if datos:
        os.makedirs(carpeta, exist_ok=True)  # Crea la carpeta si no existe
        ruta_completa = os.path.join(carpeta, archivo)

        with open(ruta_completa, "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)

        print(f"Datos guardados en: {ruta_completa}")
    else:
        print("No hay datos para guardar.")

if __name__ == "__main__":
    datos = obtener_datos_api(API_URL)  # Obtener datos de la API
    guardar_datos(datos, OUTPUT_FOLDER, OUTPUT_FILE)  # Guardar los datos
