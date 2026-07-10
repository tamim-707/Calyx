#Logging system (debugging history)
from datetime import datetime
def log(level,message):
   time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

   with open("calyx.log","a",encoding="utf-8") as file:
      file.write(f"[{level}] [{time}] {message}\n")