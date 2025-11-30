import threading
import numpy as np
import sounddevice as sd  # make sure you have sounddevice installed

#Cette classe genere par chatgpt nous permet d'enregistrer notre instruments en continue (en samples), ces samples sont en suite
#convertis en array np pour les donner directement a audio.normalise_signal. la derniere methode est la plus 
#importante pour avoir une analyse hyper precise
class AudioStream:
    def __init__(self, fs=48000, chunk_size=2048):
        """
        fs: sampling rate in Hz
        chunk_size: number of samples per chunk
        """
        self.fs = fs
        self.chunk_size = chunk_size
        self.latest_chunk = np.zeros(chunk_size, dtype=np.float32)
        self.recording = False
        self._thread = None

    def _record_loop(self):
        """
        Continuously records audio in a background thread.
        """
        def callback(indata, frames, time, status):
            # indata is shape (frames, channels), take first channel
            mono = indata[:, 0]
            # Normalize to -1.0 → +1.0 (if not already)
            self.latest_chunk = mono.astype(np.float32)

        with sd.InputStream(samplerate=self.fs, channels=1, callback=callback,
                            blocksize=self.chunk_size):
            while self.recording:
                sd.sleep(100)  # small sleep to avoid busy loop

    def start(self):
        """
        Start continuous recording in a background thread.
        """
        if self.recording:
            return  # already running
        self.recording = True
        self._thread = threading.Thread(target=self._record_loop, daemon=True)
        self._thread.start()

    def stop(self):
        """
        Stop recording cleanly.
        """
        self.recording = False
        if self._thread is not None:
            self._thread.join()
            self._thread = None

    def get_latest_samples(self):
        """
        Returns the latest recorded chunk as a NumPy float32 array.
        """
        return self.latest_chunk.copy()
