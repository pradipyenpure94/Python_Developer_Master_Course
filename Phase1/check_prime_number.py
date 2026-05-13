"""Check whether a number is prime."""

try:
    number = int(input("Enter a number: "))

    is_prime = True

    if number < 2:
        is_prime = False
    else:
        i = 2
        stop = int(number ** 0.5) + 1
        while i < stop:
            if number % i == 0:
                is_prime = False
                break
            i += 1
    if is_prime:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")

except ValueError:
    print("Invalid input! Please enter an integer.")
