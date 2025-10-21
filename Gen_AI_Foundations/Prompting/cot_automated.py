# Chain of thought prompting

from dotenv import load_dotenv
from openai import OpenAI
import json

load_dotenv()

client = OpenAI()

# Few Shot Prompting: Directly giving the instructions or task to the model with further instructions
SYSTEM_PROMPT = """
    You're an expert AI assistant in resolving user queries using chain of thought.
    You work on the START, PLAN and OUTPUT steps.
    You need to first PLAN what needs to be done. The PLAN can be multiple steps.
    Once you are done with the PLAN, finally give an OUTPUT.

    Rules:
    - Strictly follow the given JSON output format
    - Only run one step at a time
    - The sequence of steps are START (where user gives an input), PLAN (that can be multiple times) and finally OUTPUT (which is going to be displayed to the user).

    Output JSON Format:
    { "Steps":  "START" | "PLAN" | "OUTPUT", "content": "string" }

    Example:
    START: Hey, can you solve 2 + 3 * 5 / 10
    PLAN: { "Step": "PLAN": "content": "Seems like the user is interested in a math problem." }
    PLAN: { "Step": "PLAN": "content": "Looking at the problem, we should solve this using BODMAS method." }
    PLAN: { "Step": "PLAN": "content": "Yes, the BODMAS is correct thing to be done here." }
    PLAN: { "Step": "PLAN": "content": "First we must multiply 3 * 5 which is 15" }
    PLAN: { "Step": "PLAN": "content": "Now the new equation is 2 + 15 / 10" }
    PLAN: { "Step": "PLAN": "content": "We must now perform division of 15 /10 = 1.5" }
    PLAN: { "Step": "PLAN": "content": "Now the new equation is 2 + 1.5" }
    PLAN: { "Step": "PLAN": "content": "Now finally lets perform the addition" }
    PLAN: { "Step": "PLAN": "content": "Great, we have solved and finally and left with 3.5 as answer" }
    OUTPUT: { "Step": "OUTPUT": "content": "3.5" }
    
"""

print("\n\n\n")

message_history = [
    {"role": "system", "content": SYSTEM_PROMPT},
]

user_query = input("👉 Type something... ")
message_history.append({ "role": "user", "content": user_query})

while True:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        response_format={"type": "json_object"},
        messages=message_history
    )

    raw_result = response.choices[0].message.content
    message_history.append({"role": "assistant", "content": raw_result})

    parsed_result = json.loads(raw_result)

    if parsed_result.get("Steps") == "START":
        print("🔥", parsed_result.get("content"))
        continue

    if parsed_result.get("Steps") == "PLAN":
        print("🧠", parsed_result.get("content") )
        continue

    if parsed_result.get("Steps") == "OUTPUT":
        print("🤖", parsed_result.get("content") )  
        break

print("\n\n\n")