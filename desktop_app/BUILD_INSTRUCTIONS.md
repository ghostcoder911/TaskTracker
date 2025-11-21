# 🚀 Building Executables for Task Tracker

## For Linux/Ubuntu (You're on Linux now!)

### Build the Linux Executable:

```bash
cd /home/neeraj/Documents/UWR/UWR_Tools/TaskTracker/desktop_app
./build_linux.sh
```

**This will create:** `dist/TaskTracker` (Linux executable)

---

## For Windows

You need to build on a Windows machine or use Wine/Virtual Machine.

### Option 1: Build on Windows Machine

1. Copy the entire `desktop_app` folder to a Windows computer
2. Install Python 3.8+ on Windows
3. Open Command Prompt in the folder
4. Run:
   ```cmd
   build_windows.bat
   ```

**This will create:** `dist\TaskTracker.exe` (Windows executable)

### Option 2: Cross-compile from Linux (Advanced)

You can use Wine and PyInstaller, but it's more complex. Better to build on actual Windows.

---

## 📦 Distribution Package

After building, create a distribution folder:

### For Linux:
```
TaskTracker-Linux/
├── TaskTracker (executable)
├── credentials.json
├── config.json
└── README.txt
```

### For Windows:
```
TaskTracker-Windows/
├── TaskTracker.exe (executable)
├── credentials.json
├── config.json
└── README.txt
```

---

## 🎯 Quick Start for Your Team

### Linux Users:
1. Extract the zip file
2. Open terminal in that folder
3. Run: `chmod +x TaskTracker`
4. Run: `./TaskTracker`

### Windows Users:
1. Extract the zip file
2. Double-click `TaskTracker.exe`
3. Done!

---

## ⚠️ Important Notes

### File Size:
- Linux executable: ~50-80 MB
- Windows executable: ~30-50 MB
- This is normal! It includes Python and all dependencies

### First Run:
- May take 5-10 seconds to start (unpacking)
- Subsequent runs are faster

### Antivirus:
- Windows might show a warning (unsigned executable)
- This is normal for PyInstaller apps
- Tell users to "Run Anyway" or whitelist it

### Dependencies Included:
- Python runtime
- tkinter GUI library
- Google Sheets API libraries
- All required modules

---

## 🔧 Troubleshooting Build Issues

### "PyInstaller not found"
```bash
pip install pyinstaller
```

### "Module not found during build"
Make sure you're in the `desktop_app` folder and all dependencies are installed:
```bash
cd desktop_app
pip install -r requirements.txt
pip install pyinstaller
```

### Build fails on Linux
Make sure you have these system packages:
```bash
sudo apt-get install python3-tk
sudo apt-get install python3-dev
```

### Build fails on Windows
Make sure Python is in your PATH and you have Visual C++ redistributables installed.

---

## 📝 Creating README.txt for Distribution

Create this file for your team:

```txt
Task Tracker - Team Check-ins
==============================

Quick Start:
1. Double-click the TaskTracker file/icon
2. Enter your name
3. Select morning or evening check-in
4. Answer the questions
5. Done! Data is saved to Google Sheets

Requirements:
- Internet connection (for Google Sheets sync)
- The credentials.json and config.json must be in the same folder

Support:
- If you get errors, check your internet connection
- Data is always backed up locally to checkins_backup.json
- Contact [Your Name] for help

Enjoy! 🚀
```

---

## ✅ Testing Your Executable

Before distributing:

1. **Test on same OS:**
   - Run the executable
   - Complete a full check-in
   - Verify data appears in Google Sheets

2. **Test on different machine:**
   - Copy to another computer (same OS)
   - Run without Python installed
   - Should work standalone!

3. **Check file permissions:**
   - Linux: Make sure executable bit is set
   - Windows: Test with antivirus enabled

---

## 🎁 Ready-to-Share Package

Create two ZIP files:

**TaskTracker-Linux.zip:**
- TaskTracker (executable)
- credentials.json
- config.json
- README.txt
- run.sh (script: `./TaskTracker`)

**TaskTracker-Windows.zip:**
- TaskTracker.exe
- credentials.json
- config.json
- README.txt

Upload to Google Drive or internal file share and share the link with your team!

---

**Good luck with distribution!** 🚀

