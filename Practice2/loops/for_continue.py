#the continue statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

#examples:
#skip even numbers
for num in range(1, 11):
    if num % 2 == 0:
        continue
    print(num)

#skip t symbol in string
for char in "python":
    if char == "t":
        continue
    print(char)