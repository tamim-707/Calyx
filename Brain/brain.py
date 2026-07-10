from Brain.processor import process_commands
from Memory.storage import Memory
from Commands.context  import Context
from Utils.logger import log
from LLM.groq_api import ask_groq
from Utils.input import get_input
from Utils.helper import reply
from Utils.speech import speech_to_text
def run_brain():
  memory = Memory()
  context = Context()
  while True:
    user = get_input("text")
    
    if not user :
       continue
    log("INFO" , f"USER INPUT : {user} ")
        
    user_modified = user.lower()
    result = None  


    try :
      result = process_commands(user,user_modified,context )      
       
      if result == "Goodbye!" :
            reply(result)
            memory.save_chat(user,result)
            break
      elif result is None :
         result = ask_groq(user)

      log("INFO" , f"BOT RESPONSE: {result}")

      reply(result)
      memory.save_chat(user,result)

  

    except Exception as e :
        log("ERROR", f"{e}")
        print(type(e))
        print("Error:" ,e)     