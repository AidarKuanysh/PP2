#class variable shared by all instances
class Student:
  school = "Python High School"  # Class variable
  total_students = 0  # Class variable
  
  def __init__(self, name):
    self.name = name
    Student.total_students += 1

s1 = Student("Gibrat")
s2 = Student("Alibek")
print(s1.school)  # Output: Python High School
print(s2.school)  # Output: Python High School
print(Student.total_students)  # Output: 2

#modifying class variable affects all instances
class Employee:
  company = "TechCorp"
  raise_percentage = 1.05
  
  def __init__(self, name, salary):
    self.name = name
    self.salary = salary

emp1 = Employee("Epstein", 50000)
emp2 = Employee("Patrick", 60000)

print(emp1.company)  # Output: TechCorp
Employee.company = "Trump Island Inc."  # Change class variable
print(emp1.company)  # Output: NewTech Inc.
print(emp2.company)  # Output: NewTech Inc.