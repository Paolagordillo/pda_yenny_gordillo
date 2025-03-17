import numpy as np
import pandas as pd
from numpy.random import randn
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde
import os

class Matrices():
    def __init__(self):
       np.random.seed(101)
    
    #Introducción y cálculos con los arrays de NumPy:
        
    def NumPy_1(self):
        valores = ["10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29"]
        arreglos = np.array(valores)
        print("\n \n//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")
        print("\nIntroducción y cálculos con los arrays de NumPy:")

        print("\n \n______________________________________________________________________________________________________________________________")
        print("\n1. Genera un array de NumPy con valores desde 10 hasta 29.")

        print("valores:", valores)
        print("array:",arreglos)
        
    def NumPy_2(self):
        array = np.ones((10, 10))
        suma_total = array.sum()
        print("\n \n______________________________________________________________________________________________________________________________")
        print("\n2. Calcula la suma de todos los elementos en un array de NumPy de tamaño 10x10, lleno de unos.")
        print("array de NumPy de tamaño 10x10, lleno de unos:")
        print(array)
        print("\nsuma de todos los elementos del array de NumPy :", suma_total)

    def NumPy_3(self):       
        array1 = np.random.randint(1, 11, size=5)
        array2 = np.random.randint(1, 11, size=5)
        operacion_producto = array1 * array2

        print("\n \n______________________________________________________________________________________________________________________________")
        print("\n3. Dados dos arrays de tamaño 5, llenos de números aleatorios desde 1 hasta 10, realiza un producto elemento a elemento.")

        print("\nDos arrays de tamaño 5, llenos de números aleatorios desde 1 hasta 10",)
        print("Primer array:", array1)
        print("Segundo array:", array2)
        print("Operacion producto elemento a elemento:", operacion_producto)

    def NumPy_5(self):       
        array = np.random.randint(1, 101, size=100) # Crear un array de 100 elementos aleatorios entre 1 y 100

        valor_maximo = array.max()
        indice_maximo = array.argmax() # Encontrar el valor máximo y su índice

        valor_minimo = array.min()
        indice_minimo = array.argmin() # Encontrar el valor mínimo y su índice
 
        print("\n \n______________________________________________________________________________________________________________________________")
        print("\n5. Encuentra los valores máximo y mínimo en un array de 100 elementos aleatorios y muestra sus índices.")
        print("Array generado:")
        print(array)
        print(f"\nValor máximo: {valor_maximo} en el índice {indice_maximo}")
        print(f"Valor mínimo: {valor_minimo} en el índice {indice_minimo}")

#Broadcasting e indexado de Arrays:

    def Broadcasting_6(self):  
        # array de tamaño 3x1
        array_3x1 = np.array([[1], [2], [3]])
        # array de tamaño 1x3
        array_1x3 = np.array([[4, 5, 6]])
        # Sumar los arrays 
        resultado_broadcasting = array_3x1 + array_1x3

        print("\n \n//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")
        print("\nBroadcasting e indexado de Arrays:")    

        print("\n \n______________________________________________________________________________________________________________________________")
        print("\n6.Crea un array de tamaño 3x1 y uno de 1x3, y súmalos utilizando broadcasting para obtener un array de 3x3.")
        print("Array 3x1:")
        print(array_3x1)
        print("\nArray 1x3:")
        print(array_1x3)
        print("\nResultado broadcasting de la suma (3x3):")
        print(resultado_broadcasting)

    def Broadcasting_7(self): 
        matriz = np.random.randint(1, 101, size=(5, 5)) # matriz 5x5 con valores secuenciales
        submatriz = matriz[1:3, 1:3] # submatriz 2x2 comenzando en la segunda fila y segunda columna

        print("\n \n______________________________________________________________________________________________________________________________")
        print("\n7. De una matriz 5x5, extrae una submatriz 2x2 que comience en la segunda fila y columna")
        print("Matriz (5x5):")
        print(matriz)
        print("\nSubmatriz extraída (2x2):")
        print(submatriz)

    def Broadcasting_9(self): 
                #9. Dada una matriz de 3x3, invierte el orden de sus filas.
        matriz_punto_9 = np.random.randint(1, 101, size=(3, 3)) # matriz 3x3 con números aleatorios
        matriz_invertida = matriz_punto_9[::-1]# Invierte el orden de las filas

        print("\n \n______________________________________________________________________________________________________________________________")
        print("\n9. Dada una matriz de 3x3, invierte el orden de sus filas.")
        print("Matriz original de (3x3):")
        print(matriz_punto_9)
        print("\nMatriz con filas invertidas:")
        print(matriz_invertida)

    def Broadcasting_10(self): 
        #10. Dado un array de números aleatorios de tamaño 10, selecciona y muestra solo aquellos que sean mayores a 0.5.
        array_punto_10 = np.random.rand(10) # array de 10 números aleatorios entre 0 y 1
        mayores_a_05 = array_punto_10[array_punto_10 > 0.5] # Seleccionar solo los elementos mayores a 0.5

        print("\n \n______________________________________________________________________________________________________________________________")
        print("\n10. Dado un array de números aleatorios de tamaño 10, selecciona y muestra solo aquellos que sean mayores a 0.5.")
        print("Array original:")
        print(array_punto_10)
        print("\nElementos mayores a 0.5:")
        print(mayores_a_05)

# Gráficos de dispersión, densidad y contorno:

    def Graficos_11(self):  
        #11.Genera dos arrays de tamaño 100 con números aleatorios y crea un gráfico de dispersión.
        #Gráficos de dispersión, densidad y contorno:
        x = np.random.rand(100)
        y = np.random.rand(100)

        print("\n \n//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")
        print("\nGráficos de dispersión, densidad y contorno:") 

        print("\n \n______________________________________________________________________________________________________________________________")
        print("\n11. Genera dos arrays de tamaño 100 con números aleatorios y crea un gráfico de dispersión.")

        plt.figure(figsize=(6,6))
        plt.scatter(x, y, color='red', alpha=0.7, edgecolor='k')
        plt.title("Gráfico de Dispersión_punto11", fontsize=16)
        plt.show()

    def Graficos_12(self): 
        #12. Genera un gráfico de dispersión las variables 𝑥 y 𝑦 = 𝑠𝑖𝑛(𝑥)+ ruido Gaussiano. Donde x es un array con númereos entre -2𝜋 𝑦 2𝜋. Grafica también los puntos 𝑦 = 𝑠𝑖𝑛(𝑥) en el mismo plot
        x = np.linspace(-2 * np.pi, 2 * np.pi, 200)# Generar el array x con valores entre -2π y 2π
        y_sin = np.sin(x)
        ruido_gaussiano = np.random.normal(0, 0.2, size=x.shape)
        y_ruido = y_sin + ruido_gaussiano # Calcular y = sin(x) y y = sin(x) + ruido gaussiano

        print("\n \n______________________________________________________________________________________________________________________________")
        print("\n12. Genera un gráfico de dispersión las variables 𝑥 y 𝑦 = 𝑠𝑖𝑛(𝑥)+ ruido Gaussiano. Donde x es un array con númereos entre -2𝜋 𝑦 2𝜋. Grafica también los puntos 𝑦 = 𝑠𝑖𝑛(𝑥) en el mismo plot")
        plt.figure(figsize=(6, 6)) # Crear el gráfico
        plt.scatter(x, y_ruido, color='blue', alpha=0.6, label='$y = \sin(x) + \mathrm{ruido}$', edgecolor='k')# Gráfico de dispersión para y = sin(x) + ruido
        plt.plot(x, y_sin, color='red', linewidth=2, label='$y = \sin(x)$')# Línea para y = sin(x)

        plt.title("Gráfico punto 12", fontsize=16)
        plt.xlabel("X",color='blue', fontsize=12)
        plt.ylabel("Y", color='blue', fontsize=12)
        plt.show()


    #def Graficos_13(self): 
        #13.Utiliza la función np.meshgrid para crear una cuadrícula y luego aplica la función z = np.cos(x) + np.sin(y) para generar y mostrar un gráfico de contorno.

    def Graficos_14(self): 
#14. Crea un gráfico de dispersión con 1000 puntos aleatorios y utiliza la densidad de estos puntos para ajustar el color de cada punto.
        
        np.random.seed(101)
        x = np.random.randn(1000)
        y = np.random.randn(1000) # 1000 puntos aleatorios

        xy = np.vstack([x, y])
        z = gaussian_kde(xy)(xy) # Calcular la densidad de los puntos
        print("\n \n______________________________________________________________________________________________________________________________")
        print("\n14.Crea un gráfico de dispersión con 1000 puntos aleatorios y utiliza la densidad de estos puntos para ajustar el color de cada punto.")
        plt.figure(figsize=(8, 6))
        scatter = plt.scatter(x, y, c=z, cmap='viridis', s=10, edgecolors='none', alpha=0.8)# gráfico de dispersión

        cbar = plt.colorbar(scatter)
        cbar.set_label('Densidad', fontsize=12)# Añadir una barra de color

        plt.title('Gráfico 14 de dispersión con 1000 puntos aleatorios', fontsize=16)
        plt.xlabel('Eje X', fontsize=14)
        plt.ylabel('Eje Y', fontsize=14)
        plt.show()

    def Graficos_15(self): 
#15.A partir de la misma función del ejercicio 12, genera un gráfico de contorno lleno.
        x = np.linspace(-2 * np.pi, 2 * np.pi, 200)  # Valores de x entre -2π y 2π
        y = np.linspace(-2 * np.pi, 2 * np.pi, 200)  # Valores de y entre -2π y 2π
        X, Y = np.meshgrid(x, y)  # Crear malla para el contorno

        ruido_gaussiano = np.random.normal(0, 0.2, size=X.shape)
        Z = np.sin(X) + ruido_gaussiano
        y_sin = np.sin(x)

        print("\n \n______________________________________________________________________________________________________________________________")
        print("\n15. A partir de la misma función del ejercicio 12, genera un gráfico de contorno lleno.")

        plt.figure(figsize=(8, 6))
        # Gráfico de contorno lleno
        contorno = plt.contourf(X, Y, Z, levels=50, cmap="viridis", alpha=0.8)
        cbar = plt.colorbar(contorno)
        cbar.set_label(r"$Z = \sin(x) + \text{ruido}$", fontsize=12)

        # Gráfico de los puntos y = sin(x)
        plt.plot(x, y_sin, color="red", linewidth=2, label=r"$y = \sin(x)$")

        # Configuración del gráfico
        plt.title("Gráfico 15",color="blue", fontsize=16)
        plt.xlabel(r"$x$", fontsize=14)
        plt.ylabel(r"$y$", fontsize=14)
        plt.legend(fontsize=12, loc="upper right")
      
        plt.show()        

    def Graficos_16(self): 
#16- Añade etiquetas para el eje X (‘Eje X’), eje Y (‘Eje Y’) y un título (‘Gráfico de Dispersión’) a tu gráfico de dispersión del ejercicio 12 y crea leyendas para cada gráfico usando código LaTex
        x = np.linspace(-2 * np.pi, 2 * np.pi, 200)# Generar el array x con valores entre -2π y 2π
        y_sin = np.sin(x)
        ruido_gaussiano = np.random.normal(0, 0.2, size=x.shape)
        y_ruido = y_sin + ruido_gaussiano # Calcular y = sin(x) y y = sin(x) + ruido gaussiano
                
        print("\n \n______________________________________________________________________________________________________________________________")
        print("\n16. A partir de la misma función del ejercicio 12, genera un gráfico de contorno lleno.")
        plt.figure(figsize=(6, 6)) # Crear el gráfico
        plt.scatter(x, y_ruido, color='blue', alpha=0.6, label='$y = \sin(x) + \mathrm{ruido}$', edgecolor='k')# Gráfico de dispersión para y = sin(x) + ruido
        plt.plot(x, y_sin, color='red', linewidth=2, label='$y = \sin(x)$')# Línea para y = sin(x)

        plt.title("Gráfico de Dispersión punto 16", fontsize=16)
        plt.xlabel("Eje X",color='blue', fontsize=12)
        plt.ylabel("Eje Y", color='blue', fontsize=12)
        plt.show()

#Histogramas:

    def Histogramas_16(self): 
#16-Crea un histograma a partir de un array de 1000 números aleatorios generados con una distribución normal
        data = np.random.normal(loc=0, scale=1, size=1000)  # media=0, desviación estándar=1
        # Crear el histograma
        plt.figure(figsize=(8, 6))
        plt.hist(data, bins=50, color="skyblue", edgecolor="black", alpha=0.7, density=True)

        print("\n \n______________________________________________________________________________________________________________________________")
        print("\n16.Crea un histograma a partir de un array de 1000 números aleatorios generados con una distribución normal")  
        plt.title("Histograma Punto 16", fontsize=16)
        plt.axvline(0, color="black", linestyle="--", linewidth=0.8, label="Media")
        plt.show()

    def Histogramas_17(self): 
#17-Genera dos sets de datos con distribuciones normales diferentes y muéstralos en el mismo histograma

        data1 = np.random.normal(loc=2,scale=1, size=1000)  # Media=0, Desviación estándar=1
        data2 = np.random.normal(loc=3, scale=1.5, size=1000)  # Media=3, Desviación estándar=1.5
        data3 = np.random.normal(loc=5, scale=2, size=1000)  # Media=3, Desviación estándar=1.5

        print("\n \n______________________________________________________________________________________________________________________________")
        print("\n17.Genera dos sets de datos con distribuciones normales diferentes y muéstralos en el mismo histograma")
        print("\n18.Experimenta con diferentes valores de bins (por ejemplo, 10, 30, 50) en un histograma y observa cómo cambia la representación.")
        print("\n19. Añade una línea vertical que indique la media de los datos en el histograma.")
        print("\n20. Crea histogramas superpuestos para los dos sets de datos del ejercicio 17, usando colores y transparencias diferentes para distinguirlos.")
        plt.figure(figsize=(8, 6))
        plt.hist(data1, bins=10,alpha=0.6, color="skyblue", edgecolor="black", label="Distribución 1 (media=2, σ=1)", density=True)
        plt.hist(data2, bins=30, alpha=0.6, color="lightcoral", edgecolor="black", label="Distribución 2 (media=3, σ=1.5)", density=True)
        plt.hist(data3, bins=50, alpha=0.6, color="green",edgecolor="black", label="Distribución 9 (media=5, σ=2)", density=True)

        plt.title("Histograma punto 17, 18, 19 y 20 Distribuciones Normales", fontsize=16)
        plt.xlabel("Valores", fontsize=12)
        plt.ylabel("Densidad", fontsize=12)
        plt.axvline(2, color="blue", linestyle="--", linewidth=1, label="Media Dist 1")
        plt.axvline(3, color="red", linestyle="--", linewidth=1, label="Media Dist 2")
        plt.axvline(5, color="green", linestyle="--", linewidth=1, label="Media Dist 2")
        plt.show()


clase_2 = Matrices()
clase_2.NumPy_1()
clase_2.NumPy_2()
clase_2.NumPy_3()
clase_2.NumPy_5()
clase_2.Broadcasting_6()
clase_2.Broadcasting_7()
clase_2.Broadcasting_9()
clase_2.Broadcasting_10()
clase_2.Graficos_11()
clase_2.Graficos_12()
clase_2.Graficos_14()
clase_2.Graficos_15()
clase_2.Graficos_16()
clase_2.Histogramas_16()
clase_2.Histogramas_17()