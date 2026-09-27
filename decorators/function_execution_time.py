"""Measure function execution time."""

import time


def function_execution_time(func):
    """Create a sample function execution time decorator."""
    def wrapper(number: int):
        start = time.perf_counter()
        result = func(number)
        end = time.perf_counter()
        execution_time = end - start
        print(f"Total execution time: {execution_time:.2f}")
        return result
    return wrapper


@function_execution_time
def count_execution_time(number: int) -> int:
    """Count the execution time."""
    count = 0
    for _ in range(number):
        count += 1
    return count


if __name__ == "__main__":
    count_execution_time(1000000)
