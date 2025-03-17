import numpy as np
import pandas as pd
from numpy.random import randn

class Matrices():
    def __init__(self):
       np.random.seed(101)
    
        
    def serie(self):
        etiquetas = ["a","b","c"]
        valores = ["10","20","30"]
        arreglos = np.array(valores)
        directorios = {"amiiboSeries": "Mario sports superstars", "character": "metal mario"}
        mi_serie = pd.Series(data=valores, index=etiquetas)
        print(etiquetas)
        print(valores)
        print(arreglos)
        print(directorios)
        print(mi_serie)

     

    def matrices(self,filas=0, columnas=0):
        data = pd.DataFrame() # vacio
        data = pd.DataFrame(randn(6,4), index="A B C D E F".split(" "),columns="w x y z".split(" "))

        print("Matriz generada:")
        print(data)



clase_2 = Matrices()
clase_2.matrices()
clase_2.serie()
