from personality import get_personalities, personalities
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

#Basic Commands Function
def greeting():
   mode = get_personalities()
   return personalities[mode]["greeting"]

def hello():
   mode = get_personalities()
   return personalities[mode]["hello"]

def name():
   mode = get_personalities()
   return personalities[mode]["name"] 

def bye():
   return"Goodbye!"

def help_menu():
   return "Command\n Chat list:\n • hi, hello, sup, hey\n • good morning, good afternoon, good evening, good night\n • what is your name, who are you, name\n • thanks\n Calculation:\n • calc\n Clock:\n • time\n • date\n Exit:\n • bye, exit\n"


#Basic Calculator Function
def calc():
    try:
     ques = input("Question: ")
     result = eval(ques)
     return f"Answer is {result}"
    except:
     return "Invalid expression.."


#Basic Data and Time Function
from datetime import datetime
def get_time():
   t = datetime.now().strftime("%I:%M:%S %p")
   return f"Current time is: {t}"
def get_date():
   x = datetime.now().strftime("%A,%d,%B,%Y")
   return f"Today's date is: {x}"

#Web Opening
import webbrowser
def open_yt():
   webbrowser.open("http://www.youtube.com")
   return "Youtube is opening...."

def open_google():
   webbrowser.open("http://www.google.com")
   return "Google is opening....."

def open_fb():
   webbrowser.open("http://www.facebook.com")
   return "Facebook is opening....."

def open_insta():
   webbrowser.open("http://www.instagram.com")
   return "Instagram is opening...."

#App Opening
import subprocess
def open_chrome():
   subprocess.Popen("start chrome", shell=True)
   return "Opening Chrome ....."

def open_file():
   subprocess.Popen("explorer", shell=True)
   return "Opening File Explorer....."

def open_calculator():
   subprocess.Popen("calc", shell=True)
   return "Opening Calculator ....."

def open_notepad():
   subprocess.Popen("notepad", shell=True)
   return "Notepad File Explorer....."

def open_vs_code():
   subprocess.Popen("code", shell=True)
   return "Opening VS Code ....."

def open_command():
   subprocess.Popen("start cmd", shell=True)
   return "Opening Command Prompt ....."
