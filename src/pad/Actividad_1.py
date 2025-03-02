import json
import requests


class Ingestiones():
    def __init__(self):
        self.ruta_static="src/pad/static/"

    def leer_api(self,url):
        response= requests.get(url)
        return response.json()
    
    #def escribir_json(self, ruta, data):
     #   with open(ruta,'w') as f
      #  json.dump(data,f)
        
    #def escribir_json(self,ruta,/workspaces/pda_yenny_gordillo/src/pad/static/json):
     #   with open(ruta,'w') as f
      #  json.dump(data,f)

        

# vamoa a crear una instancia de la clase

Ingestion = Ingestiones()
datos_json = Ingestion.leer_api("https://api.thecatapi.com/v1/images/search?limit=10")
#print("esta es la ruta estatica:",Ingestion.ruta_static)
print("datos json:",datos_json)

#Ingestion.escribir_json(nombre="archivo_json",datos=datos_json)