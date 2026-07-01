import os

# التوكن والـ ID من GitHub Secrets
BOT_TOKEN = os.getenv('BOT_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')  # أو CHAT_IDS

# المواعيد بتوقيت مصر (8 مواعيد)
MORNING_HOUR = 16    # 12 ظهراً
AFTERNOON_HOUR = 17  # 1 ظهراً
NIGHT_HOUR = 23      # 2 ظهراً
EVENING_HOUR_1 = 18  # 3 عصراً
EVENING_HOUR_2 = 19  # 4 عصراً
EVENING_HOUR_3 = 20  # 5 مساءً
EVENING_HOUR_4 = 21  # 6 مساءً
EVENING_HOUR_5 = 22  # 7 مساءً

# فترة السماح
GRACE_MINUTES = 50
