import asyncio
import edge_tts
from playsound import playsound
import time
import os

VOICE = "en-US-AnaNeural"

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



"""
import asyncio 
-Used when task can run without b;ocking the programm
-Need cause edge_tts works with asyncio

import edge_tts
-Import edge_tts libray
-This library converts text to voice using Microsoft voice

from playsound import playsound
-Use to play audio files

import time
-Use here to create a unique file
-If every files name is voice.mp3 old files get overwritten

import os
-Lets Python interact with OS
-Used here to delete files

VOICE = "en-US-GuyNeural"
-A variable storing which voice to use

async def generate_voice(text,filename)
-Async func need
    -text  what to say
    -file where to save audio

communicare = edge_tts.Communicate(str(text),VOICE)
-Converts text into speech using selected voice
-str(text) to ensure input becomes a string

await communicate.save(filename)
-await means:“Wait here until speech generation finishes.”
-Saves speech into mp3 file.

filename = f"temp_{int(time.time() * 1000)}.mp3"
-time.time()  current time in sec
-Ensure every file gets unique name

asyncio.run(generate_voice(text, filename))
-generate_voice()  alone wont work directly.
-asyncio.run() starts async engine.

os.remove(filename)
-Deletes temp mp3 after playing.
-Otherwise hundreds of audio files pile up.

Flow
    Create temp filename
    Convert text to voice
    Save as mp3
    Play mp3
    Delete mp3
"""