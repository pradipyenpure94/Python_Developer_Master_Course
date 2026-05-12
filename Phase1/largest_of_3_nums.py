"""Largest of three numbers"""

try:
    num1 = int(input("Enter a num1: "))
    num2 = int(input("Enter a num2: "))
    num3 = int(input("Enter a num3: "))

    if num1 >= num2 and num1 >= num3:
        print(f"{num1} is the largest number.")
    elif num2 >= num3 and num2 >= num1:
        print(f"{num2} is the largest number.")
    else:
        print(f"{num3} is the largest number.")
except ValueError:
    print("Invalid input! Please enter an integer.")
