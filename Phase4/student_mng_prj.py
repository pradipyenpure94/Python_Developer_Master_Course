"""
Mini Project: JSON CRUD Application.

Operations:
    1. Add student
    2. View students
    3. Search student
    4. Update student
    5. Delete student
    6. Count students
    7. Exit
"""

import json
from pathlib import Path

FILEPATH = "Phase4/students.json"


def create_json_file() -> None:
    """Create JSON file if not exist."""
    if not Path(FILEPATH).exists():
        with open(file=FILEPATH, mode="w", encoding="utf-8") as file_obj:
            json.dump([], file_obj, indent=4)


def load_data() -> list[dict[str, int | str]]:
    """Fetch students all data from JSON file."""
    try:
        with open(file=FILEPATH, mode="r", encoding="utf-8") as file_obj:
            return json.load(file_obj)
    except FileNotFoundError:
        print("File does not exist.")
        return []
    except json.JSONDecodeError:
        print("Invalid JSON file format.")
        return []


def save_data(students: list[dict[str, int | str]]) -> None:
    """Save data into JSON file."""
    with open(file=FILEPATH, mode="w", encoding="utf-8") as file_obj:
        json.dump(students, file_obj, indent=3)


def next_student_id(students: list[dict[str, int | str]]) -> int:
    """
    Generate next student ID.

    Args:
        students (list[dict[str, int | str]]): Input students data.

    Returns:
        int: Unique student ID.
    """
    if not students:
        return 1

    return max(record.get("id", 0) for record in students) + 1


def is_record_found(students: list[dict[str, int | str]], student_id: int) -> bool:
    """
    Check whether a student record is found.

    Args:
        students (list[dict[str, int | str]]): Input students data.
        student_id (int): Input student ID.

    Returns:
        bool: True if record found, otherwise False.
    """

    return any(
        record.get("id") == student_id
        for record in students
    )


def add_student(students: list[dict[str, int | str]]) -> None:
    """
    Add a new student record into JSON File.

    Args:
        students (list[dict[str, int | str]]): Input students data.

    Returns:
        None.
    """
    student_id = next_student_id(students)
    student_name = input("Enter student name: ").strip()

    if not student_name:
        print("Student name cannot be empty.")
        return

    students.append({
        "id": student_id,
        "name": student_name
    })

    save_data(students=students)
    print("Added new student record successfully.")


def view_students(students: list[dict[str, int | str]]) -> None:
    """
    Display all students from JSON file.

    Args:
        students (list[dict[str, int | str]]): Input students data.

    Returns:
        None.
    """
    print("List of Students: ")
    if not students:
        print("Empty students data.")
        return

    print("-" * 37)
    print(f"| {'ID.':<5} | {'Name':<25} |")
    print("-" * 37)
    for record in students:
        print(f"| {record.get('id'):<5} | {record.get('name'):<25} |")
    print("-" * 37)


def search_student(students: list[dict[str, str | int]]) -> None:
    """
    Search student record from JSON File.

    Args:
        students (list[dict[str, int | str]]): Input students data.

    Returns:
        None.
    """
    try:
        student_id = int(input("Enter student ID to search: "))

    except ValueError:
        print("Invalid input. Please enter a integer.")
    else:
        for record in students:
            if record.get("id") == student_id:
                print("Student record found:")
                print(f"Student ID: {record.get('id')}\n"
                      f"Student Name: {record.get('name')}")
                break
        else:
            print("Student record not found.")
    finally:
        print("Operation completed.")


def update_student(students: list[dict[str, int | str]]) -> None:
    """
    Update student record into JSON File.

    Args:
        students list[dict[str, int | str]]: Input students data.

    Returns:
        None.
    """
    try:
        student_id = int(input("Enter student ID to update record: "))
    except ValueError:
        print("Invalid input. Please enter a integer.")
    else:
        for record in students:
            if record.get("id") == student_id:
                name = input("Enter student name: ").strip()
                if not name:
                    print("Student name cannot be empty.")
                    return
                record["name"] = name
                save_data(students=students)
                print("Student record updated successfully.")
                break
        else:
            print("Student record not found.")
    finally:
        print("Operation completed.")


def delete_student(students: list[dict[str, int | str]]) -> None:
    """
    Delete student record from JSON file.

    Args:
        students (list[dict[str, int | str]]): Input students data.

    Returns:
        None.
    """
    try:
        student_id = int(input("Enter student ID to delete: "))
    except ValueError:
        print("Invalid input. Please enter a integer.")
    else:
        if is_record_found(students=students, student_id=student_id):
            students[:] = [record for record in students
                           if record.get("id") != student_id]
            save_data(students)
            print("Student record deleted successfully.")
        else:
            print("Student record not found.")
    finally:
        print("Operation completed.")


def count_students(students: list[dict[str, int | str]]) -> None:
    """
    Return the total students count from JSON File.

    Args:
        students (list[dict[str, int | str]]): Input students data.

    Returns:
        None.
    """
    print(f"Total students count: {len(students)}")


def main():
    """Main Program"""
    # Create JSON File if not exist.
    create_json_file()

    students = load_data()

    while True:
        print("Student operations:")
        print("1. Add student")
        print("2. View students")
        print("3. Search student")
        print("4. Update student")
        print("5. Delete student")
        print("6. Count students")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice not in {"1", "2", "3", "4", "5", "6", "7"}:
            print("Invalid choice. Please select valid operations.")

        elif choice == "7":
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

        elif choice == "6":
            count_students(students=students)

        print(" * " * 15)


if __name__ == "__main__":
    main()
