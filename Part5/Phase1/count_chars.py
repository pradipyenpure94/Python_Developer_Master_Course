"""Count characters in a string."""


try:
    text = input("Enter the string: ").strip()
    if not text:
        raise ValueError("String cannot be empty.")

except ValueError as error:
    print(f"Error: {error}")
except KeyboardInterrupt:
    print("\nOperation cancelled by the user.")
else:
    input_text = "".join(char for char in text if not char.isspace())
    print(f"Count characters in a string: {len(input_text)}")
