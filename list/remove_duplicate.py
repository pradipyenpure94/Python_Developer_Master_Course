"""Remove duplicate elements from list without set()"""

fruits = ["apple", "mango", "mango", "banana", "apple", "orange", "kiwi"]

unique_fruits = []
length = len(fruits)
index = 0

while index < length:
    current_fruit = fruits[index]
    if current_fruit not in unique_fruits:
        unique_fruits.append(current_fruit)
    index += 1

print(f"Unique fruits: {unique_fruits}")
