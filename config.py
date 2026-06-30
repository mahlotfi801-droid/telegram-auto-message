import os
from datetime import datetime, timedelta
import pytz

# التوكن والـ ID
BOT_TOKEN = os.getenv('BOT_TOKEN', "8929911107:AAHWMRbeYLZSyiIeQhmEAdDZvz3Ai53Nc40")
CHAT_ID = os.getenv('CHAT_ID', "1636617652")

# طريقة 1: استخدام توقيت مصر مباشرة
def get_egypt_time():
    egypt_tz = pytz.timezone('Africa/Cairo')
    return datetime.now(egypt_tz)

# طريقة 2: استخدام UTC مع إضافة فارق التوقيت (مصر = UTC+2)
# ملاحظة: في الصيف مصر بتستخدم UTC+3
UTC_OFFSET = 2  # في الشتاء
# UTC_OFFSET = 3  # في الصيف (التوقيت الصيفي)

# المواعيد بتوقيت مصر (نفس المواعيد اللي انتي عايزاها)
MORNING_HOUR = 11    # 1 صباحاً
AFTERNOON_HOUR = 12 # 12 ظهراً
NIGHT_HOUR = 13     # 1 مساءً
