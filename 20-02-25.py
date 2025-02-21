#Declaring Variables (All Data Types)

#variables are dynamically typed, meaning you don’t need to explicitly declare their types.

# Numeric types
integer_var = 10         # Integer
float_var = 10.5         # Float
complex_var = 3 + 4j     # Complex Number

# Sequence types
string_var = "Hello"     # String
list_var = [1, 2, 3]     # List (Mutable)
tuple_var = (1, 2, 3)    # Tuple (Immutable)

# Set types
set_var = {1, 2, 3}      # Set (Unordered, Unique Elements)

# Dictionary type
dict_var = {"name": "Alice", "age": 25}  # Dictionary (Key-Value Pair)

# Boolean type
bool_var = True          # Boolean (True or False)

# None type
none_var = None          # Represents "no value"

#2. Operators

#Assignment Operators

x = 10
x += 5   # x = x + 5
x -= 3   # x = x - 3
x *= 2   # x = x * 2
x /= 2   # x = x / 2
x %= 3   # x = x % 3

#Arithmetic Operators

a = 10
b = 3
print(a + b)   # Addition
print(a - b)   # Subtraction
print(a * b)   # Multiplication
print(a / b)   # Division
print(a // b)  # Floor Division
print(a % b)   # Modulus
print(a ** b)  # Exponentiation

#Relational (Comparison) Operators

print(10 > 5)   # True
print(10 < 5)   # False
print(10 == 10) # True
print(10 != 5)  # True
print(10 >= 5)  # True
print(10 <= 5)  # False

#Logical Operators

a = True
b = False

print(a and b)  # False (Both must be True)
print(a or b)   # True (At least one is True)
print(not a)    # False (Negation)

#3. Indentation

# uses indentation to define blocks of code.

if True:
    print("This is inside the block")  # Correct indentation

# Incorrect indentation will throw an error
# if True:
# print("This will cause an indentation error")

#4. Conditional Statements

#If, Else, Elif

x = 10

if x > 0:
    print("Positive Number")
elif x == 0:
    print("Zero")
else:
    print("Negative Number")

#5. Loops

#For Loop

for i in range(5):  # Loops from 0 to 4
    print(i)

#While Loop

x = 5
while x > 0:
    print(x)
    x -= 1


#6. Jump Statements

#Break Statement

for i in range(5):
    if i == 3:
        break  # Stops the loop when i is 3
    print(i)

#Continue Statement

for i in range(5):
    if i == 2:
        continue  # Skips iteration when i is 2
    print(i)

#7. Functions

#Function Definition and Call

def greet(name):  # Function definition
    return "Hello, " + name

print(greet("Alice"))  # Function call

#Function with Default Parameters

def power(base, exponent=2):  # Default exponent is 2
    return base ** exponent

print(power(3))      # 3^2 = 9
print(power(3, 3))   # 3^3 = 27


#8. Inbuilt Functions

#It has many built-in functions. Here are some common ones:

print(len("Hello"))    # Length of string (5)
print(type(10))        # Get type of variable (<class 'int'>)
print(abs(-5))         # Absolute value (5)
print(round(3.7))      # Rounds to nearest integer (4)
print(sum([1, 2, 3]))  # Sum of list (6)
print(max(2, 5, 8))    # Maximum value (8)
print(min(2, 5, 8))    # Minimum value (2)