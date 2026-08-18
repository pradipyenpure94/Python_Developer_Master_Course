"""
Teacher + Researcher → Professor

Create a professor class inheriting from:

    Teacher
    Researcher
"""


class Teacher:
    """Represent a teacher."""

    def __init__(self, teacher_name: str) -> None:
        self.teacher_name = teacher_name


class Researcher:
    """Represent a researcher."""

    def __init__(self, researcher_name: str) -> None:
        self.researcher_name = researcher_name


class Professor(Teacher, Researcher):
    """Represent a professor."""

    def __init__(
        self,
        teacher_name: str,
        researcher_name: str,
        course: str
    ) -> None:
        Teacher.__init__(self, teacher_name=teacher_name)
        Researcher.__init__(self, researcher_name=researcher_name)
        self.course = course

    def display_professor_info(self) -> None:
        """Display professor information."""
        print("-" * 40)
        print("Professor Information: ")
        print("-" * 40)
        print(f"Teacher Name    : {self.teacher_name}")
        print(f"Researcher Name : {self.researcher_name}")
        print(f"Course          : {self.course}")
        print("-" * 40)


def main() -> None:
    """Run the main program."""
    professor = Professor(
        teacher_name="P.R Yenpure",
        researcher_name="Pradip",
        course="Python"
    )

    professor.display_professor_info()


if __name__ == "__main__":
    main()
