"""Check armstrong number"""

try:
    number = int(input("Enter a number: "))

    if number < 0:
        print("Armstrong number is not defined for negative numbers.")
    else:
        temp = number
        power = len(str(number))
        total = 0
        while temp > 0:
            digit = temp % 10
            total += digit ** power
            temp //= 10
        if total == number:
            print(f"{number} is an armstrong number.")
        else:
            print(f"{number} is not an armstrong number.")

except ValueError:
    print("Invalid input! Please enter an integer.")
