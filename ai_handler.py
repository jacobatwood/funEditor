from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def stringTranslation(input, language):
    prompt = f'Convert the following sentnce into {language} - "{input}" -- only output the text'
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a text conversation assistant"},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()
