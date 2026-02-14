#function with one argument
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus") 

#parametres vs arguments
def my_function(name): # name is a parameter
  print("Hello", name)

my_function("Emil") # "Emil" is an argument 

#number of arguments
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes") 

#default parameter values
def my_function(name = "friend"):
  print("Hello", name)

my_function("Emil")
my_function("Tobias")
my_function()
my_function("Linus") 

#default value for country parameter
def my_function(country = "Norway"):
  print("I am from", country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil") 

#keyword arguments
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(animal = "dog", name = "Buddy") 

#order of arguments doesn't matter
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(name = "Buddy", animal = "dog") 

#positional arguments
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function("dog", "Buddy") 

#order matters with positional arguments
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function("Buddy", "dog") 

#mixing positional and keyword arguments
def my_function(animal, name, age):
  print("I have a", age, "year old", animal, "named", name)

my_function("dog", name = "Buddy", age = 5)

#passing different data types
def my_function(fruits):
  for fruit in fruits:
    print(fruit)

my_fruits = ["apple", "banana", "cherry"]
my_function(my_fruits) 

#sending dictionary as a argument
def my_function(person):
  print("Name:", person["name"])
  print("Age:", person["age"])

my_person = {"name": "Emil", "age": 25}
my_function(my_person) 

result = my_function(5, 3)
print(result) 

#positional-only arguments
def my_function(name, /):
  print("Hello", name)

my_function("Emil") 

#we allowed to use keyword arguments even 
#if this function expects positional arguments
def my_function(name):
  print("Hello", name)

my_function(name = "Emil") 

#keyword-only arguments
def my_function(*, name):
  print("Hello", name)

my_function(name = "Emil") 

#combining positional-only and keyword-only
def my_function(a, b, /, *, c, d):
  return a + b + c + d

result = my_function(5, 10, c = 15, d = 20)
print(result) 