import random
import datetime
import config # تم تعديله لاستيراد الملف بالكامل
from state_manager import load_state, save_state
from sender import send_telegram_message
from message_manager import get_messages, get_next_message

def main():
    state = load_state()
    today = datetime.date.today().isoformat()
    now = datetime.datetime.now()
    current_hour = now.hour
    
    # تحديد المهام المطلوبة بناءً على الساعة الحالية
    task = None
    
    # التحقق من المواعيد الثلاثة
    if current_hour == config.MORNING_HOUR and state.get("morning") != today:
        task = ("morning", "morning")
    elif current_hour == config.AFTERNOON_HOUR and state.get("afternoon") != today:
        task = ("afternoon", "afternoon")
    elif current_hour == config.NIGHT_HOUR and state.get("night") != today:
        task = ("night", "night")

    # تنفيذ المهمة إذا كان الوقت مناسباً
    if task:
        cat, date_key = task
        max_retries = 3
        success = False
        
        print(f"بدء محاولة الإرسال لـ {cat}...")
        
        for attempt in range(max_retries):
            try:
                msgs = get_messages(f"messages/{cat}.txt")
                emojis = get_messages("emoji.txt")
                msg = get_next_message(cat, state, msgs)
                full_msg = f"{msg} {random.choice(emojis)}"
                
                if send_telegram_message(full_msg):
                    state[date_key] = today
                    save_state(state)
                    print(f"تم الإرسال بنجاح في المحاولة {attempt + 1}")
                    success = True
                    break 
                else:
                    print(f"فشلت المحاولة {attempt + 1}: لم يتم استلام تأكيد من تليجرام")
            except Exception as e:
                print(f"محاولة {attempt + 1} فشلت بسبب خطأ: {e}")
        
        if not success:
            print("فشلت جميع المحاولات، سيتم إعادة المحاولة في الساعة القادمة.")
    else:
        print("ليس وقت الإرسال أو تم الإرسال مسبقاً.")

if __name__ == "__main__":
    main()
