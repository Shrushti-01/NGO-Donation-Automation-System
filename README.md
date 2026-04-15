"# NGO-Donation-Automation-System" 
# YUVA Rural Association — Donation Chatbot
## How to Use

---

### Starting the App (every day)
1. Double-click **START.bat**
2. The website will open automatically in your browser
3. You're ready to use it!

---

### First Time Only — Linking WhatsApp
When you run START.bat for the first time, a window called
"WhatsApp Service" will show a QR code.

To link your WhatsApp:
1. Open WhatsApp on your phone
2. Go to Settings → Linked Devices → Link a Device
3. Scan the QR code shown on screen

You only need to do this ONCE. After that, it remembers your account forever.

---

### Stopping the App (end of day)
Double-click **STOP.bat**

---

### Changing the WhatsApp Number
If you want to use a different WhatsApp number:
1. Double-click **CHANGE_WHATSAPP.bat**
2. Type YES when asked
3. Run START.bat again and scan QR with the new number

---

### Daily Use
- **Send a broadcast message** — type your message and click "Send Broadcast"
  - Every number in the Excel sheet gets the message exactly once
  - Next broadcast goes to everyone again
- **Add a new donation entry** — fill the form and click Submit
  - A thank-you WhatsApp message is automatically sent to the parent

---

### Important Notes
- Keep the computer on while using the app
- Both the "WhatsApp Service" and "Python Server" windows must stay open
- The website status shows 🟢 when everything is working
- All donation data is saved in the `data/donations.xlsx` file
