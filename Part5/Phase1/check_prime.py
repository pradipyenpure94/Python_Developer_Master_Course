"""Check whether a number is prime."""


try:
    number = int(input("Enter the number: "))
except ValueError as error:
    print(f"Error: {error}")
except KeyboardInterrupt:
    print("\nOperation cancelled by the user.")
else:
    if number < 2:
        print(f"{number} is not a prime number.")
    else:
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                print(f"{number} is not a prime number.")
                break
        else:
            print(f"{number} is a prime number.")
