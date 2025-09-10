# map(), filter(), reduce()
from functools import reduce
# map() applies a function to all the items in an input list (or any iterable)
numbers = [1, 2, 3, 4, 5]
#pass it as a list to see the results
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # [1, 4, 9, 16, 25]

# filter() creates a list of elements for which a function returns true
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # [2, 4]

# reduce() applies a rolling computation to sequential pairs of values in a list
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_of_numbers)  # 15

# Reccursion
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))  # 120

# docstrings
# A docstring is a special string that is the first statement in a module, function, class, or method definition
def add(a, b):
    """Return the sum of a and b."""
    return a + b
print(add(3, 5))  # 8
print(add.__doc__)  # "Return the sum of a and b."


#annotations
#python is a dynamically typed language but you can add type hints using annotations
def greet(name: str) -> str:
    return f"Hello, {name}!"
print(greet("Alice"))  # "Hello, Alice!"
print(greet.__annotations__)  # {'name': <class 'str'>, 'return

#exceptions
# exceptions are errors that occur during the execution of a program
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
finally:
    print("Execution completed.")
# Error: division by zero
# Execution completed.

#Lists comprehensions
#list comprehensions provide a concise way to create lists
squared = [x ** 2 for x in range(10)]
print(squared)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
even_squared = [x ** 2 for x in range(10) if x % 2 == 0]
print(even_squared)  # [0, 4, 16, 36, 64]


