"""Print employee details using variables and f-strings."""


try:
    name = input("Enter a name: ")
    age = int(input("Enter an age: "))
    if age < 0:
        raise ValueError("Age cannot be negative.")
except ValueError as error:
    print(f"Error: {error}")
else:
    print("Employee Details:")
    print(f"Name : {name}")
    print(f"Age  : {age}")
