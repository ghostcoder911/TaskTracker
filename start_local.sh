#!/bin/bash

# Task Tracker - Local Development Startup Script

echo "🚀 Starting Task Tracker..."
echo ""

# Check if backend/.env exists
if [ ! -f "backend/.env" ]; then
    echo "⚠️  Warning: backend/.env not found!"
    echo "Please create backend/.env file with your Google Sheets credentials."
    echo "See backend/config_template.txt for reference."
    echo ""
fi

# Check if frontend/.env exists
if [ ! -f "frontend/.env" ]; then
    echo "⚠️  Warning: frontend/.env not found!"
    echo "Creating frontend/.env with default local settings..."
    echo "REACT_APP_API_URL=http://localhost:5000/api" > frontend/.env
    echo "✅ Created frontend/.env"
    echo ""
fi

# Start backend
echo "📦 Starting Backend Server..."
cd backend
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

source venv/bin/activate
pip install -q -r requirements.txt

echo "Backend running on http://localhost:5000"
python app.py &
BACKEND_PID=$!
cd ..

# Wait a bit for backend to start
sleep 3

# Start frontend
echo ""
echo "🎨 Starting Frontend..."
cd frontend

if [ ! -d "node_modules" ]; then
    echo "Installing dependencies..."
    npm install
fi

echo "Frontend will open on http://localhost:3000"
npm start &
FRONTEND_PID=$!
cd ..

echo ""
echo "✅ Task Tracker is running!"
echo "   Backend:  http://localhost:5000"
echo "   Frontend: http://localhost:3000"
echo ""
echo "Press Ctrl+C to stop both servers"

# Wait for Ctrl+C
trap "echo ''; echo '🛑 Stopping servers...'; kill $BACKEND_PID $FRONTEND_PID; exit" INT
wait

