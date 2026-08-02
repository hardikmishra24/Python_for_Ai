from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

#Creating a list named as conversation which stores the chatbot memory
coversation = [] 
def chat(user_message):
    converation.append({"role": "user", "parts": [{"text": user_message}]})



client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="HI my name is hardik remember it "
)

print(interaction.output_text)