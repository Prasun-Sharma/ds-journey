# """
# ========================================
# Day 04 - Strings
# ========================================

# Topics Covered
# --------------
# 1. String Basics
# 2. Indexing
# 3. Negative Indexing
# 4. Slicing
# 5. String Methods
# 6. Escape Characters
# 7. f-Strings

# ----------------------------------------
# 1. String Basics
# ----------------------------------------
# - A string is a sequence of characters.
# - Strings are enclosed in single (' '), double (" "), or triple quotes.

# Examples:
# name = "Prasun"
# city = 'Gurugram'
# message = """Hello Python"""

# ----------------------------------------
# 2. Indexing
# ----------------------------------------
# - Indexing is used to access individual characters.
# - Python uses zero-based indexing.

# Example:
# name = "Python"

# P  y  t  h  o  n
# 0  1  2  3  4  5

# print(name[0])   # P
# print(name[3])   # h

# ----------------------------------------
# 3. Negative Indexing
# ----------------------------------------
# - Negative indexing starts from the end of the string.

# Example:
# name = "Python"

# P  y  t  h  o  n
# -6 -5 -4 -3 -2 -1

# print(name[-1])   # n
# print(name[-2])   # o

# ----------------------------------------
# 4. Slicing
# ----------------------------------------
# - Slicing extracts a part of a string.

# Syntax:
# string[start : stop : step]

# Examples:
# name = "Python"

# print(name[0:3])     # Pyt
# print(name[2:])      # thon
# print(name[:4])      # Pyth
# print(name[::2])     # Pto
# print(name[::-1])    # nohtyP

# ----------------------------------------
# 5. String Methods
# ----------------------------------------

# upper()
# - Converts all characters to uppercase.

# Example:
# name.upper()

# lower()
# - Converts all characters to lowercase.

# Example:
# name.lower()

# title()
# - Capitalizes the first letter of each word.

# Example:
# "hello world".title()

# capitalize()
# - Capitalizes only the first character.

# Example:
# "python".capitalize()

# replace()
# - Replaces one substring with another.

# Example:
# name.replace("Python", "Java")

# split()
# - Splits a string into a list.

# Example:
# "apple banana mango".split()

# join()
# - Joins iterable elements into a string.

# Example:
# "-".join(["A", "B", "C"])

# strip()
# - Removes leading and trailing spaces.

# Example:
# "  Python  ".strip()

# find()
# - Returns the index of the first occurrence.
# - Returns -1 if not found.

# Example:
# name.find("t")

# count()
# - Counts the occurrences of a substring.

# Example:
# name.count("o")

# startswith()
# - Checks if the string starts with a specific value.

# Example:
# name.startswith("Py")

# endswith()
# - Checks if the string ends with a specific value.

# Example:
# name.endswith("on")

# ----------------------------------------
# 6. Escape Characters
# ----------------------------------------
# Used to include special characters inside strings.

# Common Escape Characters:

# \\n  -> New Line
# \\t  -> Tab Space
# \\'  -> Single Quote
# \\"  -> Double Quote
# \\\\  -> Backslash

# Example:
# print("Hello\\nPython")

# ----------------------------------------
# 7. f-Strings
# ----------------------------------------
# - Used for clean and readable string formatting.
# - Introduced in Python 3.6.

# Example:

# name = "Prasun"
# age = 29

# print(f"My name is {name} and I am {age} years old.")

# ----------------------------------------
# Common Beginner Mistakes
# ----------------------------------------
# ❌ Trying to modify a character directly.

# name = "Python"
# name[0] = "J"

# Strings are immutable.

# ✔ Correct:

# name = name.replace("P", "J")

# ----------------------------------------
# Key Takeaways
# ----------------------------------------
# ✔ Strings are immutable.
# ✔ Indexing starts from 0.
# ✔ Negative indexing starts from -1.
# ✔ Slicing extracts part of a string.
# ✔ String methods return a new string.
# ✔ strip() removes extra spaces.
# ✔ split() converts a string into a list.
# ✔ join() converts a list into a string.
# ✔ f-strings are the preferred way to format strings.

# ========================================
# End of Day 04
# ========================================
# """