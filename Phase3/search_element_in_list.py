"""Search element in list."""


def search_element_in_list(nums: list[int], search_element: int) -> str:
    """
    Check whether an element exists in the list.

    Args:
        nums (list[int]): Input numbers list.
        search_element (int): Element to search for.

    Returns:
        str: Message indicating whether the element was found and its index.
    """
    for index, number in enumerate(nums):
        if number == search_element:
            return f"{search_element} found at {index}"
    return f"{search_element} not found in list."


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    search_element = 51
    result = search_element_in_list(nums=numbers,
                                    search_element=search_element)
    print(result)
