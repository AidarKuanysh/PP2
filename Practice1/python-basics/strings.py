#display a string literal with print
print("Hello")
print('Hello')

#quotes inside quotes
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

#assign string to a variable
a = "Hello"
print(a) 

#multiline strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a) 
#or three single quotes
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a) 

#strings are arrays
a = "Hello, World!"
print(a[1])

#looping through a string
for x in "banana":
    print(x)

#string length
a = "Hello, World!"
print(len(a))

#check string
txt = "The best things in life are free!"
print("free" in txt)
#print only if free is present
txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")

#check if not
txt = "The best things in life are free!"
print("expensive" not in txt)
#only if
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

#slicing
b = "Hello, World!"
print(b[2:5])

#from the start
b = "Hello, World!"
print(b[:5])

#to the end
b = "Hello, World!"
print(b[2:])

#negative indexing
b = "Hello, World!"
print(b[-5:-2])

#modify string
#upper
a = "Hello, World!"
print(a.upper())

#lower
a = "Hello, World!"
print(a.lower())

#remove whitespace
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!" 

#replace
a = "Hello, World!"
print(a.replace("H", "J"))

#split
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!'] 

#string concatenation
a = "Hello"
b = "World"
c = a + b
print(c)

a = "Hello"
b = "World"
c = a + " " + b
print(c)

#string format

age = 36
# this will produce an error:
# txt = "My name is John, I am " + age
# print(txt)

#fstring
age = 36
txt = f"My name is John, I am {age}"
print(txt)

#placeholders anf modifiers
price = 59
txt = f"The price is {price} dollars"
print(txt)

#2 decimals
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

#math operation
txt = f"The price is {20 * 59} dollars"
print(txt)

#escape characters
#error: txt = "We are the so-called "Vikings" from the north."

txt = "We are the so-called \"Vikings\" from the north."

#single quote
txt = 'It\'s alright.'
print(txt) 

#backslash
txt = "This will insert one \\ (backslash)."
print(txt) 

#new line
txt = "Hello\nWorld!"
print(txt) 

#carriage return
txt = "Hello\rWorld!"
print(txt) 

#tab
txt = "Hello\tWorld!"
print(txt) 

#baskspace
#This example erases one character (backspace):
txt = "Hello \bWorld!"
print(txt) 

#octal value
#A backslash followed by three integers will result in a octal value:
txt = "\110\145\154\154\157"
print(txt) 

#hex value
#A backslash followed by an 'x' and a hex number represents a hex value:
txt = "\x48\x65\x6c\x6c\x6f"
print(txt) 

#string methods
a = "sometext sometext"
print(a.capitalize())
print(a.casefold())
print(a.center())
print(a.count())
print(a.encode())
print(a.endswith())
print(a.expandtabs())
print(a.find())
print(a.format())
print(a.format_map())
print(a.index())
print(a.isalnum())
print(a.isalpha())
print(a.isascii())
print(a.isdecimal())
print(a.isdigit())
print(a.isidentifier())
print(a.islower())
print(a.isnumeric())
print(a.isprintable())
print(a.isspace())
print(a.istitle())
print(a.isupper())
print(a.join())
print(a.ljust())
print(a.lower())
print(a.lstrip())
print(a.maketrans())
print(a.partition())
print(a.replace())
print(a.rfind())
print(a.rindex())
print(a.rjust())
print(a.rpartition())
print(a.rsplit())
print(a.rstrip())
print(a.split())
print(a.splitlines())
print(a.startswith())
print(a.strip())
print(a.swapcase())
print(a.title())
print(a.translate())
print(a.upper())
print(a.zfill())