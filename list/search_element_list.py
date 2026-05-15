"""Search element in list."""

numbers = [10, 20, 30, 40]

try:
    search_num = int(input("Enter a number to search? "))

    if search_num in numbers:
        print(f"Number found in list at index {numbers.index(search_num)}.")
    else:
        print("Number not found in list.")

except ValueError:
    print("Invalid input! Please enter an integer.")
