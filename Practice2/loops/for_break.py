#the break statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

#exit loop when x is banana
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)

#break the loop when x is 3
for x in range(6):
    if x == 3: break
    print(x)
else:
    print("Finally finished!") 

