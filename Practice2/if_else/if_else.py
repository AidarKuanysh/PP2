#the else keyword
a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

#else without elif
a = 200
b = 33
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

#checking even or odd numbers
number = 7
if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

#temperature classifier (If-Elif-Else Chain)
temperature = 22
if temperature > 30:
    print("it's hot outside!")
elif temperature > 20:
    print("it's warm outside")
elif temperature > 10:
    print("it's cool outside")
else:
    print("it's cold outside")

#else as fallback
username = "Emil"
if len(username) > 0:
    print(f"Welcome, {username}!")
else:
    print("Error: Username cannot be empty")