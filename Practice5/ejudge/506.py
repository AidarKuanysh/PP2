import re

text = input().rstrip()

match = re.search(r'\S+@\S+\.\S+', text)
if match:
    print(match.group())
else:
    print("No email")