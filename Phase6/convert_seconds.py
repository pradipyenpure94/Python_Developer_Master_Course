"""Convert number of seconds into number of hours, minutes and seconds."""

try:
    seconds = int(input("Enter the seconds (in int): "))
    if seconds < 0:
        raise ValueError("Seconds cannot be negative.")

    hours = seconds // 3600
    remaining_seconds = seconds % 3600
    minutes = remaining_seconds // 60
    secs = remaining_seconds % 60
except ValueError as error:
    print(f"Error: {error}")
else:
    print(f"Time: {hours:02d}:{minutes:02d}:{secs:02d}")
