from . import audio
from . import fft
from . import Notes_data
from . import audio_stream


def analyse_audio_bytes(signal):

    signal_norm = audio.normalise_signal(signal)

    frequence_calc = fft.estimate_pitch(signal_norm, 48000)

    note_pp, diff_note_hz = Notes_data.comparateur(frequence_calc) 
    cents_diff = Notes_data.cends_diff(frequence_calc)

    return {
        "freq": frequence_calc,
        "note": note_pp,
        "frequency difference": diff_note_hz, 
        "cents": cents_diff

    }



                                        

