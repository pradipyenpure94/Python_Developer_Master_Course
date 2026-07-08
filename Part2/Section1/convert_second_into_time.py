"""Convert second into HH:MM:SS."""

# Minimum and maximum seconds limit defined as per the requirement.
MIN_SECONDS_LIMIT = 0
# Maximum seconds representing 23:59:59 (one day).
MAX_SECONDS_LIMIT = 86399

SECONDS_PER_MINUTE = 60
SECONDS_PER_HOUR = 3600


def validate_seconds(seconds: int, minimum: int, maximum: int) -> None:
    """
    Validate the input seconds.

    Args:
        seconds (int): Input seconds.
        minimum (int): Minimum allowed value.
        maximum (int): Maximum allowed value.

    Raises:
        ValueError: If the input is outside the valid range.
    """
    if not minimum <= seconds <= maximum:
        raise ValueError(f"Seconds must be between {minimum} and {maximum}.")


def convert_seconds(seconds: int) -> tuple[int, int, int]:
    """
    Convert input seconds into hours, minutes, and seconds.

    Args:
        seconds (int): Input seconds.

    Returns:
        tuple[int, int, int]: The hours, minutes, and seconds.
    """
    # Convert seconds into hours
    hour = seconds // SECONDS_PER_HOUR
    remaining_seconds = seconds % SECONDS_PER_HOUR
    # Convert seconds into minutes
    minute = remaining_seconds // SECONDS_PER_MINUTE
    # Find remaining seconds
    second = remaining_seconds % SECONDS_PER_MINUTE
    return hour, minute, second


def main() -> None:
    """Run the seconds to HH:MM:SS converter application."""
    try:
        # Accept input from user and its validation
        seconds = int(input("Enter the seconds: "))
        validate_seconds(
            seconds=seconds,
            minimum=MIN_SECONDS_LIMIT,
            maximum=MAX_SECONDS_LIMIT
        )
    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nProgram interrupted.")
    else:
        # To get the hour, minute and second from user input seconds.
        hour, minute, second = convert_seconds(seconds=seconds)
        print(f"Result: {hour:02}:{minute:02}:{second:02}")
    finally:
        print("Operation completed.")


if __name__ == "__main__":
    main()
