input()
a = list(map(int, input().split()))
t = 0
for i in a:
    if i % 2 == 0:
        t += 1
print(t)