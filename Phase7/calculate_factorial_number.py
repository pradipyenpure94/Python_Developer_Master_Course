"""Calculate the factorial of a number using a loop."""

number = 4
factorial = 1

if number < 0:
    print("Factorial is not defined for negative number.")
elif number in (0, 1):
    factorial = 1
    print(f"Factorial of {number} is: {factorial}")
else:
    for num in range(2, number + 1):
        factorial *= num
    print(f"Factorial of {number} is: {factorial}")
