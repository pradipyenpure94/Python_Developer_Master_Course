"""Calculate percentage of five subjects."""

TOTAL_SUBJECT_MARKS = 500

first_subject = 15
second_subject = 75
third_subject = 78
fourth_subject = 85
fifth_subject = 79

percentage_of_subjects = (
    first_subject
    + second_subject
    + third_subject
    + fourth_subject
    + fifth_subject
) / TOTAL_SUBJECT_MARKS * 100

print(f"Percentage of Subjects: {percentage_of_subjects:.2f}")
