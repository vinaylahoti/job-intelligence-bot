import requests
import os

# Get values from environment variables (we'll set them later)
BOT_TOKEN = os.getenv("8139550513:AAGPf_2n0qcogI4z7EAVtgJ_DuKUSmN3dVc")
CHAT_ID = os.getenv("1053956354")

def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": "HTML"
    }
    response = requests.post(url, data=payload)
    return response.json()

if __name__ == "__main__":
    message = "✅ Job Intelligence Bot is live and working!"
    result = send_message(message)
    print(result)
