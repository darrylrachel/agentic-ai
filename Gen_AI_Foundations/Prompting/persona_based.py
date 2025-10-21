# Persona Based Prompting
# Used as way to make the model respond in a certain tone

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()

SYSTEM_PROMPT = """
    You are an AI Persona Assistant named Bruno.
    You are acting on the behalf of Burno the bodybuilding coach who has 20 years of experience.

    Example:
    Q: Hey Bruno
    A: Hey, what's up! 
"""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    response_format={"type": "json_object"},
    messages=[
        { "role": "system", "content": SYSTEM_PROMPT },
        { "role": "user", "content": "Hey, there"}
    ]
)

print("Response:", response.choices[0].message.content)