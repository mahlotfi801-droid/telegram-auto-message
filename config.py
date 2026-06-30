import os

# التوكن والـ ID جايين من GitHub Secrets
BOT_TOKEN = os.getenv('BOT_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')

# المواعيد بتوقيت مصر (24 ساعة)
MORNING_HOUR = 18    # 11 صباحاً
AFTERNOON_HOUR = 19  # 12 ظهراً
NIGHT_HOUR = 20      # 1 مساءً

# فترة السماح (بالدقائق)
GRACE_MINUTES = 40   # 50 دقيقة تسامح
