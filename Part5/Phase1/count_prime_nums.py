"""Count prime numbers between two numbers."""


count_prime_nums = 0

try:
    start_number_limit = int(input("Enter the start number limit: "))
    if start_number_limit < 2:
        raise ValueError(
            "Start number always start from 2 or greater than 2."
        )
    end_number_limit = int(input("Eneter the end number limit: "))
    if end_number_limit < start_number_limit:
        raise ValueError(
            "End number limit always greater than start number "
        )

except ValueError as error:
    print(f"Error: {error}")
except KeyboardInterrupt:
    print("\nOperation cancelled by the user.")
else:
    for number in range(start_number_limit, end_number_limit + 1):
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                break
        else:
            count_prime_nums += 1
    print(
        f"Total count of prime numbers from {start_number_limit} to "
        f"{end_number_limit}: {count_prime_nums}"
    )
