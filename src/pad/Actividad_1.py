import json
import requests


class Actividad_1():
    def __init__(self):
        self.ruta_json ="src/pad/static/"



    def leer_api(self,url):
        response= requests.get(url)
        return response.json()
    
    def escribir_json(self, ruta, data):
        # Escribir datos JSON en un archivo
        with open(ruta, 'w') as f:
            json.dump(data, f, indent=4)
    
    #def escribir_json(self, ruta, data):
     #   with open(ruta,'w') as f
      #  json.dump(data,f)
        
    #def escribir_json(self,ruta,data ="datos.json"):
        #with open(self.ruta_static,'w') as f:
        #json.dump(data,f)
        

# vamoa a crear una instancia de la clase Actividad_1
Ingestion = Actividad_1()
datos_json = Ingestion.leer_api("https://api.thecatapi.com/v1/images/search?limit=10")

# Opción 1: Guardar en una ruta personalizada
ruta_personalizada = "src/pad/static/json/actividad_1ok.json"
Ingestion.escribir_json(ruta_personalizada, datos_json)
print(f"Datos guardados en: {ruta_personalizada}")

#ruta_archivo = Ingestion.ruta_json + "datos.json"  # Combinar ruta estática con el nombre del archivo
#Ingestion.escribir_json(ruta_archivo, datos_json)
#print(f"Datos guardados en: {ruta_archivo}")

#print("esta es la ruta estatica:",Ingestion.ruta_static)
#print("datos json:",datos_json)

#Ingestion.escribir_json(nombre="archivo_json",datos=datos_json)