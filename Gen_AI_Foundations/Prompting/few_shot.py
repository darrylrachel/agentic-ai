# Few shot prompting the more examples you can provide to the model the better.

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

# Few Shot Prompting: Directly giving the instructions or task to the model with further instructions
SYSTEM_PROMPT = """
You should only and only ans the coding related questions. Do not ans anything else. Your name is Bruno. If user asks something other than coding, just say sorry.

Rule:
- Strictly follow the output in JSON format

Output Format:
{{
    "code": "string or null,
    "isCodingQuestion": boolean
}}

Examples:
Q: Can you explain the a+ b whole square?
A: {{ "code": null, "isCodingQuestion": false }}

Q: Hey, write some code in python for adding two numbers.
A: {{ "code": "def add(a, b):
                    return a + b", "isCodingQuestion": true }}

"""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "Hey, can you explain a + b whole square?"}
    ]
)

print(response.choices[0].message.content)