import random
import datetime
import config
import os
import pytz  # مهم نضيف المكتبة دي
from state_manager import load_state, save_state
from sender import send_telegram_message
from message_manager import get_messages, get_next_message

def main():
    # نجيب التوكن من GitHub Secrets
    if os.getenv('BOT_TOKEN'):
        config.BOT_TOKEN = os.getenv('BOT_TOKEN')
        config.CHAT_ID = os.getenv('CHAT_ID')
    
    # نضبط التوقيت بتاع مصر
    egypt_tz = pytz.timezone('Africa/Cairo')
    now = datetime.datetime.now(egypt_tz)
    
    # نستخدم التوقيت المصري
    current_hour = now.hour
    current_minute = now.minute
    today = now.date().isoformat()
    
    state = load_state()

    print(f"🕐 الوقت بتاع مصر: {now.strftime('%Y-%m-%d %H:%M:%S')}")
    
    task = None
    
    # دلوقتي بنستخدم التوقيت المصري مباشرة
    if current_hour == config.MORNING_HOUR and current_minute == 0 and state.get("morning") != today:
        task = ("morning", "morning")
        print("⏰ وقت الرسالة الصباحية!")
    elif current_hour == config.AFTERNOON_HOUR and current_minute == 0 and state.get("afternoon") != today:
        task = ("afternoon", "afternoon")
        print("⏰ وقت الرسالة الظهرية!")
    elif current_hour == config.NIGHT_HOUR and current_minute == 0 and state.get("night") != today:
        task = ("night", "night")
        print("⏰ وقت الرسالة المسائية!")
    
    if task:
        cat, date_key = task
        max_retries = 3
        success = False

        for attempt in range(max_retries):
            try:
                msgs = get_messages(f"messages/{cat}.txt")
                emojis = get_messages("emoji.txt")
                msg = get_next_message(cat, state, msgs)
                full_msg = f"{msg} {random.choice(emojis)}"

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
        print(f"⏳ مش وقت إرسال أو تم الإرسال مسبقاً - الساعة {current_hour}:{current_minute:02d}")

if __name__ == "__main__":
    main()
