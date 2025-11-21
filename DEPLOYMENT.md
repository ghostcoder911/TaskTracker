# 🚀 Deployment Guide for Render

This guide walks you through deploying your Task Tracker application to Render.

## Prerequisites

- GitHub account
- Render account (free tier is fine)
- Google Sheets set up (see SETUP.md)
- Code pushed to GitHub repository

## Option 1: Deploy with Blueprint (Easiest)

### Step 1: Prepare Your Repository

1. Make sure all code is committed and pushed to GitHub:
```bash
git add .
git commit -m "Ready for deployment"
git push origin main
```

2. Ensure `render.yaml` is in the root of your repository

### Step 2: Create Blueprint in Render

1. Go to [Render Dashboard](https://dashboard.render.com/)
2. Click "New" button (top right)
3. Select "Blueprint"
4. Click "Connect GitHub" (if not already connected)
5. Select your repository
6. Render will detect `render.yaml` automatically

### Step 3: Set Environment Variables

Before deploying, you need to set environment variables:

#### For Backend Service:

1. Find "tasktracker-backend" in the blueprint
2. Add environment variables:
   - **Key**: `GOOGLE_SHEETS_CREDENTIALS`
     - **Value**: Your complete service account JSON (as single line)
   - **Key**: `SPREADSHEET_ID`
     - **Value**: Your Google Spreadsheet ID

#### For Frontend Service:

1. Find "tasktracker-frontend" in the blueprint
2. Environment variable should be auto-configured from `render.yaml`
3. Verify `REACT_APP_API_URL` points to your backend URL

### Step 4: Deploy

1. Click "Apply" to create both services
2. Wait for deployment (5-10 minutes for first deploy)
3. Monitor logs for any errors

### Step 5: Update Frontend API URL

After backend is deployed:

1. Note your backend URL (e.g., `https://tasktracker-backend.onrender.com`)
2. Go to frontend service settings
3. Update `REACT_APP_API_URL` to: `https://tasktracker-backend.onrender.com/api`
4. Trigger a manual redeploy of frontend

---

## Option 2: Deploy Services Separately

### Deploy Backend

1. Go to Render Dashboard
2. Click "New" > "Web Service"
3. Connect your GitHub repository
4. Configure:
   - **Name**: `tasktracker-backend` (or your choice)
   - **Root Directory**: `backend`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`

5. Add environment variables:
   ```
   GOOGLE_SHEETS_CREDENTIALS = <your-json-credentials>
   SPREADSHEET_ID = <your-spreadsheet-id>
   ```

6. Click "Create Web Service"
7. Wait for deployment
8. **Note your backend URL** (e.g., `https://tasktracker-backend.onrender.com`)

### Deploy Frontend

1. Go to Render Dashboard
2. Click "New" > "Static Site"
3. Connect your GitHub repository
4. Configure:
   - **Name**: `tasktracker-frontend` (or your choice)
   - **Root Directory**: `frontend`
   - **Build Command**: `npm install && npm run build`
   - **Publish Directory**: `build`

5. Add environment variable:
   ```
   REACT_APP_API_URL = https://tasktracker-backend.onrender.com/api
   ```
   (Replace with your actual backend URL from previous step)

6. Click "Create Static Site"
7. Wait for deployment

---

## Post-Deployment

### Test Your Application

1. Visit your frontend URL (e.g., `https://tasktracker-frontend.onrender.com`)
2. Enter a test name
3. Complete a check-in
4. Verify data appears in Google Sheets

### Verify Backend Health

Visit: `https://your-backend-url.onrender.com/api/health`

You should see:
```json
{
  "status": "healthy",
  "timestamp": "2025-11-21T12:34:56.789012"
}
```

### Common Deployment Issues

#### Backend: Build Failed

**Check**:
- Verify `requirements.txt` is in `backend/` directory
- Check Python version in `runtime.txt`
- Review build logs for specific errors

**Solution**:
```bash
# Test locally first
cd backend
pip install -r requirements.txt
python app.py
```

#### Frontend: Build Failed

**Check**:
- Verify `package.json` is in `frontend/` directory
- Check for any missing dependencies
- Review build logs

**Solution**:
```bash
# Test locally first
cd frontend
npm install
npm run build
```

#### Backend: Application Error

**Check**:
- Environment variables are set correctly
- Google Sheets credentials are valid JSON
- Service account has access to spreadsheet

**Solution**:
- Check logs in Render dashboard
- Verify credentials work locally first
- Test with curl: `curl https://your-backend-url.onrender.com/api/health`

#### Frontend: Can't Connect to Backend

**Check**:
- `REACT_APP_API_URL` is set correctly
- Backend URL is correct and accessible
- No typos in the URL (should end with `/api`)

**Solution**:
1. Verify backend is running
2. Check browser console for CORS errors
3. Ensure backend URL is correct in frontend environment variables
4. Redeploy frontend after fixing

#### CORS Errors

This usually means:
- Backend URL is wrong in frontend config
- Backend is not running
- Backend doesn't have `flask-cors` enabled

**Solution**:
- Verify `flask-cors` is in `requirements.txt`
- Check `CORS(app)` is in `app.py`
- Ensure backend is deployed and running

---

## Automatic Deployments

Render can automatically deploy when you push to GitHub:

1. Go to service settings
2. Enable "Auto-Deploy"
3. Select branch (usually `main`)
4. Now every push to that branch will trigger a deployment

---

## Monitoring and Logs

### View Logs

1. Go to your service in Render dashboard
2. Click "Logs" tab
3. View real-time logs

### Common Log Messages

**Backend - Successful Start**:
```
[INFO] Starting gunicorn
[INFO] Listening at: http://0.0.0.0:10000
```

**Backend - Google Sheets Connected**:
```
[INFO] Google Sheets API initialized
```

**Backend - Using Fallback Storage**:
```
Warning: Could not initialize Google Sheets: ...
Will use local fallback storage
```

---

## Scaling and Performance

### Free Tier Limitations

- Services may sleep after 15 minutes of inactivity
- First request after sleep will be slow (cold start)
- Limited to 750 hours per month

### Keeping Services Active

For production use, consider:
1. Upgrading to paid plan (starts at $7/month)
2. Paid services don't sleep
3. Better performance and reliability

---

## Custom Domain (Optional)

### Add Custom Domain to Frontend

1. Go to frontend service settings
2. Click "Custom Domain"
3. Add your domain (e.g., `tasktracker.yourcompany.com`)
4. Follow DNS configuration instructions
5. SSL certificate is automatically provisioned

### Add Custom Domain to Backend

Same process as frontend. You'll also need to update:
- Frontend's `REACT_APP_API_URL` environment variable
- Redeploy frontend after changing

---

## Backup and Data

### Google Sheets as Primary Storage

Your data is automatically saved to Google Sheets, which provides:
- Automatic backups by Google
- Version history
- Easy export to Excel/CSV

### Fallback Data

If Google Sheets fails, data is saved to `fallback_data.json` on the server. However:
- This file is lost when service redeploys
- Not suitable for production use
- Ensure Google Sheets is always configured

---

## Security Best Practices

1. **Never commit credentials**:
   - Keep `.env` files out of git
   - Use `.gitignore`

2. **Rotate credentials regularly**:
   - Create new service account keys periodically
   - Delete old ones

3. **Limit spreadsheet access**:
   - Only share with service account
   - Don't make spreadsheet public

4. **Use environment variables**:
   - Never hardcode credentials
   - Use Render's secret environment variables

---

## Updating Your Application

### To Deploy Changes:

```bash
# Make your changes
git add .
git commit -m "Description of changes"
git push origin main
```

If auto-deploy is enabled, Render will automatically:
1. Pull latest code
2. Rebuild services
3. Deploy new version

---

## Cost Estimate

### Free Tier
- Backend: Free (with sleep)
- Frontend: Free
- Google Sheets: Free
- **Total: $0/month**

### Production Tier
- Backend: $7/month (no sleep, better performance)
- Frontend: Free (static sites are always free)
- Google Sheets: Free
- **Total: $7/month**

---

## Troubleshooting Commands

### Test Backend API

```bash
# Health check
curl https://your-backend-url.onrender.com/api/health

# Start session (test)
curl -X POST https://your-backend-url.onrender.com/api/start-session \
  -H "Content-Type: application/json" \
  -d '{"name":"Test User","check_type":"start"}'
```

### Check Service Status

1. Go to Render Dashboard
2. Check service status indicators
3. Green = Running
4. Yellow = Deploying
5. Red = Error

---

## Getting Help

If you're stuck:

1. **Check logs** in Render dashboard
2. **Review error messages** carefully
3. **Test locally first** before deploying
4. **Verify credentials** are correct
5. **Check Google Sheets** permissions

Common resources:
- [Render Documentation](https://render.com/docs)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [React Documentation](https://react.dev/)
- [Google Sheets API](https://developers.google.com/sheets/api)

---

## Success Checklist

After deployment, verify:

- [ ] Frontend loads at your Render URL
- [ ] Backend health endpoint responds
- [ ] Can start a morning check-in
- [ ] Can complete all questions
- [ ] Data appears in Google Sheets
- [ ] Can start an evening check-out
- [ ] Multiple users can use simultaneously
- [ ] Mobile view works correctly

---

🎉 **Congratulations!** Your Task Tracker is now live!

Share the URL with your team and start tracking those check-ins! 🚀

