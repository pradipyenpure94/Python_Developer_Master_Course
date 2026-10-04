"""Print today's weekday."""

from datetime import date

current_date = date.today()
print(f"Today weekday: {current_date.strftime('%A')}")
