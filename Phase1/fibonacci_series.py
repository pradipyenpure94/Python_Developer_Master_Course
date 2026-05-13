"""Generate Fibonacci series"""


try:
    n = int(input("Enter a number: "))

    if n < 0:
        print("Fibonacci series is not defined for negative numbers.")
    else:
        a, b = 0, 1

        for _ in range(n):
            print(a, end=" ")
            a, b = b, a + b
        print()

except ValueError:
    print("Invalid input! Please enter an integer.")
