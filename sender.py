import requests
import time
from config import BOT_TOKEN, CHAT_ID

def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text}
    
    # محاولات إعادة الإرسال لو حصل مشكلة في النت
    for wait in [0, 30, 60]:
        try:
            if wait > 0: time.sleep(wait)
            response = requests.post(url, data=payload)
            if response.status_code == 200:
                return True
        except:
            pass
    return False