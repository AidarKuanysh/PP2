# use map() and filter() on lists
numbers = [1, 2, 3, 4, 5, 6]
squared = list(map(lambda x: x**2, numbers))
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(squared)
print(even_numbers)

# aggregate with reduce() (from functools)
from functools import reduce
numbers = [1, 2, 3, 4, 5]
total = reduce(lambda a, b: a + b, numbers)
print(total)