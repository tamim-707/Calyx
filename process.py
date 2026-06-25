from commands import command
from func import set_name , set_preference , set_note 
from personality import set_personality
from perm_func import  hello 
from api_func import get_weather,get_news

def process_commands(user,user_modified) :
 if user_modified.startswith("my name is "):
        return set_name(user)

 elif user_modified.startswith("note this"):
        return set_note(user) 

 elif "my favorite colour is" in user_modified or "my hobby is" in user_modified :
       return set_preference(user)
 

 
 elif user_modified.startswith("weather of "):
       city = user_modified.replace("weather of ","").strip()
       return get_weather(city)
 
 elif user_modified.startswith("news of "):
       text = user_modified.replace("news of ","").strip()
       if "in" not in text :
         return "Type like this 'news of sports in us'"

       parts = text.split(" in ")
       category = parts[0].strip()
       country = parts[1].strip()

       return get_news(category,country)
 
 elif user_modified.startswith("change to ") :
       mode = user_modified.replace("change to ","")
       
       return set_personality(mode)
 
 elif "hi" in user_modified.split():
       return hello()
 
 for key in sorted(command,key=len,reverse=True):
      if key in user_modified :
           return command[key]()
                              
 return "Unknown command. Type 'help' for Command List"
 