import random
import datetime
import config
import os
from state_manager import load_state, save_state
from sender import send_telegram_message
from message_manager import get_messages, get_next_message

def main():
    # نجيب التوكن من GitHub Secrets
    if os.getenv('BOT_TOKEN'):
        config.BOT_TOKEN = os.getenv('BOT_TOKEN')
        config.CHAT_ID = os.getenv('CHAT_ID')
    
    state = load_state()
    today = datetime.date.today().isoformat()
    now = datetime.datetime.now()
    current_hour = now.hour
    current_minute = now.minute

    print(f"🕐 {now} - التحقق من الوقت...")
    
    # نضبط المواعيد حسب UTC (لأن GitHub Actions بتستخدم UTC)
    # لو انتي في مصر (UTC+2)، المواعيد هتكون:
    # 4 صباحاً بتوقيت مصر = 2 UTC
    # 2 ظهراً بتوقيت مصر = 12 UTC  
    # 8 مساءً بتوقيت مصر = 18 UTC
    
    # أو استخدمي التوقيت المحلي لو عايزة
    # local_hour = (current_hour + 2) % 24  # لو في مصر UTC+2
    
    task = None
    
    # نشوف لو الوقت جه
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
                # نجيب الرسائل
                msgs = get_messages(f"messages/{cat}.txt")
                emojis = get_messages("emoji.txt")
                msg = get_next_message(cat, state, msgs)
                full_msg = f"{msg} {random.choice(emojis)}"

                # نبعت الرسالة
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
