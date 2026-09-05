"""Function returning multiple values."""


def person_information(name: str, age: int) -> tuple[str, int]:
    """Return the person information."""
    return name, age


if __name__ == "__main__":
    name, age = person_information(name="Pradip", age=33)
    print("-" * 30)
    print("Person Information:")
    print("-" * 30)
    print(f"Name : {name}")
    print(f"Age  : {age}")
    print("-" * 30)
