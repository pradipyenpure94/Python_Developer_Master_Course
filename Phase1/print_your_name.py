"""Display greeting message / Print your name"""

def display_greeting() -> None:
    """Display custom greeting message"""
    name = input("Enter your name: ").strip()
    if not name:
        print("Name cannot be empty!")
        return
    print(f"Hello {name}!")

if __name__ == "__main__":
    display_greeting()
