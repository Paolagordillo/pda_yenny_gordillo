import numpy as np
import matplotlib.pyplot as plt

# Generar 1000 números aleatorios con una distribución normal
data = np.random.normal(loc=0, scale=1, size=1000)  # Media=0, Desviación estándar=1

# Calcular la media de los datos
mean = np.mean(data)

# Crear el histograma
plt.figure(figsize=(8, 6))
plt.hist(data, bins=30, color="skyblue", edgecolor="black", alpha=0.7, density=True)

# Añadir una línea vertical para la media
plt.axvline(mean, color="red", linestyle="--", linewidth=2, label=f"Media: {mean:.2f}")

# Personalizar el gráfico
plt.title("Histograma con línea de media", fontsize=16)
plt.xlabel("Valores", fontsize=14)
plt.ylabel("Densidad", fontsize=14)
plt.legend(fontsize=12)
plt.grid(alpha=0.3)

# Mostrar el gráfico
plt.show()
