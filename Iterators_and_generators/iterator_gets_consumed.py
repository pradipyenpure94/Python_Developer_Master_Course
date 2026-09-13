"""Iterator gets consumed."""

numbers = [10, 20, 30]

iterators = iter(numbers)

print(next(iterators))
print(next(iterators))

for number in iterators:
    print("For loop")
    print(number)
