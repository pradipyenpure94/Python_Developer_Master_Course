"""Explorer module using dir."""

import calculator

members = dir(calculator)

for member in members:
    print(member)
