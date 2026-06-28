from Commands.commands import command
from Commands.name_remember_me import set_name 
from Commands.note_preference import set_preference ,set_note
from Utils.personality import set_personality
from Commands.basic import  hello 
from API.weather_api import get_weather
from API.news_api import get_news
from Commands.web_app_open import open_calculator,open_chrome,open_command,open_fb,open_file,open_google,open_insta,open_notepad,open_vs_code,open_yt

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
 
 elif user_modified.startswith("open "):
      target = user_modified.replace("open ","").strip()
      open_map = {
           "youtube" : open_yt,
           "yt" : open_yt,
           "fb" : open_fb,
           "facebook" : open_fb,
           "insta" : open_insta,
           "instagram" : open_insta,
           "file" : open_file,
           "google" : open_google,
           "calcultor" : open_calculator,
           "chrome" : open_chrome,
           "Command" : open_command,
           "cmd" : open_command,
           "notepad" : open_notepad,
           "VS Code" : open_vs_code
      }
      if target in open_map :
           return open_map[target]()
      else :
          return f"I don't know how to open {target}"
      
 for key in sorted(command,key=len,reverse=True):
      if key in user_modified :
           return command[key]()
                              
 return "Unknown command. Type 'help' for Command List"
 