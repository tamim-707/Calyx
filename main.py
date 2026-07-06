from Utils.helper import load_config 
# from Commands.basic import start_up
from Brain.brain import run_brain

# start_up()
assistant_name = load_config()["assistant_name"]
print (f"Hey there! {assistant_name} v1.0 here.....")

run_brain()