from Commands.name_remember_me import show_name,show_history,remember_me
from Commands.note_preference import show_note,show_preference
from Commands.basic import the_creation_of_calyx,greeting,hello, name,bye,help_menu
from Commands.web_app_open import open_calculator,open_chrome,open_file,open_vs_code,open_command,open_notepad,open_fb,open_google,open_insta,open_yt
from Memory.storage import Memory
from Commands.time_calc import get_date,get_time,calc
from Commands.task import TaskManager
memory = Memory()
task = TaskManager(memory)
command = {
    "hey":hello,
    "sup":hello,
    "hello":hello,
    "good morning":greeting,
    "good afternoon":greeting,
    "good evening":greeting,
    "who are you":name,
    "what is your name":name,
    "bye":bye,
    "exit":bye,
    "good night":bye,
    "thanks":lambda:"My pleasure",
    "help" : help_menu,
    "calc" : calc,
    "time" : get_time,
    "date" : get_date,
    "what is my name" : show_name,
    "who am i": show_name,
    "what is my hobby" :lambda: show_preference("hobby"),
    "what is my favorite colour" :lambda: show_preference("colour"),
    "show history" : show_history,
    "history" : show_history,
    "what you know about me" : remember_me,
    "remember me" : remember_me, 
    "reset" : memory.reset,
    "when was calyx created" : the_creation_of_calyx ,
    "born" : the_creation_of_calyx,
    "start" : the_creation_of_calyx,
    "yt" : open_yt,
    "fb" : open_fb,
    "google" : open_google,
    "insta" : open_insta,
    "chrome" : open_chrome,
    "calc app": open_calculator,
    "file" : open_file,
    "vs code" : open_vs_code,
    "cmd" : open_command,
    "notepad" : open_notepad,
    "note" : show_note,
}

