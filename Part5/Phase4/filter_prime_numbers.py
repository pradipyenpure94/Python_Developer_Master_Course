"""Use filter() to find prime numbers."""

from check_prime import is_prime

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filter_prime_numbers = list(filter(is_prime, numbers))
print(f"Filtered prime numbers: {filter_prime_numbers}")
