import numpy as np
from scipy import signal

# Parámetros
R1 = 100
R2 = 300
C = 2e-6

# Numerador y denominador de H(s)
num = [R2]               # 300
den = [R1*R2*C, R1+R2]   # [0.06, 400]

# Crear la función de transferencia
H = signal.TransferFunction(num, den)

# Frecuencia en rad/s
omega = 10000  

# Obtener respuesta en frecuencia
w, Hjw = signal.freqresp(H, [omega])

# Magnitud y fase
magnitude = np.abs(Hjw[0])
phase = np.angle(Hjw[0], deg=True)

print(f"H(j{omega}) = {Hjw[0]}")
print(f"Magnitud = {magnitude}")
print(f"Fase = {phase} grados")

# Frecuencia de corte
omega_c = (R1 + R2) / (R1 * R2 * C)
f_c = omega_c / (2 * np.pi)

print(f"Frecuencia de corte ωc = {omega_c:.6f} rad/s")
print(f"Frecuencia de corte fc = {f_c:.3f} Hz")