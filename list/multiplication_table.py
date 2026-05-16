"""Create multiplication table using list comprehension."""

number = 5

multiplication_table = [i * number for i in range(1, 11)]
print(f"Multiplication table of {number} is : {multiplication_table}")
