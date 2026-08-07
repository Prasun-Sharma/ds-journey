"""
========================================
Day 05 - Python Lists
========================================

Topics Covered
--------------
1. List Basics
2. Indexing
3. Slicing
4. Nested Lists
5. List Methods
   - append()
   - insert()
   - extend()
   - remove()
   - pop()
   - clear()
   - sort()
   - reverse()
   - copy()
6. List Traversal


----------------------------------------
1. List Basics
----------------------------------------
- A list is used to store multiple values in a single variable.
- Lists are created using square brackets [].
- Lists are ordered.
- Lists are mutable (their contents can be changed).
- Lists allow duplicate values.
- A list can contain different data types.

Examples:

fruits = ["apple", "banana", "mango"]

numbers = [10, 20, 30, 40]

mixed = ["Python", 29, 5.8, True]

duplicates = ["apple", "apple", "mango"]


----------------------------------------
2. Indexing
----------------------------------------
- Indexing is used to access individual elements.
- Indexing starts from 0.
- Negative indexing starts from -1.

Example:

fruits = ["apple", "banana", "mango", "orange"]

print(fruits[0])     # apple
print(fruits[2])     # mango

print(fruits[-1])    # orange
print(fruits[-2])    # mango


----------------------------------------
3. Slicing
----------------------------------------
- Slicing is used to access a portion of a list.
- It works similarly to string slicing.

Syntax:

list[start : stop : step]

Example:

numbers = [10, 20, 30, 40, 50, 60]

print(numbers[1:4])     # [20, 30, 40]
print(numbers[:3])      # [10, 20, 30]
print(numbers[3:])      # [40, 50, 60]
print(numbers[::2])     # [10, 30, 50]
print(numbers[::-1])    # [60, 50, 40, 30, 20, 10]


----------------------------------------
4. Nested Lists
----------------------------------------
- A list can contain another list.
- Such lists are called nested lists.

Example:

students = [
    ["Prasun", 90],
    ["Rahul", 85],
    ["Aman", 88]
]

print(students[0])       # ["Prasun", 90]
print(students[0][0])    # Prasun
print(students[0][1])    # 90

Think of it as:

students[0]       -> First inner list
students[0][0]    -> First element of first inner list


----------------------------------------
5. List Methods
----------------------------------------

append()
--------
- Adds one element to the end of a list.

Example:

fruits = ["apple", "banana"]

fruits.append("mango")

print(fruits)
# ["apple", "banana", "mango"]


insert()
--------
- Adds an element at a specific index.

Syntax:

list.insert(index, value)

Example:

fruits = ["apple", "mango"]

fruits.insert(1, "banana")

print(fruits)
# ["apple", "banana", "mango"]


extend()
--------
- Adds multiple elements from another iterable to the end.

Example:

fruits = ["apple", "banana"]

fruits.extend(["mango", "orange"])

print(fruits)
# ["apple", "banana", "mango", "orange"]

Difference:

append(["mango", "orange"])
-> Adds the entire list as ONE element.

extend(["mango", "orange"])
-> Adds each element separately.


remove()
--------
- Removes the first occurrence of a specified value.

Example:

fruits = ["apple", "banana", "mango"]

fruits.remove("banana")

print(fruits)
# ["apple", "mango"]


pop()
-----
- Removes an element using its index.
- It also returns the removed element.
- Without an index, pop() removes the last element.

Example:

fruits = ["apple", "banana", "mango"]

removed = fruits.pop(1)

print(removed)      # banana
print(fruits)       # ["apple", "mango"]

fruits.pop()        # Removes last element


clear()
-------
- Removes all elements from the list.
- The list still exists, but becomes empty.

Example:

fruits = ["apple", "banana", "mango"]

fruits.clear()

print(fruits)
# []


sort()
------
- Sorts the original list.
- By default, sorting is ascending.

Example:

numbers = [40, 10, 30, 20]

numbers.sort()

print(numbers)
# [10, 20, 30, 40]

Descending:

numbers.sort(reverse=True)

print(numbers)
# [40, 30, 20, 10]


reverse()
---------
- Reverses the current order of the list.
- It does NOT sort the values.

Example:

numbers = [10, 40, 20, 30]

numbers.reverse()

print(numbers)
# [30, 20, 40, 10]

Important:

sort()
-> Arranges values in order.

reverse()
-> Simply reverses the existing order.


copy()
------
- Creates a shallow copy of a list.

Example:

original = ["apple", "banana", "mango"]

copied = original.copy()

print(copied)


----------------------------------------
6. Lists are Mutable
----------------------------------------
- Unlike strings, list elements can be changed directly.

Example:

fruits = ["apple", "banana", "mango"]

fruits[1] = "orange"

print(fruits)
# ["apple", "orange", "mango"]

String:
name[0] = "J"       # Not allowed

List:
fruits[0] = "kiwi"  # Allowed


----------------------------------------
7. List Traversal
----------------------------------------
- Traversal means accessing each element of a list one by one.
- A for loop is commonly used.

Example:

fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print(fruit)

Output:

apple
banana
mango


----------------------------------------
Useful Built-in Functions
----------------------------------------

len()
- Returns the number of elements.

numbers = [10, 20, 30]
print(len(numbers))       # 3


min()
- Returns the smallest value.

print(min(numbers))       # 10


max()
- Returns the largest value.

print(max(numbers))       # 30


sum()
- Returns the sum of numeric elements.

print(sum(numbers))       # 60


----------------------------------------
Common Beginner Mistakes
----------------------------------------

1. Index out of range:

numbers = [10, 20, 30]

print(numbers[3])
# IndexError

Valid indexes are:
0, 1, 2


2. Confusing append() and extend():

numbers.append([40, 50])
# [10, 20, 30, [40, 50]]

numbers.extend([40, 50])
# [10, 20, 30, 40, 50]


3. Confusing remove() and pop():

remove(value)
-> Removes by VALUE.

pop(index)
-> Removes by INDEX and returns the removed value.


4. Confusing sort() and reverse():

sort()
-> Sorts values.

reverse()
-> Reverses current order.


----------------------------------------
Key Takeaways
----------------------------------------
✔ Lists store multiple values.
✔ Lists are ordered and mutable.
✔ Duplicate values are allowed.
✔ Indexing starts from 0.
✔ Negative indexing starts from -1.
✔ Slicing works similarly to strings.
✔ Lists can contain other lists.
✔ append() adds one element.
✔ insert() adds an element at a specific position.
✔ extend() adds multiple elements.
✔ remove() removes by value.
✔ pop() removes by index and returns the removed value.
✔ clear() removes all elements.
✔ sort() sorts the list.
✔ reverse() reverses the current order.
✔ copy() creates a shallow copy.
✔ for loops can be used to traverse a list.

========================================
End of Day 05
========================================
"""