#the continue statement
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

#example:
#skip even numbers
x = 0
while x < 15:
    x += 1
    if x % 2 == 0:
        continue
    print(x)
print()
