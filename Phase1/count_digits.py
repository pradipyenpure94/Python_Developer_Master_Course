"""Count digits of given input number"""


try:
    number = int(input("Enter a number: "))

    temp = abs(number)
    count = 0

    if temp == 0:
        count = 1

    while temp > 0:
        digit = temp % 10
        count += 1
        temp //= 10
    print(f"Count digits: {count}")

except ValueError:
    print("Invalid input! Please enter an integer.")
