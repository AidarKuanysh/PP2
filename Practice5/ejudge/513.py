import re

text = input().rstrip()

words = re.findall(r'\w+', text)
print(len(words))