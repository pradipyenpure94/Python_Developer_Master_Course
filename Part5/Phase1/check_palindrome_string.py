"""Check whether a string is palindrome."""


try:
    text = input("Enter the string: ").strip()
    if not text:
        raise ValueError("String cannot be empty.")

except ValueError as error:
    print(f"Error: {error}")
except KeyboardInterrupt:
    print("\nOperation cancelled by the user.")
else:
    text_size = len(text)
    clean_text = text.casefold()
    reversed_text = "".join(
        clean_text[index] for index in range(text_size - 1, -1, -1)
    )
    if clean_text == reversed_text:
        print(f"{text} is a palindrome.")
    else:
        print(f"{text} is not a palindrome.")
