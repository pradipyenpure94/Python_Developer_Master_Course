"""ATM Withdraw Validation."""

from pathlib import Path
from datetime import datetime
from secrets import randbelow
from dateutil.relativedelta import relativedelta

# Accounts
FILE_PATH = "Part2/Section2/accounts.txt"
PATH = Path(FILE_PATH)
FILE_NAME = PATH.name

ACCOUNTS_HEADERS = "account_id, account_number, customer_name, "\
    "atm_card_number, balance, atm_pin, status, created_date, expiry_date"

# Transactions
TRANSACTIONS_HEADERS = "transaction_id, account_number, card_number, "\
    "transaction_type, transaction_amount, available_balance, "\
    "transaction_status, transaction_date"

TRANX_FILE_PATH = "Part2/Section2/transactions.txt"
TRANX_PATH = Path(TRANX_FILE_PATH)
TRANX_FILE = TRANX_PATH.name

BANK_CODE = 976483  # Bank Identification Code


def create_accounts_txt_file() -> None:
    """Create .txt File, if not exist."""
    if not PATH.exists():
        with open(file=FILE_PATH, mode="w", encoding="utf-8") as file_obj:
            file_obj.write(ACCOUNTS_HEADERS + "\n")


def create_transactions_txt_file() -> None:
    """Create a File if not exist."""
    if not TRANX_PATH.exists():
        with open(file=TRANX_FILE, mode="w", encoding="utf-8") as file_obj:
            file_obj.write(TRANSACTIONS_HEADERS + "\n")


def load_accounts_data() -> list[str]:
    """Fecth all accounts data."""
    with open(file=PATH, mode="r", encoding="utf-8") as file_obj:
        file_obj.readline()
        return file_obj.readlines()


def load_transactions_data() -> list[str]:
    """Fetch all transactions data from .txt File."""
    with open(file=TRANX_FILE, mode="r", encoding="utf-8") as file_obj:
        file_obj.readline()
        return file_obj.readlines()


def save_accounts_data(accounts: list[str]) -> None:
    """Save Accounts data to the .txt File."""
    with open(file=PATH, mode="w", encoding="utf-8") as file_obj:
        file_obj.write(ACCOUNTS_HEADERS + "\n")
        file_obj.writelines(accounts)


def save_transactions_data(transactions: list[str]) -> None:
    """Save transactions data to the .txt File."""
    with open(file=TRANX_FILE, mode="w", encoding="utf-8") as file_obj:
        file_obj.write(TRANSACTIONS_HEADERS + "\n")
        file_obj.writelines(transactions)


def build_accounts_record(
    account_id: int,
    account_number: str,
    customer_name: str,
    atm_card_number: int,
    balance: float,
    atm_pin: str,
    status: str,
    created_date: str,
    expiry_date: str
) -> str:
    """Build and return a record."""
    return ",".join(
        [
            account_id,
            account_number,
            customer_name,
            atm_card_number,
            balance,
            atm_pin,
            status,
            created_date,
            expiry_date
        ]
    ) + "\n"


def auto_generate_next_account_id(accounts: list[str]) -> int:
    """Return a auto generated the account ID."""
    if not accounts:
        return 1
    return max(int(record.split(",")[0]) for record in accounts) + 1


def auto_generated_account_number(accounts: list[str]) -> str:
    """Return a auto generated the account number."""
    if not accounts:
        return str(1).zfill(10)
    last_acc_no = max(
        int(record.split(",")[1]) for record in accounts) + 1
    return str(last_acc_no).zfill(10)


def validate_name(name: str, field_name: str) -> None:
    """Validate the name."""
    if not name:
        raise ValueError(f"{field_name} name cannot be empty.")
    if not all(char.isalpha() or char.isspace() for char in name):
        raise ValueError(
            f"{field_name} name must contain letters and spaces.")


def auto_generate_next_atm_number(accounts: list[str]) -> str:
    """Return a auto generated the ATM card number."""
    if not accounts:
        return str(BANK_CODE) + str(1).zfill(10)
    return max(int(record.split(",")[3]) for record in accounts) + 1


def validate_account_balance(balance: float, field_name: str) -> None:
    """Validate the account balance."""
    if balance < 0:
        raise ValueError(f"{field_name} should be zero or greater than zero.")


def auto_generate_atm_pin() -> str:
    """Return a auto generated ATM Pin."""
    return f"{randbelow(1000):04d}"


def get_name(prompt: str) -> str:
    """Return a name."""
    while True:
        try:
            name = input(prompt).strip()
            validate_name(name=name, field_name="Customer")
        except ValueError as error:
            print(f"Error: {error}")
        else:
            return name


def get_balance(prompt: str) -> float:
    """Return a balance."""
    while True:
        try:
            balance = float(input(prompt))
            validate_account_balance(balance=balance, field_name="Balance")
        except ValueError as error:
            print(f"Error: {error}")
        else:
            return balance


def register_account(accounts: list[str]) -> None:
    """Register a account."""
    try:
        account_id = auto_generate_next_account_id(accounts=accounts)
        account_number = auto_generated_account_number(accounts=accounts)
        customer_name = get_name(prompt="Enter the customer name: ")
        atm_card_number = auto_generate_next_atm_number(accounts=accounts)
        balance = get_balance(prompt="Enter the customer balance: ")

    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
    else:
        current_date = datetime.today()
        atm_pin = auto_generate_atm_pin()

        new_record = build_accounts_record(
            account_id=str(account_id),
            account_number=account_number,
            customer_name=customer_name,
            atm_card_number=str(atm_card_number),
            balance=str(balance),
            atm_pin=atm_pin,
            status="INACTIVE",
            created_date=str(current_date),
            expiry_date=str(current_date + relativedelta(years=5))
            )
        accounts.append(new_record)
        save_accounts_data(accounts=accounts)
        print("Registered the account successfully.")
    finally:
        print("Operation completed.")


def activate_bank_account(accounts: list[str]) -> None:
    """Activate a bank account."""
    try:
        account_number = int(input("Enter the bank account: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
    else:
        for index, record in enumerate(accounts):
            record = record.split(",")
            if record[0] == str(account_number):
                update_record = build_accounts_record(
                    account_id=record[0],
                    account_number=record[1],
                    customer_name=record[2],
                    atm_card_number=record[3],
                    balance=record[4],
                    atm_pin=record[5],
                    status="ACTIVE",
                    created_date=record[7],
                    expiry_date=record[8][:-1]
                )
                accounts[index] = update_record
                save_accounts_data(accounts=accounts)
                print("Successfully activated the bank account.")
                break
        else:
            print("Account does not exist.")
    finally:
        print("Operation completed.")


def build_transactions_record(
    transaction_id: str,
    account_number: str,
    card_number: str,
    transaction_type: str,
    transaction_amount: float,
    available_balance: float,
    transaction_status: str,
    transaction_date: str
) -> str:
    """Build and return a transaction record."""
    return ",".join(
        [
            transaction_id,
            account_number,
            card_number,
            transaction_type,
            transaction_amount,
            available_balance,
            transaction_status,
            transaction_date,
        ]) + "\n"


def main() -> None:
    """Run the ATM Withdraw Validation."""
    # Create File (accounts.txt), if not exist.
    create_accounts_txt_file()
    # Create File (transactions.txt), if not exist.
    create_transactions_txt_file()

    # Fetch all accounts data.
    accounts = load_accounts_data()
    transactions = load_transactions_data()

    while True:
        print("Operations Menu:")
        print("1. Register Account")
        print("2. Activate Account")
        print("3. Withdraw Cash")
        print("4. Deposit Cash")
        print("5. Balance Enquiry")
        print("6. Mini Statement")
        print("7. Change Pin")
        print("8. Search Account")
        print("9. Exit")

        try:
            choice = input("Enter your choice: ")
        except KeyboardInterrupt:
            print("\nOperation cancelled by the user.")
        else:
            if choice not in {"1", "2", "3", "4", "5", "6", "7", "8", "9"}:
                print("Invalid choice. Please select a valid option (1-9).")

            elif choice == "9":
                print("Exit from operations.")
                break

            elif choice == "1":
                register_account(accounts=accounts)

            elif choice == "2":
                activate_bank_account(accounts=accounts)

            elif choice == "3":
                pass

            elif choice == "4":
                pass

            elif choice == "5":
                pass

            elif choice == "6":
                pass

            elif choice == "7":
                pass

            elif choice == "8":
                pass

        print("-" * 50)


if __name__ == "__main__":
    main()
