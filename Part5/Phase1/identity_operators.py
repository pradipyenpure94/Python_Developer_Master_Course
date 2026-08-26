"""Demonstrate the identity operators."""

car1 = ["Innova", "Maruti"]
car2 = car1
car3 = ["Innova", "Maruti"]
car4 = ["Innova"]

print(f"IS Operator     : {car1 is car2}")
print(f"IS NOT Operator : {car1 is not car3}")
print(f"IS Operator     : {car3 is car4}")
print(f"IS NOT Operator : {car3 is not car4}")
