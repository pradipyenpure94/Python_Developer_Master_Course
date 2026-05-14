"""Guessing game"""

import random

highest = 10
secret = random.randint(1, highest)

guess = int(input("Enter a number: "))

if guess == secret:
    print("Correct guess!")
else:
    print("Wrong guess!")
