import re

text = input().rstrip()

matches = re.findall(r'\d{2,}', text)
print(" ".join(matches))