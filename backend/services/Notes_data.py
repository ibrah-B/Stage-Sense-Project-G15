import numpy as np

#POUR L'INSTANT ON CVA NORMALISER LES INSTRUMENTS ET LES SOLFEGES: VOIR DANS TUNER.PY

#Initialisation du tableau de notes/Frequences sur 8 octaves en solfège FR: 

NOTES_SOLFEGE = [
    ["La0", 27.50],
    ["Sib0", 29.14],
    ["Si0", 30.87],

    ["Do1", 32.70],
    ["Reb1", 34.65],
    ["Re1", 36.71],
    ["Mib1", 38.89],
    ["Mi1", 41.20],
    ["Fa1", 43.65],
    ["Solb1", 46.25],
    ["Sol1", 49.00],
    ["Lab1", 51.91],

    ["La1", 55.00],
    ["Sib1", 58.27],
    ["Si1", 61.74],

    ["Do2", 65.41],
    ["Reb2", 69.30],
    ["Re2", 73.42],
    ["Mib2", 77.78],
    ["Mi2", 82.41],
    ["Fa2", 87.31],
    ["Solb2", 92.50],
    ["Sol2", 98.00],
    ["Lab2", 103.83],

    ["La2", 110.00],
    ["Sib2", 116.54],
    ["Si2", 123.47],

    ["Do3", 130.81],
    ["Reb3", 138.59],
    ["Re3", 146.83],
    ["Mib3", 155.56],
    ["Mi3", 164.81],
    ["Fa3", 174.61],
    ["Solb3", 185.00],
    ["Sol3", 196.00],
    ["Lab3", 207.65],

    ["La3", 220.00],
    ["Sib3", 233.08],
    ["Si3", 246.94],

    ["Do4", 261.63],
    ["Reb4", 277.18],
    ["Re4", 293.66],
    ["Mib4", 311.13],
    ["Mi4", 329.63],
    ["Fa4", 349.23],
    ["Solb4", 369.99],
    ["Sol4", 392.00],
    ["Lab4", 415.30],

    ["La4", 440.00],
    ["Sib4", 466.16],
    ["Si4", 493.88],

    ["Do5", 523.25],
    ["Reb5", 554.37],
    ["Re5", 587.33],
    ["Mib5", 622.25],
    ["Mi5", 659.26],
    ["Fa5", 698.46],
    ["Solb5", 739.99],
    ["Sol5", 783.99],
    ["Lab5", 830.61],

    ["La5", 880.00],
    ["Sib5", 932.33],
    ["Si5", 987.77],

    ["Do6", 1046.50],
    ["Reb6", 1108.73],
    ["Re6", 1174.66],
    ["Mib6", 1244.51],
    ["Mi6", 1318.51],
    ["Fa6", 1396.91],
    ["Solb6", 1479.98],
    ["Sol6", 1567.98],
    ["Lab6", 1661.22],

    ["La6", 1760.00],
    ["Sib6", 1864.66],
    ["Si6", 1975.53],

    ["Do7", 2093.00],
    ["Reb7", 2217.46],
    ["Re7", 2349.32],
    ["Mib7", 2489.02],
    ["Mi7", 2637.02],
    ["Fa7", 2793.83],
    ["Solb7", 2959.96],
    ["Sol7", 3135.96],
    ["Lab7", 3322.44],

    ["La7", 3520.00],
    ["Sib7", 3729.31],
    ["Si7", 3951.07],

    ["Do8", 4186.01]
]





#Fonction de comparaison de la fréquence enregistrée avec les differentes notes des tableaux.
def comparateur(frequence, table=NOTES_SOLFEGE) -> tuple:
    '''La fonction renvoie la note fr ou en international selon le solfege choisi en fonction de la fréquence enregistrée et de l'instruments choisi et l'écart entre la fréquence enregistrée et la note la plus proche en Hz.
    les tableaux des notes sont ordonnees en fonction de la fréquence'''


    #on cherche la note la plus proche de la frequence dans la table
    for i in range(len(table)):
            if table[i][1] == frequence:
                note = table[i][1]
            if table[i][1] <= frequence and table[i+1][1] >= frequence:
                if np.abs(table[i][1] - frequence) < np.abs(table[i+1][1] - frequence):
                    note = (table[i][1], (table[i][1] - frequence) )
    #notez que notes est de forme : ( nom, difference de frequece avec a note parfaite)

    return note[0], note[1]
                    
                
def cends_diff(frequence):
    note_freq =  comparateur(frequence)[0]
    return (1200 * np.log2(frequence  /  note_freq))
