import os

# التوكن والـ ID من GitHub Secrets
BOT_TOKEN = os.getenv('BOT_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')  # أو CHAT_IDS

# المواعيد بتوقيت مصر (8 مواعيد)
MORNING_HOUR = 7    # 7 صباحا
EVENING_HOUR_1 = 11  # 11 صباجاً
EVENING_HOUR_2 = 15  # 3 عصراً
AFTERNOON_HOUR = 17  # 5 ظهراً
EVENING_HOUR_4 = 18  # 6 مساءً
EVENING_HOUR_5 = 20  # 8 مساءً
EVENING_HOUR_3 = 22  # 10 مساءً
NIGHT_HOUR = 00      # 12 في منصف الليلاً
# فترة السماح
GRACE_MINUTES = 55
