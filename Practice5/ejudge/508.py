import re
a = input()
d = input()
for i in range(len(re.split(d,a))):
    if i != (len(re.split(d,a))-1):
        print(re.split(d,a)[i], end=',')
    else:
        print(re.split(d,a)[i])