"""Determine employee bonus eligibility using multiple conditions."""

MAX_SERVICE_YEARS = 50
MIN_SERVICE_YEARS = 0


def is_eligible_to_bonus(years: int, performance_rating: int) -> bool:
    return (
        years >= 3 and performance_rating >= 4
        ) or (
            years >= 5 and performance_rating >= 3
        )


if __name__ == "__main__":
    try:
        years = int(input("Enter the years: "))
        if not (years >= 0 and years <= MAX_SERVICE_YEARS):
            raise ValueError(
                f"Employee service years must be between {MIN_SERVICE_YEARS}"
                f" and {MAX_SERVICE_YEARS}."
            )

        performance_rating = int(input("Enter the performance rating: "))
        if not 0 <= performance_rating <= 5:
            raise ValueError("Performance rating must be between 0 and 5.")
    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("Operation cancelled by the user.")
    else:
        if is_eligible_to_bonus(
            years=years,
            performance_rating=performance_rating
        ):
            print("Eligible for a bonus.")
        else:
            print("Not eligible for a bonus.")
