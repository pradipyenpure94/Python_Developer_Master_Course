"""
Password Validation.
Raise an exception if password length is less than 8.
"""

from getpass import getpass

try:
    password = getpass("Enter password (at least 8 characters): ")
    if len(password) < 8:
        raise ValueError("Password length must be at least 8 characters.")

except ValueError as error:
    print(f"Error: {error}")
except KeyboardInterrupt:
    print("\nProgram interrupted.")
else:
    print("Password accepted.")
finally:
    print("Operation completed.")
