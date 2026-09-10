"""Implement polymorphic notification system."""


class NotificationSystem:
    """Represent a notification system."""

    def send(self) -> None:
        print("Sending notification.")


class Email(NotificationSystem):
    """Represent an email notification."""

    def send(self) -> None:
        print("Sending Email.")


class SMS(NotificationSystem):
    """Represent an sms notification."""

    def send(self) -> None:
        print("Sending SMS.")


def main() -> None:
    """Run the main program."""
    notifications = [SMS(), Email(), NotificationSystem()]

    for notification in notifications:
        notification.send()


if __name__ == "__main__":
    main()
