"""Convert seconds into hours, minutes and seconds."""


def validate_seconds(seconds: int) -> None:
    """Validate the seconds."""
    if seconds < 0:
        raise ValueError("Seconds cannot be negative.")


try:
    seconds = int(input("Enter the seconds: "))
    validate_seconds(seconds=seconds)
except ValueError as error:
    print(f"Error: {error}")
except KeyboardInterrupt:
    print("\nOperation cancelled by the user.")
else:
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    remaining_seconds = seconds % 60
    print(f"{hours}:{minutes}:{remaining_seconds}")
