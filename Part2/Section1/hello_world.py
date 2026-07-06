"""Print Hello World."""

name = input("Enter a name: ").strip()
print(f"Hello {name or 'World'}..!")
