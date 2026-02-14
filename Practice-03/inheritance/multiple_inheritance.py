#multiple inheritance
class Flyer:
  def fly(self):
    return "I can fly!"

class Swimmer:
  def swim(self):
    return "I can swim!"

class Duck(Flyer, Swimmer):
  def quack(self):
    return "Quack!"

donald = Duck()
print(donald.fly())   # Output: I can fly!
print(donald.swim())  # Output: I can swim!
print(donald.quack()) # Output: Quack!

#method resolution order (MRO) in multiple inheritance
class A:
  def process(self):
    return "Processing in A"

class B:
  def process(self):
    return "Processing in B"

class C(A, B):  # Inherits from A first, then B
  pass

class D(B, A):  # Inherits from B first, then A
  pass

obj_c = C()
obj_d = D()
print(obj_c.process())  # Output: Processing in A (from A, because A comes first)
print(obj_d.process())  # Output: Processing in B (from B, because B comes first)