# Stage Sense
Groupe 15 MI8
Membres du groupe:

Ibrahim Boubaya

Yassine Elmokhtari

Jules Decorps n0 21506930



Un accordeur (ou tuner, en anglais) est un dispositif — physique ou logiciel — permettant de déterminer la hauteur exacte d’un son musical afin d’ajuster un instrument pour qu’il produise les notes correctes. En d’autres termes, il aide les musiciens à s’assurer que chaque corde ou note émise correspond à la fréquence souhaitée.


Lorsqu’un instrument (comme une guitare, un violon ou une basse) joue une note, le son produit est une onde caractérisée par sa fréquence — mesurée en hertz (Hz).
L’accordeur capte ce son à l’aide d’un microphone ou d’un capteur de vibration, puis analyse le signal pour identifier :

- La fréquence fondamentale (la note principale jouée).

- L’écart entre cette fréquence et la fréquence de référence (par exemple, 440 Hz pour le La standard).

À partir de cette analyse, l’accordeur indique si la note est :

Trop basse (flat ou grave),

Trop haute (sharp ou aiguë),

Ou juste (in tune).

Dans ce projet on utilisera la methode de Transformation de Fourier Rapide une methode seulement vue en L3.
 (TFD) (fr.wikipedia.org/wiki/Transoformation_de_Fourier_rapide)

---------------------------
Notes:
19/11/25:
Jules- Jai realise que j'ai cree une fonction "record_sample" qui ne sert franchement a rien, car si un individus utilisant cet accordeur aurait ses deux mains prises, un arche et le violon lui meme dans ses mains, il n'a donc pas de doigts disponibles pour appuyer sur "Enregistrer" qui appele la fonction record_sample.

Donc jai change pas mal de trucs, ajoute un fichier .py audio_stream (jai demande a chatgpt comment faire bien sur) qui nous laisse enregistrer en continue et calculer la frequence fondamentale, qui a beaucoup plus de sens. Le changement appropries ont eu lieu dans app.py

jai aussi cree la structure html de base pour qu'on puisse lire des infos lorsquon test.



