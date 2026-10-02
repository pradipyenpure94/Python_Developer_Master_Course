"""Import and reuse the functions."""

from utilities.arithmetic import add, sub
from utilities.string_operations import reverse_string
from utilities.validators import is_positive, is_negative


# Arithmetic Operations:
print(f"Addition    : {add(first_number=10.5, second_number=8.5)}")
print(f"Subtraction : {sub(first_number=10.5, second_number=4.5)}")

# String Operations:
print(f"Reversed String: {reverse_string(text="Pradip")}")

# Validation functions:

print(f"Is Positive? {is_positive(number=10)}")
print(f"Is Negative? {is_negative(number=5)}")
