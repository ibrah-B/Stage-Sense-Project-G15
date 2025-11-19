from fastapi import FastAPI 
from services.audio import init_audio
from services.audio_stream import AudioStream

app = FastAPI(title="Stage Sense")

#Initialisation de PyAudio et trouver l'appereil d'enregistrement.
p, device_index = init_audio()

#On commence l'enregistrement ( mains libres)
audio_stream = AudioStream(device_index)
audio_stream.start()

@app.get("/pitch")
def get_pitch():
    """ Renvoie la derniere frequence detectee en Hz (mains libres)"""
    frequency = audio_stream.get_frequency()
    return {"frequency_hz": round(frequency, 2)}

    