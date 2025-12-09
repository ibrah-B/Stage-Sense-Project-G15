from . import audio
from . import fft
from . import Notes_data
from . import audio_stream


def analyse_audio_bytes(signal):

    signal_norm = audio.normalise_signal(signal)

    frequence_calc = fft.estimate_pitch(signal_norm, 48000)

    note_name, freq_note_pp = Notes_data.comparateur(frequence_calc) 
    cents_diff = Notes_data.cents_diff(frequence_calc, freq_note_pp)

    return {
        "freq": frequence_calc,
        "note": note_name, 
        "cents": cents_diff
    }



                                        

