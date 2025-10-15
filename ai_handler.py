from openai import OpenAI
import os
from dotenv import load_dotenv

#retrieves the OpenAI API key from the environment
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


##sends the string to ChatGPT for translation
def string_translation(input, language):
    prompt = f'Convert the following sentnce into {language}: {input}\nonly output the text without quotes or punctuation'
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a text conversation assistant"},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()
