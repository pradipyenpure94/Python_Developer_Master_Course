"""Student information"""

student = dict()
student['name'] = input("Enter a name: ")
student['age'] = int(input("Enter age: "))

for key, value in student.items():
    print(key, ":", value)
