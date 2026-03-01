import re
a = input()
if re.match("^[a-zA-Z].*[0-9]$", a):
    print("Yes")
else:
    print("No")