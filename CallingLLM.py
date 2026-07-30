from google import genai
from dotenv import load_dotenv


load_dotenv()


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

    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    return response.text


print(recipe("tomato, onion, paneer", "Indian", "Vegetarian"))