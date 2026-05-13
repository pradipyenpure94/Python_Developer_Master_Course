"""Check student grade based on marks."""

try:
    marks = float(input("Enter student marks: "))
    if marks > 90:
        print("Grade A")
    elif marks >= 75:
        print("Grade B")
    elif marks >= 60:
        print("Grade C")
    elif marks >= 35:
        print("Pass")
    else:
        print("Fail")
except ValueError:
    print("Invalid input! Please enter a number.")
