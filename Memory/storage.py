import json
#Stores command in memory
class Memory :
  def  __init__(self,file="memory.json") :
     self.file = file

  def load(self):
   try:
    with open(self.file,"r") as file:
      data = json.load(file)

    if not isinstance(data,dict):
        data = {}
      
    data.setdefault("pref", {})
    data.setdefault("name", None)
    data.setdefault("memory", [])
    data.setdefault("notes", [])
    data.setdefault("tasks", [])

    return data
  
   except FileNotFoundError :
      return{"name":None,"pref":{},"memory":[],"notes":[],"tasks" :[]}

  def save_chat(self,user_msg,bot_msg):
    data =self.load()
    chat = {
        "user":user_msg,
        "bot" :bot_msg
    }
    data["memory"].append(chat)

    with open(self.file,"w") as file:
      json.dump(data,file,indent=4)

  def save(self,data):
      with open(self.file, "w") as file:
          json.dump(data, file, indent=4)
      

  def reset(self):
    data = {
          "name" : None,
          "pref" : {},
          "memory" : [],
          "notes": [],
          "tasks": []
    }
    try:
      with open (self.file, "w") as file:
        json.dump(data, file,indent=4)
        return "Memory has been reset...."
    except Exception as e:
        return f"Error reseting memeory : {e}"
    

