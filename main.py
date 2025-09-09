
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

# functions
def greet(name):
    return f"Hello, {name}!"
print(greet("Bob"))       # "Hello, Bob!"
# default parameters
def power(base, exponent=2):
    return base ** exponent
print(power(3))           # 9
print(power(2, 3))        # 8   
#nested functions
def counter():
    count = 0
    def increment():
        #to access the count variable from the enclosing scope
        #declare it as nonlocal
        nonlocal count
        count += 1
        return count
    return increment
count_func = counter()
print(count_func())      # 1
print(count_func())      # 2
print(count_func())      # 3

#lambda functions
add = lambda x, y: x + y
print(add(3, 5))         # 8

#loops
# while loop
count=0
while count < 5:
    print(f"count  is {count}")
    count += 1  
# for loop
for i in range(5):
    print(f"i is {i}")
# loop through a list
colors = ["red", "green", "blue"]
for color in colors:
    print(color)
# loop through a dictionary
person = {"name": "Alice", "age": 30}
for key, value in person.items():
    print(f"{key}: {value}")
# break and continue
for i in range(10):
    if i == 5:
        break  # exit the loop when i is 5
    if i % 2 == 0:
        continue  # skip even numbers
    print(i)  # prints odd numbers less than 5

#classes and objects
class Dog:
    #constructor
    # __init__ method is called when an object is created. self refers to the instance being created.
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return "Woof!"
my_dog = Dog("Buddy", 3)
print(my_dog.name)        # "Buddy"
print(my_dog.age)         # 3
print(my_dog.bark())      # "Woof!"

#inheritance
class Animal:
    def speak(self):
        return "Animal sound"
class Cat(Animal):
    #constructor
    def __init__(self, name):
        self.name = name

my_cat = Cat("Whiskers")
print(my_cat.name)        # "Whiskers"
print(my_cat.speak())     # "Animal sound"
#polymorphism
#polymorphism allows methods to do different things based on the object it is acting upon.
class Bird(Animal):
    #override speak method
    def speak(self):
        return "Chirp!"
my_bird = Bird()
print(my_bird.speak())    # "Chirp!"
# encapsulation
# encapsulation restricts direct access to some of an object's components, which can prevent the accidental modification of data.
class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance  # private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance
account = BankAccount(100)
account.deposit(50)

account.deposit(50)
account.withdraw(30)
print(account.get_balance())  # 120


#modules and packages
import dog
print(dog.bark())  # "Woof! woof!"

#import specific function from a module
from dog import bark
print(bark())  # "Woof! woof!"

#importing from a sub folder
#assuming cat.py is in a folder named lib
#when importing from a subfolder, ensure the folder contains an __init__.py file to be recognized as a package.
from lib.cat import meow
print(meow())  # "Meow! meow!"

#or import the entire module
import lib.cat as cat
print(cat.meow())  # "Meow! meow!"

#python standard library
import math
print(math.sqrt(16))      # 4.0
print(math.pi)            # 3.141592653589793
import random
print(random.randint(1, 10))  # random integer between 1 and 10
print(random.choice(['apple', 'banana', 'cherry']))  # random choice from list
import datetime
now = datetime.datetime.now()
print(now)                # current date and time
print(now.year)           # current year
print(now.month)          # current month
print(now.day)            # current day
print(now.hour)           # current hour
print(now.minute)         # current minute
print(now.second)         # current second
import os
print(os.getcwd())        # current working directory
print(os.listdir())       # list files in current directory
import sys
print(sys.version)        # Python version
print(sys.platform)       # platform information
import json
data = {'name': 'Alice', 'age': 30}
json_str = json.dumps(data)  # convert dictionary to JSON string
print(json_str)          # '{"name": "Alice", "age": 30}'
data_back = json.loads(json_str)  # convert JSON string back to dictionary
print(data_back)        # {'name': 'Alice', 'age': 30}
import re
pattern = r'\b\w{3}\b'  # words with exactly 3
text = "The cat sat on the mat."
matches = re.findall(pattern, text)
print(matches)          # ['The', 'cat', 'sat', 'the', 'mat']












