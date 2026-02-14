#method overriding in inheritance
class Animal:
  def make_sound(self):
    return "Some generic sound"

class Dog(Animal):
  def make_sound(self):  # Overrides parent method
    return "Woof! Woof!"

class Cat(Animal):
  def make_sound(self):  # Overrides parent method
    return "Meow!"

animal = Animal()
dog = Dog()
cat = Cat()
print(animal.make_sound())  # Output: Some generic sound
print(dog.make_sound())     # Output: Woof! Woof!
print(cat.make_sound())     # Output: Meow!

#method overriding with super() call
class Vehicle:
  def __init__(self, brand):
    self.brand = brand
  
  def info(self):
    return f"Brand: {self.brand}"

class Car(Vehicle):
  def __init__(self, brand, model):
    super().__init__(brand)  # Call parent's __init__
    self.model = model
  
  def info(self):  # Overrides parent method
    parent_info = super().info()  # Call parent's info
    return f"{parent_info}, Model: {self.model}"

my_car = Car("Toyota", "Corolla")
print(my_car.info())  # Output: Brand: Toyota, Model: Corolla