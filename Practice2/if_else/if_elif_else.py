#the elif keyword
a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")

#multiple elif statements
score = 75
if score >= 90:
    print("grade a")
elif score >= 80:
    print("grade b")
elif score >= 70:
    print("grade c")
elif score >= 60:
    print("grade d")

#how elif works
age = 25
if age < 13:
    print("you're child")
elif age < 20:
    print("you're teenager")
elif age < 65:
    print("you're adult")
elif age >= 65:
    print("you're senior")

#when to use elif
day = 3
if day == 1:
  print("monday")
elif day == 2:
  print("tuesday")
elif day == 3:
  print("wednesday")
elif day == 4:
  print("thursday")
elif day == 5:
  print("friday")
elif day == 6:
  print("saturday")
elif day == 7:
  print("sunday")