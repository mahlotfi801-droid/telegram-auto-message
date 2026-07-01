import json
import os

STATE_FILE = "state.json"

def load_state():
    """تحميل الحالة من الملف"""
    if not os.path.exists(STATE_FILE):
        # الحالة الافتراضية لـ 8 رسائل
        return {
            "morning": "",
            "afternoon": "",
            "night": "",
            "evening1": "",
            "evening2": "",
            "evening3": "",
            "evening4": "",
            "evening5": "",
            "morning_index": 0,
            "afternoon_index": 0,
            "night_index": 0,
            "evening1_index": 0,
            "evening2_index": 0,
            "evening3_index": 0,
            "evening4_index": 0,
            "evening5_index": 0
        }
    with open(STATE_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_state(state):
    """حفظ الحالة في الملف"""
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=4, ensure_ascii=False)
