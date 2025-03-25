import matplotlib.pyplot as plt   # Para Instalar la libreria, en terminal integrado usar:  "pip3 install matplotlib"   , sin las comillas.
import numpy as np


print(plt.matplotlib.__version__)


x = [1, 2, 3, 4, 5]
y1 = [2, 4, 1, 5, 3]
y2 = [12, 10, 7, 5, 2]

plt.plot(x, y1, label="Serie 1")
plt.plot(x, y2, label="Serie 2")


plt.plot(x, y1, 'r--', label="Datos")
plt.title("Gráfico x-y")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.legend()
plt.grid(True)


plt.plot(x, y1, label="Serie 1")
plt.plot(x, y2, label="Serie 2")
plt.show()  # Esta línea es crucial para mostrar el gráfico
