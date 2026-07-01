import os

# التوكن والـ ID من GitHub Secrets
BOT_TOKEN = os.getenv('BOT_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')  # أو CHAT_IDS

# المواعيد بتوقيت مصر (8 مواعيد)
MORNING_HOUR = 12    # 12 ظهراً
AFTERNOON_HOUR = 13  # 1 ظهراً
NIGHT_HOUR = 14      # 2 ظهراً
EVENING_HOUR_1 = 15  # 3 عصراً
EVENING_HOUR_2 = 16  # 4 عصراً
EVENING_HOUR_3 = 17  # 5 مساءً
EVENING_HOUR_4 = 18  # 6 مساءً
EVENING_HOUR_5 = 19  # 7 مساءً

# فترة السماح
GRACE_MINUTES = 50
