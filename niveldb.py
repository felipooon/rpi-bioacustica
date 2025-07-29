import numpy as np
from scipy.io import wavfile

fs, data = wavfile.read('grabacion.wav')

# Si estéreo, usar solo un canal
if data.ndim > 1:
    data = data[:, 0]

# Normalizar si está en int16
data = data / np.max(np.abs(data))

# Calcular RMS (Root Mean Square)
rms = np.sqrt(np.mean(data**2))

# Convertir a decibel
db = 20 * np.log10(rms)

print(f"Nivel promedio: {db:.2f} dB")
