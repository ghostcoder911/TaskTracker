#!/bin/bash

echo "=========================================="
echo "  Building Task Tracker for Linux"
echo "=========================================="
echo ""

# Install PyInstaller if not already installed
echo "Installing PyInstaller..."
pip install pyinstaller

# Clean previous builds
echo "Cleaning previous builds..."
rm -rf build dist *.spec

# Build the executable
echo "Building executable..."
pyinstaller --onefile \
    --windowed \
    --name="TaskTracker" \
    --add-data="credentials.json:." \
    --add-data="config.json:." \
    tasktracker_modern.py

echo ""
echo "=========================================="
echo "  Build Complete!"
echo "=========================================="
echo ""
echo "Your executable is in: dist/TaskTracker"
echo ""
echo "To distribute to your team:"
echo "1. Create a folder named 'TaskTracker'"
echo "2. Copy dist/TaskTracker to that folder"
echo "3. Copy credentials.json to that folder"
echo "4. Copy config.json to that folder"
echo "5. Zip the folder and share!"
echo ""
echo "Your team can then:"
echo "1. Extract the zip"
echo "2. Open terminal in that folder"
echo "3. Run: chmod +x TaskTracker"
echo "4. Run: ./TaskTracker"
echo ""

