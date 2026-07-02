#loader file
import json
from Utils.voice import speak
def load_config():
    with open ("config.json","r") as file:
      return  json.load(file)
    
def reply(text):
    speak(text)
    print("Calyx:", text)
    