"""Without match-case example."""


import calendar

days = list(calendar.day_name)

try:
    day_number = int(input("Enter the day (int): "))

    if 0 <= day_number < len(days):
        print(days[day_number])
    else:
        print("Invalid day. Please enter a number 0 to 6.")

except ValueError:
    print("Invalid input. Please enter an integer.")
except KeyboardInterrupt:
    print("\nOperation cancelled by the user.")
