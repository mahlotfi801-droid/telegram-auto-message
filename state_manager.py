import json
import os

STATE_FILE = "state.json"

def load_state():
    if not os.path.exists(STATE_FILE):
        return {"morning_index": 0, "afternoon_index": 0, "night_index": 0, 
                "last_morning_date": "", "last_afternoon_date": "", "last_night_date": ""}
    with open(STATE_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_state(state):
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=4)