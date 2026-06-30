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

def main():
    # نجيب التوكن من GitHub Secrets لو موجود
    if os.getenv('BOT_TOKEN'):
        config.BOT_TOKEN = os.getenv('BOT_TOKEN')
        config.CHAT_ID = os.getenv('CHAT_ID')
    
    # نجيب الوقت بتوقيت مصر
    now = get_egypt_time()
    current_hour = now.hour
    current_minute = now.minute
    today = now.date().isoformat()
    
    # نحمل الحالة السابقة
    state = load_state()

    print(f"🕐 الوقت بتاع مصر: {now.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"📅 النهاردة: {today}")
    print(f"⏰ الساعة دلوقتي: {current_hour}:{current_minute:02d}")
    print(f"📋 المواعيد المحددة: {config.MORNING_HOUR}, {config.AFTERNOON_HOUR}, {config.NIGHT_HOUR}")
    
    # نحدد المهمة المطلوبة
    task = None
    
    # نتحقق من المواعيد الثلاثة (فقط في الدقيقة 0 عشان مايبعتش كذا مرة)
    if current_hour == config.MORNING_HOUR and current_minute == 0 and state.get("morning") != today:
        task = ("morning", "morning")
        print("⏰ وقت الرسالة الصباحية!")
    elif current_hour == config.AFTERNOON_HOUR and current_minute == 0 and state.get("afternoon") != today:
        task = ("afternoon", "afternoon")
        print("⏰ وقت الرسالة الظهرية!")
    elif current_hour == config.NIGHT_HOUR and current_minute == 0 and state.get("night") != today:
        task = ("night", "night")
        print("⏰ وقت الرسالة المسائية!")
    
    # لو في مهمة، ننفذها
    if task:
        cat, date_key = task
        max_retries = 3
        success = False

        print(f"📤 بدء إرسال رسالة {cat}...")

        for attempt in range(max_retries):
            try:
                # نجيب الرسائل
                msgs = get_messages(f"messages/{cat}.txt")
                emojis = get_messages("emoji.txt")
                msg = get_next_message(cat, state, msgs)
                full_msg = f"{msg} {random.choice(emojis)}"

                print(f"📝 الرسالة: {full_msg}")

                # نبعت الرسالة
                if send_telegram_message(full_msg):
                    # نحفظ التاريخ عشان مايبعتش تاني النهاردة
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
        print(f"⏳ مش وقت إرسال أو تم الإرسال مسبقاً")

if __name__ == "__main__":
    main()
