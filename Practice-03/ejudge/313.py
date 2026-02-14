nums = list(map(int, input().split()))

def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

primes = list(filter(lambda x: is_prime(x), nums))

if primes:
    print(*primes)
else:
    print("No primes")