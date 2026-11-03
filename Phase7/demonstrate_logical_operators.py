"""Demonstrate logical and, or and not."""


first_number = 10
second_number = 7

and_operator_result = first_number > second_number and first_number < second_number
print(f"AND Operator Result: {and_operator_result}")

or_operator_result = first_number >= second_number or second_number == first_number
print(f"OR Operator Result: {or_operator_result}")

not_operator_result = not (first_number <= second_number)
print(f"Not Operator Result: {not_operator_result}")
