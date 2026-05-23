"""Convert tuple into dictionary."""

numbers = ((1, "1"), (2, "2"))

result = {key: value for key, value in numbers}
print(f"Convert tuple into dictionary: {result}")
