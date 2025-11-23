from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from audio.analyser import analyse_audio_file 
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


class AnalyseResponse(BaseModel):
    frequency: float
    note: str
    cents_off: float

@app.post("/analyse", response_model=AnalyseResponse)
async def analyse(file:UploadFile = File(...)):
    """Recoit l'audio (wav, mp3, raw) et renvoie la note et frequence"""
    audio_bytes = await file.read()

    result = analyse_audio_file(audio_bytes)

    return AnalyseResponse(
        frequency=result['frequency'], 
        note=result['note']
        cents_off=result['cents_off']
    )    

