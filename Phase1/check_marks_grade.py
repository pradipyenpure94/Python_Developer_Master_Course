"""Check student grade based on marks."""

try:
    marks = float(input("Enter student marks: "))
    if marks < 0 or marks > 100:
        print("Marks must be between 1 to 100.")
    else:
        match marks:
            case marks if marks > 90:
                print("Grade A")
            case marks if marks >= 75:
                print("Grade B")
            case marks if marks >= 60:
                print("Grade C")
            case marks if marks >= 35:
                print("Pass")
            case _:
                print("Fail")
except ValueError:
    print("Invalid input! Please enter a number.")
