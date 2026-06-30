"""Count frequency of each element using a dictionary."""

from typing import TypeVar
T = TypeVar("T")


def frequency_count(data: list[T]) -> dict[T, int]:
    """
    Return the frequency count of each element using a dictionary.

    Args:
        data (list[T]): Input data list.

    Returns:
        dict[T, int]: Dictionary containing the frequency count.
    """
    freq = {}
    for item in data:
        freq[item] = freq.get(item, 0) + 1
    return freq


if __name__ == "__main__":
    input_data = ["Mango", "Orange", "Mango", "Banana", "Orange"]
    print(f"Data: {input_data}")
    result = frequency_count(data=input_data)
    print(f"Frequency count of each element: {result}")
