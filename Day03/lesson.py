# """
# ========================================
# Day 03 - User Input & Type Conversion
# ========================================

# Topics Covered
# --------------
# 1. input()
# 2. int()
# 3. float()
# 4. str()
# 5. bool()
# 6. Implicit Type Conversion
# 7. Explicit Type Conversion
# 8. User Input Programs

# ----------------------------------------
# 1. input()
# ----------------------------------------
# - Used to take input from the user.
# - The input() function always returns a string (str).

# Example:
# name = input("Enter your name: ")
# print(name)

# ----------------------------------------
# 2. int()
# ----------------------------------------
# - Converts a value into an integer.
# - Useful for mathematical operations on user input.

# Example:
# age = int(input("Enter your age: "))
# print(age)

# ----------------------------------------
# 3. float()
# ----------------------------------------
# - Converts a value into a floating-point number.

# Example:
# height = float(input("Enter your height: "))
# print(height)

# ----------------------------------------
# 4. str()
# ----------------------------------------
# - Converts a value into a string.

# Example:
# age = 29
# print(str(age))

# ----------------------------------------
# 5. bool()
# ----------------------------------------
# - Converts a value into a boolean.

# Rules:
# bool(0)        -> False
# bool("")       -> False
# bool(None)     -> False
# bool(1)        -> True
# bool("Hello")  -> True

# Example:
# print(bool(10))
# print(bool(0))

# ----------------------------------------
# 6. Implicit Type Conversion
# ----------------------------------------
# - Python automatically converts one data type to another
#   when it is safe to do so.

# Example:
# a = 10
# b = 5.5

# print(a + b)

# Output:
# 15.5

# ----------------------------------------
# 7. Explicit Type Conversion
# ----------------------------------------
# - The programmer manually converts one data type into another.

# Functions:
# int()
# float()
# str()
# bool()

# Example:
# num = "100"

# print(int(num) + 50)

# ----------------------------------------
# 8. User Input Programs
# ----------------------------------------
# Common examples:
# - Name Input
# - Age Calculator
# - Sum of Two Numbers
# - Area of Rectangle
# - Area of Circle
# - Simple Interest Calculator
# - Temperature Converter

# ----------------------------------------
# Common Beginner Mistakes
# ----------------------------------------
# ❌ input() returns a number
# ✔ input() always returns a string.

# ❌ "10" + 5
# TypeError

# ✔ int("10") + 5
# 15

# ❌ int("Hello")
# ValueError

# ----------------------------------------
# Key Takeaways
# ----------------------------------------
# ✔ input() always returns a string.
# ✔ Use int() for integer conversion.
# ✔ Use float() for decimal values.
# ✔ Use str() for string conversion.
# ✔ Use bool() to convert values into True or False.
# ✔ Python performs implicit conversion automatically.
# ✔ Explicit conversion is done using built-in functions.

# ========================================
# End of Day 03
# ========================================