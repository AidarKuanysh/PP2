#type function
x = 5
print(type(x))

#str
x = "Hello World"
print(type(x))
#int
x = 20
print(type(x))
#float
x = 20.5	
print(type(x))
#ccomplex
x = 1j
print(type(x))
#list
x = ["apple", "banana", "cherry"]
print(type(x))
#tuple
x = ("apple", "banana", "cherry") 
print(type(x))
#range
x = range(6) 
print(type(x))
#dict
x = {"name" : "John", "age" : 36} 
print(type(x))
#set
x = {"apple", "banana", "cherry"} 
print(type(x))
#frozenset
x = frozenset({"apple", "banana", "cherry"}) 
print(type(x))
#bool
x = True 
print(type(x))
#bytes
x = b"Hello" 
print(type(x))
#bytearray
x = bytearray(5) 	
print(type(x))
#memoryview
x = memoryview(bytes(5))	
print(type(x))
#NoneType
x = None 
print(type(x))

#setting specific type
x = str("Hello World") 	#str
x = int(20)	#int
x = float(20.5) #float	
x = complex(1j) #complex	
x = list(("apple", "banana", "cherry")) #list 
x = tuple(("apple", "banana", "cherry")) #tuple
x = range(6) #range
x = dict(name="John", age=36) #dict
x = set(("apple", "banana", "cherry")) #set	
x = frozenset(("apple", "banana", "cherry")) #frozenset 	
x = bool(5) #bool
x = bytes(5) #bytes	
x = bytearray(5) #bytearray
x = memoryview(bytes(5)) #memoryview