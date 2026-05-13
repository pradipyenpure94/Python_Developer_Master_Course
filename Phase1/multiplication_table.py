"""Display multiplication table."""

try:
    n = int(input("Enter a number: "))
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")
except ValueError:
    print("Invalid input! Please enter an integer.")
