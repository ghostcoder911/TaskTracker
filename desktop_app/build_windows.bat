@echo off
echo ==========================================
echo   Building Task Tracker for Windows
echo ==========================================
echo.

REM Install PyInstaller if not already installed
echo Installing PyInstaller...
pip install pyinstaller

REM Clean previous builds
echo Cleaning previous builds...
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist
del *.spec 2>nul

REM Build the executable
echo Building executable...
pyinstaller --onefile ^
    --windowed ^
    --name="TaskTracker" ^
    --add-data="credentials.json;." ^
    --add-data="config.json;." ^
    --icon=NONE ^
    tasktracker_modern.py

echo.
echo ==========================================
echo   Build Complete!
echo ==========================================
echo.
echo Your executable is in: dist\TaskTracker.exe
echo.
echo To distribute to your team:
echo 1. Create a folder named 'TaskTracker'
echo 2. Copy dist\TaskTracker.exe to that folder
echo 3. Copy credentials.json to that folder
echo 4. Copy config.json to that folder
echo 5. Zip the folder and share!
echo.
echo Your team can then:
echo 1. Extract the zip
echo 2. Double-click TaskTracker.exe
echo.

pause

