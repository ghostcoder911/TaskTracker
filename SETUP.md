# 🔧 Setup Guide

This guide will help you set up the Task Tracker application step by step.

## Environment Variables Setup

### Backend Environment Variables

Create a file `backend/.env` with the following content:

```env
# Google Sheets Configuration
# Paste your entire service account JSON credentials as a single line
GOOGLE_SHEETS_CREDENTIALS={"type":"service_account","project_id":"your-project","private_key_id":"...","private_key":"...","client_email":"...","client_id":"..."}

# Your Google Spreadsheet ID (from the URL)
SPREADSHEET_ID=your_spreadsheet_id_here

# Server Configuration
PORT=5000
FLASK_ENV=production
```

### Frontend Environment Variables

Create a file `frontend/.env` with the following content:

For local development:
```env
REACT_APP_API_URL=http://localhost:5000/api
```

For production:
```env
REACT_APP_API_URL=https://your-backend-url.onrender.com/api
```

## Google Sheets Setup (Detailed)

### 1. Create Google Cloud Project

1. Visit https://console.cloud.google.com/
2. Click on the project dropdown at the top
3. Click "New Project"
4. Enter project name (e.g., "TaskTracker")
5. Click "Create"

### 2. Enable Google Sheets API

1. In the Google Cloud Console, go to "APIs & Services" > "Library"
2. Search for "Google Sheets API"
3. Click on it and click "Enable"
4. Wait for it to be enabled

### 3. Create Service Account

1. Go to "APIs & Services" > "Credentials"
2. Click "Create Credentials" button
3. Select "Service Account"
4. Fill in details:
   - Service account name: `tasktracker-service`
   - Service account ID: (auto-generated)
   - Description: "Service account for Task Tracker app"
5. Click "Create and Continue"
6. Skip the optional permissions (click "Continue")
7. Skip the access grants (click "Done")

### 4. Download Credentials

1. Find your service account in the list
2. Click on it to open details
3. Go to the "Keys" tab
4. Click "Add Key" > "Create new key"
5. Select "JSON" format
6. Click "Create"
7. A JSON file will download - **keep this safe!**

### 5. Prepare Credentials for Environment Variable

The downloaded JSON file looks like this:

```json
{
  "type": "service_account",
  "project_id": "tasktracker-123456",
  "private_key_id": "abc123...",
  "private_key": "-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----\n",
  "client_email": "tasktracker-service@tasktracker-123456.iam.gserviceaccount.com",
  "client_id": "123456789",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "..."
}
```

**Important**: You need to convert this to a single line for the environment variable.

You can use an online JSON minifier or just remove all newlines and extra spaces.

### 6. Create and Share Google Spreadsheet

1. Go to https://sheets.google.com/
2. Click the "+" button to create a new spreadsheet
3. Name it "Team Task Tracker"
4. Copy the Spreadsheet ID from URL:
   ```
   https://docs.google.com/spreadsheets/d/SPREADSHEET_ID_IS_HERE/edit
   ```
5. Click the "Share" button (top right)
6. Paste the service account email (from the JSON: `client_email` field)
7. Give it "Editor" permission
8. Uncheck "Notify people"
9. Click "Share"

### 7. Update Environment Variables

1. Open `backend/.env`
2. Paste the minified JSON as the value for `GOOGLE_SHEETS_CREDENTIALS`
3. Paste the Spreadsheet ID as the value for `SPREADSHEET_ID`

Example:
```env
GOOGLE_SHEETS_CREDENTIALS={"type":"service_account","project_id":"tasktracker-123456","private_key_id":"abc123","private_key":"-----BEGIN PRIVATE KEY-----\nXXXXX\n-----END PRIVATE KEY-----\n","client_email":"tasktracker-service@tasktracker-123456.iam.gserviceaccount.com","client_id":"123456789","auth_uri":"https://accounts.google.com/o/oauth2/auth","token_uri":"https://oauth2.googleapis.com/token","auth_provider_x509_cert_url":"https://www.googleapis.com/oauth2/v1/certs","client_x509_cert_url":"..."}
SPREADSHEET_ID=1abc123def456ghi789jkl
```

## Local Testing

### Test Backend

```bash
cd backend
python app.py
```

Visit http://localhost:5000/api/health - you should see:
```json
{"status":"healthy","timestamp":"..."}
```

### Test Frontend

```bash
cd frontend
npm start
```

Visit http://localhost:3000 - you should see the welcome screen.

### Test Complete Flow

1. Enter your name
2. Select "Start of Day"
3. Click "Start Check-in"
4. Answer all questions
5. Check your Google Spreadsheet - you should see a new sheet with today's date and your responses!

## Common Issues

### Issue: "Invalid session" error

**Solution**: The backend server restarted and lost session data. Just refresh the page and start a new check-in.

### Issue: Google Sheets credentials error

**Solutions**:
- Make sure the JSON is properly formatted (valid JSON)
- Check that the service account has Editor access to the spreadsheet
- Verify Google Sheets API is enabled
- Check if credentials are properly set in environment variables

### Issue: CORS errors in browser console

**Solution**: 
- Make sure backend is running on port 5000
- Check frontend `.env` has correct `REACT_APP_API_URL`
- Restart both frontend and backend

### Issue: "Module not found" errors

**Backend Solution**:
```bash
cd backend
pip install -r requirements.txt
```

**Frontend Solution**:
```bash
cd frontend
rm -rf node_modules package-lock.json
npm install
```

### Issue: Spreadsheet not updating

**Solution**:
- Check backend console for errors
- Verify service account email has Editor access
- Check if data is being saved to `fallback_data.json` (means Google Sheets connection failed)

## Deployment Checklist

Before deploying to Render:

- [ ] Code is pushed to GitHub
- [ ] `render.yaml` is configured
- [ ] Backend environment variables are ready:
  - [ ] `GOOGLE_SHEETS_CREDENTIALS`
  - [ ] `SPREADSHEET_ID`
- [ ] Frontend environment variable is ready:
  - [ ] `REACT_APP_API_URL`
- [ ] Google Spreadsheet is created and shared with service account
- [ ] Google Sheets API is enabled

## Testing Deployment

After deploying:

1. Visit your frontend URL
2. Complete a check-in
3. Verify data appears in Google Sheets
4. Test both morning and evening check-ins
5. Test with multiple team members

## Support

If you encounter issues not covered here, check:
1. Backend logs in Render dashboard
2. Frontend build logs in Render dashboard
3. Browser console for frontend errors
4. Google Cloud Console for API quota issues

Happy tracking! 🚀

