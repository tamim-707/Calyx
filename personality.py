from storage import load_memory
import json
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
        "greeting": "System active. Awaiting your command.",
        "hello": "Greetings. How may I assist you today?",
        "name" : "Name is Calyx , your personal assistant " 
    },
    "friendly" : {
        "greeting" : "Calyx online. How can I assist you?",
        "hello" : "Hi, how may I help you today?",
        "name" : "Im Calyx your personal assistant " 
    },
    "funny" : {
        "greeting": "Calyx booted up... surprisingly without bugs.",
        "hello": "Yo human, what chaos are we solving today?",
        "name" : "Me? Im Calyx your crime partner" 
    }
}
#Get Personalities
def get_personalities() :
   data = load_memory()
   return data.get("personality", "friendly")
      