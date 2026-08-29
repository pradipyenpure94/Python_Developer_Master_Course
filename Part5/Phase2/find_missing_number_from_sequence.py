"""Find missing number from a sequence."""


numbers = [1, 2, 3, 5]
n = len(numbers) + 1
expected_sum = n * (n + 1) // 2
actual_sum = sum(numbers)
missing_number = expected_sum - actual_sum
print(f"Missing number: {missing_number}")
