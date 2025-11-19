import pyaudio
import numpy as np
from audio import normalise_signal
from fft import estimate_pitch
import threading
import time

class AudioStream:
    def __init__(self, device_index, fs=44100, chunk_size=1024):
        self.fs = fs
        self.chunk_size = chunk_size
        self.device_index = device_index
        self.signal = np.zeros(chunk_size)
        self.freq = 0
        self.running = False
        self.p = pyaudio.PyAudio()
        self.stream = None

    def start(self):
        self.running = True
        self.stream = self.p.open(format=pyaudio.paInt16, channels=1, rate=self.fs, input=True, input_device_index=self.device_index, frames_per_buffer=self.chunk_size)
        threading.Thread(target=self._update, daemon=True).start()

    def _update(self):
        while self.running:
            data = self.stream.read(self.chunk_size, exception_on_overflow=False)
            signal = normalise_signal(np.frombuffer(data, dtype=np.int16))
            self.signal = signal
            self.freq = estimate_pitch(signal, self.fs)
            time.sleep(0.01) #petit decalage pour ne pas griller le processeur
    def get_frequency(self):
        return self.freq

    def stop(self):
        self.running = False
        if self.stream:
            self.stream.stop_stream()
            self.stream.close()
        self.p.terminate()
