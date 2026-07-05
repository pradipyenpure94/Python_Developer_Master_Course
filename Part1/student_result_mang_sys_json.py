"""
Student Result Management System
Use:
    Dictionary
    Functions
    Exception Handling
    File Handling
"""

import json
from pathlib import Path
from typing import Any

FILE_PATH = "Part1/student_result_mang_sys.json"
FILE_NAME = Path(FILE_PATH).name
TOTAL_MARKS = 300
PASS_PERCENT = 35


def create_json_file() -> None:
    """Create a json file if not exist."""
    try:
        if not Path(FILE_PATH).exists():
            with open(file=FILE_PATH, mode="w", encoding="utf-8") as file_obj:
                json.dump([], file_obj)
    except OSError as error:
        print(f"Error: {error}")


def load_students_data() -> list[dict[str, str | int | float]]:
    """Fetch all students data from .json File."""
    try:
        with open(file=FILE_PATH, mode="r", encoding="utf-8") as file_obj:
            return json.load(file_obj)
    except PermissionError:
        print("Permission denied.")
        return []
    except FileNotFoundError:
        print(f"{FILE_NAME} does not exist.")
        return []
    except json.JSONDecodeError:
        print("Invalid JSON File.")
        return []


def save_students_data(students: list[dict[str, str | int | float]]) -> None:
    """Save students data into .json File."""
    try:
        with open(file=FILE_PATH, mode="w", encoding="utf-8") as file_obj:
            json.dump(students, file_obj, indent=4)
    except PermissionError:
        print("Permission denied.")
    except OSError as error:
        print(f"Error: {error}")


def get_total_marks(python_marks: float,
                    db_marks: float,
                    github_marks: float) -> float:
    """
    Return the total marks of student.

    Args:
        python_marks (float): Input python marks.
        db_marks (float): Input database marks.
        github_marks: Input github marks.
    Returns:
        float: Return a total marks of subjects.
    """
    return python_marks + db_marks + github_marks


def get_per_of_marks(total: float) -> float:
    """
    Return the percentage of marks.

    Args:
        total (float): Input total marks of subjects.

    Returns:
        float: Return a percentage of marks.
    """
    return (total / TOTAL_MARKS) * 100


def build_student_record(
    roll_no: int | str,
    name: str,
    python_marks: float,
    db_marks: float,
    github_marks: float) -> dict[str, Any]:
    """Build and return a student record."""
    # Total all subject of marks
    total = get_total_marks(
        python_marks=python_marks,
        db_marks=db_marks,
        github_marks=github_marks
    )
    # Percentage of marks
    percentage = get_per_of_marks(total=total)
    # Student result
    result = "Pass" if percentage >= PASS_PERCENT else "Fail"
    return {
        "roll_no": roll_no,
        "name": name,
        "subjects":
            [
                {
                    "python_marks": python_marks,
                    "db_marks": db_marks,
                    "github_marks": github_marks
                }
            ],
        "total": total,
        "percentage": round(percentage, 2),
        "result": result
    }


def gen_next_student_roll_no(students: list[dict[str, str]]) -> int:
    """
    Generate next and return a student roll no.
    """
    if not students:
        return 1
    return max(int(record.get("roll_no")) for record in students) + 1


def validate_marks(subject: str, marks: float) -> None:
    """Raise error message and validate student marks between 0 and 100."""
    if not 0 <= marks <= 100:
        raise ValueError(f"{subject} marks must be between 0 and 100.")


def validate_name(name: str) -> None:
    """Raise error message and validate name."""
    if not name:
        raise ValueError("Name cannot be empty.")


def add_student(students: list[dict[str, Any]]) -> None:
    """Add a new student record into json. File."""

    # Auto generate student roll no.
    roll_no = gen_next_student_roll_no(students=students)

    try:
        name = input("Enter a student name: ").strip()
        validate_name(name=name)

        python_marks = float(input("Enter a Python marks: "))
        validate_marks(subject="Python", marks=python_marks)

        db_marks = float(input("Enter a Database marks: "))
        validate_marks(subject="Database", marks=db_marks)

        github_marks = float(input("Enter a Github marks: "))
        validate_marks(subject="Github", marks=github_marks)

    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nProgram interrupted.")
    else:
        new_record = build_student_record(
            roll_no=roll_no,
            name=name,
            python_marks=python_marks,
            db_marks=db_marks,
            github_marks=github_marks
        )
        students.append(new_record)
        save_students_data(students=students)
        print("Added a new student record successfully.")
    finally:
        print("Operation completed.")


def view_students(students: list[dict[str, str]]) -> None:
    """Display list of students data in tabular format."""
    if not students:
        print("Students record not found.")
        return

    print("Students result:")
    print("-" * 88)
    print(f"| {'Roll No.':>8}| {'Name':<20} | {'Python':>5}| {'Database':>5}"
        f"| {'Github':>5}| {'Total':>5} | {'Per (%)':>7} | {'Result':>7} |")
    print("-" * 88)
    for student in students:
        for subject in student.get('subjects'):
            print(f"| {student.get('roll_no'):>7} | {student.get('name'):<20}"
                f" | {subject['python_marks']:>5} | {subject['db_marks']:>7} |"
                f" {subject['github_marks']:>5} | {student.get('total'):>5} | "
                f"{student.get('percentage'):>7} | {student.get('result'):<7}"
                f" | ")

    print("-" * 88)


def search_student(students: list[dict[str, str | int | float]]) -> None:
    """
    Search student record from .json File.

    Args:
        students (list[dict[str, str | int | float]]): Input list of students.

    Raises:
        ValueError: If invalid roll no.
    """
    try:
        roll_no = int(input("Enter student roll no to be search: "))

    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nProgram interrupted.")
    else:
        for record in students:
            if record.get('roll_no') == roll_no:
                print(f"Roll No.: {record.get('roll_no')}\n"
                    f"Name: {record.get('name')}")
                break
        else:
            print("Student record not found.")
    finally:
        print("Operation completed.")


def update_student(students: list[dict[str, int | str | float]]) -> None:
    """
    Update student record, by roll no.

    Args:
        students (list[dict[str, int | str | float]]): Input list of students.
    """
    try:
        roll_no = int(input("Enter student roll no. to update record: "))
        for index, record in enumerate(students):
            if record.get("roll_no") == roll_no:
                new_name = input("Enter a new name: ").strip()
                validate_name(name=new_name)

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
                save_students_data(students=students)
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
    Delete a student record from .json File.

    Args:
        students (list[dict[str, int | float | str]]): Input list of students.
    """
    try:
        roll_no = int(input("Enter a student roll no. to be delete: "))

    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nProgram interrupted.")
    else:
        for index, record in enumerate(students):
            if record.get("roll_no") == roll_no:
                students.pop(index)
                save_students_data(students=students)
                print("Students record deleted successfully.")
                break
        else:
            print("Student record not found.")


def main() -> None:
    """Student Result Management System running App."""
    # Create .json File if not exist.
    create_json_file()

    students = load_students_data()

    while True:
        print("Student operations menu: ")
        print("1. Add student")
        print("2. View students")
        print("3. Search student")
        print("4. Update student")
        print("5. Delete student")
        print("6. Exit")

        try:
            choice = input("Enter your choice: ")
        except KeyboardInterrupt:
            print("\nProgram interrupted.")
        else:
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
