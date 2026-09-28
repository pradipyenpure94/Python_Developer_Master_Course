"""Validate age."""


def validate_age(func):
    """Create decorator of validate age."""
    def wrapper(age: int):
        if age < 18:
            raise ValueError("User must be 18 or old.")
        return func(age)
    return wrapper


@validate_age
def user_resgistration(age: int):
    print("Registration successful.")


if __name__ == "__main__":
    print(user_resgistration(age=18))
