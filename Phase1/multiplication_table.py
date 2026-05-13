"""Display multiplication table."""

try:
    n = int(input("Enter a number: "))
    if n <= 0:
        print("Please enter a positive integer.")
    else:
        i = 1
        while i <= 10:
            print(f"{n} x {i} = {n * i}")
            i += 1
except ValueError:
    print("Invalid input! Please enter an integer.")
