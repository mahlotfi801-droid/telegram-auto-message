import os

# التوكن والـ ID جايين من GitHub Secrets
BOT_TOKEN = os.getenv('BOT_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')

# المواعيد بتوقيت مصر (24 ساعة)
MORNING_HOUR = 15    # 11 صباحاً
AFTERNOON_HOUR = 16  # 12 ظهراً
NIGHT_HOUR = 17      # 1 مساءً

# فترة السماح (بالدقائق)
GRACE_MINUTES = 50   # 50 دقيقة تسامح
