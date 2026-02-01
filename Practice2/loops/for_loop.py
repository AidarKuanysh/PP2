#for loops
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

#looping through a string
for x in "banana":
    print(x) 

#the range function
for x in range(6):
    print(x)
#using the start parameter
for x in range(2, 6):
    print(x)
#increment the sequence with 3
for x in range(2, 30, 3):
    print(x)

#else in for loop
for x in range(6):
    print(x)
else:
    print("Finally finished!")

#nested loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)

#the pass statement
for x in [0, 1, 2]:
    pass