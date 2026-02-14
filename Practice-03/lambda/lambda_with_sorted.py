#using lambda with sorted()
students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)

# Example 1: Sort a list of dictionaries by age
people = [
    {'name': 'Emma', 'age': 30},
    {'name': 'Liam', 'age': 25},
    {'name': 'Olivia', 'age': 35}
]
sorted_by_age = sorted(people, key=lambda person: person['age'])
print(sorted_by_age)  # Output: [{'name': 'Liam', 'age': 25}, {'name': 'Emma', 'age': 30}, {'name': 'Olivia', 'age': 35}]

# Example 2: Sort a list of strings by their length
fruits = ['kiwi', 'banana', 'apple', 'strawberry', 'fig']
sorted_by_length = sorted(fruits, key=lambda fruit: len(fruit))
print(sorted_by_length)  # Output: ['fig', 'kiwi', 'apple', 'banana', 'strawberry']