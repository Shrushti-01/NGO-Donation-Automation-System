import requests


WHATSAPP_SERVICE_URL = "http://localhost:3001"


def send_whatsapp(phone, message):
    """
    Sends a WhatsApp message via the local whatsapp-web.js service.
    The service must be running: cd whatsapp-service && node index.js
    """
    try:
        print(f"Sending WhatsApp to {phone}...")

        response = requests.post(
            f"{WHATSAPP_SERVICE_URL}/send",
            json={"phone": phone, "message": message},
            timeout=30
        )

        result = response.json()

        if result.get("success"):
            print(f"✅ Message sent to {phone}")
            return True
        else:
            print(f"❌ Failed to send to {phone}: {result.get('error')}")
            return False

    except requests.exceptions.ConnectionError:
        print(f"❌ WhatsApp service is not running! Start it with: cd whatsapp-service && node index.js")
        return False
    except Exception as e:
        print(f"❌ Error sending to {phone}: {e}")
        return False


def is_whatsapp_ready():
    """Check if the WhatsApp service is running and logged in."""
    try:
        response = requests.get(f"{WHATSAPP_SERVICE_URL}/status", timeout=5)
        return response.json().get("ready", False)
    except:
        return False
