# Prompt Styles

### ChatML

{
"role": "system" | "user" | "assistant"
"content": "string"
}

Example:
messages=[
{"role": "system", "content": SYSTEM_PROMPT},
{"role": "user", "content": "Hey, can you explain a + b whole square?"}
]

## Alpaca Prompt

### Instructions: <SYSTEM_PROMPT>\n

### Input: <USER_QUERY>

### Response:\n
