from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

# Creating a list named conversation which stores the chatbot memory
conversation = []

def chat(user_message):
    conversation.append({
        "role": "user",
        "parts": [{"text": user_message}]
    })

    print(conversation)

    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    try:
        interaction = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=conversation
        )

        conversation.append({"role": "model", "parts": [{"text": interaction.text}]})


        print(interaction.text)

    except Exception as e:
        print(f"An error occurred: {e}")


chat("Hi, my name is Hardik. Remember it.")
chat("What's my name?")
