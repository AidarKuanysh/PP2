n = int(input())

is_valid = True
n = abs(n)

if n == 0:
    is_valid = True 
else:
    while n > 0:
        digit = n % 10
        if digit % 2 != 0:
            is_valid = False
            break
        n //= 10

if is_valid:
    print("Valid")
else:
    print("Not valid")