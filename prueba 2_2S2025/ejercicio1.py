import numpy as np
from scipy import signal

# Parámetros
R = 0.25
L = 1
C = 1  

# Numerador y denominador de H(s)
num = [R]               # 0.25
den = [R*L*C, L, R]   # 

# Crear la función de transferencia
H = signal.TransferFunction(num, den)

# Frecuencia en rad/s
omega = 1/np.sqrt(2)  

# Obtener respuesta en frecuencia
w, Hjw = signal.freqresp(H, [omega])

# Magnitud y fase
magnitude = np.abs(Hjw[0])
phase = np.angle(Hjw[0], deg=True)

print(f"H(j{omega}) = {Hjw[0]}")
print(f"Magnitud = {magnitude}")
print(f"Fase = {phase} grados")