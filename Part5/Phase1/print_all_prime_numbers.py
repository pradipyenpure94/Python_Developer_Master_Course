"""Print all prime numbers from 1 to N."""


try:
    number_limit = int(input("Enter the number limit: "))
except ValueError as error:
    print(f"Error: {error}")
except KeyboardInterrupt:
    print("\nOperation cancelled by the user.")
else:
    if number_limit < 2:
        print("Not Prime numbers are found.")
    else:
        print("Prime numbers are:")
        for number in range(2, number_limit + 1):
            for i in range(2, int(number ** 0.5) + 1):
                if number % i == 0:
                    break
            else:
                print(number)
