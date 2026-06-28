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
   return "Opening Notepad....."

def open_vs_code():
   subprocess.Popen("code", shell=True)
   return "Opening VS Code ....."

def open_command():
   subprocess.Popen("start cmd", shell=True)
   return "Opening Command Prompt ....."
