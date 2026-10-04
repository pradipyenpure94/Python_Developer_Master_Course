"""Extract date and time components."""

from datetime import datetime

now = datetime.now()
print(f"Current date and time: {now}")

print("Current date:")
print(f"Year  : {now.year}")
print(f"Month : {now.month}")
print(f"Day   : {now.day}")
print("Current time:")
print(f"Hour   : {now.hour}")
print(f"Minute : {now.minute}")
print(f"Second : {now.second}")
