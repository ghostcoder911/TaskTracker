# Task Tracker Desktop Application

A standalone desktop application for team check-ins that saves directly to Google Sheets.

## ✨ Features

- ✅ Beautiful GUI interface
- ✅ Works on Windows, Linux, and Mac
- ✅ Saves directly to Google Sheets
- ✅ Local backup (works offline)
- ✅ No web browser needed
- ✅ Easy to distribute as executable

## 🚀 Quick Start

### Option 1: Run with Python

**1. Install Python 3.8+** (if not already installed)

**2. Install dependencies:**
```bash
cd desktop_app
pip install -r requirements.txt
```

**3. Setup Google Sheets:**
- Copy your service account JSON file to this folder
- Rename it to `credentials.json`
- Copy `config_template.json` to `config.json`
- Edit `config.json` and add your spreadsheet ID (already set)

**4. Run the app:**
```bash
python tasktracker_app.py
```

---

### Option 2: Create Executable (Distribute to Team)

**For Windows:**
```bash
cd desktop_app
pip install -r requirements.txt
pyinstaller --onefile --windowed --name="TaskTracker" --icon=icon.ico tasktracker_app.py
```

The executable will be in `dist/TaskTracker.exe`

**For Linux:**
```bash
cd desktop_app
pip install -r requirements.txt
pyinstaller --onefile --windowed --name="TaskTracker" tasktracker_app.py
```

The executable will be in `dist/TaskTracker`

---

## 📁 Required Files

When distributing to team, include these files in the same folder as the executable:

1. **TaskTracker.exe** (or TaskTracker on Linux)
2. **credentials.json** - Your Google service account credentials
3. **config.json** - Contains the spreadsheet ID

Your team just needs to:
1. Download the folder
2. Double-click the executable
3. Start checking in!

---

## 🔧 Setup Instructions

### 1. Get Google Service Account Credentials

You already have this JSON file! Just:
- Copy it to the `desktop_app` folder
- Rename it to `credentials.json`

### 2. Configure Spreadsheet ID

- Copy `config_template.json` to `config.json`
- The spreadsheet ID is already set: `1EY7ZV0oxvvW-IFToMHFz-wHwtTP3U0u7vipcyNYdFk0`

### 3. Test It

```bash
python tasktracker_app.py
```

Enter your name, do a check-in, and verify data appears in Google Sheets!

---

## 📦 Building Executables

### Windows Executable

```bash
# Install PyInstaller
pip install pyinstaller

# Build
pyinstaller --onefile --windowed --name="TaskTracker" tasktracker_app.py

# Output: dist/TaskTracker.exe
```

### Linux Executable

```bash
# Install PyInstaller
pip install pyinstaller

# Build
pyinstaller --onefile --windowed --name="TaskTracker" tasktracker_app.py

# Output: dist/TaskTracker
```

### Mac Executable

```bash
# Install PyInstaller
pip install pyinstaller

# Build
pyinstaller --onefile --windowed --name="TaskTracker" tasktracker_app.py

# Output: dist/TaskTracker.app
```

---

## 📤 Distribution

### Package for Team:

Create a folder with:
```
TaskTracker/
├── TaskTracker.exe (or TaskTracker on Linux)
├── credentials.json
├── config.json
└── README_FOR_TEAM.txt
```

Zip it and share with your team!

---

## 💾 Data Storage

### Google Sheets (Primary)
- Data is saved to your spreadsheet
- One worksheet per date
- Same format as the web app

### Local Backup (Automatic)
- Saves to `checkins_backup.json`
- Works even if Google Sheets is unavailable
- Can be imported later

---

## 🎨 How It Looks

1. **Welcome Screen**
   - Enter your name
   - Select morning or evening check-in
   - Click "Start Check-in"

2. **Question Screens**
   - One question at a time
   - Large text area for answers
   - Progress indicator
   - Back button to edit previous answers

3. **Completion Screen**
   - Success confirmation
   - Summary of your responses
   - Options to start new check-in or exit

---

## 🆘 Troubleshooting

### "credentials.json not found"
- Make sure `credentials.json` is in the same folder as the executable
- Check the filename is exactly `credentials.json`

### "config.json not found"
- Copy `config_template.json` to `config.json`
- Make sure it's in the same folder

### "Could not connect to Google Sheets"
- Check your internet connection
- Verify the service account has access to the spreadsheet
- Data will save locally as backup

### App won't start
- Make sure you have Python 3.8+ installed
- Install dependencies: `pip install -r requirements.txt`
- Check for error messages in terminal

---

## ✅ Advantages Over Web App

- ✅ No deployment needed
- ✅ Works offline (saves locally)
- ✅ Faster - runs natively
- ✅ No browser required
- ✅ Easy to distribute
- ✅ One-time setup
- ✅ More reliable

---

## 🎯 Next Steps

1. Test the Python version first
2. Build an executable for your OS
3. Package with credentials and config
4. Share with your team
5. Everyone can use it immediately!

---

**Made with ❤️ for efficient team collaboration!** 🚀

