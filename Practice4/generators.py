#ex 1
def square_gen(n):
    for i in range(n + 1):
        yield i * i


#ex 2
def even_gen(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i


#ex 3
def div3and4_gen(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i


#ex 4
def squares(a, b):
    for i in range(a, b + 1):
        yield i * i


#ex 5
def countdown(n):
    while n >= 0:
        yield n
        n -= 1


n = int(input())
print(",".join(str(x) for x in even_gen(n)))

print(" ".join(str(x) for x in div3and4_gen(n)))

a, b = map(int, input().split())
for v in squares(a, b):
    print(v)

n2 = int(input())
for v in countdown(n2):
    print(v)