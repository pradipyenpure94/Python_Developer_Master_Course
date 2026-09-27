"""Decorator supporting *args, **kwargs."""


def logger(func):
    """Supporting arguments."""
    def wrapper(*args, **kwargs):
        print(f"Function Arguments: {args}")
        print(f"Keyword Arguments: {kwargs}")
        result = func(*args, **kwargs)
        print(f"Result: {result}")
        return result
    return wrapper


@logger
def student_information(name: str, age: int, city="Pune"):
    """Return the student information."""
    return f"\n Name : {name} \n Age  : {age} \n City : {city}"


if __name__ == "__main__":
    student_information(name="Pradip", age=34)
