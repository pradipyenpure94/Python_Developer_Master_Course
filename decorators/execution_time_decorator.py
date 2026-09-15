"""Execution Time Decorator."""

import time


def execution_time(func):
    """A simple execution time decorator."""
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Execution time: {(end - start):.2f} seconds.")
        return result
    return wrapper


@execution_time
def calculate_sum():
    """Return the calculate sum."""
    return sum(range(1, 100000001))


print(calculate_sum())
