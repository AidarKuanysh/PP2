#using lambda with map()
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)

# Example 1: Convert temperatures from Celsius to Fahrenheit
celsius_temps = [0, 20, 30, 40]
fahrenheit_temps = list(map(lambda c: (c * 9/5) + 32, celsius_temps))
print(fahrenheit_temps)  # Output: [32.0, 68.0, 86.0, 104.0]

# Example 2: Capitalize a list of names
names = ['alice', 'bob', 'charlie', 'diana']
capitalized_names = list(map(lambda name: name.capitalize(), names))
print(capitalized_names)  # Output: ['Alice', 'Bob', 'Charlie', 'Diana']