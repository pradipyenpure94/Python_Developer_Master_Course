"""Import and reuse custom functions."""

from calculator import add


def main() -> None:
    """Run the main program."""
    result = add(first_number=10.5, second_number=1.5)
    print(f"Addition: {result:.2f}")


if __name__ == "__main__":
    main()
