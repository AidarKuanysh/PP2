# use enumerate() and zip() for paired iteration
names = ["alice", "bob", "charlie"]
scores = [85, 90, 78]
for index, name in enumerate(names):
    print(index, name)
for name, score in zip(names, scores):
    print(name, score)

# demonstrate type checking and conversions
value = "123"
if isinstance(value, str):
    number = int(value)
print(number)
float_number = float(number)
string_number = str(float_number)
print(type(number))
print(type(float_number))
print(type(string_number))