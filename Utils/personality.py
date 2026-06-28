from Memory.storage import load_memory
import json
import random
def set_personality(mode):
   data = load_memory()
   data["personality"] = mode

   if mode not in personalities :
      return "Available Personalities: Formal, Funny, Friendly"

   with open("memory.json","w") as file:
      json.dump(data,file,indent=4)

   return f"Personality has changed to {mode}"


personalities = {
    "formal" : {
        "greeting":[ 
            "System active. Awaiting your command.",
            "Calyx is ready for your command Sir.",
            "Hello Sir, Calyx is here!"],
        "hello": [
            "Greetings. How may I assist you today?",
            "Hello. Awaiting your instruction.",
            "Good day. What can I do for you?"],
      "name": [
            "I am Calyx, your personal assistant.",
            "My designation is Calyx. I am here to assist you.",
            "I am Calyx, designed to support your tasks efficiently."]
    },

    "friendly" : {
        "greeting": [
            "Calyx online. How can I assist you?",
            "System ready! What do you need?",
            "I'm here and ready to help."],
        "hello": [
            "Hi, how may I help you today?",
            "Hello! Nice to see you again.",
            "Hey! What can I do for you?"],
        "name": [
            "Im Calyx your personal assistant",
            "I'm Calyx, your smart assistant.",
            "Calyx here, ready to help anytime."],
    },

    "funny" : {
        "greeting": [
            "Calyx booted up... surprisingly without bugs.",
            "System online... and somehow nothing exploded.",
            "I have awakened. Chaos level: manageable."],
      "hello": [
            "Yo human, what chaos are we solving today?",
            "Ah, my favorite human is back.",
            "Ready to break reality today?"],
      "name": [
            "Me? I'm Calyx, your crime partner.",
            "People call me Calyx",
            "Calyx here. Smarter than a toaster, funnier than most bots."]
    }
}

#Get Personalities
def get_personalities() :
   data = load_memory()
   return data.get("personality", "friendly")

def get_response(response_type):
   mode = get_personalities()
   responses = personalities[mode][response_type]
   return random.choice(responses)
      