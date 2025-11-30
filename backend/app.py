from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from services.audio import init_audio
from services.audio_stream import AudioStream

app = FastAPI(title="Stage Sense")

#Initialisation de PyAudio et trouver l'appareil d'enregistrement.
p, device_index = init_audio()

#On commence l'enregistrement ( mains libres)
audio_stream = AudioStream(device_index)
audio_stream.start()

@app.get("/pitch")
def get_pitch():
    """ Renvoie la derniere frequence detectee en Hz (mains libres)"""
    frequency = audio_stream.get_frequency()
    return {"frequency_hz": round(frequency, 2)}


class AnalyseResponse(BaseModel):
    frequency: float
    note: str
    cents_off: float

from services.audio import analyse_audio_bytes

@app.post("/analyse")
async def analyse(file: UploadFile = File(...)):
    audio_bytes = await file.read()
    instrument, solfege = 'Guitare', 'francais'
    result = analyse_audio_bytes(audio_bytes, instrument, solfege)
    return result