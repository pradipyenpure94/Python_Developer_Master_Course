"""Calculate subject-wise and overall student-percentages."""

try:
    number_of_subjects = int(input("Enter the number of subjects: "))
    if number_of_subjects <= 0:
        raise ValueError("Number of subjects must be greater than zero.")

    total_marks = 0
    for i in range(1, number_of_subjects + 1):
        marks = float(input(f"Enter the marks for subject {i} : "))
        if not 0 <= marks <= 100:
            raise ValueError("Marks must be between 0 and 100.")
        total_marks += marks

    percentage = total_marks / number_of_subjects
except ValueError as error:
    print(f"Error: {error}")
except KeyboardInterrupt:
    print("\nOperation cancelled by the user.")
else:
    print(f"Percentage : {percentage:.2f}%")
