#AND operator
citizen = "Norway"
year = 1995
print(citizen == "Norway" and year > 1994) #true

#OR operator
phone_brand = "iPhone"
memory = 128
print(phone_brand == "Samsung" or memory > 64) #true

#NOT operator
age = 19
print(not age > 18) #false

#Operators with both False
print(age != 19 and phone_brand == "Nokia") #false
print(year == 1994 or citizen == "USA") #false