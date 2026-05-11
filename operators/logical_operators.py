"""Logical operators examples"""

x = 10
y = 5

print(x > 5 and y < 6)     # Result: True
print(x < 5 and y < 5)     # Result: False

print(x == 10 or y < 6)    # Result: True
print(x == 1 or y > 6)     # Result: False

print(not x < 15)          # Result: False
print(not x < 5)           # Result: True
