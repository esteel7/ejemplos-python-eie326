import matplotlib.pyplot as plt
from scipy import signal

# Parámetros
R = 100       # 100 Ω
L = 250e-3      # 250 mH

# \omega_c = R/L = 400 rad/s (63.7 Hz)

# Numerador y denominador de H(s) = sL / (R + sL)
num = [L, 0]
den = [L, R]

# Crear sistema
system = signal.TransferFunction(num, den)

# Obtener diagrama de Bode
w, mag, phase = signal.bode(system)

# Graficar
plt.figure(figsize=(8,6))

plt.subplot(2,1,1)
plt.semilogx(w, mag)
plt.title(r'Diagrama de Bode $H(\omega)=j\omega L /(R+j\omega L)$')
plt.ylabel('Magnitud [dB]')
plt.grid(True, which='both', ls='--')

plt.subplot(2,1,2)
plt.semilogx(w, phase)
plt.ylabel('Fase [°]')
plt.xlabel(r'Frecuencia angular $\omega$ [rad/s]')
plt.grid(True, which='both', ls='--')

plt.tight_layout()
plt.show()