"""Check whether a number is Armstrong."""

try:
    number = int(input("Enter the number: "))
    if number < 0:
        raise ValueError(
            "The Armstrong number is not defined for negative number."
        )
except ValueError as error:
    print(f"Error: {error}")
except KeyboardInterrupt:
    print("\nOperation cancelled by the user.")
else:
    # Count numbers digits length
    digits_count = 0

    temp = number

    if temp == 0:
        digits_count = 1

    while temp > 0:
        digit = temp % 10
        digits_count += 1
        temp //= 10

    total = 0
    temp2 = number

    while temp2 > 0:
        digit = temp2 % 10
        total += digit ** digits_count
        temp2 //= 10

    if number == total:
        print(f"{number} is an Armstrong number.")
    else:
        print(f"{number} is not an Armstrong number.")
