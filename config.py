import os

# التوكن والـ ID جايين من GitHub Secrets
BOT_TOKEN = os.getenv('BOT_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')

# المواعيد بتوقيت مصر (24 ساعة)
MORNING_HOUR = 12    # 11 صباحاً
AFTERNOON_HOUR = 13  # 12 ظهراً
NIGHT_HOUR = 14      # 1 مساءً

# فترة السماح (بالدقائق)
GRACE_MINUTES = 50   # 50 دقيقة تسامح
