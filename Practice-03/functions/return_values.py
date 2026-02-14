#return values
def my_function(x, y):
  return x + y

#returning different data types
def my_function():
  return ["apple", "banana", "cherry"]

fruits = my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2]) 

#function that returns a tuple
def my_function():
  return (10, 20)

x, y = my_function()
print("x:", x)
print("y:", y) 
