"""Calculate the sum of digits of a number."""


try:
    number = int(input("Enter a number: "))

    total = 0
    temp = abs(number)

    while temp > 0:
        digit = temp % 10
        total += digit
        temp //= 10

    print(f"Sum of digits: {total}")

except ValueError:
    print("Invalid input! Please enter an integer.")
