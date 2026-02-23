def limited_cycle(lst, n):
    for _ in range(n):
        for item in lst:
            yield item

lst = input().split()
n = int(input())
print(*limited_cycle(lst, n))