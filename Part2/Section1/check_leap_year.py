"""Check leap year."""

try:
    year = int(input("Enter a year: "))
except ValueError:
    print("Invalid input. Please enter an integer.")
except KeyboardInterrupt:
    print("\nProgram interrupted.")
else:
    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")
finally:
    print("Operation completed.")
