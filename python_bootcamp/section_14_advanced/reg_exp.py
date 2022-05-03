import re

text = "The agent's phone number is 408-555-1234. Call soon!"

pattern = r'\d{3}-\d{3}-\d{4}'
match = re.search(pattern, text)
print(match.span())
print(match.start())
print(match.end())

pattern = 'not in text'

print(re.search(pattern, text))
