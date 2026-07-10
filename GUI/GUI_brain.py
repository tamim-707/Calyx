from Brain.processor import process_commands
from Commands.context import Context
from LLM.groq_api import ask_groq

context = Context()

def process_message(user):
    user_modified = user.lower()

    result = process_commands(user, user_modified, context)

    if result is None:
        result = ask_groq(user)

    return result