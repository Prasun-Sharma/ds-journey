name = "python programming"
print (name)
print (name[0])
print (name[17])

print (name[0:6])
print (name[7:18])

print (name[0])
print (name[4])
print (name[10])

text = "data science"
print (text[0:4])
print (text[5:12])
print (text[-1:])
print (text[::2])
print (text[8:12])

name = " python programming "
print (name.upper())
print (name.lower())
print (name.title())
print (name.capitalize())
print (name.strip())
print (name.replace("python", "java"))

sentence = "apple mango banana apple"
print (sentence.count("apple"))
print (sentence.find("banana"))

language ="python"
print (language.startswith("py"))
print (language.endswith("on")) 

fruits = "apple, banana, mango"
print (fruits.split(","))       

print ("-".join(["A", "B", "C"]))

print ("Hello\nPython")

print ("Name\tAge")

A = "He said, \"Python is awesome\""
print (A)

Name = input("Enter your name: ")
Age = input("Enter your age: ")
City = input("Enter your city: ")
print ("My name is " + Name + "\nMy age is " + Age + "\nI live in " + City)

text = "Python Programming"
print (text[::-1])

Name = input("Enter your name: ")
Age = input("Enter your age: ")
City = input("Enter your city: ")

print (f"My name is {Name}")
print (f"My age is {Age}")
print (f"I live in {City}")
