"""Return the number of non-overlapping occurrence
of substring sub in the range[start, end]
"""

def sub_string_count(text: str, sub_str: str, start: int = 0, end: int | None = None) -> int:
    """Return the number of non-overlapping substring occurrences of substring
    Args:
        text (str): input text
        sub_str (str): substring of input text
        start (int): start index of input text
        end (int | None): end index of input text
    Returns:
        int: substring occurrences count
    """
    return text.count(sub_str, start, end)

if __name__ == "__main__":
    try:
        input_text = input("Enter a text: ").strip()
        input_sub_str = input("Enter substring: ").strip()
        if not input_sub_str:
            raise ValueError("Substring cannot be empty!")
        input_start = input("Enter start index: ").strip()
        input_end = input("Enter end index: ").strip()

        start_index = int(input_start) if input_start else 0
        if start_index < 0:
            raise ValueError("Start index can not be negative.")

        end_index = int(input_end) if input_end else None
        if end_index is not None and start_index > end_index:
            raise ValueError("Start index cannot be greater than input end")

        result = sub_string_count(text=input_text,
                                    sub_str=input_sub_str,
                                    start=start_index,
                                    end=end_index)
        print(f"Result: {result}")
    except ValueError as error:
        print(f"Error: {error}")
