import numpy as np
import matplotlib.pyplot as plt

# Definición de la función v_o(t)
t = np.linspace(0, 3, 300)
v = (3/np.sqrt(2)) * np.exp(-4*t) * np.sin(np.sqrt(2)*t)

# Crear la gráfica
plt.figure(figsize=(10, 6))
plt.plot(t, v, linewidth=2)
plt.title(r"$v_o(t) = \frac{3}{\sqrt{2}} e^{-4t} \sin(\sqrt{2}t)$", color='blue')
plt.xlabel('Tiempo (s)')
plt.ylabel('$v_o(t)$')
plt.grid(True)
plt.show()