"""Count even and odd digits in a number"""


try:
    num = int(input("Enter a number: "))

    even = 0
    odd = 0

    temp = abs(num)

    if temp == 0:
        even = 1

    while temp > 0:
        digit = temp % 10
        if digit % 2 == 0:
            even += 1
        else:
            odd += 1
        temp //= 10

    print(f"Even digits: {even}\nOdd digits: {odd}")

except ValueError:
    print("Invalid input! Please enter an integer.")
