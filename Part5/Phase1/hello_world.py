"""Print hello world."""

try:
    name = input("Enter the name: ").strip()

    name = " ".join(name.split())
    if not name:
        print("Name cannot be empty.")

    elif name.replace(" ", "").isalpha():
        print(f"Hello {name}!")
    else:
        print("Please enter only characters and spaces.")

except KeyboardInterrupt:
    print("\nOperation cancelled by the user.")
