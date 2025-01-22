from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environmental variables
load_dotenv()

# Create an instance of the OpenAI class
openAI = OpenAI(api_key = os.getenv('OPENAI_API_KEY'))

# Define a function that generates text using the OpenAi API
def generate_text_basic(prompt: str, model='gpt-3.5-turbo', system_prompt: str = ''):
    response = openAI.chat.completions.create(
        model = model,
        messages=[
                {'role':'system','content': system_prompt},
                {'role':'user','content': prompt}
        ]
    )
    return response.choices[0].message.content