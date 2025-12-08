import audio
import fft
import instruments
import Notes_data


def analyse_audio_bytes(audio_bytes, instrument='guitare', solfege='francais'):

    signal_raw = audio.pcm_sampler(audio_bytes)
    signal_norm = audio.normalise_signal(signal_raw)

    frequence_calc = fft.estimate_pitch(signal_norm, 48000)

    note_pp, diff_note_hz = Notes_data.comparateur(frequence_calc) 
    cents_diff = Notes_data.cends_diff(frequence_calc)

    return {
        "freq": frequence_calc,
        "note": note_pp,
        "frequency difference": diff_note_hz, 
        "cents": cents_diff

    }



                                        

