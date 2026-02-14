#create a parent class
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname() 

#create a child class
class Student(Person):
  pass 

#use the Student class to create an object
#and then execute the printname method
x = Student("Mike", "Olsen")
x.printname() 

#add the __init__() function
class Student(Person):
  def __init__(self, fname, lname):
    #add properties etc. 
    pass
  
#to keep the inheritance of the parent's __init__() function
#add a call to the parent's __init__() function
class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname) 


