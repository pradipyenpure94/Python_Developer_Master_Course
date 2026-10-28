"""Generate the Fibonacci sequence up to N terms."""


number = 10

first_term, second_term = 0, 1

for _ in range(number):
    print(first_term)
    first_term, second_term = second_term, first_term + second_term
