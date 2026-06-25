"""
Input Age
Accept only integer values.
"""

try:
    age = int(input("Enter an age: "))
except ValueError:
    print("Invalid input. Please enter an integer.")
else:
    print(f"Age: {age}")
finally:
    print("Operation completed.")
