from google import genai
from dotenv import load_dotenv
import os

load_dotenv()  # It will load the env file which contains the API key.  

# Here we have defined a function called recipe that takes three parameters: ingredients, cuisine, diet. The function generates a recipe based on the provided ingredients, cuisine, and diet preferences.
# It uses an f-string to create a prompt that is sent to the Gemini API for content generation. The response from the API is then returned as the output of the function. Finally, we call the recipe function with specific parameters and print the result.
# Function recipe is defined till return response.text .
def recipe(ingredients, cuisine, diet):
    '''
    Generate a recipe based on the provided ingredients.
    cuisine can be indian, italian, or mexican.
    and diet can be vegetarian, vegan, or non-vegetarian.
    ''' #-> This line represents dockstring for the function, explaining its purpose and parameters. It is different from comments and is only used after the function, class or method definiton.

    # f-string inserts variable values directly into the string
    prompt = f"""
    Generate a recipe using these ingredients: {ingredients}.
    The recipe should not be more than 100 words.
    Cuisine: {cuisine}
    Diet: {diet}
    """

    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))  # Here we have created an object from class Client which is located in genai module and stored object reference inside the variable named client. 
    #Client is responsible for connecting the client to the llm model by using the api key

    try:
        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt
        )
    except Exception as e: #Catch any exception. Store it inside variable e.  
        return f"An error occurred: {e}"

    return response.text


print(recipe("tomato, onion, paneer", "Indian", "Vegetarian"))