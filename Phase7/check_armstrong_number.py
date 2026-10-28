"""Check whether a number is an Armstrong number."""

number = 1634

power = len(str(number))

total = sum(int(digit) ** power for digit in str(number))

if total == number:
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not Armstrong number.")
