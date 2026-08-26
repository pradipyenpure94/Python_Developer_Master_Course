"""Check whether a person is eligible to vote."""

MIN_VOTE_AGE_LIMIT = 18
MAX_VOTE_AGE_LIMIT = 100


try:
    age = int(input("Enter the person age: "))
except ValueError as error:
    print(f"Error: {error}")
except KeyboardInterrupt:
    print("\nOperation cancelled by the user.")
else:
    if not MIN_VOTE_AGE_LIMIT <= age <= MAX_VOTE_AGE_LIMIT:
        print("You are not eligible to vote.")
    else:
        print("You are eligible to vote.")
