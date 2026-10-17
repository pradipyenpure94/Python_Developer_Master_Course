"""Match case example."""

try:
    day = int(input("Enter the day (int): "))

    match day:
        case 0:
            print("Sunday")
        case 1:
            print("Monday")
        case 2:
            print("Tuesday")
        case 3:
            print("Wednesday")
        case 4:
            print("Thursday")
        case 5:
            print("Friday")
        case 6:
            print("Saturday")
        case _:
            print("Invalid day. Please enter an integer from 0 to 6.")
except KeyboardInterrupt:
    print("\nOperation cancelled by the user.")
except ValueError:
    print("Invalid input. Please enter an integer.")
