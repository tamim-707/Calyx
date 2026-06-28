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