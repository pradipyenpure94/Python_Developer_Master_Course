"""
Student Result Management System

Use:
    Dictionary
    Functions
    Exception Handling
    File Handling
"""

from pathlib import Path
import csv

FILE_PATH = "Part1/student_result_mang_sys.csv"
FILE_NAME = Path(FILE_PATH).name
HEADERS = ["roll_no", "name", "python_marks", "db_marks", "github_marks",
           "total", "percentage", "result"]
TOTAL_MARKS = 300
PASS_PERCENT = 35


def create_csv_file() -> None:
    """Create a CSV File if not exist."""
    if not Path(FILE_PATH).exists():
        with open(file=FILE_PATH, mode="w", encoding="utf-8",
                  newline="") as file_obj:
            csv_writer = csv.writer(file_obj)
            csv_writer.writerow(HEADERS)
            print(f"{FILE_NAME} is created successfully.")


def load_students() -> list[dict[str, str]]:
    """
    Read the CSV file and fetch all data.

    Returns:
        list[dict[str, str]] : Return the list of students.
    """
    try:
        with open(file=FILE_PATH, mode="r", encoding="utf-8",
                  newline="") as file_obj:
            return list(csv.DictReader(file_obj))
    except FileNotFoundError:
        print("File does not exist.")
        return []
    except PermissionError:
        print("Permission denied.")
        return []


def save_students(students: list[dict[str, int | float | str]]) -> None:
    """
    Save student data into .csv File.

    Args:
        students (list[dict[str, int | float | str]]): Input list of students.
    """
    try:
        with open(file=FILE_PATH, mode="w", encoding="utf-8",
                newline="") as file_obj:
            csv_writer = csv.DictWriter(file_obj, fieldnames=HEADERS)
            csv_writer.writeheader()
            csv_writer.writerows(students)

    except PermissionError:
        print("Permission denied.")
    except OSError as error:
        print(f"Error: {error}")
    finally:
        print("Operation completed.")


def build_student_record(
    roll_no: int | str,
    name: str,
    python_marks: float,
    db_marks: float,
    github_marks: float
) -> dict[str, int | float | str]:
    """
    Build and return a student record.

    Args:
        roll_no (int | str): Input Roll No.
        name (str): Input name.
        python_marks (float): Input Python marks.
        db_marks (float): Input Database marks.
        github_marks (float): Input Github marks.

    Returns:
        str: Build and return a student record.
    """
    # All subject marks.
    total = python_marks + db_marks + github_marks
    # Calculate percentage of marks
    percentage = (total / TOTAL_MARKS) * 100
    # Result of students.
    result = "Pass" if percentage >= PASS_PERCENT else "Fail"

    return {
        "roll_no": roll_no,
        "name": name,
        "python_marks": python_marks,
        "db_marks": db_marks,
        "github_marks": github_marks,
        "total": total,
        "percentage": round(percentage, 2),
        "result": result,
    }


def validate_marks(subject: str, marks: float) -> None:
    """
    Validate subject marks and return a validation message.

    Args:
        subject (str): Input subject name.
        marks (float): Input subject marks.

    Raises:
        ValueError: If marks are not between 0 and 100.
    """
    if not 0 <= marks <= 100:
        raise ValueError(f"{subject} marks must be between 0 and 100.")


def gen_next_student_roll_no(students: list[dict[str, int | str | float]]) -> int:
    """
    Return the next student roll no.

    Args:
        students (list[dict[str, int | str | float]]): Input list of students.

    Returns:
        int: Student roll no.
    """
    if not students:
        return 1
    return max(int(record.get('roll_no')) for record in students) + 1


def add_student(students: list[dict[str, int | float | str]]) -> None:
    """
    Added a new student record into .csv File.

    Args:
        students (list[dict[str, int | float | str]]): Input list of student
                                                        records

    Raises:
        ValueError: If user enter invalid input marks.
        KeyboardInterrupt: If user enter Ctrl + C.
    """
    try:
        # Auto generate student roll_no. / ID.
        roll_no = gen_next_student_roll_no(students=students)

        # Student name.
        name = input("Enter student name: ").strip()
        if not name:
            raise ValueError("Name cannot be empty.")

        # Subject marks.
        python_marks = float(input("Enter Python marks: "))
        validate_marks(subject="Python", marks=python_marks)

        db_marks = float(input("Enter Database marks: "))
        validate_marks(subject="Database", marks=db_marks)

        github_marks = float(input("Enter github marks: "))
        validate_marks(subject="Github", marks=github_marks)

        # Build a student record.
        record = build_student_record(
            roll_no=roll_no,
            name=name,
            python_marks=python_marks,
            db_marks=db_marks,
            github_marks=github_marks
        )

    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nProgram interrupted.")
    else:
        # Save student record into .csv File.
        students.append(record)
        save_students(students=students)
        print("Added a new student record successfully.")
    finally:
        print("Operation completed.")


def view_students(students: list[dict[str, int | str | float]]) -> None:
    """Return the list of student details.
    Args:
        students (list[dict[str, int | str | float]]): Input list of students.
    """
    if not students:
        print("Students record not found.")
        return
    print("Students Result: ")
    print("-" * 90)
    print(f"| {'Roll No.':<7} | {'Name':<20} | {'Python':<5} | {'DB':<5} |"
        f" {'Github':<7} | {'Total':<5} | {'Per (%)':<5} | {'Result':<8} |")
    print("-" * 90)
    for record in students:
        print(f"| {record.get('roll_no'):>7}  | {record.get('name'):<20} |"
            f" {record.get('python_marks'):>6} | {record.get('db_marks'):>5}"
            f" | {record.get('github_marks'):>7} | {record.get('total'):>5}"
            f" | {record.get('percentage'):>7} | {record.get('result'):<8} |")
    print("-" * 90)


def search_student(students: list[dict[str, int | str | float]]) -> None:
    """
    Return the student details, search by roll no.

    Args:
        students (list[dict[str, int | str | float]]): Input list of students.

    Raises:
        ValueError: If user enter invalid input.
    """
    try:
        roll_no = int(input("Enter student Roll No.: "))
    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nProgram interrupted.")
    else:
        for record in students:
            if record.get('roll_no') == str(roll_no):
                print(f"Roll No.: {record.get('roll_no')}")
                print(f"Name: {record.get('name')}")
                break
        else:
            print("Student record not found.")
    finally:
        print("Operation completed.")


def update_student(students: list[dict[str, int | str | float]]) -> None:
    """
    Update student record details search by Roll No.

    Args:
        students (list[dict[str, int | str | float]]): Input list of students.
    """
    try:
        roll_no = int(input("Enter student roll no. to update: "))

        for index, record in enumerate(students):
            if record.get("roll_no") == str(roll_no):
                new_name = input("Enter a new name: ").strip()
                if not new_name:
                    raise ValueError("Name cannot be empty.")

                python_marks = float(input("Enter a new Python marks: "))
                validate_marks(subject="Python", marks=python_marks)

                db_marks = float(input("Enter a new Database marks: "))
                validate_marks(subject="Database", marks=db_marks)

                github_marks = float(input("Enter a new Github marks: "))
                validate_marks(subject="Github", marks=github_marks)

                update_record = build_student_record(
                    roll_no=roll_no,
                    name=new_name,
                    python_marks=python_marks,
                    db_marks=db_marks,
                    github_marks=github_marks
                )
                students[index] = update_record
                save_students(students=students)
                print("Updated student record successfully.")
                break
        else:
            print("Student record not found.")

    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nProgram interrupted.")
    finally:
        print("Operation completed.")


def delete_student(students: list[dict[str, int | float | str]]) -> None:
    """
    Delete a student record from .csv File.
    Args:
        students (list[dict[str, int | float | str]]): Input list of students.
    """
    try:
        roll_no = int(input("Enter a student roll no. to delete: "))
    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nProgram interrupted.")
    else:
        for index, record in enumerate(students):
            if record.get("roll_no") == str(roll_no):
                students.pop(index)
                save_students(students=students)
                print("Delete a student record successfully.")
                break
        else:
            print("Student record not found.")
    finally:
        print("Operation completed.")


def main() -> None:
    """Run student result managment system app."""

    # Create CSV file if not exist.
    create_csv_file()
    students = load_students()

    while True:
        print("Operations menu:")
        print("1. Add student")
        print("2. View students")
        print("3. Search student")
        print("4. Update student")
        print("5. Delete student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice not in {"1", "2", "3", "4", "5", "6"}:
            print("Invalid choice. Please select a valid option (1-6).")

        elif choice == "6":
            print("Exit from operations.")
            break

        elif choice == "1":
            add_student(students=students)

        elif choice == "2":
            view_students(students=students)

        elif choice == "3":
            search_student(students=students)

        elif choice == "4":
            update_student(students=students)

        elif choice == "5":
            delete_student(students=students)

        print("-" * 50)


if __name__ == "__main__":
    main()
