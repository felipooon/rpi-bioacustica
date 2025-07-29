import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile
from scipy.signal import spectrogram

# Cargar archivo WAV
fs, data = wavfile.read('grabacion.wav')

# Si es estéreo, tomar solo un canal
if data.ndim > 1:
    data = data[:, 0]

# Calcular el espectrograma
f, t, Sxx = spectrogram(data, fs)

# Mostrar el espectrograma
plt.figure(figsize=(10, 4))
plt.pcolormesh(t, f, 10 * np.log10(Sxx), shading='gouraud')
plt.ylabel('Frecuencia [Hz]')
plt.xlabel('Tiempo [s]')
plt.title('Espectrograma')
plt.colorbar(label='dB')
plt.tight_layout()
plt.show()
