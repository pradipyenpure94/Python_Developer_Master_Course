"""Find total marks of students."""

from functools import reduce


def find_total_marks_of_student(students: list[dict[str, str | list[int]]]
                                ) -> dict[str, int]:
    """
    Return the total marks obtained by each student.

    Args:
        students (list[dict[str, str | list[int]]]): Input list of student
        records.

    Returns:
        dict[str, int]: Mapping of student names to their total marks.
    """
    return {student['name']: reduce(lambda x, y: x + y, student['marks'], 0)
            for student in students}


if __name__ == "__main__":
    student_info = [{"name": "Pradip", "marks": [1, 2, 3, 4, 5, 6]},
                    {"name": "Amit", "marks": [1, 2, 3, 4, 5]}
                    ]
    result = find_total_marks_of_student(students=student_info)
    print(f"Total mark of students:{result}")
