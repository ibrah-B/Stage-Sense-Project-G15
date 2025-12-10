# Stage Sense – Accordeur Musical
**Groupe 15 MI8**  

**Membres :**  
- Ibrahim Boubaya  
- Yassine Elmokhtari  
- Jules Decorps (n° 21506930)  

---

## Description du projet

Ce projet vise à créer un **accordeur musical logiciel** utilisable sur un Raspberry Pi 4B avec un microphone USB.  
Un accordeur (ou *tuner*) est un dispositif permettant de déterminer la hauteur exacte d’un son musical pour ajuster un instrument et s’assurer que chaque note émise correspond à la fréquence souhaitée.

Lorsqu’un instrument (guitare, violon, basse…) joue une note, le son produit est une **onde sonore caractérisée par sa fréquence** (mesurée en Hertz, Hz). L’accordeur capte cette onde et l’analyse pour déterminer :

- La **fréquence fondamentale** de la note jouée  
- L’écart entre cette fréquence et la fréquence de référence (exemple : 440 Hz pour le La standard)  

Grâce à cette analyse, l’accordeur peut indiquer si la note est :  

- Trop basse (*flat* ou grave)  
- Trop haute (*sharp* ou aiguë)  
- Correcte (*in tune*)  

Pour ce projet, nous utilisons la **Transformée de Fourier Rapide (TFD / FFT)** afin de transformer le signal temporel capté en un signal fréquentiel. Cette méthode permet d’isoler les différentes fréquences composant un son complexe et d’identifier précisément la note jouée.  

> La décomposition d’un signal en série de Fourier consiste à représenter une fonction périodique comme une somme de sinus et de cosinus de différentes fréquences et amplitudes. C’est ce principe qui est exploité dans la FFT pour analyser les sons en temps réel.

---

## Structure du projet

```markdown
.
├── README.md
├── backend
│   ├── app.py
│   ├── requirements.txt
│   └── services
│       ├── Notes_data.py
│       ├── audio.py
│       ├── audio_stream.py
│       ├── fft.py
│       ├── instruments.py
│       └── tuner.py
└── frontend
    ├── package.json
    ├── public
    │   └── index.html
    └── src
        ├── App.js
        ├── Tuner.jsx
        └── index.js


```
---

## Fonctionnement général

1. **Capture audio** : le microphone USB envoie le flux sonore vers le backend.  
2. **Analyse du signal** : le backend utilise la FFT (dans `ftt.py`)pour convertir le signal en domaine fréquentiel.  
3. **Comparaison avec les notes de référence** : le module `Notes_data.py` contient les fréquences standard de chaque note et permet de calculer l’écart en *cents*.  
4. **Transmission au frontend** : l’information sur la note détectée et son écart est envoyée à l’interface React.  
5. **Affichage utilisateur** : `Tuner.jsx` affiche en temps réel la note jouée, la fréquence et l’écart, permettant à l’utilisateur d’accorder son instrument rapidement.

---

## Installation & Exécution

### Backend (Python)
```bash
cd backend
python -m venv venv        # Créer un environnement virtuel
source venv/bin/activate   # Activer l'environnement
pip install -r requirements.txt
python app.py              # Lancer le serveur
```

### Frontend(React)
```bash
cd frontend
npm install
npm start                  # Lancer l’interface utilisateur
```
---

## Points techniques clés

FFT (Fast Fourier Transform) : permet d’extraire les fréquences dominantes d’un signal complexe.

Cents : unité logarithmique mesurant l’écart entre deux fréquences musicales.

Interface React : conçue pour un affichage lisible même en conditions de scène, avec informations claires sur la justesse de la note.

---

## Remarques

Le projet est conçu pour être facilement extensible à différents instruments (guitare, basse, violon…).

La précision dépend de la qualité du microphone et du traitement en temps réel.

Les caches Python (`__pycache__`) sont générés automatiquement et peuvent être ignorés pour la version finale.