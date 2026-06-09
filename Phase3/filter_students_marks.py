"""Filter students with marks > 75."""


def filter_students_marks_greater_than_75(
        marks: list[dict[str, int | str]]) -> list[dict[str, int | str]]:
    """
    Return a new list containing the student marks greater than 75.

    Args:
        marks (list[dict[str, int | str]]): Input student records.

    Returns:
        list[dict[str, int | str]]: A new list containing the students scores
                            greater than 75.
    """
    return list(filter(lambda student: student['score'] > 75, marks))


if __name__ == "__main__":
    students = [{"name": "Pradip", "score": 96}, {"name": "amit", "score": 76},
                {"name": "ravi", "score": 45}, {"name": "sanjay", "score": 56}]
    result = filter_students_marks_greater_than_75(marks=students)
    print(f"Filter students marks:{result}")
