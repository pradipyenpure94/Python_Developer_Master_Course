"""Find the second largest number."""

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if (num1 >= num2 and num1 <= num3) or (num1 <= num2 and num1 >= num3):
    second = num1
elif (num2 >= num1 and num2 <= num3) or (num2 <= num1 and num2 >= num3):
    second = num2
else:
    second = num3
print(f"Second largest number: {second}.")
