import pyaudio
import numpy as np

def init_audio():
    """
    Lister tous les systemes d'input (micros) et print les infos de l'appareil (par defaut)
    """
    p = pyaudio.PyAudio()
    print('===SYSTEMES SONORES DISPONIBLES===')
    for i in range(p.get_device_count()):
        info = p.get_device_info_by_index(i)
        if info['maxInputChannels'] > 0:
            print(f"{i}:{info['name']} (Input channels: {info['maxInputChannels']})")

        default_index = p.get_default_input_device_info() ['index']
        print(f"\nDefault input device index: {default_index}")
        print(f"Device info: {p.get_device_info_by_index(default_index)}")

    return p, default_index

def record_sample(p, device_index, duration=2, fs=44100):
    """
    Enregistre du mono audio, (un sample) depuis le micro donne.
    Renvoie un vecteur numpy de floats normalises €[-1;1].
    """
    print(f"Enregistrement de {duration} secondes utilisant l'appareil {device_index}...")

    stream = p.open(format=pyaudio.paInt16, channels=1, rate=fs, input=True, input_device_index=device_index, frames_per_buffer=1024)

    frames = []
    for _ in range(0, int(fs / 1024 * duration)):
        data = stream.read(1024,exeption_on_overflow=False)
        frames.append(np.frombuffer(data, dtype=np.int16))

    stream.stop_stream()
    stream.close()

    signal = np.concatenate(frames)
    signal = normalise_signal(signal)
    return signal, fs

def normalise_signal(signal):
    """Normalise le sample audio a un float32 dans [-1;1] et suprime le decalage CC (le deplacement d'amplitude moyen par rappport a zero)"""

    signal = signal.astype(np.float32)
    signal -= np.mean(signal) #enlever le offset
    max_val = np.max(np.abs(signal))

    if max_val > 0:
        signal /= max_val #le normaliser entre -1 et 1
    return signal
