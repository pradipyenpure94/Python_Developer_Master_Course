"""Validate API request."""


def validate_request(func):
    """Create decorator that create request."""
    def wrapper(request):
        if not request:
            raise ValueError("Invalid request.")
        if "user_id" not in request:
            raise ValueError("User Id is reqired.")
        return func(request)
    return wrapper


@validate_request
def get_user(request):
    """Fetching user info."""
    print(f"Fetching user: {request['user_id']}")


if __name__ == "__main__":
    try:
        get_user({"user_id": 101})
    except ValueError as e:
        print(f"Error: {e}")
