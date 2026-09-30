"""Decorator factory."""


def prefix_message(prefix: str):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return prefix + result
        return wrapper
    return decorator


@prefix_message("INFO: ")
def message():
    return "Python program executed."


if __name__ == "__main__":
    print(message())
