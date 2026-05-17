"""Find min and max in tuple."""

t = (1, 2, 3, 4, 5)

if t:
    min_value = t[0]
    max_value = t[0]

    for number in t:
        if number < min_value:
            min_value = number
        if number > max_value:
            max_value = number

    print(f"Minimum value: {min_value}")
    print(f"Maximum value: {max_value}")
else:
    print("Tuple is empty!")
