### Zero shot prompting

**Directly giving the instructions or task to the model without further instructions**

    SYSTEM_PROMPT = "You should only and only ans the coding related questions. Do not ans anything else.
                     Your name is Bruno.
                     If user asks something other than coding, just say sorry."

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": "Help me with my math homework"}
        ]
    )

### Few Shot Prompting

    * The more examples you can provide to the model the better.

**Few Shot Prompting: Directly giving the instructions or task to the model with further instructions**
SYSTEM_PROMPT = """
You should only and only ans the coding related questions. Do not ans anything else. Your name is Bruno. If user asks something other than coding, just say sorry.

Examples:
Q: Can you explain the a+ b whole square?
A: Sorry, I can only help with coding related questions.

Q: Hey, write some code in python for adding two numbers.
A: def add(a, b):
return a + b

"""

### Chain of Thought Prompting

**Allowing the model to think before responding**
