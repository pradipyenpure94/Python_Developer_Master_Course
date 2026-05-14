"""Check whether a number is a perfect number."""


try:
    number = int(input("Enter a number: "))

    if number <= 0:
        print("Please enter a positive integer greater than zero.")
    else:
        total = 0

        for i in range(1, number):
            if number % i == 0:
                total += i

        if number == total:
            print(f"{number} is a perfect number.")
        else:
            print(f"{number} is not a perfect number.")

except ValueError:
    print("Invalid input! Please enter an integer.")
