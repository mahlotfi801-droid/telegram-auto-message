import datetime
import random
from config import MORNING_HOUR, AFTERNOON_HOUR, NIGHT_HOUR
from state_manager import load_state, save_state
from message_manager import get_messages, get_next_message
from sender import send_telegram_message

def main():
    state = load_state()
    # توقيت القاهرة
    now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=2)))
    today = now.strftime("%Y-%m-%d")
    hour = now.hour

    task = None
    if hour == MORNING_HOUR and state['last_morning_date'] != today:
        task = ("morning", "last_morning_date")
    elif hour == AFTERNOON_HOUR and state['last_afternoon_date'] != today:
        task = ("afternoon", "last_afternoon_date")
    elif hour == NIGHT_HOUR and state['last_night_date'] != today:
        task = ("night", "last_night_date")

    if task:
        cat, date_key = task
        msgs = get_messages(f"messages/{cat}.txt")
        emojis = get_messages("emoji.txt")
        
        msg = get_next_message(cat, state, msgs)
        full_msg = f"{msg} {random.choice(emojis)}"
        
        if send_telegram_message(full_msg):
            state[date_key] = today
            save_state(state)
            print(f"تم إرسال رسالة الـ {cat} بنجاح!")

if __name__ == "__main__":
    main()