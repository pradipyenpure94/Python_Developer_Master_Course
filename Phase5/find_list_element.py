"""Find list element."""

from typing import Any


def find_element_of_list(data: list[Any], index: int) -> Any:
    """
    Return the element at the specified index.

    Args:
        data (list[Any]): Input list.
        index (int): Index of the element to retrieve.

    Returns:
        Any: Element at the specified index.
    """
    return data[index]


if __name__ == "__main__":
    input_data = [2, 4, 6, 8, 10]
    print(f"Input data: {input_data}")

    try:
        index_number = int(input("Enter index of list elements: "))
        result = find_element_of_list(data=input_data, index=index_number)
    except IndexError:
        print("List index out of range.")
    except ValueError:
        print("Invalid input. Please enter an index number.")
    except KeyboardInterrupt:
        print("\nProgram interrupted.")
    else:
        print(f"Element at index: {result}")
    finally:
        print("Program execution finished.")
