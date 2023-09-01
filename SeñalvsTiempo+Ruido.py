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

def add_gaussian_noise(signal, mu, sigma):
    noise = np.random.normal(mu, sigma, len(signal))
    noisy_signal = signal + noise
    return noisy_signal

# Crear una señal de ejemplo (una señal sinusoidal)
sample_rate = 1000  # Frecuencia de muestreo en Hz
frequency = 5  # Frecuencia de la señal en Hz
time = np.arange(0, 1, 1/sample_rate)  # Tiempo de 0 a 1 segundo
signal_example = np.sin(2 * np.pi * frequency * time)

# Parámetros para el ruido gaussiano
mu = 0
sigma = 0.1

# Agregar ruido gaussiano a la señal de ejemplo
noisy_signal = add_gaussian_noise(signal_example, mu, sigma)

# Graficar la señal en función del tiempo con ruido
plot_signal_vs_time(noisy_signal, sample_rate)
