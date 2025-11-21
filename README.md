# 📋 Task Tracker - Engineering Team Check-ins

A modern, chat-based task tracking system for engineering teams to do daily check-ins. Team members can log their start-of-day and end-of-day updates through an intuitive chat interface, with all responses automatically saved to Google Sheets for easy review.

## ✨ Features

- 🎨 **Beautiful Chat Interface** - Modern, responsive UI that feels natural
- 🌅 **Start-of-Day Check-ins** - Track energy levels, priorities, and blockers
- 🌇 **End-of-Day Check-outs** - Document wins, learnings, and challenges
- 📊 **Google Sheets Integration** - Automatic data logging organized by date
- 🚀 **Easy Deployment** - One-click deploy to Render
- 💾 **Fallback Storage** - Local JSON backup if Google Sheets is unavailable
- 📱 **Mobile Friendly** - Works seamlessly on all devices

## 🏗️ Architecture

### Backend (Python/Flask)
- RESTful API for chat interactions
- Session management for active conversations
- Google Sheets API integration
- Fallback to local JSON storage

### Frontend (React)
- Modern chat interface with smooth animations
- Real-time progress tracking
- Responsive design
- Clean, intuitive UX

## 📋 Questions Asked

### 🌅 Start-of-Day Check-In
0. **Energy Check**: What's your energy drink or vibe this morning?
1. **Progress**: What key tasks did you complete yesterday?
2. **Today's Focus**: What are the top 1–3 priorities you're focusing on today?
3. **Blockers**: Anything slowing you down or you need help with?
4. **State of Mind**: One word for how you're feeling as you start the day?

### 🌇 End-of-Day Check-Out
1. **Wins**: What did you accomplish today (big or small)?
2. **Learnings**: Anything new you learned or discovered?
3. **Stuck Points**: Any challenges you faced today?
4. **Tomorrow Prep**: What will be your focus tomorrow?
5. **Mood Check**: How are you ending the day?

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- Node.js 16+
- Google Cloud account (for Google Sheets integration)

### Local Development

#### 1. Clone the repository
```bash
git clone <your-repo-url>
cd TaskTracker
```

#### 2. Set up the Backend

```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Copy environment variables
cp .env.example .env

# Edit .env and add your Google Sheets credentials (see setup below)

# Run the backend
python app.py
```

Backend will start on `http://localhost:5000`

#### 3. Set up the Frontend

```bash
# In a new terminal, navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Copy environment variables
cp .env.example .env

# Run the frontend
npm start
```

Frontend will start on `http://localhost:3000`

## 🔑 Google Sheets Setup

### Step 1: Create a Google Cloud Project

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select an existing one
3. Enable the **Google Sheets API**:
   - Go to "APIs & Services" → "Library"
   - Search for "Google Sheets API"
   - Click "Enable"

### Step 2: Create Service Account

1. Go to "APIs & Services" → "Credentials"
2. Click "Create Credentials" → "Service Account"
3. Fill in the service account details
4. Click "Create and Continue"
5. Skip the optional steps and click "Done"

### Step 3: Create and Download Credentials

1. Click on the service account you just created
2. Go to the "Keys" tab
3. Click "Add Key" → "Create new key"
4. Select "JSON" format
5. Download the JSON file

### Step 4: Create Google Spreadsheet

1. Go to [Google Sheets](https://sheets.google.com/)
2. Create a new spreadsheet
3. Name it "Team Task Tracker" (or any name you prefer)
4. Copy the **Spreadsheet ID** from the URL:
   ```
   https://docs.google.com/spreadsheets/d/SPREADSHEET_ID_HERE/edit
   ```
5. Share the spreadsheet with the service account email:
   - Click "Share" button
   - Add the service account email (found in the JSON file: `client_email`)
   - Give it "Editor" access

### Step 5: Configure Environment Variables

1. Open the downloaded JSON credentials file
2. Copy its entire content (it should be one long JSON string)
3. In your `backend/.env` file, paste it as the value for `GOOGLE_SHEETS_CREDENTIALS`
4. Add your `SPREADSHEET_ID` from Step 4

Example:
```env
GOOGLE_SHEETS_CREDENTIALS={"type":"service_account","project_id":"your-project",...}
SPREADSHEET_ID=1abc123xyz456789
```

## 🌐 Deploying to Render

### Option 1: Using render.yaml (Recommended)

1. Push your code to GitHub
2. Go to [Render Dashboard](https://dashboard.render.com/)
3. Click "New" → "Blueprint"
4. Connect your GitHub repository
5. Render will automatically detect `render.yaml`
6. Set the environment variables in Render dashboard:
   - `GOOGLE_SHEETS_CREDENTIALS`
   - `SPREADSHEET_ID`
7. Deploy!

### Option 2: Manual Setup

#### Deploy Backend

1. Go to Render Dashboard → "New" → "Web Service"
2. Connect your repository
3. Configure:
   - **Name**: tasktracker-backend
   - **Root Directory**: backend
   - **Environment**: Python
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
4. Add environment variables:
   - `GOOGLE_SHEETS_CREDENTIALS`
   - `SPREADSHEET_ID`
5. Deploy!

#### Deploy Frontend

1. Go to Render Dashboard → "New" → "Static Site"
2. Connect your repository
3. Configure:
   - **Name**: tasktracker-frontend
   - **Root Directory**: frontend
   - **Build Command**: `npm install && npm run build`
   - **Publish Directory**: build
4. Add environment variable:
   - `REACT_APP_API_URL`: Your backend URL (e.g., `https://tasktracker-backend.onrender.com/api`)
5. Deploy!

## 📊 Viewing the Data

All check-in responses are saved to your Google Spreadsheet:

- Each date gets its own worksheet (sheet tab)
- Data is organized with timestamps, names, and all responses
- Easy to filter, sort, and analyze
- Can be exported to other formats (Excel, CSV, etc.)

### Spreadsheet Structure

| Timestamp | Name | Type | Energy Check | Progress | Today's Focus | ... |
|-----------|------|------|--------------|----------|---------------|-----|
| 09:15:00  | John | 🌅 Morning Check-in | Coffee ☕ | Fixed bug #123 | Work on feature X | ... |
| 17:30:00  | Jane | 🌇 Evening Check-out | - | - | - | Completed feature Y |

## 🛠️ Technology Stack

### Backend
- **Flask** - Lightweight Python web framework
- **Flask-CORS** - Cross-origin resource sharing
- **gspread** - Google Sheets Python API
- **google-auth** - Google authentication
- **gunicorn** - Production WSGI server

### Frontend
- **React** - UI library
- **Axios** - HTTP client
- **CSS3** - Modern styling with animations

### Deployment
- **Render** - Cloud hosting platform
- **Google Sheets API** - Data storage

## 🔧 Configuration

### Backend Environment Variables

```env
GOOGLE_SHEETS_CREDENTIALS=<json-credentials>
SPREADSHEET_ID=<your-spreadsheet-id>
PORT=5000
FLASK_ENV=production
```

### Frontend Environment Variables

```env
REACT_APP_API_URL=<backend-api-url>
```

## 📝 Usage

1. **Open the application** in your browser
2. **Enter your name** and select check-in type (Morning/Evening)
3. **Answer the questions** as they appear in the chat
4. **Submit responses** - they're automatically saved to Google Sheets
5. **Start a new check-in** or close the browser

## 🤝 Contributing

Feel free to submit issues and enhancement requests!

## 📄 License

This project is open source and available under the MIT License.

## 🆘 Troubleshooting

### Google Sheets Not Working
- Check if the service account email has Editor access to the spreadsheet
- Verify the `GOOGLE_SHEETS_CREDENTIALS` is properly formatted JSON
- Check if Google Sheets API is enabled in your Google Cloud project
- Fallback data will be saved to `fallback_data.json`

### Backend Connection Issues
- Verify the `REACT_APP_API_URL` in frontend `.env`
- Check if backend is running and accessible
- Look for CORS errors in browser console

### Deployment Issues
- Ensure all environment variables are set in Render
- Check build logs for errors
- Verify the correct Python/Node versions

## 💡 Tips

- Keep responses concise for better tracking
- Be honest about blockers to get help faster
- Review the Google Sheet weekly to spot patterns
- Use the data to improve team processes

## 🎯 Future Enhancements

- [ ] Email notifications for missed check-ins
- [ ] Analytics dashboard with charts
- [ ] Slack integration
- [ ] Team summary reports
- [ ] Customizable questions
- [ ] Multi-team support

---

Made with ❤️ for engineering teams who want to stay aligned and move faster together! 🚀

