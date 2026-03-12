input()
a = list(map(int, input().split()))
t = 0
for i in a:
    t += i * i
print(t)