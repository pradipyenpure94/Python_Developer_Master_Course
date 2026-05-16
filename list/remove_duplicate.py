"""Remove duplicate elements from list without set()"""

fruits = ["apple", "mango", "mango", "banana", "apple", "orange", "kiwi"]

unique_fruits = []

for fruit in fruits:
    if fruit not in unique_fruits:
        unique_fruits.append(fruit)

print(f"Unique fruits: {unique_fruits}")
