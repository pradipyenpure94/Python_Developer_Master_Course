"""
Time Duration

Create a TimeDuration class containing:

    hours
    minutes
    seconds

Implement methods to:

    display duration
    convert everything to seconds
    normalize values

    For example:

        90 seconds → 1 minute 30 seconds

        Concepts: Class design, methods, validation.
"""


class TimeDuration:
    """Represent a time duration."""

    def __init__(self, hours: int, minutes: int, seconds: int) -> None:
        if not all(isinstance(value, int) for value in (
            hours, minutes, seconds)
        ):
            raise TypeError("Hours, minutes, and seconds must be integers.")

        if hours < 0 or minutes < 0 or seconds < 0:
            raise ValueError("Hours, minutes, and seconds cannot be negative.")

        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def display_duration(self) -> str:
        """Return the time duration as a formatted string."""
        return (
            f"{self.hours}h, {self.minutes}m, "
            f"{self.seconds}s"
        )

    def to_seconds(self) -> int:
        """Return the total duration in seconds."""
        return (
            self.hours * 3600
            + self.minutes * 60
            + self.seconds
        )

    def normalize(self) -> str:
        """Normalize the time duration."""
        total_seconds = self.to_seconds()
        hours = total_seconds // 3600
        remaining_seconds = total_seconds % 3600
        minutes = remaining_seconds // 60
        seconds = remaining_seconds % 60
        return f"{hours}h, {minutes}m, {seconds}s"


def main() -> None:
    """Run the main program."""
    time_duration = TimeDuration(hours=2, minutes=150, seconds=45)
    print(f"Display Duration         : {time_duration.display_duration()}")
    print(f"Convert to seconds       : {time_duration.to_seconds()} seconds")
    print(f"Normalize time duration  : {time_duration.normalize()}")


if __name__ == "__main__":
    main()
