student = ("John", 20, "A" )
print(student)
print (student[0])
print (student[-1])

numbers = (1, 2, 3, 4, 5)
print(numbers[1])
print(numbers[3])
print(numbers[-1])

My_tuple = ("apple", 3.12, True)
print(My_tuple)

person = ("John", 20, "A")
name, age, grade = person
print(name)
print(age)
print(grade)

numbers = (1, 2, 3, 4, 5, 5,3,6,7)
print(numbers.count(5))
print(numbers.index(3))


fruits = {"apple", "banana", "cherry"}
print(fruits)
fruits.add("orange")
print(fruits)
fruits.update(["mango", "grapes"])
print(fruits)
fruits.remove("banana")
print(fruits)
fruits.discard("banana")
print(fruits)

nymbers = {1, 2, 3, 4, 5, 5, 6,6}
print(nymbers)

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
print(a.union(b))
print(a.intersection(b))    
print(a.difference(b))
print(b.difference(a))


student = {
    "name": "Prasun",
    "age": 30,
    "city": "India"
}
print(student)
print(student["name"])
print(student["age"])
print(student["city"])
print(student.keys()) 
print(student.values())
print(student.items())
print(student.get("city"))
  

student.update({"age": 31})  
print(student) 

student.update({"salary": 50000})
print(student)

removed_city = student.pop("city")
print(removed_city)
print("removed city:", removed_city )
print("removed disctionary:", student)

student = {
    "name": "Prasun",
    "marks": (85, 90, 88)
}
print(student["name"])
print(student["marks"])
print(student["marks"][0])
print(len(student["marks"]))
print(max(student["marks"]))

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print(A.union(B))
print(A.intersection(B))
print(A.difference(B))
print(B.difference(A))

employee = {
    "id": "E101",
    "name": "Prasun",
    "skills": {"Python", "SQL", "Git"},
    "experience": 2
}
print(employee["name"])
print(employee["experience"])   
print(employee["skills"])
print("Python" in employee["skills"])  
employee["skills"].add("pandas")
print(employee["skills"])
employee["experience"] = 3
print(employee["experience"])