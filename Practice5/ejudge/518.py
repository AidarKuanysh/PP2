import re

text = input()       
pattern = input()    

escaped = re.escape(pattern)
matches = re.findall(escaped, text)
print(len(matches))