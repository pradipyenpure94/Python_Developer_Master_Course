"""Check leap year."""

from calendar import isleap

try:
    year = int(input("Enter a year: "))
except ValueError:
    print("Invalid input. Please enter an integer.")
except KeyboardInterrupt:
    print("\nProgram interrupted.")
else:
    if isleap(year=year):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")
finally:
    print("Operation completed.")
