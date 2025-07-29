import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import spectrogram
import csv

# Carpeta con audios
carpeta_audios = 'audios'
carpeta_salida = 'resultados'

# Crear carpeta de salida si no existe
os.makedirs(carpeta_salida, exist_ok=True)

# Archivo CSV de salida
csv_path = os.path.join(carpeta_salida, 'analisis_audio.csv')

# Crear o sobrescribir CSV
with open(csv_path, mode='w', newline='') as csvfile:
    escritor = csv.writer(csvfile)
    escritor.writerow(['archivo', 'nivel_db', 'duracion_seg'])

    # Procesar cada archivo WAV
    for archivo in os.listdir(carpeta_audios):
        if archivo.endswith('.wav'):
            ruta_audio = os.path.join(carpeta_audios, archivo)

            try:
                fs, data = wavfile.read(ruta_audio)

                # Estéreo: usar solo un canal
                if data.ndim > 1:
                    data = data[:, 0]

                # Normalizar si está en int16 o similar
                data = data.astype(np.float32)
                data = data / np.max(np.abs(data))

                # Calcular RMS y dB
                rms = np.sqrt(np.mean(data**2))
                db = 20 * np.log10(rms) if rms > 0 else -np.inf

                # Duración del audio
                duracion = len(data) / fs

                # Guardar datos en CSV
                escritor.writerow([archivo, round(db, 2), round(duracion, 2)])

                # Calcular espectrograma
                f, t, Sxx = spectrogram(data, fs)

                # Crear imagen
                plt.figure(figsize=(10, 4))
                plt.pcolormesh(t, f, 10 * np.log10(Sxx + 1e-10), shading='gouraud')
                plt.ylabel('Frecuencia [Hz]')
                plt.xlabel('Tiempo [s]')
                plt.title(f'Espectrograma: {archivo}')
                plt.colorbar(label='dB')
                plt.tight_layout()

                # Guardar PNG
                nombre_png = archivo.replace('.wav', '.png')
                ruta_png = os.path.join(carpeta_salida, nombre_png)
                plt.savefig(ruta_png)
                plt.close()

                print(f'Procesado: {archivo}')

            except Exception as e:
                print(f'Error con {archivo}: {e}')
