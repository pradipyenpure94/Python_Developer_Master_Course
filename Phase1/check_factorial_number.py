"""Check factorial of a number."""

try:
    n = int(input("Enter a number: "))
    if n < 0:
        print("Factorial is not defined for negative numbers.")
    elif n == 0:
        print(f"Factorial number {n} is 1.")
    else:
        fact = 1
        i = 1
        while i <= n:
            fact *= i
            i += 1
        print(f"Factorial of {n} is {fact}")
except ValueError:
    print("Invalid input! Please enter an integer.")
