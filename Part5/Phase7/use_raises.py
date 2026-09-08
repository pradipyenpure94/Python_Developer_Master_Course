"""Use raise for validation."""


try:
    age = int(input("Enter the age: "))
    if age < 0:
        raise ValueError("Age cannot be negative.")
except ValueError as error:
    print(f"Error: {error}")
else:
    print(f"Age: {age}")
