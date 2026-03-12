input()
xc = False
a = list(map(int, input().split()))
for f in a:
    if f < 0:
        xc = True
        break
if xc:
    print("No")
else:
    print("Yes")