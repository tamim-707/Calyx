import requests
import os
from dotenv import load_dotenv
load_dotenv()
# import json
api_key = os.getenv("gemini_api_key")

def ask_gemini(prompt) :
  url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"

  payload = {
    "contents" : [
      {
      "parts" : [{"text" : prompt}]
      }
    ]
  }

  response = requests.post(url,json = payload,timeout = 20)
  print("Status:", response.status_code)
  print("Response:", response.text)

  data = response.json()
  return data["candidates"][0]["content"]["parts"][0]["text"]