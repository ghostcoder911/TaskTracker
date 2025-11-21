@echo off
REM Task Tracker - Local Development Startup Script (Windows)

echo 🚀 Starting Task Tracker...
echo.

REM Check if backend\.env exists
if not exist "backend\.env" (
    echo ⚠️  Warning: backend\.env not found!
    echo Please create backend\.env file with your Google Sheets credentials.
    echo See backend\config_template.txt for reference.
    echo.
)

REM Check if frontend\.env exists
if not exist "frontend\.env" (
    echo ⚠️  Warning: frontend\.env not found!
    echo Creating frontend\.env with default local settings...
    echo REACT_APP_API_URL=http://localhost:5000/api > frontend\.env
    echo ✅ Created frontend\.env
    echo.
)

REM Start backend
echo 📦 Starting Backend Server...
cd backend

if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
)

call venv\Scripts\activate.bat
pip install -q -r requirements.txt

echo Backend running on http://localhost:5000
start "Task Tracker Backend" cmd /k "venv\Scripts\activate.bat && python app.py"

cd ..
timeout /t 3 /nobreak > nul

REM Start frontend
echo.
echo 🎨 Starting Frontend...
cd frontend

if not exist "node_modules" (
    echo Installing dependencies...
    call npm install
)

echo Frontend will open on http://localhost:3000
start "Task Tracker Frontend" cmd /k "npm start"

cd ..

echo.
echo ✅ Task Tracker is running!
echo    Backend:  http://localhost:5000
echo    Frontend: http://localhost:3000
echo.
echo Close the terminal windows to stop the servers.

pause

