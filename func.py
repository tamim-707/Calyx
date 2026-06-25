from storage import load_memory,save_data

#Save your name in Calyx
def save_name(name):
   data = load_memory()
   data["name"]= name.capitalize()

   save_data(data)

def set_name(user):
   name = user.replace("my name is","").strip().capitalize()
   save_name(name)
   return f"Hey {name} ! Nice to meet you"

def show_name():
   data = load_memory()
   name = data.get("name")
   if name :
      return f"You are {name}"
   else :
      return "I don't know your name yet, sorry :)"


#Stores Preference in Memory
def save_preference(key,value):
   data = load_memory()

   if "pref" not in data:
     data["pref"]={}

   data["pref"][key] = value.capitalize()
   save_data(data)

def set_preference(user):
   if "my favorite colour is" in user:
      colour = user.replace("my favorite colour is","").strip()
      save_preference("colour",colour)
      return f"{colour.capitalize()}! Thats a nice choice"

   elif "my hobby is" in user: 
      hobby = user.replace("my hobby is","").strip()
      save_preference("hobby",hobby)
      return f"{hobby.capitalize()}? Oh! You got some interesting hobby"
   
   return "I didn't understand your preference"

def show_preference(item=None):
   pref = load_memory().get("pref",{})
   colour = pref.get("colour")
   hobby = pref.get("hobby")

   if item== "colour" :
      return f"Your favorite colour is {colour if colour else 'unknown'}"
   elif item== "hobby" :
      return f"Your hobby is {hobby if hobby else 'unknown'}"   
   else:
      return "Please specify your 'colour' or 'hobby' "
   

#Make Notes
def save_note(note):
   data = load_memory ()
   data.setdefault("notes", [])
   data["notes"].append(note)
   save_data(data)

def set_note(user):
   note = user.lower().replace("note this","").strip()
   if not note :
      return "Please tell me what to remember"
   save_note(note)
   return f"I've noted : {note}"

def show_note ():
   data = load_memory()
   notes = data.get("notes",[])
   if not notes :
      return "No notes save yet."
   output = "Your Note :\n"
   for item in notes:
      output += f"{item}\n"
   return output     

#History Function
def show_history():
   data = load_memory()
   history = ""

   for chat in data["memory"] :
     history += f"You: {chat['user']}\n"
     history += f"Calyx: {chat['bot']}\n\n"
   return history

#MY memory in Calyx
def remember_me():
   memory = load_memory()
   pref = memory.get("pref",{})
   name= memory.get("name")
   colour = pref.get("colour")
   hobby = pref.get("hobby")

   if not name and not colour and not hobby : 
      return "I don't know anything about you yet :)"
   return f"Your name is {name} \n You like {colour}\n And {name} your hobby is {hobby}."


      

