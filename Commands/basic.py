from Utils.personality import get_personalities, personalities, get_response
from datetime import datetime
import time
#The Beginning
def the_creation_of_calyx() :
    start_date = datetime(2026 , 6 , 19 , 19 , 5 , 0)
    today = datetime.now()
    differ = (today - start_date)
    days = differ.days
    hours = differ.seconds // 3600
    minutes =( differ.seconds % 3600 ) // 60
    sec = (differ.seconds % 60)

    return f"Friday,19th June, 2026\nThat was {days} days, {hours} hours, {minutes} minutes,{sec} seconds ago "

#start up
import time

def start_up():
    step = "Loading memory...."
    print(step, end="", flush=True)
    time.sleep(1)
    print("\r" + " " * len(step), end="\r")

    step = "Loading API...."
    print(step, end="", flush=True)
    time.sleep(1)
    print("\r" + " " * len(step), end="\r")

    step = "Initializing commands...."
    print(step, end="", flush=True)
    time.sleep(1)
    print("\r" + " " * len(step), end="\r")

#Basic Commands Function
def greeting():
   mode = get_personalities()
   return get_response("greeting")

def hello():
   mode = get_personalities()
   return get_response("hello")

def name():
   mode = get_personalities()
   return get_response("name")

def bye():
   return"Goodbye!"

def help_menu():
   return "Command\n Chat list:\n • hi, hello, sup, hey\n • good morning, good afternoon, good evening, good night\n • what is your name, who are you, name\n • thanks\n Calculation:\n • calc\n Clock:\n • time\n • date\n Exit:\n • bye, exit\n"




