"""Build a menu-driven calculator using match-case or if-elif-else."""

status_code = 404

match status_code:
    case 200:
        print("Success")
    case 400:
        print("Bad Request")
    case 404:
        print("Page Not Found.")
    case _:
        print("Unknown status code.")
