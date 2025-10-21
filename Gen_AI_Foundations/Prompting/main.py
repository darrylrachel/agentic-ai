from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are an expert in Math and only answer math related question. If the query is not related to math, just don't answer and say sorry and do not answer"}
        {"role": "user", "content": "Help me with my math homework"}
    ]
)

print(response.choices[0].message.content)