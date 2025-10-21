import tiktoken

# Encoder
enc = tiktoken.encoding_for_model("gpt-4o")

text = "Hey there! My name is Darryl Rachel"
tokens = enc.encode(text)

print("Tokens,", tokens)
# output: Tokens, [25216, 1354, 0, 3673, 1308, 382, 17214, 93031, 52043]

decoded = enc.decode([25216, 1354, 0, 3673, 1308, 382, 17214, 93031, 52043])
print("Decoded,", decoded)