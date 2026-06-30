import os

# التوكن والـ ID
BOT_TOKEN = os.getenv('BOT_TOKEN', "8929911107:AAHWMRbeYLZSyiIeQhmEAdDZvz3Ai53Nc40")
CHAT_ID = os.getenv('CHAT_ID', "1636617652")

# المواعيد بتوقيت مصر (24 ساعة)
MORNING_HOUR = 11    # 11 صباحاً
AFTERNOON_HOUR = 12  # 12 ظهراً
NIGHT_HOUR = 13      # 1 مساءً

# المدة المسموح فيها بالتأخير (بالدقائق)
GRACE_MINUTES = 50  # 15 دقيقة تسامح
