import numpy as np

#POUR L'INSTANT ON CVA NORMALISER LES INSTRUMENTS ET LES SOLFEGES: VOIR DANS TUNER.PY

#Initialisation des tables de notes/Frequences selon les instruments.
#Pour les Violons   Note fr, Note international et la fréquence en HZ, selon les octaves utiles d'un violon, 3-7:
Table_note_violon  =[
    #Corde 4 
    ["Sol3", "G3", 196.00],
    ["Sol#3 / Lab3", "G#3 / Ab3", 207.65],
    ["La3", "A3", 220.00],
    ["La#3 / Sib3", "A#3 / Bb3", 233.08],
    ["Si3", "B3", 246.94],
    ["Do4", "C4", 261.63],
    ["Do#4 / Reb4", "C#4 / Db4", 277.18],
    
    #Corde 3
    ["Re4", "D4", 293.66],
    ["Re#4 / Mib4", "D#4 / Eb4", 311.13],
    ["Mi4", "E4", 329.63],
    ["Fa4", "F4", 349.23],
    ["Fa#4 / Solb4", "F#4 / Gb4", 369.99],
    ["Sol4", "G4", 392.00],
    ["Sol#4 / Lab4", "G#4 / Ab4", 415.30],
    
    #Corde 2
    ["La4", "A4", 440.00],
    ["La#4 / Sib4", "A#4 / Bb4", 466.16],
    ["Si4", "B4", 493.88],
    ["Do5", "C5", 523.25],
    ["Do#5", "C#5", 554.37],
    ["Re5", "D5", 587.33],
    ["Re#5", "D#5", 622.25],

    #Corde 1
    ["Mi5", "E5", 659.26],
    ["Fa5", "F5", 698.46],
    ["Fa#5", "F#5", 739.99],
    ["Sol5", "G5", 783.99],
    ["Sol#5", "G#5", 830.61],
    ["La5", "A5", 880.00],
    ["La#5", "A#5", 932.33],
    ["Si5", "B5", 987.77],
    ["Do6", "C6", 1046.50],
    ["Re6", "D6", 1174.66],
    ["Mi6", "E6", 1318.51],
    ["Sol6", "G6", 1567.98],
    ["La6", "A6", 1760.00],
    ["Si6", "B6", 1975.53],
    ["Do7", "C7", 2093.00],
    ["Re7", "D7", 2349.32],
    ["Mi7", "E7", 2637.02],
]
#Pour les basses, suivant le meme schema, selon un accordage standard.
Table_note_basse = [
    # Corde 4 
    ["Mi1", "E1", 41.20],
    ["Fa1", "F1", 43.65],
    ["Fa#1 / Solb1", "F#1 / Gb1", 46.25],
    ["Sol1", "G1", 49.00],
    ["Sol#1 / Lab1", "G#1 / Ab1", 51.91],
    ["La1", "A1", 55.00],
    ["La#1 / Sib1", "A#1 / Bb1", 58.27],
    ["Si1", "B1", 61.74],
    ["Do2", "C2", 65.41],
    ["Do#2 / Reb2", "C#2 / Db2", 69.30],
    ["Re2", "D2", 73.42],
    ["Re#2 / Mib2", "D#2 / Eb2", 77.78],
    ["Mi2", "E2", 82.41],

    # Corde 3 
    ["La1", "A1", 55.00],
    ["La#1 / Sib1", "A#1 / Bb1", 58.27],
    ["Si1", "B1", 61.74],
    ["Do2", "C2", 65.41],
    ["Do#2 / Reb2", "C#2 / Db2", 69.30],
    ["Re2", "D2", 73.42],
    ["Re#2 / Mib2", "D#2 / Eb2", 77.78],
    ["Mi2", "E2", 82.41],
    ["Fa2", "F2", 87.31],
    ["Fa#2 / Solb2", "F#2 / Gb2", 92.50],
    ["Sol2", "G2", 98.00],
    ["Sol#2 / Lab2", "G#2 / Ab2", 103.83],
    ["La2", "A2", 110.00],

    # Corde 2 
    ["Re2", "D2", 73.42],
    ["Re#2 / Mib2", "D#2 / Eb2", 77.78],
    ["Mi2", "E2", 82.41],
    ["Fa2", "F2", 87.31],
    ["Fa#2 / Solb2", "F#2 / Gb2", 92.50],
    ["Sol2", "G2", 98.00],
    ["Sol#2 / Lab2", "G#2 / Ab2", 103.83],
    ["La2", "A2", 110.00],
    ["La#2 / Sib2", "A#2 / Bb2", 116.54],
    ["Si2", "B2", 123.47],
    ["Do3", "C3", 130.81],
    ["Do#3 / Reb3", "C#3 / Db3", 138.59],
    ["Re3", "D3", 146.83],

    # Corde 1 
    ["Sol2", "G2", 98.00],
    ["Sol#2 / Lab2", "G#2 / Ab2", 103.83],
    ["La2", "A2", 110.00],
    ["La#2 / Sib2", "A#2 / Bb2", 116.54],
    ["Si2", "B2", 123.47],
    ["Do3", "C3", 130.81],
    ["Do#3 / Reb3", "C#3 / Db3", 138.59],
    ["Re3", "D3", 146.83],
    ["Re#3 / Mib3", "D#3 / Eb3", 155.56],
    ["Mi3", "E3", 164.81],
    ["Fa3", "F3", 174.61],
    ["Fa#3 / Solb3", "F#3 / Gb3", 185.00],
    ["Sol3", "G3", 196.00],
]
#Pour les guitares selon un accordage standard: 
Table_note_guitare = [
    # Corde 6 
    ["Mi2", "E2", 82.41],
    ["Fa2", "F2", 87.31],
    ["Fa#2 / Solb2", "F#2 / Gb2", 92.50],
    ["Sol2", "G2", 98.00],
    ["Sol#2 / Lab2", "G#2 / Ab2", 103.83],
    ["La2", "A2", 110.00],
    ["La#2 / Sib2", "A#2 / Bb2", 116.54],
    ["Si2", "B2", 123.47],
    ["Do3", "C3", 130.81],
    ["Do#3 / Reb3", "C#3 / Db3", 138.59],
    ["Re3", "D3", 146.83],
    ["Re#3 / Mib3", "D#3 / Eb3", 155.56],
    ["Mi3", "E3", 164.81],

    # Corde 5 
    ["La2", "A2", 110.00],
    ["La#2 / Sib2", "A#2 / Bb2", 116.54],
    ["Si2", "B2", 123.47],
    ["Do3", "C3", 130.81],
    ["Do#3 / Reb3", "C#3 / Db3", 138.59],
    ["Re3", "D3", 146.83],
    ["Re#3 / Mib3", "D#3 / Eb3", 155.56],
    ["Mi3", "E3", 164.81],
    ["Fa3", "F3", 174.61],
    ["Fa#3 / Solb3", "F#3 / Gb3", 185.00],
    ["Sol3", "G3", 196.00],
    ["Sol#3 / Lab3", "G#3 / Ab3", 207.65],
    ["La3", "A3", 220.00],

    # Corde 4 
    ["Re3", "D3", 146.83],
    ["Re#3 / Mib3", "D#3 / Eb3", 155.56],
    ["Mi3", "E3", 164.81],
    ["Fa3", "F3", 174.61],
    ["Fa#3 / Solb3", "F#3 / Gb3", 185.00],
    ["Sol3", "G3", 196.00],
    ["Sol#3 / Lab3", "G#3 / Ab3", 207.65],
    ["La3", "A3", 220.00],
    ["La#3 / Sib3", "A#3 / Bb3", 233.08],
    ["Si3", "B3", 246.94],
    ["Do4", "C4", 261.63],
    ["Do#4 / Reb4", "C#4 / Db4", 277.18],
    ["Re4", "D4", 293.66], 

    # Corde 3 
    ["Sol3", "G3", 196.00],
    ["Sol#3 / Lab3", "G#3 / Ab3", 207.65],
    ["La3", "A3", 220.00],
    ["La#3 / Sib3", "A#3 / Bb3", 233.08],
    ["Si3", "B3", 246.94],
    ["Do4", "C4", 261.63],
    ["Do#4 / Reb4", "C#4 / Db4", 277.18],
    ["Re4", "D4", 293.66],
    ["Re#4 / Mib4", "D#4 / Eb4", 311.13],
    ["Mi4", "E4", 329.63],
    ["Fa4", "F4", 349.23],
    ["Fa#4 / Solb4", "F#4 / Gb4", 369.99],
    ["Sol4", "G4", 392.00],

    # Corde 2 
    ["Si3", "B3", 246.94],
    ["Do4", "C4", 261.63],
    ["Do#4 / Reb4", "C#4 / Db4", 277.18],
    ["Re4", "D4", 293.66],
    ["Re#4 / Mib4", "D#4 / Eb4", 311.13],
    ["Mi4", "E4", 329.63],
    ["Fa4", "F4", 349.23],
    ["Fa#4 / Solb4", "F#4 / Gb4", 369.99],
    ["Sol4", "G4", 392.00],
    ["Sol#4 / Lab4", "G#4 / Ab4", 415.30],
    ["La4", "A4", 440.00],
    ["La#4 / Sib4", "A#4 / Bb4", 466.16],
    ["Si4", "B4", 493.88],

    # Corde 1 
    ["Mi4", "E4", 329.63],
    ["Fa4", "F4", 349.23],
    ["Fa#4 / Solb4", "F#4 / Gb4", 369.99],
    ["Sol4", "G4", 392.00],
    ["Sol#4 / Lab4", "G#4 / Ab4", 415.30],
    ["La4", "A4", 440.00],
    ["La#4 / Sib4", "A#4 / Bb4", 466.16],
    ["Si4", "B4", 493.88],
    ["Do5", "C5", 523.25],
    ["Do#5", "C#5", 554.37],
    ["Re5", "D5", 587.33],
    ["Re#5", "D#5", 622.25],
    ["Mi5", "E5", 659.26],
]



#Fonction de comparaison de la fréquence enregistrée avec les differentes notes des tableaux.
def comparateur(frequence, instrument='guitare', solfege='francais'):
    '''La fonction renvoie la note fr ou en international selon le solfege choisi en fonction de la fréquence enregistrée et de l'instruments choisi et l'écart entre la fréquence enregistrée et la note la plus proche en Hz.
    les tableaux des notes sont ordonnees en fonction de la fréquence'''

    #calcul de la diff en cents: utile pour une mesure plus precise
    
    #on prend la table selon l'instrument utilise par l'utilisateur
    if instrument == 'violon':
        table = Table_note_violon
    elif instrument == 'guitare':
        table = Table_note_guitare
    else:
        table = Table_note_basse

    #on cherche la note la plus proche de la frequence dans la table
    for i in range(len(table)):
            if table[i][2] == frequence:
                note = table[i][2]
            if table[i][2] <= frequence and table[i+1][2] >= frequence:
                if np.abs(table[i][2] - frequence) < np.abs(table[i+1][2] - frequence):
                    note = (table[i][2], (table[i][2] - frequence) )
    

    #on renvoie la note en solfege francais ou international selon les choix de l'utilisateur
    if solfege == 'francais':
        return (note[0][0], note[1])
    if solfege == 'international':
        return (note[0][1], note[1]) 
                    
                
def cends_diff( frequence,instrument='guitare', solfege='francais'):
    note_freq =  comparateur(frequence, instrument, solfege='francais')[0]

    return (1200 * np.log2(frequence  /  note_freq))
