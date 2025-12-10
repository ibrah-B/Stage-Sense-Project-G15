#!/bin/bash

# activation du vitual environment venv
echo "Starting backend..."
cd backend
if [ ! -d "venv" ]; then
  python3 -m venv venv
fi
source venv/bin/activate
pip install -r requirements.txt

# lancement du backend
uvicorn app:app --host 0.0.0.0 --port 8000 &
BACKEND_PID=$!

# lancement du frontend
echo "Starting frontend..."
cd ../frontend
npm install
npm start &
FRONTEND_PID=$!

# attente de l'achevement du frontend et backend
wait $BACKEND_PID $FRONTEND_PID