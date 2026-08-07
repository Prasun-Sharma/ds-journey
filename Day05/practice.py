fruits = ["apple", "banana", "orange"]
print (fruits)
print (fruits[0])
print (fruits[2])

student = ["prasun", 29, 166, True]
print (student[0])
print (student[1])
print (student[2])
print (student[3])

number = [1, 2, 3, 4, 5]
print (number[0])
print (number[2])
print (number[4])

numbers = [10,20,30]
print (type(numbers))
print (len(numbers))

numbers = [10,20,30,40,50,60]
print (numbers[1:4])
print (numbers[:3])
print (numbers[3:])
print (numbers[-1::-1])

student = [
    ["prasun",90],
        ["rahul",85],
        ["aman",88],
]
print (student[0][0])
print (student[1][1])   

fruits = ["apple","banana"]
fruits.append("mango")
print (fruits)
fruits.insert(1,"orange")
print (fruits)
fruits.extend(["grapes","kiwi"])
print (fruits)
fruits.remove("banana")
print (fruits)
fruits.pop(3)
removed = fruits.pop(3)
print (fruits)
print (removed)

fruits.clear()
print (fruits)

numbers = [40,10,60,20,30]
numbers.sort()
print (numbers)
numbers.sort(reverse=True)
print (numbers)

numbers = [40,10,60,20,30]
numbers.reverse()
print (numbers)

cpy_list = numbers.copy()
print (cpy_list)   
print (numbers)

fruits = ["apple","banana","orange","kiwi"] 
for fruit in fruits:
    print (fruit)

marks = [90,85,88,95]
print (max(marks))
print (min(marks))
print (sum(marks)) 
print (len(marks))

cities = ["delhi","mumbai","kolkata","chennai"]
print (cities[0])
print (cities[-1])
print (cities[-1::-1])
print (len(cities))
print (cities[0::2])
