import re

text = input().rstrip()

match = re.search(r'Name:\s*(.+),\s*Age:\s*(.+)', text)
if match:
    name, age = match.groups()
    print(name, age)