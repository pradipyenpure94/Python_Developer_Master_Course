"""Before and After Function Execution."""


def execute_logger(func):
    """Simple execute logger."""
    def wrapper():
        """Simple wrapper."""
        print("Before execution.")
        func()
        print("After execution.")
    return wrapper


@execute_logger
def display():
    """print message."""
    print("Executing display message.")


display()
