import random
import datetime
import config
import os
import pytz
from state_manager import load_state, save_state
from sender import send_telegram_message
from message_manager import get_messages, get_next_message

def get_egypt_time():
    """تجيب الوقت الحالي بتوقيت مصر"""
    egypt_tz = pytz.timezone('Africa/Cairo')
    return datetime.datetime.now(egypt_tz)

def is_time_to_send(target_hour, current_hour, current_minute):
    """تتحقق إذا كان الوقت مناسب للإرسال"""
    diff_minutes = (current_hour - target_hour) * 60 + current_minute
    if diff_minutes >= 0 and diff_minutes <= config.GRACE_MINUTES:
        return True
    return False

def main():
    # نجيب التوكن من GitHub Secrets
    if os.getenv('BOT_TOKEN'):
        config.BOT_TOKEN = os.getenv('BOT_TOKEN')
        config.CHAT_ID = os.getenv('CHAT_ID')
    
    # نتحقق إن التوكن موجود
    if not config.BOT_TOKEN or not config.CHAT_ID:
        print("❌ التوكن أو الـ CHAT_ID مش موجودين في Secrets!")
        return
    
    now = get_egypt_time()
    current_hour = now.hour
    current_minute = now.minute
    today = now.date().isoformat()
    
    state = load_state()

    print(f"🕐 الوقت بتاع مصر: {now.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"📅 النهاردة: {today}")
    
    # قائمة المواعيد وملفاتها
    schedule = [
        (config.MORNING_HOUR, "morning", "morning"),
        (config.AFTERNOON_HOUR, "afternoon", "afternoon"),
        (config.NIGHT_HOUR, "night", "night"),
        (config.EVENING_HOUR_1, "evening1", "evening1"),
        (config.EVENING_HOUR_2, "evening2", "evening2"),
        (config.EVENING_HOUR_3, "evening3", "evening3"),
        (config.EVENING_HOUR_4, "evening4", "evening4"),
        (config.EVENING_HOUR_5, "evening5", "evening5"),
    ]
    
    task = None
    for hour, cat, date_key in schedule:
        if is_time_to_send(hour, current_hour, current_minute) and state.get(date_key) != today:
            task = (cat, date_key)
            break
    
    if task:
        cat, date_key = task
        max_retries = 3
        success = False

        print(f"📤 بدء إرسال رسالة {cat}...")

        for attempt in range(max_retries):
            try:
                msgs = get_messages(f"messages/{cat}.txt")
                emojis = get_messages("emoji.txt")
                msg = get_next_message(cat, state, msgs)
                full_msg = f"{msg} {random.choice(emojis)}"

                print(f"📝 الرسالة: {full_msg}")

                if send_telegram_message(full_msg):
                    state[date_key] = today
                    save_state(state)
                    print(f"✅ تم إرسال رسالة {cat} بنجاح!")
                    success = True
                    break
                else:
                    print(f"❌ فشلت المحاولة {attempt + 1}")
            except Exception as e:
                print(f"⚠️ خطأ في المحاولة {attempt + 1}: {e}")

        if not success:
            print("❌ فشل إرسال جميع المحاولات")
    else:
        print("⏳ مش وقت إرسال أو تم الإرسال مسبقاً")

if __name__ == "__main__":
    main()
