"""Guard clause example."""


def login(user_name, password, user) -> str:
    if not user_name:
        return "Username is required."
    if not password:
        return "Password is required."
    if user is None:
        return "User not found."
    if not user["is_active"]:
        return "User is inactive"
    if user["password"] != password:
        return "Invalid credentials."
    return "Login successful."
