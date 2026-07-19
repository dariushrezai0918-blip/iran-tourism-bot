import json
import os

FILE = "history.json"


def load_history():

    if not os.path.exists(FILE):
        return []

    with open(FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_history(history):

    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, ensure_ascii=False)


def add_place(title):

    history = load_history()

    history.append(title)

    save_history(history)


def exists(title):

    history = load_history()

    return title in history
