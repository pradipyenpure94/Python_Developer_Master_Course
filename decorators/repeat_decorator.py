"""Repeat decorator."""


def repeat_decorator(times):
    def decorator(func):
        def wrapper(name: str):
            for _ in range(times):
                func(name)
        return wrapper
    return decorator


@repeat_decorator(3)
def greet(name: str):
    print(f"Hello {name}")


if __name__ == "__main__":
    greet(name="Pradip")
