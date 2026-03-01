import re

text = input().rstrip()

words = re.findall(r'\b\w{3}\b', text)
print(len(words))