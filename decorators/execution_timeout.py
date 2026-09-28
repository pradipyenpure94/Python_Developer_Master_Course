"""Decorator for execution timeout concept."""

import time


def execution_limit(seconds):
    """Create decorator that execution time exceeded."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            elapsed = end - start
            if elapsed > seconds:
                print("Warning: Execution time exceeded.")
            return result
        return wrapper
    return decorator


@execution_limit(2)
def calculate():
    time.sleep(1)
    return "Done"


if __name__ == "__main__":
    print(calculate())
