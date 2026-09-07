"""Create a student data file."""

from pathlib import Path

FILE_PATH = Path("Part5/Phase5/student_data.txt")
HEADERS = "id,name,marks\n"

MIN_MARKS = 0
MAX_MARKS = 100

def create_txt_file() -> None:
    """Create the student data file if it does not exist."""
    if not FILE_PATH.exists():
        with open(file=FILE_PATH, mode="w", encoding="utf-8") as file_obj:
            file_obj.write(HEADERS)
        print(f"{FILE_PATH.name} file is created successfully.")


def get_students_data() -> list[str]:
    """Get students data."""
    with open(file=FILE_PATH, mode="r", encoding="utf-8") as file_obj:
        next(file_obj)  # Skip header
        return file_obj.readlines()


def save_student(student: str) -> None:
    """Save student data to file."""
    with open(file=FILE_PATH, mode="a", encoding="utf-8") as file_obj:
        file_obj.write(student)


def auto_generate_next_id() -> int:
    """Return the next available student ID."""
    student_records = get_students_data()
    if not student_records:
        return 1
    max_student_id = max(
        int(record.split(",")[0]) for record in student_records
    ) + 1
    return max_student_id


def validate_student_name(name: str) -> str:
    """Validate and normalize the student name."""
    name = name.strip()

    if not name:
        raise ValueError("Student name cannot be empty.")

    if not all(char.isspace() or char.isalpha() for char in name):
        raise ValueError(
            "Student name must contain only alphabetic letters and spaces."
        )

    return name


def validate_student_marks(student_marks: float) -> None:
    """Validate the student marks."""
    if not MIN_MARKS <= student_marks <= MAX_MARKS:
        raise ValueError(
            f"Student marks must be between {MIN_MARKS} and {MAX_MARKS}."
        )


def add_student() -> None:
    """Add new student record."""
    try:
        student_id = auto_generate_next_id()
        student_name = input("Enter the student name: ")
        student_name = validate_student_name(name=student_name)
        student_marks = float(input("Enter the marks: "))
        validate_student_marks(student_marks=student_marks)

    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
    else:
        student_data = f"{student_id},{student_name},{student_marks}\n"
        save_student(student=student_data)
        print("Added a new student record successfully.")


def average_marks() -> None:
    """Calculate the average of student marks."""
    total_marks = 0
    total_students = 0

    for record in get_students_data():
        if record.strip():
            total_marks += float(record.split(",")[2])
            total_students += 1
    if total_students == 0:
        print("No students records available")
    else:
        average_marks = total_marks / total_students
        print(f"Student Average Marks: {average_marks:.2f}")


def main() -> None:
    """Run the main program."""
    # Create .txt file if not exists.
    create_txt_file()

    while True:
        print("1. Add student")
        print("2. Average Marks")
        print("3. Exit.")

        try:
            choice = input("Enter your choice: ").strip()

            if choice not in {"1", "2", "3"}:
                print("Please select a valid option (1-3).")
                continue

            if choice == "3":
                print("Exit from operations.")
                break

            if choice == "1":
                add_student()
            elif choice == "2":
                average_marks()

        except KeyboardInterrupt:
            print("\nOperation cancelled by the user.")
            break


if __name__ == "__main__":
    main()
