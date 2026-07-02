import asyncio
import edge_tts
from playsound import playsound
import time
import os

VOICE = "en-US-GuyNeural"

async def generate_voice(text, filename):
    communicate = edge_tts.Communicate(str(text), VOICE)
    await communicate.save(filename)

def speak(text):
    filename = f"temp_{int(time.time() * 1000)}.mp3"

    asyncio.run(generate_voice(text, filename))
    playsound(filename)

    try:
        os.remove(filename)
    except:
        pass