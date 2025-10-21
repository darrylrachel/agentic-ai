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

response = client.chat.completions.create(
    model="gpt-4o-mini",
    response_format={"type": "json_object"},
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "Hey, write some code in python to add n numbers."},

        # Adding to the memory manually
        {"role": "assistant", "content": json.dumps({"Steps": "START", "content": "The user is asking for Python code to add n numbers."})},
        {"role": "assistant", "content": json.dumps({"Steps": "PLAN", "content": "First, we need to find a way to accept multiple numbers as input from the user."})},
        {"role": "assistant", "content": json.dumps({"Steps": "PLAN", "content": "We can use a loop to repeatedly ask the user for numbers until they choose to stop."})},
        {"role": "assistant", "content": json.dumps({"Steps": "PLAN", "content": "Next, we should convert the input numbers from strings to integers or floats for addition."})},
        {"role": "assistant", "content": json.dumps({"Steps": "PLAN", "content": "Finally, we will accumulate the sum of these numbers and display the result."})},
        {"role": "assistant", "content": json.dumps({"Steps": "PLAN", "content": "Let's outline the code structure that encapsulates all these steps."})},
        {"role": "assistant", "content": json.dumps({"Steps": "PLAN", "content": "We can use a list to store the numbers entered by the user and use a 'while' loop for continuous input."})},
        {"role": "assistant", "content": json.dumps({"Steps": "PLAN", "content": "Here is the Python code to add n numbers: \n\n```python\nsum = 0\nwhile True:\n    num = input('Enter a number (or type "    ,  " to stop): ')\n    if num.lower() == 'exit':\n        break\n    sum += float(num)  # Convert the input to float and add it to the sum\nprint('The total sum is:', sum)\n```."  :  "The user has asked for code to add multiple numbers, so we provided that with clear steps defined in the code."})},
        
        # OUTPUT
        {"role": "assistant", "content": json.dumps({"Steps": "OUTPUT", "content": "Here is the Python code to add n numbers:\n\n```python\nsum = 0\nwhile True:\n    num = input('Enter a number (or type \"exit\" to stop): ')\n    if num.lower() == 'exit':\n        break\n    sum += float(num)  # Convert the input to float and add it to the sum\nprint('The total sum is:', sum)\n```"})},
    ]
)

print(response.choices[0].message.content)