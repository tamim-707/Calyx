from groq import Groq
import os
from dotenv import load_dotenv
load_dotenv()

client = Groq(api_key=os.getenv("groq_api_key"))

def ask_groq(prompt):
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {                                                                           #multi line string   """ ...."""     
                    "role" : "system",                                                                      
                    "content" : """                                                                          
                    You are Calyx personal an AI agent,created by Md. Rafiul Islam (Tamim)
                    Your personality:
                    -smart but casual
                    -short and sharp
                    -Calm
                    -Humble
                    -Concise
                    -Joyful
                    Rules:
                    -Keep answer short unless user ask detailed answer
                    -If you dont know anthing say honestly
                    -Be clear and practical
                    -Try to give answers using bullets
                    """
                },

                {
                    "role": "user",
                    "content": prompt
                }
            ],
            model="llama-3.1-8b-instant"
        )

        return chat_completion.choices[0].message.content

    except Exception as e:
        return f"Groq Error: {e}"