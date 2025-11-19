import numpy as np

def compute_fft(signal, fs):
    """Calcule la transformation de Fourier discrete du signal normalise.
    Renvoie un vecteur de frequence et un spectre de magnitude."""

    N = len(signal)
    fft_vals = np.fft.rfft(signal)
    fft_magnitude = np.abs(fft_vals) / N
    freqs = np.fft.rfftfreq(N, 1/fs)
    return freqs, fft_magnitude

def estimate_pitch(signal, fs):
    """Estime la frequence en utilisant la maximum du vecteur FFT qu'on a trouve.
    Frequence en Hz."""

    freqs, magnitude = compute_fft(signal, fs)
    peak_index = np.argmax(magnitude)
    fundamental_freq = freqs[peak_index]
    return fundamental_freq

