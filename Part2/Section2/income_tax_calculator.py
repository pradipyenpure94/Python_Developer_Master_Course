"""Income tax calculator management system."""

from pathlib import Path
import re


FILE_PATH = "Part2/Section2/income_tax_calculator_sheet.txt"
PATH = Path(FILE_PATH)
FILE_NAME = PATH.name
PAN_PATTERN = r"[A-Z]{5}[0-9]{4}[A-Z]$"
HEADERS = ("tax_payer_id, full_name, age, pan_number, mobile, email, "
           "annual_income, deductions, tax_rate (%), tax_amount")

# As per the business requirements, defined the age limits,
# annual income limits, deduction limits, tax slab limits, and tax rate limits.

# Age limits
MIN_AGE_LIMIT = 18
MAX_AGE_LIMIT = 120

# Annual income limits
MIN_ANNUAL_INCOME = 0
MAX_ANNUAL_INCOME = 1000000000  # 10 Crore

# Deduction limit
MIN_DEDUCTIONS = 0

# Income tax slabs limits
SLAB_1_LIMIT = 300000
SLAB_2_LIMIT = 700000
SLAB_3_LIMIT = 1000000
SLAB_4_LIMIT = 1500000

# Tax rates limits
SLAB_1_TAX_RATE = 0
SLAB_2_TAX_RATE = 5
SLAB_3_TAX_RATE = 10
SLAB_4_TAX_RATE = 20
SLAB_5_TAX_RATE = 30


def create_txt_file() -> None:
    """Create the file if it does not exist."""
    if not PATH.exists():
        with open(file=FILE_PATH, mode="w", encoding="utf-8") as file_obj:
            file_obj.write(HEADERS)
        print(f"{FILE_NAME} is created successfully.")


def load_data() -> list[str]:
    """
    Fetch all data from .txt File.

    Returns:
        list[str]: Fetch all data from .txt File.
    """
    with open(file=FILE_PATH, mode="r", encoding="utf-8") as file_obj:
        file_obj.readline()
        return file_obj.readlines()


def save_data(tax_payers: list[str]) -> None:
    """Save data to the .txt File."""
    with open(file=FILE_PATH, mode="w", encoding="utf-8") as file_obj:
        file_obj.write(HEADERS + "\n")
        file_obj.writelines(tax_payers)


# Validations
def validate_name(name: str) -> None:
    """
    Validate the name.

    Args:
        name (str): Input name of Taxpayer.

    Raises:
        ValueError: Name cannot be empty,
                    and it must contain only letters and spaces.
    """
    if not name:
        raise ValueError("Name cannot be empty.")
    if not all(char.isalpha() or char.isspace() for char in name):
        raise ValueError(
            "Name cannot contain numbers or special characters. "
            "Only letters and spaces are allowed"
        )


def validate_age(age: int) -> None:
    """
    Validate the age.

    Args:
        age (int): Input age of Taxpayer.

    Raises:
        ValueError: Age must be within the valid range.
    """
    if not MIN_AGE_LIMIT <= age <= MAX_AGE_LIMIT:
        raise ValueError(
            "Invalid age. Taxpayer age must be between "
            f"{MIN_AGE_LIMIT} and {MAX_AGE_LIMIT} years."
        )


def validate_pan_number(pan_number: str) -> None:
    """
    Validate the PAN number.

    Args:
        pan_number (str): Input PAN number of Taxpayer.

    Raises:
        ValueError: Invalid PAN number. Please ensure it is not empty,
                    is exactly 10 characters long, follows the correct format,
                    and does not already exist.
    """
    if not pan_number:
        raise ValueError("PAN number must be required.")
    if len(pan_number) != 10:
        raise ValueError(
            "Invalid PAN number. "
            "It must be exactly 10 characters long."
        )
    if not re.fullmatch(pattern=PAN_PATTERN, string=pan_number):
        raise ValueError(
            "Invalid PAN number format. "
            "Please enter a valid PAN number (eg. ABCDE1234F)."
        )
    if pan_number in get_all_pan_numbers():
        raise ValueError(
            "This PAN number already exist. "
            "Please enter a different PAN number."
        )


def validate_mobile_number(mobile_number: str) -> None:
    """
    Validate the mobile number.

    Args:
        mobile_number (str): Input mobile number of Taxpayer.

    Raises:
        ValueError: Mobile number must be exactly 10 digits long.
                    Mobile number must contain only digits.
    """
    if len(mobile_number) != 10:
        raise ValueError(
            "Invalid mobile number. It must be exactly 10 digits long."
        )
    if not mobile_number.isdigit():
        raise ValueError("Invalid mobile number. it must contain only digits.")


def validate_email(email: str) -> None:
    """
    Validate the email.

    Args:
        email (str): Input email address of Taxpayer.
    """
    if not email:
        raise ValueError("Email address is required.")
    if len(email) > 254:
        raise ValueError(
            "The email address must be less than 254 characters long."
        )
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
        ValueError: Annual income must be within the valid range.
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
            f"Total deductions cannot exceed {annual_income}."
        )


# Get all user input values
def get_name(prompt: str) -> str | None:
    """
    Get the name input from user.

    Args:
        prompt (str): Input string of prompt.

    Returns:
        str | None: Return the name if it is valid, otherwise return None.
    """
    while True:
        try:
            name = input(prompt).strip()
            validate_name(name=name)
        except ValueError as error:
            print(f"Error: {error}")
        else:
            return name


def get_age(prompt: str) -> int | None:
    """
    Get the age input from the user.

    Args:
        prompt (str): Input prompt string.

    Returns:
        int | None: Return the age if it is valid, otherwise return None.
    """
    while True:
        try:
            age = int(input(prompt))
            validate_age(age=age)
        except ValueError as error:
            print(f"Error: {error}")
        else:
            return age


def get_pan_number(prompt: str) -> str | None:
    """
    Get PAN number from the user.
    Args:
        prompt (str): Input prompt string
    """
    while True:
        try:
            pan_number = input(prompt).strip()
            validate_pan_number(pan_number=pan_number)
        except ValueError as error:
            print(f"Error: {error}")
        else:
            return pan_number


def get_mobile_number(prompt: str) -> str | None:
    """Get mobile number from the user."""
    while True:
        try:
            mobile_number = input(prompt)
            validate_mobile_number(mobile_number=mobile_number)
        except ValueError as error:
            print(f"Error: {error}")
        else:
            return mobile_number


def get_email(prompt: str) -> None:
    """Get email address from the user."""
    while True:
        try:
            email = input(prompt).strip()
            validate_email(email=email)
        except ValueError as error:
            print(f"Error: {error}")
        else:
            return email


def get_annual_income(prompt: str) -> float | None:
    """Get the annual income from the Taxpayer."""
    while True:
        try:
            annual_income = float(input(prompt))
            validate_annual_income(annual_income=annual_income)
        except ValueError as error:
            print(f"Error: {error}")
        else:
            return annual_income


def get_total_deductions(prompt: str, annual_income: float) -> float | None:
    """Get the Taxpayer's total deductions from the user."""
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
    """Get all PAN numbers from the records in the .txt File."""
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
        float: Return the tax amount.
    """
    return (taxable_income * tax_rate) / 100


def get_tax_rate(taxable_income: float) -> float:
    """
    Calculate and return the tax rate based on the taxpayer's taxable income.

    Args:
        taxable_income (float): Input of taxable income.

    Returns:
        float: Return the tax rate (%).
    """
    if taxable_income <= SLAB_1_LIMIT:
        return SLAB_1_TAX_RATE
    if taxable_income <= SLAB_2_LIMIT:
        return SLAB_2_TAX_RATE
    if taxable_income <= SLAB_3_LIMIT:
        return SLAB_3_TAX_RATE
    if taxable_income <= SLAB_4_LIMIT:
        return SLAB_4_TAX_RATE
    return SLAB_5_TAX_RATE


def parse_record(record: str) -> list[str]:
    """Return a record in list format."""
    return record.strip().split(",")


def auto_gen_next_tax_payer_id(tax_payers: list[str]) -> int:
    """Generate a new unique taxpayer ID automatically."""
    if not tax_payers:
        return 1
    return max(int(record.split(",")[0]) for record in tax_payers) + 1


def build_new_record(
    tax_payer_id: str,
    full_name: str,
    age: int,
    pan_number: str,
    mobile_number: str,
    email: str,
    annual_income: float,
    total_deductions: float
) -> str:
    """
    Build and return a new record.

    Args:
        tax_payer_id (str): Input of tax_payer ID.
        full_name (str): Input of full name.
        age (int): Input of age.
        pan_number (str): Input of PAN number.
        mobile_number (str): Input of mobile number.
        email (str): Input of email address.
        annual_income (float): Input of annual income.
        total_deductions (float): Input of total deductions.
    Returns:
        str: Return a taxpayer record.
    """
    # To get the taxable income
    taxable_income = calculate_taxable_income(
        annual_income=annual_income,
        total_deductions=total_deductions
    )
    # To get the tax rate
    tax_rate = get_tax_rate(taxable_income=taxable_income)
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


def add_tax_payer(tax_payers: list[str]) -> None:
    """Save the new taxpayer record into the .txt File."""
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
        print("\nOperation cancelled by user.")
    else:
        new_record = build_new_record(
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
    """
    Generate a report of all taxpayers.

    Args:
        tax_payers (list[str]): Retrieve all taxpayer records.
    """
    if not tax_payers:
        print("No taxpayer records found.")
        return
    print("-" * 85)
    print(
        f"{'PAN':<12} | {'Name':<20} | {'Income':>20} | {'Tax':>20}"
    )
    print("-" * 85)
    for record in tax_payers:
        record = parse_record(record=record)
        print(
            f"{record[3]:<12} | {record[1]:<20} | {float(record[6]):>20,.2f} | "
            f"{float(record[9]):>20,.2f}"
        )
    print("-" * 85)


def search_taxpayer(taxpayers: list[str]) -> None:
    """
    Search for a taxpayer record in the .txt File.

    Args:
        taxpayers (list[str]): Input of taxpayer records.
    """
    try:
        pan_number = input("Enter the PAN number to search: ").strip()
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
    else:
        _, record = find_tax_payer(pan_number=pan_number, taxpayers=taxpayers)
        if record:
            print("Taxpayer details:")
            print(f"Name: {record[1]}")
            print(f"PAN number: {record[3]}")
            print(f"Annual income: {record[6]}")
            print(f"Income Tax: {record[9]}")
        else:
            print(f"PAN: {pan_number} not found.")
    finally:
        print("Operation completed.")


def update_tax_payer(taxpayers: list[str]) -> None:
    """
    Search for the taxpayer record by PAN number and
    update it in the .txt File.
    Args:
        taxpayers (list[str]): Input Taxpayer records.
    """
    try:
        pan_number = input("Enter the PAN number to search: ").strip()
        index, record = find_tax_payer(
            pan_number=pan_number,
            taxpayers=taxpayers
        )

        if record:
            annual_income = get_annual_income(prompt="Enter the Annual Income: ")
            total_deductions = get_total_deductions(
                prompt="Enter the total deductions: ",
                annual_income=annual_income
            )

            update_record = build_new_record(
                    tax_payer_id=str(record[0]),
                    full_name=record[1],
                    age=str(record[2]),
                    pan_number=record[3],
                    mobile_number=record[4],
                    email=record[5],
                    annual_income=annual_income,
                    total_deductions=total_deductions
                )
            taxpayers[index] = update_record
            save_data(tax_payers=taxpayers)
            print("Updated taxpayer record successfully.")
        else:
            print(f"PAN: {pan_number} not found.")

    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
    finally:
        print("Operation completed.")


def delete_tax_payer(taxpayers: list[str]) -> None:
    """
    Search for a taxpayer record and delete it from the .txt file.

    Args:
        taxpayers (list[str]): Input of Taxpayer records.
    """
    try:
        pan_number = input("Enter the PAN number to delete record: ").strip()
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
    else:
        index, record = find_tax_payer(pan_number=pan_number, taxpayers=taxpayers)
        if record:
            taxpayers.pop(index)
            save_data(tax_payers=taxpayers)
            print("Deleted record successfully.")
        else:
            print(f"PAN: {pan_number} not found.")
    finally:
        print("Operation completed.")


def get_taxable_income(record: list[str]) -> float:
    """Return the taxable income."""
    return float(record[6]) - float(record[7])


def find_tax_payer(
    pan_number: str,
    taxpayers: list[str]
) -> tuple[int | None, list[str] | None]:
    """
    Return the index and taxpayer record.
    Args:
        pan_number (str): Input of taxpayer PAN number.
        taxpayers (list[str]): Input of taxpayer records.
    Returns:
        tuple[int | None, list[str] | None]: Find and return the index
        and taxpayer record"""
    for index, record in enumerate(taxpayers):
        record = parse_record(record=record)
        if record[3] == pan_number:
            return index, record
    return None, None


def individual_tax_report(taxpayers: list[str]) -> None:
    """
    Display individual tax report.

    Args:
        taxpayers (list[str]): Input of taxpayer records.
    """
    if not taxpayers:
        print("No taxpayer records found.")
        return
    pan_number = input("Enter the PAN number: ")
    _, record = find_tax_payer(pan_number=pan_number, taxpayers=taxpayers)
    if record:
        print("=" * 50)
        print("Individual Tax Report".center(50))
        print("=" * 50)
        print(f"\u25AA Taxpayer ID       : {record[0]}")
        print(f"\u25AA Full Name         : {record[1]}")
        print(f"\u25AA Age               : {record[2]}")
        print(f"\u25AA PAN Number        : {pan_number}")
        print(f"\u25AA Mobile            : {record[4]}")
        print(f"\u25AA Email             : {record[5]}")
        print("-" * 50)
        print("Income Details:")
        print("-" * 50)
        print(f"\u25AA Annual Income     : {float(record[6]):.2f}")
        print(f"\u25AA Total Deductions  : {float(record[7]):.2f}")
        print("-" * 50)
        print("Tax Calculation:")
        print("-" * 50)
        taxable_income = get_taxable_income(record=record)
        print(f"\u25AA Taxable Income   : {taxable_income:.2f}")
        print(f"\u25AA Tax Rate (%)     : {float(record[8]):.2f}")
        print(f"\u25AA Tax Amount       : {float(record[9]):.2f}")
        print("=" * 50)
    else:
        print(f"PAN: {pan_number} not found.")


def all_tax_payers_report(taxpayers: list[str]) -> None:
    """
    Display all Taxpayer's reports.

    Args:
        taxpayers (list[str]): Input of Taxpayer records.
    """
    if not taxpayers:
        print("No taxpayer records found.")
        return
    print("=" * 165)
    print("ALL TAXPAYER REPORT".center(100))
    print("=" * 165)
    print(
        f"{'ID':>5} | {'Name':<25} | {'Age':>10} | {'PAN':<12} | "
        f"{'Mobile':>12} | {'Income':>20} | {'Deduction':>20} | "
        f"{'Taxable Income':>20} | {'Tax':>20}")
    print("-" * 165)
    for record in taxpayers:
        record = parse_record(record=record)
        taxable_income = get_taxable_income(record=record)
        print(
            f"{record[0]:>5} | {record[1]:<25} | {record[2]:>10} | "
            f"{record[3]:<12} | {record[4]:>12} | {float(record[6]):>20,.2f} | "
            f"{float(record[7]):>20,.2f} | {taxable_income:>20,.2f} | "
            f"{float(record[9]):>20,.2f}"
        )
    print("-" * 165)


def display_report_menu() -> None:
    """Display the generate report submenu."""
    taxpayers = load_data()
    while True:
        print("1. Individual Report (PAN)")
        print("2. All Reports")
        print("3. Back to the Main menu")
        try:
            choice = input("Enter your choice: ")
        except KeyboardInterrupt:
            print("\nOperation cancelled by user.")
        else:
            if choice not in {"1", "2", "3"}:
                print("Invalid choice. Please select a valid option (1-3).")
            elif choice == "1":
                individual_tax_report(taxpayers=taxpayers)
            elif choice == "2":
                all_tax_payers_report(taxpayers=taxpayers)
            elif choice == "3":
                display_main_menu()
                return
        finally:
            print("Operation completed.")
        print("-" * 50)


def display_main_menu() -> None:
    """Main menu operations."""
    # Create a File if not exist.
    create_txt_file()
    # Fetch all data from .txt File.
    tax_payers = load_data()

    while True:
        print("Operations Menu: ")
        print("1. Register Taxpayer")
        print("2. View All Taxpayers")
        print("3. Search Taxpayer")
        print("4. Update Taxpayer")
        print("5. Delete Taxpayer")
        print("6. Generate Report")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice not in {"1", "2", "3", "4", "5", "6", "7"}:
            print("Invalid choice. Please select a valid option (1-7).")

        elif choice == "1":
            add_tax_payer(tax_payers=tax_payers)

        elif choice == "2":
            view_all_tax_payers(tax_payers=tax_payers)

        elif choice == "3":
            search_taxpayer(taxpayers=tax_payers)

        elif choice == "4":
            update_tax_payer(taxpayers=tax_payers)

        elif choice == "5":
            delete_tax_payer(taxpayers=tax_payers)

        elif choice == "6":
            display_report_menu()
            return
        elif choice == "7":
            print("Exit from operations.")
            break

        print("-" * 50)


def main():
    """Run the Income Tax Calculator Management System application."""

    # Main menu
    display_main_menu()


if __name__ == "__main__":
    main()
