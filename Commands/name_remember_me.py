from Memory.storage import Memory
memory = Memory()
#Save your name in Calyx
def save_name(name):
   data = memory.load()
   data["name"]= name.capitalize()

   memory.save(data)

def set_name(user):
   name = user.replace("my name is","").strip().capitalize()
   save_name(name)
   return f"Hey {name} ! Nice to meet you"

def show_name():
   data = memory.load()
   name = data.get("name")
   if name :
      return f"You are {name}"
   else :
      return "I don't know your name yet, sorry :)"


   

#History Function
def show_history():
   data = memory.load()
   history = ""

   for chat in data["memory"] :
     history += f"You: {chat['user']}\n"
     history += f"Calyx: {chat['bot']}\n\n"
   return history

#MY memory in Calyx
def remember_me():
   memory = memory.load()
   pref = memory.get("pref",{})
   name= memory.get("name")
   colour = pref.get("colour")
   hobby = pref.get("hobby")

   if not name and not colour and not hobby : 
      return "I don't know anything about you yet :)"
   return f"Your name is {name} \n You like {colour}\n And {name} your hobby is {hobby}."


      

