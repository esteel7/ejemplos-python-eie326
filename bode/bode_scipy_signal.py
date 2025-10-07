import matplotlib.pyplot as plt
from scipy import signal

# Parámetros
R = 1e3       # 1 kΩ
C = 1e-6      # 1 µF

# Numerador y denominador de H(w) = 1 / (1 + jwRC)
num = [1]
den = [R*C, 1]

# Crear sistema
system = signal.TransferFunction(num, den)

# Obtener diagrama de Bode
w, mag, phase = signal.bode(system)

# Graficar
plt.figure(figsize=(8,6))

plt.subplot(2,1,1)
plt.semilogx(w, mag)
plt.title(r'Diagrama de Bode $H(\omega)=1 /(1+j\omega RC)$')
plt.ylabel('Magnitud [dB]')
plt.grid(True, which='both', ls='--')

plt.subplot(2,1,2)
plt.semilogx(w, phase)
plt.ylabel('Fase [°]')
plt.xlabel(r'Frecuencia angular $\omega$ [rad/s]')
plt.grid(True, which='both', ls='--')

plt.tight_layout()
plt.show()