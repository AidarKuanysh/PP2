import sys

n = int(sys.stdin.readline())

def even_numbers(limit):
    i = 0
    while i <= limit:
        yield str(i)
        i += 2

first = True
for num in even_numbers(n):
    if first:
        sys.stdout.write(num)
        first = False
    else:
        sys.stdout.write("," + num)