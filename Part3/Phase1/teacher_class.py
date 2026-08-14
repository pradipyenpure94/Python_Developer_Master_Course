"""Teacher + Researcher → Professor. Multiple inheritance."""


class Teacher:
    """Represent a teacher."""

    def show_teacher_info(self) -> None:
        """Show teacher information."""
        print("Show teacher information.")


class Researcher:
    """Represent a researcher."""

    def show_researcher_info(self) -> None:
        """show researcher information."""
        print("Show researcher information.")


class Professor(Teacher, Researcher):
    """Represent a professor."""

    def show_professor_info(self) -> None:
        """Show professor information."""
        print("Show professor information.")


def main() -> None:
    """Run the main program."""
    professor_object = Professor()
    professor_object.show_teacher_info()
    professor_object.show_researcher_info()
    professor_object.show_professor_info()


if __name__ == "__main__":
    main()
