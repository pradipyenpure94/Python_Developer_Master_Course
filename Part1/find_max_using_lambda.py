"""Find maximum using lambda."""


def find_max(data: dict[str, int]) -> tuple[str, int]:
    """
    Return the key and its maximum value pair.

    Args:
        data (dict[str, int]): Input data.

    Returns:
        tuple[str, int]: A tuple containing the key and its maximum value.
    """
    return max(data.items(), key=lambda x: x[1])


if __name__ == "__main__":
    input_data = {"orange": 1, "cheery": 5, "banana": 4}
    print(f"Input data: {input_data}")

    try:
        result = find_max(data=input_data)
    except ValueError as error:
        print(f"Error: {error}")
    else:
        print(f"Max.: {result}")
    finally:
        print("Operation completed.")
