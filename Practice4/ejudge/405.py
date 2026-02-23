n = int(input())

def countdown(start):
    i = start
    while i >= 0:
        yield i
        i -= 1

for value in countdown(n):
    print(value)