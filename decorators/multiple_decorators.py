"""Multiple decorators."""


def decorator1(func):
    def wrapper(name: str):
        print("Before decorator1:")
        result = func(name)
        print("After decorator1:")
        return result
    return wrapper


def decorator2(func):
    def wrapper(name: str):
        print("Before decorator2:")
        result = func(name)
        print("After decorator2:")
        return result
    return wrapper


@decorator1
@decorator2
def greeting_message(name: str):
    print(f"Hello {name}")


if __name__ == "__main__":
    greeting_message(name="Pradip")
