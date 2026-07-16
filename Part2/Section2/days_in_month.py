"""Days in month."""


from calendar import isleap

MIN_MONTH_LIMIT = 1
MAX_MONTH_LIMIT = 12

MIN_YEAR_LIMIT = 1
MAX_YEAR_LIMIT = 9999

DAYS_IN_MONTH = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)


def is_leap_year(year: int) -> bool:
    """Check whether a year is leap or not."""
    return isleap(year=year)


def get_days_in_month(year: int, month: int) -> int:
    """Return the number of days in the specified month."""
    if month == 2 and is_leap_year(year=year):
        return 29
    return DAYS_IN_MONTH[month - 1]


def validate_range(
    value: int,
    minimum_limit: int,
    maximum_limit: int,
    field_name: str
) -> None:
    """Validate that the field is within the supported range."""
    if not minimum_limit <= value <= maximum_limit:
        raise ValueError(
            f"The {field_name} input range should be between "
            f"{minimum_limit} and {maximum_limit}."
        )


def main() -> None:
    """Run the Program."""
    try:
        year = int(input("Enter the year (eg. 2026): "))
        validate_range(
            value=year,
            minimum_limit=MIN_YEAR_LIMIT,
            maximum_limit=MAX_YEAR_LIMIT,
            field_name="year"
        )
        month = int(input("Enter the month (eg. 1,2,3..12): "))

        validate_range(
            value=month,
            minimum_limit=MIN_MONTH_LIMIT,
            maximum_limit=MAX_MONTH_LIMIT,
            field_name="month"
        )

    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
    else:
        days = get_days_in_month(year=year, month=month)
        print(f"Total days: {days}")
    finally:
        print("Operation finished.")


if __name__ == "__main__":
    main()
