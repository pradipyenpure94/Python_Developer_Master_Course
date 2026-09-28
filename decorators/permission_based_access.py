"""Permission-based access."""


def permission_required(permission):
    """Create decorator that permission based access."""
    def decorator(func):
        def wrapper(user_permissions, *args, **kwargs):
            if permission not in user_permissions:
                return "Access denied."
            return func(user_permissions, *args, **kwargs)
        return wrapper
    return decorator


@permission_required("delete")
def user_rights(user_permissions):
    """User based access right"""
    print("Record deleted.")


if __name__ == "__main__":
    print(user_rights(user_permissions=["edit", "create", "delete"]))
