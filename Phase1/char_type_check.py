"""Check whether a character type is a digit, alphabet or special character."""


char = input("Enter a character: ").strip()

if len(char) != 1:
    print("Please enter a single character.")
else:
    match char:
        case val if val.isalpha():
            print("It is an alphabet.")
        case val if val.isdigit():
            print("It is a digit.")
        case _:
            print("It is a special character.")
