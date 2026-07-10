"""Income tax calculator management system."""

from pathlib import Path
import  re


FILE_PATH = "Part2/Section2/income_tax_calculator_sheet.txt"
FILE_NAME = Path(FILE_PATH).name
PAN_PATTERN = r"[A-Z]{5}[0-9]{4}[A-Z]$"
HEADERS = "tax_payer_id, full_name, age, pan_number, mobile, email, " \
    "annual_income, deductions, tax_rate (%), tax_amount"


MIN_AGE_LIMIT = 18
MAX_AGE_LIMIT = 120
MIN_ANNUAL_INCOME = 0
MAX_ANNUAL_INCOME = 1000000000  # 10 Crore
MIN_DEDUCTIONS = 0

# Income Slabs
SLAB_1_LIMT = 300000
SLAB_2_LIMT = 700000
SLAB_3_LIMT = 1000000
SLAB_4_LIMT = 1500000

# Tax rates
SLAB_1_TAX_RATE = 0
SLAB_2_TAX_RATE = 5
SLAB_3_TAX_RATE = 10
SLAB_4_TAX_RATE = 20
SLAB_5_TAX_RATE = 30


def create_txt_file() -> None:
    """Create a File if not exist."""
    if not Path(FILE_PATH).exists():
        with open(file=FILE_PATH, mode="w", encoding="utf-8") as file_obj:
            file_obj.write(HEADERS)
        print(f"{FILE_NAME} is created successfully.")


def load_data() -> list[str]:
    """Fecth all data from .txt File."""
    with open(file=FILE_PATH, mode="r", encoding="utf-8") as file_obj:
        file_obj.readline()
        return file_obj.readlines()


def save_data(tax_payers) -> None:
    """Save store data into .txt File."""
    with open(file=FILE_PATH, mode="w", encoding="utf-8") as file_obj:
        file_obj.write("".join(HEADERS) + "\n")
        file_obj.writelines(tax_payers)


# Validations
def validate_name(name: str) -> None:
    """
    Validate the name.

    Args:
        name (str): Input name.

    Raises:
        ValueError: Name cannot be empty or
        name must contain letters or spaces.
    """
    if not name:
        raise ValueError("Name cannot be empty.")

    if not all(char.isalpha() or char.isspace() for char in name):
        raise ValueError("Name not contain excluding letters or spaces.")


def validate_age(age: int) -> None:
    """
    Validate the age.

    Args:
        age (int): Input age of Tax payer.

    Raises:
        ValueError: if not the age inside range limit.
    """
    if not MIN_AGE_LIMIT <= age <= MAX_AGE_LIMIT:
        raise ValueError(
            "Tax Payer age must be between "
            f"{MIN_AGE_LIMIT} and {MAX_AGE_LIMIT}"
        )


def validate_pan_number(pan_number: str) -> None:
    """
    Validate the PAN number.

    Args:
        pan_number (str): Input PAN number of Tax payer.

    Raises:
        ValueError: if not PAN number or not exactly 10 characters
        or not a valid foramt or already exist.
    """
    if not pan_number:
        raise ValueError("PAN number must be required.")
    if len(pan_number) != 10:
        raise ValueError("PAN number exactly 10 characters.")
    if not re.fullmatch(pattern=PAN_PATTERN, string=pan_number):
        raise ValueError("Invalid PAN number format. (ABCDE-1234-F).")
    if pan_number in get_all_pan_numbers():
        raise ValueError(
            "PAN number already exist. Please enter another PAN number."
        )


def validate_mobile_number(mobile_number: str) -> None:
    """
    Validate the mobile number.

    Args:
        mobile_number (str): Input mobile number of Taxpayer.

    Raises:
        ValueError: If not mobile number length 10 digits or
        not all number in digit.
    """
    if len(mobile_number) != 10:
        raise ValueError("Mobile number length should be 10 digit.")
    if not mobile_number.isdigit():
        raise ValueError("Mobile number input should be in digit.")


def validate_email(email: str) -> None:
    """
    Validate the email.

    Args:
        email (str): Input email of Tax payer.
    """
    if not email:
        raise ValueError("Email address is required.")
    if len(email) > 254:
        raise ValueError("Email address cannot exceed 254 characters.")
    if email.count("@") != 1:
        raise ValueError("Email address contain at least one '@' symbol.")
    user_name, domain = email.split("@")
    if not user_name:
        raise ValueError("Email username cannot be empty.")
    if not domain:
        raise ValueError("Email domain cannot be empty.")
    if "." not in domain:
        raise ValueError("Email domain must contain '.'.")
    if domain.startswith(".") or domain.endswith("."):
        raise ValueError("Invalid email domain.")
    if " " in email:
        raise ValueError("Email address cannot contain spaces.")


def validate_annual_income(annual_income: float) -> None:
    """
    Validate the annual income.

    Args:
        annual_income (float): Input of annual income.

    Raises:
        ValueError: If not annual income inside range limit.
    """
    if not MIN_ANNUAL_INCOME <= annual_income <= MAX_ANNUAL_INCOME:
        raise ValueError(
            f"Annual income must be between {MIN_ANNUAL_INCOME} "
            f"and {MAX_ANNUAL_INCOME}"
        )


def validate_total_deductions(
    total_deductions: float,
    annual_income: float
) -> None:
    """
    Validate the total deductions.

    Args:
        total_deductions (float): Input of Total deductions.
        annual_income (float): Input of annual income.
    """
    if total_deductions < MIN_DEDUCTIONS:
        raise ValueError(
            f"Total deductions cannot be less than {MIN_DEDUCTIONS}."
        )
    if total_deductions > annual_income:
        raise ValueError(
            f"Total deductions cannot excced than {annual_income}."
        )


# Get the all input value
def get_name(prompt: str) -> str | None:
    """To get the name input from user."""
    while True:
        try:
            name = input(prompt).strip()
            validate_name(name=name)
        except ValueError as error:
            print(f"Error: {error}")
        else:
            return name


def get_age(prompt: str) -> int | None:
    """To get the age from user."""
    while True:
        try:
            age = int(input(prompt))
            validate_age(age=age)
        except ValueError as error:
            print(f"Error: {error}")
        else:
            return age


def get_pan_number(prompt: str) -> str | None:
    """To get the PAN number from user."""
    while True:
        try:
            pan_number = input(prompt).strip()
            validate_pan_number(pan_number=pan_number)
        except ValueError as error:
            print(f"Error: {error}")
        else:
            return pan_number


def get_mobile_number(prompt: str) -> str | None:
    """To get the mobile number from user."""
    while True:
        try:
            mobile_number = input(prompt)
            validate_mobile_number(mobile_number=mobile_number)
        except ValueError as error:
            print(f"Error: {error}")
        else:
            return mobile_number


def get_email(prompt: str) -> None:
    """To get the email from user."""
    while True:
        try:
            email = input(prompt).strip()
            validate_email(email=email)
        except ValueError as error:
            print(f"Error: {error}")
        else:
            return email


def get_annual_income(prompt: str) -> float | None:
    """To get the annual income of Tax payer."""
    while True:
        try:
            annual_income = float(input(prompt))
            validate_annual_income(annual_income=annual_income)
        except ValueError as error:
            print(f"Error: {error}")
        else:
            return annual_income


def get_total_deductions(prompt: str, annual_income: float) -> float | None:
    """To get the total income from user."""
    while True:
        try:
            total_deductions = float(input(prompt))
            validate_total_deductions(
                total_deductions=total_deductions,
                annual_income=annual_income
            )
        except ValueError as error:
            print(f"Error: {error}")
        else:
            return total_deductions


def get_all_pan_numbers() -> set[str]:
    """To get the all the PAN numbers from .txt File."""
    tax_payers = load_data()
    return {record.split(",")[3] for record in tax_payers
            if record.split(",")[3]}


def calculate_taxable_income(
    annual_income: float,
    total_deductions: float
) -> float:
    """
    Calculate and return a taxable income amount.

    Args:
        annual_income (float): Input of annual income.
        total_deductions (float): Input of total deductions.

    Returns:
        float: Return a taxable income.
    """
    return annual_income - total_deductions


def calculate_tax_amount(taxable_income: float, tax_rate: float) -> float:
    """
    Calculate and return a tax amount.

    Args:
        taxable_income (float): Input of taxable income.
        tax_rate (float): Input of tax rate (%).

    Returns:
        float: Return a tax amount.
    """
    return taxable_income * tax_rate


def get_tax_rate(annual_income: float) -> float:
    """
    Return a tax rate based on tax payer annual income.

    Args:
        annual_income (float): Input of annual income.

    Returns:
        float: Return a tax rate (%).
    """
    if annual_income <= SLAB_1_LIMT:
        return SLAB_1_TAX_RATE
    if annual_income <= SLAB_2_LIMT:
        return SLAB_2_TAX_RATE
    if annual_income <= SLAB_3_LIMT:
        return SLAB_3_TAX_RATE
    if annual_income <= SLAB_4_LIMT:
        return SLAB_4_TAX_RATE
    return SLAB_5_TAX_RATE


def auto_gen_next_tax_payer_id(tax_payers) -> int:
    """Auto generate the new tax payer ID."""
    if not tax_payers:
        return 1
    return max(int(record.split(",")[0]) for record in tax_payers) + 1


def buil_new_record(
    tax_payer_id: str,
    full_name: str,
    age: int,
    pan_number: str,
    mobile_number: str,
    email: str,
    annual_income: float,
    total_deductions: float
) -> str:
    """Build and return a new record."""
    # To get the taxable income
    taxable_income = calculate_taxable_income(
        annual_income=annual_income,
        total_deductions=total_deductions
    )
    # To get the tax rate
    tax_rate = get_tax_rate(annual_income=annual_income)
    # To get the tax amount
    tax_amount = calculate_tax_amount(
        taxable_income=taxable_income,
        tax_rate=tax_rate
    )
    return ",".join([
        str(tax_payer_id),
        full_name,
        str(age),
        pan_number,
        mobile_number,
        email,
        str(annual_income),
        str(total_deductions),
        str(tax_rate),
        str(tax_amount),
    ]) + "\n"


def add_tax_payer(tax_payers) -> None:
    """Add a new tax payer record into .txt File."""
    try:
        # Accept inputs from user and its validation.
        tax_payer_id = auto_gen_next_tax_payer_id(tax_payers=tax_payers)
        name = get_name(prompt="Enter the full name: ")
        age = get_age(prompt="Enter the age: ")
        pan_number = get_pan_number(prompt="Enter the PAN number: ")
        mobile_number = get_mobile_number(prompt="Enter the Mobile number: ")
        email = get_email(prompt="Enter the email: ")
        annual_income = get_annual_income(prompt="Enter the Annual Income: ")
        total_deductions = get_total_deductions(
            prompt="Enter the total deductions: ",
            annual_income=annual_income
        )

    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nProgram interrupted.")
    else:
        new_record = buil_new_record(
            tax_payer_id=str(tax_payer_id),
            full_name=name,
            age=str(age),
            pan_number=pan_number,
            mobile_number=mobile_number,
            email=email,
            annual_income=annual_income,
            total_deductions=total_deductions
        )
        tax_payers.append(new_record)
        save_data(tax_payers=tax_payers)
        print("Added a new record successfully.")
    finally:
        print("Operation completed.")


def view_all_tax_payers(tax_payers: list[str]) -> None:
    # print(tax_payers, "+++++++++")
    if not tax_payers:
        print("Tax payers record not found.")
        return
    print("-" * 50)
    

def display_report_menu() -> None:
    """Display sun menu of generate report."""
    while True:
        print("1. Individual Report (PAN)")
        print("2. All Reports")
        print("3. Back to the Main menu")

        choice = input("Enter your choice: ")

        if choice not in {"1", "2", "3"}:
            print("Invalid choice. Please select a valid option (1-3).")
        elif choice == "1":
            pass
        elif choice == "2":
            pass
        elif choice == "3":
            display_main_menu()

        print("-" * 50)


def display_main_menu() -> None:
    """Main menu operations."""
    # Create a File if not exist.
    create_txt_file()
    # Fecth all data from .txt File.
    tax_payers = load_data()

    while True:
        print("Operations Menu: ")
        print("1. Register Taxpayer")
        print("2. View All Taxpayers")
        print("3. Search Taxpayer")
        print("4. Update Taxpayer")
        print("5. Delete Taxpayer")
        print("6. Calculate Tax")
        print("7. Generate Report")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice not in {"1", "2", "3", "4", "5", "6", "7", "8"}:
            print("Invalid choice. Please select a valid option (1-8).")

        elif choice == "1":
            add_tax_payer(tax_payers=tax_payers)

        elif choice == "2":
            view_all_tax_payers(tax_payers=tax_payers)

        elif choice == "3":
            pass

        elif choice == "4":
            pass

        elif choice == "5":
            pass

        elif choice == "6":
            pass

        elif choice == "7":
            display_report_menu()

        elif choice == "8":
            print("Exit from operations.")
            break

        print("-" * 50)


def main():
    """Run the Income Tax Calculator Management System Application."""

    # Main menu
    display_main_menu()


if __name__ == "__main__":
    main()
