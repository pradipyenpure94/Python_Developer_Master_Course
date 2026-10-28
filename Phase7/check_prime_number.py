"""Check whether a number is prime."""

number = 2

if number <= 1:
    print("Not Prime number.")
else:
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            print("Not Prime number")
            break
    else:
        print("Prime number.")
