"""Check whether a number is a palindrome"""


try:
    number = int(input("Enter a number: "))

    if number < 0:
        print("Negative numbers are not palindrome numbers.")
    else:
        temp = number
        reversed_number = 0

        while temp > 0:
            reversed_number = reversed_number * 10 + temp % 10
            temp //= 10

        if number == reversed_number:
            print(f"{number} is a palindrome number.")
        else:
            print(f"{number} is not a palindrome number.")

except ValueError:
    print("Invalid input! Please enter an integer.")
