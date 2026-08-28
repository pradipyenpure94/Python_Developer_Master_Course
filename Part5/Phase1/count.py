"""Count uppercase, lowercase, digits and special characters."""


try:
    text = input("Enter the string: ").strip()
    if not text:
        raise ValueError("String cannot be empty.")
except ValueError as error:
    print(f"Error: {error}")
except KeyboardInterrupt:
    print("\nOperation cancelled by the user.") 
else:
    uppercase_count = 0
    lowercase_count = 0
    digits_count = 0
    special_chars_count = 0

    for char in text:
        if char.islower():
            lowercase_count += 1
        elif char.isupper():
            uppercase_count += 1
        elif char.isdigit():
            digits_count += 1
        else:
            special_chars_count += 1
    print(f"Uppercase Count          : {uppercase_count}")
    print(f"Lowercase Count          : {lowercase_count}")
    print(f"Digits Count             : {digits_count}")
    print(f"Special Characters Count : {special_chars_count}")
