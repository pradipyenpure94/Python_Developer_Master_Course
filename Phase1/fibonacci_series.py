"""Generate Fibonacci series"""


try:
    n = int(input("Enter a number: "))

    if n < 0:
        print("Fibonacci series is not defined for negative numbers.")
    else:
        a, b = 0, 1
        i = 0
        while i < n:
            print(a, end=" ")
            a, b = b, a + b
            i += 1
        print()

except ValueError:
    print("Invalid input! Please enter an integer.")
