"""Explorer module using dir."""

import math

members = dir(math)

for member in members:
    print(member)
