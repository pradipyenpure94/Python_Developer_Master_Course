"""ASCII value of character."""


char = input("Enter a character: ").strip()

if len(char) != 1:
    print("Please enter a single character!")
else:
    print(f"ASCII value of character: {ord(char)}")
