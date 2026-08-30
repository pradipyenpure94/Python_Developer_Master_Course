"""Find the largest sublist sum."""

numbers = [[1, 2, 3], [4, 3, 25], [2, 3, 15]]

max_sub_list = max(numbers, key=sum)
print(max_sub_list)
