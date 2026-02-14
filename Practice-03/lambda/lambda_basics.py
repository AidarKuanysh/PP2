#lambda functions
x = lambda a : a + 10
print(x(5)) 

#multiple argument a with argument b and return the result
x = lambda a, b : a * b
print(x(5, 6)) 

#summarize argument a, b and c and return the result
x = lambda a, b, c : a + b + c
print(x(5, 6, 2)) 

#why use lambda functions
def myfunc(n):
  return lambda a : a * n 

#function that doubles the number that you send in
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

#function that triples the number that you send in
def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11))

#function definition to make both functions
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))


