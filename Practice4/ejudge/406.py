n = int(input())

def fibonacci(count):
    a, b = 0, 1
    i = 0
    while i < count:
        yield str(a)
        a, b = b, a + b
        i += 1

first = True
for num in fibonacci(n):
    if first:
        print(num, end="")
        first = False
    else:
        print("," + num, end="")