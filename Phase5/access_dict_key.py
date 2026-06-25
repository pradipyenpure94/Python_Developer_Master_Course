"""
Access dictionary key.
Handle KeyError.
"""

from typing import Any


def access_dictionary_key(data: dict[Any, Any], key: Any) -> Any:
    """
    Return the value associated with the specified key.

    Args:
        data (dict[Any, Any]): Input data dictionary.
        key (Any): Key to retrieve from the dictionary.

    Returns:
        Any: Value associated with the specified key.
    """
    return data[key]


if __name__ == "__main__":
    input_data = {"name": "Pradip", "age": 32}
    print(f"Data: {input_data}")

    try:
        dict_key = input("Enter a key of dictionary: ")
        result = access_dictionary_key(data=input_data, key=dict_key)

    except KeyError:
        print("Key not found in dictionary.")

    except KeyboardInterrupt:
        print("\nProgram interrupted.")
    else:
        print(f"Result: {result}")
    finally:
        print("Operation completed.")
