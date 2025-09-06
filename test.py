# define a variable with your name and print a greeting message
name = "clement"
print(f"Hello, {name}!")

# indentation matters in Python
if 5 > 2:
    print("Five is greater than two!")

#arithmetic operations
#10 + 5= 15
#10 - 5= 5
#10 * 5= 50  
#10 / 5= 2.0 (float division)
#11 // 5= 2 (integer division) rounds down to nearest integer 
#10 % 5= 0  (remainder)
#10 ** 5= 100000

#comparison operators
# == (equal to)
# != (not equal to)
# > (greater than)
# < (less than)
# >= (greater than or equal to)
# <= (less than or equal to)
# and (logical AND)
# or (logical OR)
# not (logical NOT)
# in (membership operator)
# is (identity operator)
# ternary operator (conditional expression)
age = 20
status = "teenager" if age < 21 else "adult"
print(status)

#multi-line strings
multi_line_string = """This is a
multi-line string."""
print(multi_line_string)

#string methods
text = "hello World"
print(text.upper())        # "HELLO WORLD"
print(text.lower())        # "hello world"
print(text.capitalize())   # "Hello world"
print(text.replace("world", "there"))  # "hello there"
print(text.split())        # ['hello', 'world']
print(text.strip())        # "hello world" (removes leading/trailing whitespace)    
print(text.find("world"))  # 6 (index of substring)
print(text.startswith("hello"))  # True
print(text.endswith("world"))    # True
print(text.count("o"))     # 2 (number of occurrences of substring)
#print(text.index("world"))  6 (index of substring, raises error if not found)
print(text.isalpha())      # False (checks if all characters are alphabetic)
print(text.isdigit())      # False (checks if all characters are digits)
print(text.islower())      # True (checks if all characters are lowercase)
print(text.isupper())      # False (checks if all characters are uppercase)
print(text.isspace())     # False (checks if all characters are whitespace)
print(text.title())       # "Hello World" (title case)

#input from user
user_name = input("Enter your name: ")
print(f"Hello, {user_name}!")

#control statements
# if-elif-else
num = 10
if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")


#lists
fruits = ["apple", "banana", "cherry"]
print(fruits[0])          # "apple"
fruits.append("date")     # add "date" to the end
print(fruits)             # ['apple', 'banana', 'cherry', 'date']
fruits.remove("banana")   # remove "banana"
print(fruits)             # ['apple', 'cherry', 'date']
print(len(fruits))        # 3
print(fruits.sort())      # sort the list
print(fruits.reverse())   # reverse the list
print(fruits)
print(fruits.insert(1, "blueberry"))  # insert "blueberry" at index 1
print(fruits.pop())       # remove and return the last item
print(fruits.index("cherry"))  # 1 (index of "cherry")

#Tuples
point = (10, 20)
print(point[0])           # 10
print(len(point))        # 2
#point[0] = 15           # Error: tuples are immutable

#Dictionaries
person = {"name": "Alice", "age": 30}
print(person["name"])     # "Alice"
person["age"] = 31       # update age
print(person)            # {'name': 'Alice', 'age': 31}
person["city"] = "New York"  # add new key-value pair

#sets
unique_numbers = {1, 2, 3, 4, 5}
print(unique_numbers)     # {1, 2, 3, 4, 5}
unique_numbers.add(6)    # add 6
print(unique_numbers)     # {1, 2, 3, 4, 5, 6}
unique_numbers.remove(3) # remove 3

#intersection
set_a = {1, 2, 3}
set_b = {3, 4, 5}
print(set_a & set_b)     # {3}





