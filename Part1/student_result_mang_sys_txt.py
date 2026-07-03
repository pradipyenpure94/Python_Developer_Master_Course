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
            file_obj.write(record)


def calculate_result(python: float, db: float,
                     github: float) -> tuple[float, float, str]:
    """
    Return the total marks, percentage of marks and result.

    Args:
        python (float): Input Python subject marks.
        github (float): Input Github subject marks.
        db (float): Input Database subject marks.

    Returns:
        tuple[float, float, str]: A new tuple containing the total marks,
        percentage of marks and result like Pass or Fail
    """
    TOTAL_MARKS = 300
    # Total subject marks.
    total = python + db + github
    # Percentage of marks.
    percentage = (total / TOTAL_MARKS) * 100
    # Student result: Pass / Fail.
    result = "Pass" if percentage >= 35 else "Fail"
    return total, percentage, result


def next_gen_student_id(students: list[str]) -> int:
    """
    Generate next student roll_no ID.

    Returns:
        int: Students Roll No.
    """
    if not students:
        return 1
    return max(int(record.split(",")[0]) for record in students
               if record and record.split(",") and record.split(",")[0]) + 1


def add_new_record_line(students: list[str]) -> str:
    """Append new student record line."""
    record = ""

    # Auto generate next student ID.
    roll_no = next_gen_student_id(students=students)
    record += str(roll_no) + ","
    try:
        # Student name
        name = input("Enter student name: ")
        record += name + ","

        # Student subject marks.
        python_marks = float(input("Enter python marks: "))
        record += str(python_marks) + ","

        db_marks = float(input("Enter Database marks: "))
        record += str(db_marks) + ","

        github_marks = float(input("Enter github marks: "))
        record += str(github_marks) + ","

        total, percentage, result = calculate_result(python=python_marks,
                                                     db=db_marks,
                                                     github=github_marks)
        record += str(total) + ","
        record += str(round(percentage, 2)) + ","
        record += result + "\n"
        return record
    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nProgram interrupted.")
    finally:
        print("Operation completed.")


def add_student(students: list[str]) -> None:
    """Add student new record into .txt file."""
    record = add_new_record_line(students=students)
    if record is not None:
        students.append(record)
        save_students(students=students)
        print("Added a new student record successfully.")


def view_students(students: list[str]) -> None:
    """Display all students."""
    if not students:
        print("Student record not found.")
    else:
        print("-" * 66)
        print(f"|{'Roll|\n|No. ':<4}|{'Name':<15}|{'Python':<7}|{'DB':<5}|"
              f"{'GitHub':<7}|{'Total':<5}|{'Per (%)':<8}|{'Result':<6}|")
        print("-" * 66)
        for rec in students:
            rec = rec.split(",")
            print(f"|{rec[0]:>4}|{rec[1]:<15}|{rec[2]:>7}|{rec[3]:>5}|"
                  f"{rec[4]:>7}|{rec[5]:>5}|{rec[6]:>8}|{rec[7]:<6}|")
        print("-" * 66)


def search_student(students: list[str]) -> None:
    """Search student record by Roll No."""
    try:
        student_id = int(input("Enter student ID to search: "))

    except ValueError as error:
        print(f"Error: {error}")
    else:
        for rec in students:
            rec = rec.split(",")
            if rec[0] == str(student_id):
                print(f"Roll No.: {rec[0]}\n"
                      f"Name: {rec[1]}")
                break
        else:
            print("Student record not found.")
    finally:
        print("Operation completed.")


def update_student(students: list[str]) -> None:
    """Update editable fields into .txt file."""
    try:
        student_id = int(input("Enter student ID to update: "))
        update_record = ""
        for index, rec in enumerate(students):
            record = rec.split(",")
            if record and record[0] == str(student_id):
                update_record += record[0] + ","
                # Update student name
                record[1] = input("Update a new name: ")
                update_record += record[1] + ","
                # Update Python marks
                record[2] = float(input("Update a new Python marks: "))
                update_record += str(record[2]) + ","
                # Update Databse marks
                record[3] = float(input("Update a new Database marks: "))
                update_record += str(record[3]) + ","
                # Update Github marks
                record[4] = float(input("Update a new Github marks: "))
                update_record += str(record[4]) + ","

                total, percentage, result = calculate_result(python=record[2],
                                                             db=record[3],
                                                             github=record[4])

                update_record += str(total) + ","
                update_record += str(round(percentage, 2)) + ","
                update_record += result + "\n"
                students[index] = update_record
                # Update record into .txt File.
                save_students(students=students)
                break
        else:
            print("Student record not found.")

    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nProgram interrupted.")
    else:
        print("Updated record successfully.")
    finally:
        print("Operation completed.")


def delete_student(students: list[str]) -> None:
    """Delete a student record by student ID from .txt File."""
    try:
        delete_student_id = int(input("Enter a student ID to delete: "))
        for index, rec in enumerate(students):
            record = rec.split(",")
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
