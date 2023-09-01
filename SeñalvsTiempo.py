import numpy as np
import matplotlib.pyplot as plt

def plot_signal_vs_time(signal, sample_rate):
    time = np.arange(len(signal)) / sample_rate
    plt.figure(figsize=(10, 6))
    plt.plot(time, signal)
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Amplitud')
    plt.title('Señal en función del tiempo')
    plt.grid(True)
    plt.show()

# Crear una señal de ejemplo (señal sinusoidal)
sample_rate = 1000  # Frecuencia de muestreo en Hz
frequency = 5  # Frecuencia de la señal en Hz
time = np.arange(0, 1, 1/sample_rate)  # Tiempo de 0 a 1 segundo
signal_example = np.sin(2 * np.pi * frequency * time)

# Graficar la señal en función del tiempo
plot_signal_vs_time(signal_example, sample_rate)
