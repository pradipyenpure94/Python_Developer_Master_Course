"""Create a dictionary from two lists."""

from typing import TypeVar
K = TypeVar("K")
V = TypeVar("V")


def make_dictionary(list1: list[K], list2: list[V]) -> dict[K, V]:
    """
    Return a new dictionary from both input lists.

    Args:
        list1 (list[K]): First input list.
        list2 (list[V]): Second input list.

    Returns:
        dict[K, V]: A dictionary created by pairing elements from the two input
        lists.

    Raises:
        ValueError: If the input lists have different lengths.
    """
    if len(list1) != len(list2):
        raise ValueError("Both lists must have the same length.")
    return dict(zip(list1, list2))


if __name__ == "__main__":
    fruits = ["Mango", "Orange"]
    print(f"List1: {fruits}")
    weights = [4, 5]
    print(f"List2: {weights}")

    try:
        result = make_dictionary(list1=fruits, list2=weights)
    except ValueError as error:
        print(f"Error: {error}")
    else:
        print(f"After creation dictionary: {result}")
    finally:
        print("Operation completed.")
