input()
a = list(map(str, input().split()))
maxl = -1
ind = 0
for c in range(len(a)):
    if len(a[c]) > maxl:
        maxl = len(a[c])
        ind = c
print(a[ind])