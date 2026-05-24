"""Check two lists have common element"""

list1 = [2, 4, 6, 8, 10]
list2 = [8, 6, 4, 2]

has_common = not set(list1).isdisjoint(list2)
print(f"Has common element? {has_common}")
