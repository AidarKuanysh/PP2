x = 5
y = "John"
print(x)
print(y)

x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0 

x = 5
y = "John"
print(type(x))
print(type(y)) 

x = "John"
# is the same as
x = 'John'

a = 4
A = "Sally"
#A will not overwrite a 

#legal variable names:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#illegal variable names:
# 2myvar = "John"
# my-var = "John"
# my var = "John"

#multiword variable names:
myVariableName = "John" #camel case
MyVariableName = "John" #pascal case
my_variable_name = "John" #snake case

#many values to many variables:
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#one value to multiple variables:
x = y = z = "Orange"
print(x)
print(y)
print(z)

#unpack a collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#output variables
x = "Python is awesome"
print(x)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

x = 5
y = 10
print(x + y)

#error combining string and integer
# x = 5
# y = "John"
# print(x + y)

x = 5
y = "John"
print(x, y)

#global variables
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc() 

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x) 

#global keyword

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x) 

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x) 