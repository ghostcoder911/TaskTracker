# ⚡ Quick Deploy Reference Card

Your code is ready! Here's everything you need at a glance.

---

## 🔐 Step 1: Push to GitHub (2 min)

```bash
cd /home/neeraj/Documents/UWR/UWR_Tools/TaskTracker
git push -u origin main
```

**Verify**: https://github.com/ghostcoder911/TaskTracker

---

## 📊 Step 2: Google Sheets Setup (10 min)

### Quick Links:
1. **Cloud Console**: https://console.cloud.google.com/
2. **Enable API**: Search "Google Sheets API" → Enable
3. **Service Account**: APIs & Services → Credentials → Create Credentials → Service Account
4. **Download JSON**: Service Account → Keys → Add Key → JSON
5. **Create Sheet**: https://sheets.google.com/ → New Spreadsheet
6. **Copy ID from URL**: `docs.google.com/spreadsheets/d/COPY_THIS_ID/edit`

### What to Save:
- ✅ JSON credentials file (entire content)
- ✅ Spreadsheet ID
- ✅ Service account email (`xxx@xxx.iam.gserviceaccount.com`)

### Don't Forget:
- **Share** spreadsheet with service account email (Editor permission)

---

## 🚀 Step 3: Deploy Backend to Render (8 min)

**Go to**: https://dashboard.render.com/

### Settings:

| Setting | Value |
|---------|-------|
| **Type** | Web Service |
| **Repo** | TaskTracker |
| **Name** | tasktracker-backend |
| **Root Directory** | `backend` |
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `gunicorn app:app` |

### Environment Variables (IMPORTANT!):

```
GOOGLE_SHEETS_CREDENTIALS = {paste entire JSON here as one line}
SPREADSHEET_ID = your_spreadsheet_id_here
```

### Test:
```
https://tasktracker-backend.onrender.com/api/health
```

**Save your backend URL!** 📝

---

## 🎨 Step 4: Deploy Frontend to Render (8 min)

**Dashboard**: https://dashboard.render.com/ → New → Static Site

### Settings:

| Setting | Value |
|---------|-------|
| **Type** | Static Site |
| **Repo** | TaskTracker |
| **Name** | tasktracker-frontend |
| **Root Directory** | `frontend` |
| **Build Command** | `npm install && npm run build` |
| **Publish Directory** | `build` |

### Environment Variable:

```
REACT_APP_API_URL = https://your-backend-url.onrender.com/api
```

⚠️ Replace with YOUR backend URL from Step 3!

---

## ✅ Step 5: Test (2 min)

1. **Visit**: `https://tasktracker-frontend.onrender.com`
2. **Enter name**: Test User
3. **Select**: Start of Day
4. **Complete** all 5 questions
5. **Check** Google Sheets for your data

**✨ If data appears in Sheets = SUCCESS!**

---

## 📱 Share with Team

```
Team Task Tracker: https://tasktracker-frontend.onrender.com

Use this for daily check-ins:
🌅 Morning: Start of Day check-in
🌇 Evening: End of Day check-out
```

---

## 🆘 Quick Troubleshooting

### Backend not working?
```bash
# Check environment variables in Render
# Verify JSON is valid (use jsonlint.com)
# Check service account has Sheet access
```

### Frontend can't connect?
```bash
# Verify REACT_APP_API_URL is correct
# Make sure it ends with /api
# Redeploy frontend after changing
```

### Data not in Sheets?
```bash
# Share spreadsheet with service account
# Check Sheets API is enabled
# Verify spreadsheet ID is correct
# Check backend logs in Render
```

---

## 📋 Checklist

- [ ] Code pushed to GitHub
- [ ] Google Cloud project created
- [ ] Sheets API enabled
- [ ] Service account created
- [ ] JSON downloaded
- [ ] Spreadsheet created & shared
- [ ] Backend deployed to Render
- [ ] Backend env vars set
- [ ] Backend health check passes
- [ ] Frontend deployed to Render
- [ ] Frontend API URL set
- [ ] End-to-end test complete
- [ ] Data in Google Sheets ✅
- [ ] URL shared with team

---

## 🎯 Important URLs

| Service | URL | Purpose |
|---------|-----|---------|
| **GitHub** | https://github.com/ghostcoder911/TaskTracker | Code repository |
| **Google Cloud** | https://console.cloud.google.com/ | Service account setup |
| **Google Sheets** | https://sheets.google.com/ | Data storage |
| **Render** | https://dashboard.render.com/ | Hosting platform |
| **Backend** | `your-backend.onrender.com` | API server |
| **Frontend** | `your-frontend.onrender.com` | User interface |

---

## 💡 Pro Tips

1. **Free tier**: Backend sleeps after 15 min → First request slow
2. **Paid tier**: $7/mo → No sleep, faster response
3. **Auto-deploy**: Enable in Render → Deploy on every push
4. **Monitor**: Check Render logs regularly
5. **Backup**: Export Google Sheet weekly

---

## 🎉 That's It!

**Total time**: ~30 minutes  
**Total cost**: $0/month (or $7 for always-on backend)  
**Total awesomeness**: 💯

**Need detailed help?** See `COMPLETE_DEPLOYMENT_GUIDE.md`

🚀 **Let's deploy!**

