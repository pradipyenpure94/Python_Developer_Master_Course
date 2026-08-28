"""Check whether a number is palindrome."""


try:
    number = int(input("Enter the number: "))
    if number < 0:
        raise ValueError("Number cannot be negative.")

except ValueError as error:
    print(f"Error: {error}")
except KeyboardInterrupt:
    print("\nOperation cancelled by the user.")
else:
    reversed_number = 0
    temp = number

    while temp > 0:
        digit = temp % 10
        reversed_number = reversed_number * 10 + digit
        temp //= 10

    if number == reversed_number:
        print("It is a palindrome.")
    else:
        print("It is not a palindrome.")
