#if statement
a = 33
b = 200
if b > a:
    print("b is greater than a")

#checking if a number is positive
number = 15
if number > 0:
    print("The number is positive")

#if statement without indentation
a = 33
b = 200
if b > a:
    print()
    # print("b is greater than a")  you will get an error

#multiple statements in an if block
age = 20
if age >= 18:
    print("You are an adult")
    print("You can vote")
    print("You have full legal rights")

#using a boolean variable
is_logged_in = True
if is_logged_in:
    print("Welcome back!")