"""Function using **kwargs."""


def person_information(**kwargs: int | str) -> None:
    """Display person Information."""
    print("-" * 30)
    print("Person Information")
    print("-" * 30)
    print(f"Name      : {kwargs['name']}")
    print(f"Age       : {kwargs['age']}")
    print("-" * 30)


if __name__ == "__main__":
    person_information(name="Pradip", age=33)
