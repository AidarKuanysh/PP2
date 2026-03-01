import re

text = input().rstrip()

words = re.findall(r'[A-Z]', text)
print(len(words))