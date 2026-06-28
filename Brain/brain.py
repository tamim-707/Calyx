from Commands.commands import command
from Brain.processor import process_commands
from Memory.storage import save_memory
from Utils.logger import log
def run_brain():
  while True:
    user = input("You: ").strip()

    log("INFO" , f"USER INPUT : {user} ")
        
    user_modified = user.lower()
    result = None  


    try :
      result = process_commands(user,user_modified )      
      log("INFO" , f"BOT RESPONSE: {result}")
       
      if result == "Goodbye!" :
            print ("Calyx:",result)
            break
      
      print ("Calyx:",result)
      save_memory(user,result)

    except Exception as e :
        log("ERROR", f"{e}")
        print(type(e))
        print("Error:" ,e)     