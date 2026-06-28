import json
#Stores command in memory
def load_memory():
 try:
   with open("memory.json","r") as file:
    data = json.load(file)

   if not isinstance(data,dict):
      data = {}
    
   data.setdefault("pref", {})
   data.setdefault("name", None)
   data.setdefault("memory", [])
   data.setdefault("notes", [])

   return data
 
 except FileNotFoundError :
     return{"name":None,"pref":{},"memory":[]}

def save_memory(user_msg,bot_msg):
   data =load_memory()
   chat = {
      "user":user_msg,
      "bot" :bot_msg
   }
   data["memory"].append(chat)

   with open("memory.json","w") as file:
    json.dump(data,file,indent=4)

def save_data(data):
    with open("memory.json", "w") as file:
        json.dump(data, file, indent=4)
    

def reset_memory():
   data = {
        "name" : None,
        "pref" : {},
        "memory" : []
   }
   try:
     with open ("memory.json", "w") as file:
       json.dump(data, file,indent=4)
       return "Memory has been reset...."
   except Exception as e:
       return f"Error reseting memeory : {e}"
   

