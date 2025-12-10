#!/bin/bash

#trouver le path pour notre projet
PROJECT_DIR="$(cd "$(dirname "$0")" && pwd)"

# --- BACKEND ---
echo "Starting backend..."

cd "$PROJECT_DIR/backend"

# creer environnement virtuel
if [ ! -d "venv" ]; then
  python3 -m venv venv
fi

# activer venv
source "$PROJECT_DIR/backend/venv/bin/activate"

# installer les lib
pip install -r requirements.txt

# lancement du backend
uvicorn app:app --host 0.0.0.0 --port 8000 &
BACKEND_PID=$!



# --- FRONTEND ---
echo "Starting frontend..."

cd "$PROJECT_DIR/frontend"

npm install
npm start &

FRONTEND_PID=$!

wait $BACKEND_PID $FRONTEND_PID

