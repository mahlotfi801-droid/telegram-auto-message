import os

# التوكن والـ ID من GitHub Secrets
BOT_TOKEN = os.getenv('BOT_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')  # أو CHAT_IDS

# المواعيد بتوقيت مصر (8 مواعيد)
MORNING_HOUR = 7    # 7 ظهراً
AFTERNOON_HOUR = 20  # 9 ظهراً
NIGHT_HOUR = 24      # 11 ظهراً
EVENING_HOUR_1 = 11  # 11 صباجاً
EVENING_HOUR_2 = 23  # 1 عصراً
EVENING_HOUR_3 = 16  # 4 مساءً
EVENING_HOUR_4 = 18  # 7 مساءً
EVENING_HOUR_5 = 22  # 10 مساءً

# فترة السماح
GRACE_MINUTES = 60
