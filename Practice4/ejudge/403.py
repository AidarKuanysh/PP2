n = int(input())

def divisible_numbers(limit):
    i = 0
    while i <= limit:
        if i % 12 == 0:
            yield i
        i += 1

first = True
for num in divisible_numbers(n):
    if first:
        print(num, end="")
        first = False
    else:
        print(" " + str(num), end="")