# backend.py
from fastapi import FastAPI
from services.tuner import analyse_audio_bytes  
from services.audio_stream import AudioStream 

app = FastAPI()

# Start AudioStream at server start
audio_stream = AudioStream()
audio_stream.start()

@app.get("/analyse")
def analyse_endpoint():
    # get latest chunk
    signal = audio_stream.get_latest_samples()
    # call your analyser pipeline
    result = analyse_audio_bytes(signal)
    # add recording status
    result["recording"] = audio_stream.recording
    return result
