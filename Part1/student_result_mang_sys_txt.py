"""
Student Result Management System

Use:
    1. Dictionary
    2. Functions
    3. Exception Handling
    4. File Handling
"""

from pathlib import Path

FILE_PATH = "Part1/student_result_mng_system.txt"
FILE_NAME = Path(FILE_PATH).name
HEADERS = "roll_no,name,python,database,github,total,percentage,result\n"
TOTAL_MARKS = 300


def create_txt_file() -> None:
    """Create a .txt file for storing student data."""
    if not Path(FILE_PATH).exists():
        with open(file=FILE_PATH, mode="w", encoding="utf-8") as file_obj:
            file_obj.write(HEADERS)
            print(f"{FILE_NAME} is created successfully.")


def load_students() -> list[str]:
    """Fetch all students data."""
    with open(file=FILE_PATH, mode="r", encoding="utf-8") as file_obj:
        next(file_obj)
        return file_obj.read().splitlines()


def save_students(students: list[str]) -> None:
    """Save students data into .txt file."""
    with open(file=FILE_PATH, mode="w", encoding="utf-8") as file_obj:
        file_obj.write(HEADERS)
        for record in students:
            file_obj.write(record + "\n")


def parse_student(student: str) -> list[str]:
    """Return the parse student record as a list of fields."""
    return student.split(",")


def build_student_record(
    roll_no: int | str, name: str, python_marks: float, db_marks: float,
                github_marks: float) -> str:
    """
    Build a student record based on user inputs.

    Args:
        roll_no (int): Auto generate student Id.
        name (str): Input student name.
        python_marks (float): Input Python marks.
        db_marks (float): Input Database marks.
        github_marks (float): Input Github marks.

    Returns:
        str: Build a record.
    """
    # Total subject marks.
    total = python_marks + db_marks + github_marks
    percentage = (total / TOTAL_MARKS) * 100
    # Student result: Pass / Fail.
    result = "Pass" if percentage >= 35 else "Fail"
    return ",".join(
        [
            str(roll_no),
            name,
            str(python_marks),
            str(db_marks),
            str(github_marks),
            str(total),
            str(round(percentage, 2)),
            result
        ]
    )


def next_gen_student_id(students: list[str]) -> int:
    """
    Generate next student roll_no ID.

    Returns:
        int: Students Roll No.
    """
    if not students:
        return 1
    return max(int(parse_student(student)[0]) for student in students) + 1


def add_student(students: list[str]) -> None:
    """Add student new record into .txt file."""

    # Auto generate next student ID.
    roll_no = next_gen_student_id(students=students)

    try:
        # Student name
        name = input("Enter student name: ").strip()
        if not name:
            raise ValueError("Name cannot be empty.")

        # Student subject marks.
        python_marks = float(input("Enter python marks: "))
        if not 0 <= python_marks <= 100:
            raise ValueError("Python marks must be between 0 and 100.")

        db_marks = float(input("Enter Database marks: "))
        if not 0 <= db_marks <= 100:
            raise ValueError("Database marks must be between 0 and 100.")

        github_marks = float(input("Enter github marks: "))
        if not 0 <= github_marks <= 100:
            raise ValueError("Github marks must be between 0 and 100.")

        # Build a student record
        record = build_student_record(
            roll_no=roll_no, name=name,
            python_marks=python_marks,
            db_marks=db_marks,
            github_marks=github_marks)

    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nProgram interrupted.")
    else:
        students.append(record)
        save_students(students=students)
        print("Added a new student record successfully.")
    finally:
        print("Operation completed.")


def view_students(students: list[str]) -> None:
    """Display all students."""
    if not students:
        print("Student record not found.")
    else:
        print("-" * 70)
        print(
            f"|{'Roll No.':<8}|{'Name':<15}|{'Python':<7}|{'DB':<5}|"
            f"{'GitHub':<7}|{'Total':<5}|{'Per (%)':<8}|{'Result':<6}|")
        print("-" * 70)
        for student in students:
            record = parse_student(student=student)
            print(
                f"|{record[0]:>8}|{record[1]:<15}|{record[2]:>7}|"
                f"{record[3]:>5}|{record[4]:>7}|{record[5]:>5}|"
                f"{record[6]:>8}|{record[7]:<6}|")
        print("-" * 70)


def search_student(students: list[str]) -> None:
    """Search student record by Roll No."""
    try:
        student_id = int(input("Enter student ID to search: "))

    except ValueError as error:
        print(f"Error: {error}")
    else:
        for student in students:
            record = parse_student(student=student)
            if record[0] == str(student_id):
                print(
                    f"Roll No.: {record[0]}\n"
                    f"Name: {record[1]}")
                break
        else:
            print("Student record not found.")
    finally:
        print("Operation completed.")


def update_student(students: list[str]) -> None:
    """Update editable fields into .txt file."""
    try:
        student_id = int(input("Enter student ID to update: "))

        for index, student in enumerate(students):
            record = parse_student(student=student)
            if record and record[0] == str(student_id):
                # Update student name
                record[1] = input("Update a new name: ").strip()
                if not record[1]:
                    raise ValueError("Name cannot be empty.")

                # Update Python marks
                record[2] = float(input("Update a new Python marks: "))
                if not 0 <= record[2] <= 100:
                    raise ValueError("Python marks must be between 0 and 100.")

                # Update Databse marks
                record[3] = float(input("Update a new Database marks: "))
                if not 0 <= record[3] <= 100:
                    raise ValueError("Database marks must be between 0 and 100.")

                # Update Github marks
                record[4] = float(input("Update a new Github marks: "))
                if not 0 <= record[4] <= 100:
                    raise ValueError("Github marks must be between 0 and 100.")

                # Build a student record
                update_record = build_student_record(
                    roll_no=record[0],
                    name=record[1],
                    python_marks=record[2],
                    db_marks=record[3],
                    github_marks=record[4])

                # Update record into .txt File.
                students[index] = update_record
                save_students(students=students)
                print("Updated record successfully.")
                break
        else:
            print("Student record not found.")

    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nProgram interrupted.")
    finally:
        print("Operation completed.")


def delete_student(students: list[str]) -> None:
    """Delete a student record by student ID from .txt File."""
    try:
        delete_student_id = int(input("Enter a student ID to delete: "))
        for index, student in enumerate(students):
            record = parse_student(student=student)
            if record[0] == str(delete_student_id):
                students.pop(index)
                save_students(students=students)
                print("Deleted record successfully.")
                break
        else:
            print("Student record not found.")
    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nProgram interrupted.")
    finally:
        print("Operation completed.")


def main() -> None:
    """Run the Student Application."""
    # Create .txt file if not exist.
    create_txt_file()

    students = load_students()

    while True:
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
