"""Convert temperature celsius to fahrenheit"""

try:
    celsius = float(input("Enter a celsius: "))
    farenheit = celsius * 9/5 + 32
    print(f"Conversion of Celsius to Farenehit: {farenheit:.2f}")
except ValueError:
    print("Invalid input! Please enter a number.")
