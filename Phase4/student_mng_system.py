"""Student management system."""

import csv
from pathlib import Path


HEADERS = ["id", "name", "marks"]
FILEPATH: str = "file_handling/student_csv_file.csv"


def create_csv_file() -> None:
    """Create CSV file if not exist."""
    if not Path(FILEPATH).exists():
        with open(FILEPATH, mode="w", encoding="utf-8",
                  newline="") as file_obj:
            csv_writer = csv.writer(file_obj)
            csv_writer.writerow(HEADERS)
            file_name = Path(FILEPATH).name
            print(f"{file_name} is created successfully.")


def load_data() -> list[dict[str, str]]:
    """Fetch all student records from CSV file."""
    with open(FILEPATH, mode="r", encoding="utf-8") as file_obj:
        csv_reader = csv.DictReader(file_obj)
        return list(csv_reader)


def save_data(students: list[dict[str, str]]) -> None:
    """Write all student records into CSV file."""
    with open(FILEPATH, mode="w", encoding="utf-8", newline="") as file_obj:
        csv_writer = csv.DictWriter(file_obj, fieldnames=HEADERS)
        csv_writer.writeheader()
        csv_writer.writerows(students)


def next_student_id(students: list[dict[str, str]]) -> int:
    """
    Generate next student Id.

    Args:
        students (list[dict]): Students data.

    Returns:
        int: Students record Id.
    """
    if not students:
        return 1
    return max(int(record['id']) for record in students) + 1


def unique_student_name(students: list[dict[str, str]]) -> str | None:
    """
    Return the unique name of a student.

    Args:
        students (list[dict[str, str]]): Students data.

    Returns:
        str | None: Student name if unique, otherwise None.
    """
    student_name = input("Enter a student name: ").strip()
    if not student_name or " " in student_name:
        return None

    student_names = {
        record["name"].casefold()
        for record in students
        if record["name"]
        }
    if student_name.casefold() in student_names:
        return None
    return student_name


def add_student(students: list[dict[str, str]]) -> None:
    """
    Add a new student record to the CSV file.

    Args:
        students (list[dict]): Students data.

    Returns:
        None.
    """
    student_id = next_student_id(students=students)
    student_name = unique_student_name(students=students)

    if student_name is None:
        print("Student name already exists or is invalid.")
        return

    try:
        student_marks = float(input("Enter student marks:"))
        if student_marks < 0 or student_marks > 100:
            print("Student marks should be between 0 and 100.")
            return

        # Add new record into CSV file.
        students.append({
            "id": str(student_id),
            "name": student_name,
            "marks": str(student_marks)
            })
        # Save record into CSV file.
        save_data(students=students)
        print("Added new record successfully.")

    except ValueError:
        print("Invalid input. Please enter a number.")


def search_student(students: list[dict[str, str]]) -> None:
    """
    Check whether student record is found or not.

    Args:
        students (list[dict]): Students data.

    Returns:
        None.
    """
    try:
        student_id = int(input("Enter student ID to search? "))

        for record in students:
            if record['id'] == str(student_id):
                print(f"Student record found:\n"
                      f"ID: {record['id']}\n"
                      f"Name: {record['name']}\n"
                      f"Marks: {record['marks']}")
                break
        else:
            print("Student record not found.")
    except ValueError:
        print("Invalid input. Please enter an integer.")


def view_all_students(students: list[dict[str, str]]) -> None:
    """
    Display all students.

    Args:
        list[dict]: Students data.

    Returns:
        None.
    """
    if not students:
        print("No student records available.")
        return

    print("Students Information:")
    print("--"*27)  # Separator line
    # print header
    print(f"| {'ID.':<5} | {'Name':<30} | {'Marks':<10} |")
    print("--"*27)  # Separator line
    for record in students:
        print(f"| {record['id']:<5} | {record['name']:<30}"
              f" | {record['marks']:<10} |")
    print("--"*27)  # Separator line


def calculate_avg_marks(students: list[dict[str, str]]) -> None:
    """
    Calculate average marks of students.

    Args:
        students (list[dict[str, str]]): Students data.

    Returns:
        None.
    """
    if not students:
        print("No student records available.")
        return
    valid_marks = [float(record["marks"])
                   for record in students
                   if record["marks"]]
    average_marks = sum(valid_marks) / len(valid_marks)
    print(f"Avg. marks of student: {average_marks:.2f}")


def main() -> None:
    """Main Program."""

    # Create new CSV file if not exist.
    create_csv_file()

    # Fetch all students data.
    students = load_data()

    while True:
        print("*"*50)
        print("Student operations menu: ")
        print("1. Add student")
        print("2. Search student")
        print("3. Display all students")
        print("4. Calculate Average of Marks")
        print("5. Exit")

        choice = input("Enter your choice? ")

        if choice not in {"1", "2", "3", "4", "5"}:
            print("Invalid choice. Please select valid operations choice.")

        elif choice == "5":
            print("Exit from operations.")
            break

        elif choice == "1":
            add_student(students=students)

        elif choice == "2":
            search_student(students=students)

        elif choice == "3":
            view_all_students(students=students)

        elif choice == "4":
            calculate_avg_marks(students=students)

        print("*"*50)


if __name__ == "__main__":
    main()
