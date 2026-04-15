# How to Run — YUVA NGO Staff Portal

## 🚀 First-Time Setup (Do this once only)

### Step 1: Install Node.js
Download from https://nodejs.org (choose LTS version) and install.

### Step 2: Install WhatsApp service packages
Open a terminal in the project folder and type:
```
cd whatsapp-service
npm install
cd ..
```

### Step 3: Install Python packages
```
pip install -r requirements.txt
```

---

## ▶️ Starting the App (Do this every time)

You need **two terminal windows** open at the same time.

### Terminal 1 — WhatsApp Service
```
cd whatsapp-service
node index.js
```
Leave this running.

### Terminal 2 — Main Server
```
uvicorn app.main:app --reload
```
Leave this running too.

### Open the Website
Open `frontend/index.html` in your browser (double-click it).

---

## 👤 First Login

1. The website will show a **Sign In / Register** screen
2. First time: click **Register** tab and create your account
3. After that, just use **Sign In** with your username and password
4. Each NGO employee can have their own login

---

## 📱 Connecting WhatsApp

1. After logging in, you'll see a **"Connect WhatsApp"** button at the top
2. Click it — a QR code will appear **right on the website**
3. Open WhatsApp on your phone → tap ⋮ Menu → Linked Devices → Link a Device
4. Scan the QR code shown on screen
5. The status will automatically change to ✅ Connected

> **Note:** After scanning once, WhatsApp stays connected even after restarting the app.

---

## ⏹ Stopping the Session

- Click the red **"Stop Session"** button in the top bar
- Confirm and it will log you out and stop all background tasks
- To restart: open the terminals again and refresh the page

---

## 🔒 Security

- Each employee must log in with their own username and password
- Sessions automatically expire after 8 hours
- No one can use the app without being logged in

---

## 📢 How Broadcast Works

- Select a school from the dropdown
- Type your message
- Click "Send Broadcast" — it sends to all donors in that school's list
- Each unique message is sent only once per person
