import re

pattern = "Hello"
a = input()
if re.match(pattern, a):
    print("Yes")
else:
    print("No")