"""Check two lists have common element"""

list1 = [2, 4, 6, 8, 10]
list2 = [8, 6, 4, 2]

has_common = False
list2_set = set(list2)
index = 0

while index < len(list1):
    if list1[index] in list2_set:
        has_common = True
        break

    index += 1

print(f"Has common element? {has_common}")
