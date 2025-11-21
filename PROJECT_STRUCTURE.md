# 📁 Project Structure

Complete overview of the Task Tracker application structure.

## Directory Tree

```
TaskTracker/
├── backend/                      # Flask backend application
│   ├── app.py                   # Main Flask API server
│   ├── chatbot.py               # Chatbot conversation logic
│   ├── sheets_api.py            # Google Sheets integration
│   ├── requirements.txt         # Python dependencies
│   ├── runtime.txt              # Python version for deployment
│   ├── Procfile                 # Render deployment config
│   └── config_template.txt      # Environment variables template
│
├── frontend/                     # React frontend application
│   ├── package.json             # Node.js dependencies
│   ├── config_template.txt      # Environment variables template
│   ├── public/
│   │   └── index.html          # HTML template
│   └── src/
│       ├── index.js            # React entry point
│       ├── index.css           # Global styles
│       ├── App.js              # Main App component
│       ├── App.css             # App styles
│       └── components/
│           ├── WelcomeScreen.js      # Initial screen
│           ├── WelcomeScreen.css     # Welcome screen styles
│           ├── ChatInterface.js      # Chat UI component
│           └── ChatInterface.css     # Chat UI styles
│
├── README.md                     # Main documentation
├── QUICKSTART.md                 # 5-minute setup guide
├── SETUP.md                      # Detailed setup instructions
├── DEPLOYMENT.md                 # Render deployment guide
├── PROJECT_STRUCTURE.md          # This file
│
├── render.yaml                   # Render blueprint configuration
├── .gitignore                    # Git ignore rules
├── start_local.sh               # Linux/Mac startup script
└── start_local.bat              # Windows startup script
```

## File Descriptions

### Backend Files

#### `app.py`
- Main Flask application server
- RESTful API endpoints for chat interactions
- Session management for active conversations
- Health check endpoint for monitoring

**Key Endpoints:**
- `GET /api/health` - Health check
- `POST /api/start-session` - Initialize new check-in
- `POST /api/send-message` - Process user responses
- `POST /api/cancel-session` - Cancel active session

#### `chatbot.py`
- ChatBot class implementation
- Manages conversation flow
- Stores questions for morning/evening check-ins
- Tracks progress and responses

**Key Methods:**
- `get_next_question()` - Returns next question
- `process_answer()` - Stores user's answer
- `is_complete()` - Checks if all questions answered
- `get_responses()` - Returns all collected data

#### `sheets_api.py`
- Google Sheets API integration
- Automatic worksheet creation per date
- Fallback to local JSON storage
- Data formatting and saving

**Key Methods:**
- `save_checkin()` - Main save method
- `_save_to_sheets()` - Save to Google Sheets
- `_save_to_fallback()` - Save to local JSON

#### `requirements.txt`
Python packages:
- `Flask` - Web framework
- `flask-cors` - CORS support
- `gspread` - Google Sheets API
- `google-auth` - Authentication
- `gunicorn` - Production server

### Frontend Files

#### `App.js`
- Main React component
- Manages application state
- Routes between Welcome and Chat screens

#### `WelcomeScreen.js`
- Initial user interface
- Name input form
- Check-in type selection (Morning/Evening)
- Session initialization

#### `ChatInterface.js`
- Chat UI component
- Message display and handling
- Progress tracking
- Real-time updates

### Configuration Files

#### `render.yaml`
Render deployment blueprint:
- Backend web service config
- Frontend static site config
- Environment variables
- Build and start commands

#### `.gitignore`
Excludes from version control:
- Python virtual environments
- Node modules
- Environment variables
- Build artifacts
- Credentials

### Documentation Files

#### `README.md`
- Project overview
- Features list
- Architecture description
- Setup instructions
- Deployment guide

#### `QUICKSTART.md`
- Fast 5-minute setup
- Minimal instructions
- Quick troubleshooting

#### `SETUP.md`
- Detailed setup guide
- Google Sheets configuration
- Step-by-step instructions
- Common issues and solutions

#### `DEPLOYMENT.md`
- Render deployment guide
- Environment configuration
- Post-deployment testing
- Monitoring and logs

#### `PROJECT_STRUCTURE.md`
- Complete file structure
- File descriptions
- Data flow explanation

### Utility Scripts

#### `start_local.sh` (Linux/Mac)
- Automated local development startup
- Checks for .env files
- Starts backend and frontend
- Creates virtual environment if needed

#### `start_local.bat` (Windows)
- Windows version of startup script
- Same functionality as bash script

## Data Flow

```
User Browser
    ↓
[React Frontend]
    ↓ (HTTP REST API)
[Flask Backend]
    ↓
[ChatBot Logic]
    ↓
[Google Sheets API]
    ↓
[Google Spreadsheet]
```

### Detailed Flow

1. **User Opens App**
   - Frontend loads `WelcomeScreen`
   - User enters name and selects check-in type

2. **Session Start**
   - Frontend calls `POST /api/start-session`
   - Backend creates ChatBot instance
   - Returns session ID and first question

3. **Conversation**
   - User answers question in chat
   - Frontend calls `POST /api/send-message`
   - Backend processes answer, returns next question
   - Repeat until all questions answered

4. **Completion**
   - Backend saves to Google Sheets
   - Creates worksheet if needed (named by date)
   - Fallback to JSON if Sheets unavailable
   - Returns completion message

## Environment Variables

### Backend (.env)

```env
GOOGLE_SHEETS_CREDENTIALS=<json-credentials>
SPREADSHEET_ID=<spreadsheet-id>
PORT=5000
FLASK_ENV=production
```

### Frontend (.env)

```env
REACT_APP_API_URL=<backend-url>
```

## Dependencies

### Backend (Python)
- Flask 3.0.0 - Web framework
- flask-cors 4.0.0 - CORS handling
- gspread 5.12.0 - Google Sheets API
- google-auth 2.23.4 - Authentication
- gunicorn 21.2.0 - WSGI server

### Frontend (JavaScript)
- react 18.2.0 - UI library
- react-dom 18.2.0 - React DOM renderer
- react-scripts 5.0.1 - Build tools
- axios 1.6.0 - HTTP client

## Build Process

### Backend Build
1. Install Python dependencies
2. Set environment variables
3. Start gunicorn server

### Frontend Build
1. Install Node.js dependencies
2. Set environment variables
3. Run React build (creates optimized bundle)
4. Serve static files

## API Reference

### Health Check
```http
GET /api/health
```

Response:
```json
{
  "status": "healthy",
  "timestamp": "2025-11-21T12:00:00.000000"
}
```

### Start Session
```http
POST /api/start-session
Content-Type: application/json

{
  "name": "John Doe",
  "check_type": "start"
}
```

Response:
```json
{
  "session_id": "john_doe_1732190400.123",
  "message": "Good morning, John Doe! 🌅 Let's do your start-of-day check-in.",
  "progress": {"current": 0, "total": 5}
}
```

### Send Message
```http
POST /api/send-message
Content-Type: application/json

{
  "session_id": "john_doe_1732190400.123",
  "message": "Coffee and ready to code!"
}
```

Response:
```json
{
  "message": "1️⃣ Progress: What key tasks did you complete yesterday? 📋",
  "completed": false,
  "progress": {"current": 1, "total": 5}
}
```

## Storage Format

### Google Sheets Structure

**Worksheet Name:** YYYY-MM-DD (e.g., "2025-11-21")

**Columns:**
| Timestamp | Name | Type | Energy Check | Progress | Today's Focus | Blockers | State of Mind |
|-----------|------|------|--------------|----------|---------------|----------|---------------|
| 09:15:00 | John | 🌅 Morning | Coffee ☕ | Fixed bug | Feature X | None | Energized |

### Fallback JSON Structure

```json
[
  {
    "user_name": "John Doe",
    "check_type": "start",
    "timestamp": "2025-11-21T09:15:00.000000",
    "date": "2025-11-21",
    "time": "09:15:00",
    "responses": {
      "energy_check": {
        "label": "Energy Check",
        "answer": "Coffee ☕",
        "timestamp": "2025-11-21T09:15:10.000000"
      },
      // ... more responses
    }
  }
]
```

## Security Considerations

1. **Credentials**
   - Never commit .env files
   - Use environment variables for secrets
   - Rotate service account keys regularly

2. **API**
   - CORS configured for frontend origin
   - Session IDs are unique and temporary
   - No authentication required (add if needed)

3. **Data**
   - Google Sheets provides access control
   - Service account has minimal permissions
   - Data is not publicly accessible

## Performance

### Backend
- Lightweight Flask server
- In-memory session storage
- Quick response times (<100ms)

### Frontend
- Single-page application
- Minimal bundle size
- Smooth animations
- Mobile-optimized

### Scalability
- Backend can handle multiple concurrent users
- Google Sheets has rate limits (100 requests/100 seconds)
- Consider caching for high-traffic scenarios

## Testing

### Local Testing
```bash
# Test backend
curl http://localhost:5000/api/health

# Test complete flow
# 1. Open http://localhost:3000
# 2. Complete a check-in
# 3. Verify in Google Sheets
```

### Production Testing
```bash
# Test deployed backend
curl https://your-app.onrender.com/api/health

# Test frontend
# Visit your Render URL
```

## Maintenance

### Regular Tasks
- Monitor Google Sheets API quota
- Check Render logs for errors
- Review fallback_data.json for failed saves
- Update dependencies periodically

### Backup
- Google Sheets auto-saves and provides history
- Export spreadsheet regularly as backup
- Download fallback_data.json if using fallback

## Future Enhancements

Potential features to add:
1. User authentication
2. Email notifications
3. Analytics dashboard
4. Slack integration
5. Custom questions per team
6. Multi-team support
7. Response templates
8. Search and filtering
9. Export to PDF
10. Weekly/monthly reports

---

This project structure is designed to be:
- ✅ Simple to understand
- ✅ Easy to deploy
- ✅ Maintainable
- ✅ Scalable
- ✅ Well-documented

Happy coding! 🚀

