"""
========================================
Day 06 - Tuple • Set • Dictionary
========================================

Topics Covered
--------------
1. Tuple
2. Set
3. Dictionary

========================================
1. Tuple
========================================

- A tuple is an ordered collection of elements.
- Tuples are created using parentheses ().
- Tuples are immutable (cannot be modified after creation).
- Duplicate values are allowed.
- Different data types can be stored together.

Examples:

student = ("Prasun", 29, True)

numbers = (10, 20, 30, 40)

----------------------------------------
Tuple Indexing
----------------------------------------

- Indexing starts from 0.
- Negative indexing starts from -1.

Example:

fruits = ("apple", "banana", "mango")

print(fruits[0])      # apple
print(fruits[-1])     # mango

----------------------------------------
Tuple Packing
----------------------------------------

- Packing means storing multiple values into a tuple.

Example:

student = ("Prasun", 29, "India")

----------------------------------------
Tuple Unpacking
----------------------------------------

- Unpacking assigns tuple elements to variables.

Example:

name, age, country = student

print(name)
print(age)
print(country)

----------------------------------------
Tuple Methods
----------------------------------------

count()

- Counts the occurrences of a value.

Example:

numbers = (10, 20, 10, 30)

print(numbers.count(10))
# 2

index()

- Returns the first index of a value.

Example:

print(numbers.index(30))
# 3

========================================
2. Set
========================================

- A set is an unordered collection.
- Sets do not allow duplicate values.
- Sets are mutable.
- Indexing is NOT supported.

Example:

fruits = {"apple", "banana", "mango"}

----------------------------------------
add()
----------------------------------------

- Adds one element.

Example:

fruits.add("orange")

----------------------------------------
update()
----------------------------------------

- Adds multiple elements.

Example:

fruits.update(["kiwi", "grapes"])

----------------------------------------
remove()
----------------------------------------

- Removes a specific element.
- Raises an error if the element does not exist.

Example:

fruits.remove("banana")

----------------------------------------
discard()
----------------------------------------

- Removes an element if it exists.
- Does NOT raise an error if missing.

Example:

fruits.discard("banana")

----------------------------------------
union()
----------------------------------------

- Combines two sets.

Example:

a = {1,2,3}
b = {3,4,5}

print(a.union(b))

Output:

{1,2,3,4,5}

----------------------------------------
intersection()
----------------------------------------

- Returns common elements.

Example:

print(a.intersection(b))

Output:

{3}

----------------------------------------
difference()
----------------------------------------

- Returns elements present only in the first set.

Example:

print(a.difference(b))

Output:

{1,2}

========================================
3. Dictionary
========================================

- A dictionary stores data in key-value pairs.
- Dictionaries use curly braces {}.
- Keys must be unique.
- Values can be duplicated.
- Dictionaries are mutable.

Example:

student = {
    "name": "Prasun",
    "age": 29,
    "city": "Gurugram"
}

----------------------------------------
Accessing Values
----------------------------------------

Example:

print(student["name"])

print(student["age"])

----------------------------------------
keys()
----------------------------------------

- Returns all keys.

Example:

print(student.keys())

----------------------------------------
values()
----------------------------------------

- Returns all values.

Example:

print(student.values())

----------------------------------------
items()
----------------------------------------

- Returns key-value pairs.

Example:

print(student.items())

----------------------------------------
get()
----------------------------------------

- Returns the value of a key.
- Returns None if the key is missing.
- Does not raise an error.

Example:

print(student.get("city"))

----------------------------------------
update()
----------------------------------------

- Updates an existing key or adds a new key.

Example:

student.update({"age":30})

student.update({"salary":756000})

----------------------------------------
pop()
----------------------------------------

- Removes a key and returns its value.

Example:

student.pop("city")

========================================
Useful Built-in Functions
========================================

len()

Returns the number of elements.

max()

Returns the maximum value.

min()

Returns the minimum value.

sum()

Returns the sum (numeric values only).

========================================
Common Beginner Mistakes
========================================

Tuple
-----
❌ Trying to modify a tuple.

numbers = (10,20,30)

numbers[0] = 50

TypeError

----------------------------------------

Set
---

❌ Expecting ordered output.

Sets are unordered.

❌ Accessing by index.

fruits[0]

TypeError

----------------------------------------

Dictionary
----------

❌ Accessing a missing key.

student["salary"]

KeyError

Better:

student.get("salary")

========================================
Key Takeaways
========================================

✔ Tuple is ordered and immutable.
✔ Set is unordered and stores unique values.
✔ Dictionary stores data as key-value pairs.
✔ Tuples support indexing.
✔ Sets do not support indexing.
✔ Dictionaries use keys instead of indexes.
✔ count() and index() work with tuples.
✔ add() adds one element to a set.
✔ update() adds multiple elements.
✔ remove() raises an error if missing.
✔ discard() ignores missing values.
✔ union() combines sets.
✔ intersection() returns common elements.
✔ difference() returns unique elements.
✔ keys(), values(), items() are used with dictionaries.
✔ get() safely retrieves values.
✔ update() modifies or adds key-value pairs.
✔ pop() removes a key.

========================================
End of Day 06
========================================