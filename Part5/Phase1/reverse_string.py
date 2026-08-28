"""Reverse a string."""


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
    reversed_text = "".join(
        text[index] for index in range(text_size - 1, -1, -1)
    )
    print(f"Reversed string: {reversed_text}")
