from commands import command
from process import process_commands
from storage import save_memory,log
def run_brain():
  while True:
    user = input("You: ").strip()

    log(f"USER INPUT : {user} ")
        
    user_modified = user.lower()
    result = None  


    try :
      result = process_commands(user,user_modified )      
      log(f"BOT RESPONSE: {result}")
       
      if result == "Goodbye!" :
            print ("Calyx:",result)
            break
      
      print ("Calyx:",result)
      save_memory(user,result)

    except Exception as e :
        log(f"ERROR: {e}")
        print(type(e))
        print("Error:",e)     