"""Identity operators"""

x = [1, 2, 3]
y = [1, 2, 3]

# is operators check memory location of object,
# if memory address is same then return True, Otherwise False
print(id(x))
print(id(y))

print(x is y)
print(x is not y)

# == operators check content/value of objects,
# if value/content will be same then return True, Otherwise False
print(x == y)
print(x != y)
