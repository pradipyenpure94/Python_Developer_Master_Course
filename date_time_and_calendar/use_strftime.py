"""Format date using strftime()."""

from datetime import datetime

now = datetime.now()

# Different date formats
print(now.strftime("%d-%m-%Y"))
print(now.strftime("%d-%m-%y"))
print(now.strftime("%A, %d %B %Y"))
print(now.strftime("%a, %d %b %y"))
