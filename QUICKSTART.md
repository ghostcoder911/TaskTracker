# ⚡ Quick Start Guide

Get Task Tracker running in 5 minutes!

## Prerequisites

- Python 3.11+
- Node.js 16+
- Google Cloud account (free)

## Step 1: Clone and Setup

```bash
cd TaskTracker
```

## Step 2: Install Dependencies

### Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
cd ..
```

### Frontend
```bash
cd frontend
npm install
cd ..
```

## Step 3: Configure Google Sheets (5 minutes)

### A. Create Google Cloud Project
1. Visit: https://console.cloud.google.com/
2. Create new project: "TaskTracker"
3. Enable "Google Sheets API"

### B. Create Service Account
1. Go to: APIs & Services > Credentials
2. Create Credentials > Service Account
3. Download JSON key file

### C. Create Spreadsheet
1. Go to: https://sheets.google.com/
2. Create new spreadsheet: "Team Task Tracker"
3. Share with service account email (from JSON)
4. Copy Spreadsheet ID from URL

### D. Configure Environment
1. Create `backend/.env`:
```env
GOOGLE_SHEETS_CREDENTIALS={"type":"service_account",...}
SPREADSHEET_ID=your_spreadsheet_id_here
PORT=5000
```

2. Create `frontend/.env`:
```env
REACT_APP_API_URL=http://localhost:5000/api
```

> 💡 Tip: See `backend/config_template.txt` for detailed format

## Step 4: Run the Application

### Option A: Use Startup Script (Easiest)

**Linux/Mac:**
```bash
chmod +x start_local.sh
./start_local.sh
```

**Windows:**
```bash
start_local.bat
```

### Option B: Manual Start

**Terminal 1 - Backend:**
```bash
cd backend
source venv/bin/activate  # Windows: venv\Scripts\activate
python app.py
```

**Terminal 2 - Frontend:**
```bash
cd frontend
npm start
```

## Step 5: Test It Out! 🎉

1. Open: http://localhost:3000
2. Enter your name
3. Select "Start of Day"
4. Answer the questions
5. Check your Google Spreadsheet!

## Troubleshooting

### Google Sheets Error?
- Verify service account has Editor access
- Check if API is enabled
- Ensure JSON credentials are valid
- Data will save to `fallback_data.json` if Sheets fails

### Connection Error?
- Check backend is running on port 5000
- Verify `REACT_APP_API_URL` in frontend/.env
- Try restarting both servers

### Dependencies Error?
```bash
# Backend
cd backend
pip install -r requirements.txt

# Frontend
cd frontend
rm -rf node_modules
npm install
```

## Next Steps

- ✅ Test with your team
- 📖 Read [SETUP.md](SETUP.md) for detailed configuration
- 🚀 Deploy with [DEPLOYMENT.md](DEPLOYMENT.md)
- 📊 Check your Google Sheet for collected data

## Quick Tips

- Keep responses concise for better tracking
- Use the same Google Sheet for all team members
- Each date gets its own worksheet automatically
- Can switch between morning and evening check-ins anytime

---

Need more help? Check out:
- [SETUP.md](SETUP.md) - Detailed setup instructions
- [README.md](README.md) - Full documentation
- [DEPLOYMENT.md](DEPLOYMENT.md) - Deploy to Render

Happy tracking! 🚀

