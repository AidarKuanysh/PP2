import re

text = input().rstrip()

result = re.sub(r'\d', lambda m: m.group() * 2, text)
print(result)