"""Find pairs with given sum."""

numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
target = 10

pairs = [(number, target - number) for number in numbers
         if target - number in numbers and number < (target - number)]

print(f"Sum pairs: {pairs}")
