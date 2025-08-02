# Deployment Guide - Get Your Permanent Web Address

## Option 1: Render (Recommended - Free & Easy)

### Step 1: Create Render Account
1. Go to [render.com](https://render.com)
2. Sign up with GitHub or email
3. Verify your email

### Step 2: Deploy Your App
1. Click "New +" → "Web Service"
2. Connect your GitHub repository (or upload files)
3. Configure the service:
   - **Name**: `text-to-speech-converter`
   - **Environment**: `Python`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Plan**: Free

### Step 3: Get Your URL
- Render will give you a URL like: `https://your-app-name.onrender.com`
- This URL will be permanent and accessible from anywhere!

---

## Option 2: Railway (Alternative - Free)

### Step 1: Create Railway Account
1. Go to [railway.app](https://railway.app)
2. Sign up with GitHub
3. Create new project

### Step 2: Deploy
1. Connect your GitHub repository
2. Railway will auto-detect Python
3. Deploy automatically

### Step 3: Get Your URL
- Railway provides: `https://your-app-name.railway.app`

---

## Option 3: Heroku (Paid Option)

### Step 1: Create Heroku Account
1. Go to [heroku.com](https://heroku.com)
2. Sign up for account
3. Install Heroku CLI

### Step 2: Deploy
```bash
heroku create your-app-name
git add .
git commit -m "Deploy to Heroku"
git push heroku main
```

### Step 3: Get Your URL
- Heroku provides: `https://your-app-name.herokuapp.com`

---

## Option 4: PythonAnywhere (Free)

### Step 1: Create Account
1. Go to [pythonanywhere.com](https://pythonanywhere.com)
2. Create free account
3. Upload your files

### Step 2: Configure Web App
1. Go to Web tab
2. Add new web app
3. Choose Flask
4. Upload your files
5. Set up WSGI file

### Step 3: Get Your URL
- PythonAnywhere provides: `https://yourusername.pythonanywhere.com`

---

## Quick Deploy Commands

### For Render:
```bash
# If you have git repository
git add .
git commit -m "Ready for deployment"
git push origin main
# Then follow Render web interface
```

### For Railway:
```bash
# Install Railway CLI
npm install -g @railway/cli
railway login
railway init
railway up
```

---

## Important Notes

### Environment Variables (if needed):
- Add any API keys or secrets in your deployment platform's environment variables
- The app currently doesn't require any external API keys

### File Storage:
- The app creates temporary files in the `uploads/` folder
- These are automatically cleaned up
- For production, consider using cloud storage (AWS S3, etc.)

### Performance:
- Free tiers have limitations
- Consider upgrading for better performance
- Monitor your usage

---

## Your Permanent URL

Once deployed, you'll get a URL like:
- `https://text-to-speech-converter.onrender.com`
- `https://your-app.railway.app`
- `https://your-app.herokuapp.com`

This URL will be:
✅ **Permanent** - Won't change  
✅ **Public** - Accessible from anywhere  
✅ **24/7** - Always available  
✅ **Secure** - HTTPS enabled  

---

## Testing Your Deployment

After deployment, test:
1. Text input functionality
2. File upload functionality
3. Audio conversion
4. Download functionality
5. Different tone options

---

## Support

If you encounter issues:
1. Check the deployment platform's logs
2. Verify all files are uploaded
3. Ensure requirements.txt is correct
4. Check Python version compatibility

---

## Recommended: Render

**Why Render is recommended:**
- ✅ Free tier available
- ✅ Easy deployment
- ✅ Automatic HTTPS
- ✅ Good performance
- ✅ Reliable uptime
- ✅ Simple interface

**Steps to deploy on Render:**
1. Go to render.com
2. Sign up
3. Connect GitHub repo
4. Deploy
5. Get your permanent URL!

Your app will be live at: `https://your-app-name.onrender.com` 