from Brain.processor import process_commands
from Memory.storage import Memory
from Commands.context  import Context
from Utils.logger import log
from LLM.groq_api import ask_groq
def run_brain():
  memory = Memory()
  context = Context()
  while True:
    user = input("You: ").strip()

    log("INFO" , f"USER INPUT : {user} ")
        
    user_modified = user.lower()
    result = None  


    try :
      result = process_commands(user,user_modified,context )      
      log("INFO" , f"BOT RESPONSE: {result}")
       
      if result == "Goodbye!" :
            print ("Calyx:",result)
            memory.save_chat(user,result)
            break
      elif result is None :
         result = ask_groq(user)

      print ("Calyx:",result)
      memory.save_chat(user,result)

  

    except Exception as e :
        log("ERROR", f"{e}")
        print(type(e))
        print("Error:" ,e)     