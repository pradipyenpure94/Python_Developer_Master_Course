"""Calculator using operators."""

# As per the business requirement, defined arithmetic operators.
VALID_OPERATORS = {
    "+",
    "-",
    "/",
    "//",
    "*",
    "**",
    "%"
}


def validate_operator(operator_symbol: str) -> None:
    """
    Validate the operators.

    Args:
        operator_symbol (str): Input operator symbol.

    Raises:
        ValueError: If not valid operator.
    """
    if not operator_symbol:
        raise ValueError("Please enter the operator symbol.")
    if operator_symbol not in VALID_OPERATORS:
        raise ValueError(
            "Invalid operators. Please enter the valid operators.")


def perform_operation(
    first_number: float,
    second_number: float,
    operator_symbol: str
) -> float | int:
    """
    Perform the arithmetic operations.

    Args:
        first_number (float): First input number.
        second_number (float): Second input number.
        operator_symbol (str): Arithmetic operator.

    Returns:
        float | int: Result of the Arithmetic operation.

    Raises:
        ValueError: If division or modulus by zero is attempted.
    """
    match operator_symbol:
        case "+":
            return first_number + second_number
        case "-":
            return first_number - second_number
        case "*":
            return first_number * second_number
        case "/":
            if second_number == 0:
                raise ValueError("Cannot divide by zero.")
            return first_number / second_number
        case "//":
            if second_number == 0:
                raise ValueError("Cannot divide by zero.")
            return first_number // second_number
        case "%":
            if second_number == 0:
                raise ValueError("Cannot divide by zero.")
            return first_number % second_number
        case "**":
            return first_number ** second_number


def print_result(
    first_number: float,
    second_number: float,
    operator_symbol: str,
    result: float | int
) -> None:
    """
    Print calculator report.

    Args:
        first_number (float): First input number.
        second_number (float): Second input number.
        operator_symbol (str): Operator input.
        result (float | int): Result of the arithmetic operation.
    """
    print("\nCalculator:")
    print("-" * 30)
    print(f"First Number   : {first_number}")
    print(f"Operator       : {operator_symbol}")
    print(f"Second Number  : {second_number}")
    print("-" * 30)
    print(f"Result         : {result}")
    print("-" * 30)


def main() -> None:
    """Run the Operator Calculator Application."""
    try:
        # Accept input from user and its validations
        first_number = float(input("Enter the first number: "))
        operator = input("Enter the operator: ").strip()
        validate_operator(operator_symbol=operator)
        second_number = float(input("Enter the second number: "))

        result = perform_operation(
            first_number=first_number,
            second_number=second_number,
            operator_symbol=operator
        )

    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nProgram interrupted.")
    else:
        # Display result of arithmetic operations.
        print_result(
            first_number=first_number,
            second_number=second_number,
            operator_symbol=operator,
            result=result
        )
    finally:
        print("Operation completed.")


if __name__ == "__main__":
    main()
