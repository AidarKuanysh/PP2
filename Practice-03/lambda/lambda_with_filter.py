#using lambda with filter()
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)

# Example 1: Filter words shorter than 5 characters
words = ['cat', 'elephant', 'dog', 'butterfly', 'ant', 'dragon']
short_words = list(filter(lambda word: len(word) < 5, words))
print(short_words)  # Output: ['cat', 'dog', 'ant']

# Example 2: Filter positive numbers from a mixed list
mixed_numbers = [-5, 3, -1, 101, -20, 50, 0, -3]
positive_numbers = list(filter(lambda x: x > 0, mixed_numbers))
print(positive_numbers)  # Output: [3, 101, 50]