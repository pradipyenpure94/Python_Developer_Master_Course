"""Membership operators"""

# to check string
text = "Python"
print("P" in text)
print("p" not in text)
print("z" in text)

# to check list
fruits = ["Mango", "apple", "Banana"]
print("apple" in fruits)
print(2 not in fruits)

# to check tuple
numbers = (1, 2, 3)
print(23 in numbers)
print(2 in numbers)

# to check dictionary
student = {"name": "Pradip", "age":33}
print("Pradip" in student.values())
print("Pradip" not in student.values())

# to check set
even = {2, 4, 6, 8}
print(2 in even)
print(10 in even)
