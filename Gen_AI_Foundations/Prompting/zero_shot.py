# Zero shot prompting

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

# Zero Shot Prompting: Directly giving the instructions or task to the model without further instructions
SYSTEM_PROMPT = "You should only and only ans the coding related questions. Do not ans anything else. Your name is Bruno. If user asks something other than coding, just say sorry."

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "Help me with my math homework"}
    ]
)

print(response.choices[0].message.content)