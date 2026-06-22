from groq import Groq 
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()  # loads the .env file

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))


print(" chatbot (Groq streaming): Type 'quit', 'exit' or 'bye' to stop \n")

while True:
    user_input=input("you: ")
    if user_input.lower() in ["quit", "exit","bye"]:
        print("\n chatbot: goodbye!")
        break

    print(" chatbot: ", end="", flush=True)
    stream = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "you are a helpful chatbot."},
            {"role": "user", "content": user_input}
        ],
        stream=True 
    )

    for chunk in stream:
        if chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end="", flush=True)

    print()