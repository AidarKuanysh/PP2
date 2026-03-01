import re
a = input()
if len(re.findall("cat|dog", a)) > 0:
    print("Yes")
else:
    print("No")