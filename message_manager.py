import random

def get_messages(filepath):
    """تقرأ الرسائل من ملف"""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        return ["مفيش رسائل في الملف ده!"]

def get_next_message(category, state, messages):
    """تجيب الرسالة التالية حسب الترتيب"""
    index_key = f"{category}_index"
    if state.get(index_key, 0) >= len(messages):
        random.shuffle(messages)
        state[index_key] = 0

    msg = messages[state[index_key]]
    state[index_key] += 1
    return msg
