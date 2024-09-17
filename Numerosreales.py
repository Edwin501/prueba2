import matplotlib.pyplot as plt
import numpy as np

# Valores a representar en la recta numérica
values = [-3, -2.5, -1.5, 2, 2.5, np.sqrt(5), np.pi, np.sqrt(14), 7, 9]
labels = ['-3', '-2 1/2', '-3/2', '2', '5/2', '√5', 'π', '√14', '7', '3^2']

# Configuración de la recta numérica
plt.figure(figsize=(10, 2))
plt.axhline(0, color='black', lw=2)

# Representación de los valores en la recta numérica
for i, (value, label) in enumerate(zip(values, labels)):
    plt.plot(value, 0, 'ro')  # Punto rojo en la recta
    plt.text(value, 0.1, label, ha='center', fontsize=12)  # Etiqueta encima del puntocls

plt.title("Representación en la Recta Numérica")
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.show()