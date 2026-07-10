# Utils/input.py

from Utils.speech import speech_to_text

def get_input(mode):
    if mode == "voice":
        return speech_to_text().strip()

    elif mode == "text":
        return input("You: ").strip()