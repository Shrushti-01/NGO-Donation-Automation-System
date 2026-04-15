import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.whatsapp import send_whatsapp

if len(sys.argv) < 6:
    print("Usage: send_thankyou.py <phone> <parent_name> <student_name> <school> <amount>")
    sys.exit(1)

phone        = sys.argv[1].strip()
parent_name  = sys.argv[2].strip()
student_name = sys.argv[3].strip()
school       = sys.argv[4].strip()
amount       = sys.argv[5].strip()

LOG_FILE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "sent_log.txt")

# ── Clean phone number ──
phone = phone.replace("+", "").replace(" ", "").replace(".0", "")
while phone.startswith("91") and len(phone) > 10:
    phone = phone[2:]
if len(phone) == 10:
    phone = "91" + phone
phone = "+" + phone

# ── Check if already sent ──
try:
    with open(LOG_FILE, "r") as f:
        sent_numbers = f.read().splitlines()
except:
    sent_numbers = []

if phone in sent_numbers:
    print(f"Thank-you already sent to {phone}. Skipping.")
    sys.exit(0)

# ── Build and send message ──
message = f"Hello Dear {parent_name} \U0001f44b We hope you are doing well. We are delighted to inform you that your ward, {student_name} from {school}, has successfully raised a generous amount of \u20b9{amount} in support of our NGO. This contribution is helping us continue our mission of empowering children and creating positive change in the community. We truly appreciate the efforts of {student_name} as well as your encouragement and support. Thank you once again for being a part of this noble cause. YUVA Rural Association \U0001f331 Helping People... To Help Themselves"

print(f"Sending thank-you to {phone}...")
success = send_whatsapp(phone, message)

if success:
    with open(LOG_FILE, "a") as f:
        f.write(phone + "\n")
    print(f"Thank-you sent and logged for {phone}")
else:
    print(f"Failed to send thank-you to {phone}")
