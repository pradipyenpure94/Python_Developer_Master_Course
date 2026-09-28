"""Role based authorization."""


def role_required(required_role):
    """Create decorator of access permission."""
    def decorator(func):
        def wrapper(role, *args, **kwargs):
            if role != required_role:
                return "Access denied"
            return func(role, *args, **kwargs)
        return wrapper
    return decorator


@role_required("admin")
def delete_user(role):
    print("User deleted.")


if __name__ == "__main__":
    result = delete_user(role="admin")
    print(result)
