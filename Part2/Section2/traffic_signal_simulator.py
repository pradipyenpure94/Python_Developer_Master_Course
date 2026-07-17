"""Traffic signal simulator."""

SIGNAL_COLOR_ACTIONS = {
    "RED": "STOP",
    "GREEN": "GO",
    "YELLOW": "WAIT",
}


def validate_signal_color(signal_color: str) -> None:
    """Validate the signal color input."""
    if signal_color not in SIGNAL_COLOR_ACTIONS:
        raise ValueError("Invalid traffic signal.")


def get_signal_action(signal_color: str) -> str:
    """Return the action associated with the traffic signal."""
    return SIGNAL_COLOR_ACTIONS[signal_color]


def main() -> None:
    """Run the Program."""

    try:
        signal_color = input(
            "Enter the traffic signal color (RED/GREEN/YELLOW): "
        ).strip().upper()
        validate_signal_color(signal_color=signal_color)

    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
    else:
        signal_action = get_signal_action(signal_color=signal_color)
        print(f"Action: {signal_action}")
    finally:
        print("Operation finished.")


if __name__ == "__main__":
    main()
