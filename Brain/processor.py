from Commands.commands import command
from Commands.time_calc import  get_time, get_date
from Commands.name_remember_me import set_name 
from Commands.note_preference import set_preference ,set_note
from Utils.personality import set_personality
from Commands.basic import  hello , the_creation_of_calyx , bye
from API.weather_api import get_weather
from API.news_api import get_news
from Commands.context import Context
from Commands.task import TaskManager
from Memory.storage import Memory
from Commands.open_google import google_search
from Commands.web_search import web_search
from Commands.monitoring import get_battery,get_cpu,get_ram
from Commands.web_app_open import open_calculator,open_chrome,open_command,open_google,open_fb,open_file,open_insta,open_notepad,open_vs_code,open_yt
memory = Memory()
task = TaskManager(memory)

def process_commands(user,user_modified,context) :
 if user_modified.startswith("my name is "):
        return set_name(user)
  
  #Web search
 elif user_modified.startswith("search web "):
    query = user[11:].strip()
    print("Searching:", query)
    return web_search(query)

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
 elif "time" in user_modified:
    return get_time()
 elif "date" in user_modified:
    return get_date()
 elif "creation of calyx" in user_modified:
    return the_creation_of_calyx()
 elif "bye" in user_modified:
    return bye()
 elif "exit" in user_modified:
    return bye()
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
           "calculator" : open_calculator,
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
      
#Context
 elif "python" in user_modified :
      context.set_topic("python")
      return "Python is a programming language"
 elif "who created it" in user_modified:
    topic = context.get_topic()

    if topic == "python":
        return "Guido van Rossum created Python."

    return "I don't know what 'it' refers to."
 
#task Manager
 elif user_modified.startswith("add task"):
    task_text = user.replace("add task", "").strip()
    return task.add_task(task_text)

 elif user_modified == "show tasks":
    return task.show_tasks()

 elif user_modified.startswith("mark task"):
    try:
        task_number = int(user_modified.split()[2])
        return task.mark_done(task_number)
    except:
        return "Invalid command."

 elif user_modified.startswith("delete task"):
    try:
        task_number = int(user_modified.split()[2])
        return task.delete_task(task_number)
    except:
         return "Invalid command."
 
 #Google Search
 elif user_modified.startswith("google,") :
     query = user.replace("google,","").strip()
     google_search(query)
     return f"Searching google for {query}"
 elif user_modified.startswith("google ") :
     query = user.replace("google ","").strip()
     google_search(query)
     return f"Searching google for {query}"
 elif user_modified.startswith("google") :
     query = user.replace("google","").strip()
     google_search(query)
     return f"Searching google for {query}"
 


#Monitoring
 elif "CPU" in user :
     return get_cpu ()
 elif "battery" in user :
     return get_battery ()
 elif "RAM" in user :
     return get_ram ()
 #command key    
#  for key in sorted(command,key=len,reverse=True):
#       if key in user_modified :
#            return command[key]()
 
#  return None
