"""Find min and max in tuple."""

t = (1, 2, 3, 4, 5)

if t:
    min_value = t[0]
    max_value = t[0]
    index = 0
    length = len(t)

    while index < length:
        current_number = t[index]

        if current_number < min_value:
            min_value = current_number
        if current_number > max_value:
            max_value = current_number

        index += 1

    print(f"Minimum value: {min_value}")
    print(f"Maximum value: {max_value}")
else:
    print("Tuple is empty!")
