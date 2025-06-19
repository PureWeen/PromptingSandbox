# Python Cheat Sheet

## Basics
```python
# Print to console
print("Hello, World!")

# Variables
x = 5           # Integer
y = 3.14        # Float
name = "Alice"  # String
is_happy = True # Boolean
```

## Data Types
```python
# List (array)
fruits = ["apple", "banana", "cherry"]

# Tuple (immutable list)
point = (10, 20)

# Dictionary (key-value pairs)
age = {"Alice": 25, "Bob": 30}

# Set (unique values)
colors = {"red", "green", "blue"}
```

## Control Flow
```python
# If statement
if x > 0:
    print("Positive")
elif x == 0:
    print("Zero")
else:
    print("Negative")

# For loop
for fruit in fruits:
    print(fruit)

# While loop
count = 0
while count < 5:
    print(count)
    count += 1
```

## Functions
```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
```

## Classes
```python
class Dog:
    def __init__(self, name):
        self.name = name
    def bark(self):
        print(f"{self.name} says woof!")

my_dog = Dog("Fido")
my_dog.bark()
```

## Common Built-ins
```python
len(fruits)           # Length of list
range(5)              # 0,1,2,3,4
sum([1,2,3])          # 6
min([1,2,3])          # 1
max([1,2,3])          # 3
sorted([3,1,2])       # [1,2,3]
input("Enter: ")      # User input
```

## File I/O
```python
# Write to file
with open("file.txt", "w") as f:
    f.write("Hello!")

# Read from file
with open("file.txt", "r") as f:
    content = f.read()
```

## Importing Modules
```python
import math
print(math.sqrt(16))

from random import randint
print(randint(1, 10))
```

## List Comprehensions
```python
squares = [x*x for x in range(5)]  # [0,1,4,9,16]
```

## Exception Handling
```python
try:
    1 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
```

## Useful Tips
- Indentation matters (use 4 spaces)
- Comments start with #
- Use `pip install package` to add packages
- Use `help(object)` or `dir(object)` for help
