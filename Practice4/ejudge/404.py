a, b = map(int, input().split())

def squares(a, b):
    i = a
    while i <= b:
        yield i * i
        i += 1

for value in squares(a, b):
    print(value)