"""ATM Withdraw Validation."""

from pathlib import Path
from datetime import datetime
from secrets import randbelow
from dateutil.relativedelta import relativedelta

# Accounts
FILE_PATH = "Part2/Section2/accounts.txt"
PATH = Path(FILE_PATH)
FILE_NAME = PATH.name

# Transactions
TRANX_FILE_PATH = "Part2/Section2/transactions.txt"
TRANX_PATH = Path(TRANX_FILE_PATH)
TRANX_FILE = TRANX_PATH.name

# Account headers
ACCOUNTS_HEADERS = "account_id, account_number, customer_name, "\
    "atm_card_number, balance, atm_pin, status, created_date, expiry_date"

# Transactions headers
TRANSACTIONS_HEADERS = "transaction_id, account_number, card_number, "\
    "transaction_type, transaction_amount, available_balance, "\
    "transaction_status, transaction_date"


BANK_CODE = 976483  # Bank Identification Code
BANK_NAME = "Canara Bank ATM"

MIN_WITHDRAW_AMOUNT = 100
MAX_WITHDRAW_AMOUNT = 10000
WITHDRAW_MULTIPLE = 100

MIN_DEPOSIT_AMOUNT = 100
DEPOSIT_MULTIPLE = 100
MAX_DEPOSIT_AMOUNT = 50000

MIN_ACCOUNT_BALANCE = 5000
MAX_DAILY_WITHDRAW_LIMIT = 20000
MAX_DAILY_TRANSACTION_COUNT = 10

MAX_PIN_ATTEMPTS = 3
ATM_PIN_LIMITS = 4

TRANSACTION_TYPE_WITHDRAW = "WITHDRAW"

ACCOUNT_STATUS_ACTIVE = "ACTIVE"
ACCOUNT_STATUS_INACTIVE = "INACTIVE"

ACCOUNT_STATUS_BLOCKED = "BLOCKED"
ACCOUNT_STATUS_CLOSED = "CLOSED"

SUCCESS = "SUCCESS"
FAILSED = "FAILED"


def create_accounts_txt_file() -> None:
    """Create .txt File, if not exist."""
    if not PATH.exists():
        with open(file=FILE_PATH, mode="w", encoding="utf-8") as file_obj:
            file_obj.write(ACCOUNTS_HEADERS + "\n")
            print(f"{FILE_NAME} file is created successfully.")


def create_transactions_txt_file() -> None:
    """Create a File if not exist."""
    if not TRANX_PATH.exists():
        with open(file=TRANX_FILE_PATH, mode="w", encoding="utf-8") as file_obj:
            file_obj.write(TRANSACTIONS_HEADERS + "\n")
            print(f"{TRANX_FILE} file is created successfully.")


def load_accounts_data() -> list[str]:
    """Fecth all accounts data."""
    with open(file=PATH, mode="r", encoding="utf-8") as file_obj:
        file_obj.readline()
        return file_obj.readlines()


def load_transactions_data() -> list[str]:
    """Fetch all transactions data from .txt File."""
    with open(file=TRANX_FILE_PATH, mode="r", encoding="utf-8") as file_obj:
        file_obj.readline()
        return file_obj.readlines()


def save_accounts_data(accounts: list[str]) -> None:
    """Save Accounts data to the .txt File."""
    with open(file=PATH, mode="w", encoding="utf-8") as file_obj:
        file_obj.write(ACCOUNTS_HEADERS + "\n")
        file_obj.writelines(accounts)


def save_transactions_data(transactions: list[str]) -> None:
    """Save transactions data to the .txt File."""
    with open(file=TRANX_FILE_PATH, mode="w", encoding="utf-8") as file_obj:
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
    )


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
            status=ACCOUNT_STATUS_INACTIVE,
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
                    status=ACCOUNT_STATUS_ACTIVE,
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


def get_account_record(atm_card_num: int, accounts: list[str]) -> list[int]:
    """Return the account record."""
    for index, record in enumerate(accounts):
        record = record.split(",")
        atm_num = int(record[3])
        if atm_num == atm_card_num:
            return index, record


def validate_atm_card_number(atm_card_num: int, accounts: list[str]) -> None:
    """Validate the ATM card number."""
    _, account_record = get_account_record(
        atm_card_num=atm_card_num,
        accounts=accounts
    )
    if account_record[6] != ACCOUNT_STATUS_ACTIVE:
        raise ValueError(
            f"Your account is not {ACCOUNT_STATUS_ACTIVE}. "
            "Please activate it first."
        )

    if account_record is None or (str(atm_card_num) != account_record[3]):
        raise ValueError(
            "Invalid ATM card number. "
            "Please enter a valid number (16 digits).")


def get_atm_store_pin(
    atm_number: int,
    accounts: list[str]
) -> None:
    """Validate the ATM pin."""
    _, store_atm_pin = get_account_record(
        atm_card_num=atm_number,
        accounts=accounts
    )
    store_atm_pin = store_atm_pin[5]
    return validate_atm_pin_extend(store_atm_pin)


def validate_atm_pin_extend(stored_pin):
    """Validate the ATM PIN."""
    attempts = 0

    while attempts < MAX_PIN_ATTEMPTS:

        pin = input("Enter the again ATM PIN : ")

        if pin == "":
            print("PIN is required.")
            continue

        if not pin.isdigit():
            print("PIN must contain only numbers.")
            continue

        if len(pin) != ATM_PIN_LIMITS:
            print(f"PIN must be exactly {ATM_PIN_LIMITS} digits.")
            continue

        if pin != stored_pin:
            attempts += 1

            if attempts == MAX_PIN_ATTEMPTS:
                return False

            print(
                "Invalid PIN. Remaining Attempts : "
                f"{MAX_PIN_ATTEMPTS - attempts}")
            continue

        print("Login Successful.")
        return True


def get_atm_card_number(prompt: str, accounts: list[str]) -> int:
    """Get and return the ATM card number from user."""
    while True:
        try:
            atm_card_number = int(input(prompt))
            validate_atm_card_number(
                atm_card_num=atm_card_number,
                accounts=accounts
            )
        except ValueError as error:
            print(f"Error: {error}")
        else:
            return atm_card_number


def get_atm_pin(prompt: str, atm_number: int, accounts: list[str]) -> str:
    """Get and return ATM PIN from user."""
    try:
        atm_pin = input(prompt).strip()
        result = get_atm_store_pin(
            atm_number=atm_number,
            accounts=accounts
        )
        if not result:
            print("Card Blocked.")
            index, account_record = get_account_record(
                atm_card_num=atm_number,
                accounts=accounts
            )
            update_record = build_accounts_record(
                account_id=account_record[0],
                account_number=account_record[1],
                customer_name=account_record[2],
                atm_card_number=account_record[3],
                balance=account_record[4],
                atm_pin=account_record[5],
                status=ACCOUNT_STATUS_BLOCKED,
                created_date=account_record[7],
                expiry_date=account_record[8],
            )
            accounts[index] = update_record
            save_accounts_data(accounts=accounts)

    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
    else:
        return atm_pin


def atm_login(accounts: list[str]) -> None:
    """ATM Login"""
    try:
        atm_card_number = get_atm_card_number(
            prompt="Enter the ATM card number: ",
            accounts=accounts
        )
        atm_pin = get_atm_pin(
            prompt="Enter the ATM PIN: ",
            atm_number=atm_card_number,
            accounts=accounts
        )
    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
    else:
        if atm_pin:
            main_main(atm_number=atm_card_number)


def atm_login_menu() -> None:
    """Return a ATM Login Menu."""
    # Create File (accounts.txt), if not exist.
    create_accounts_txt_file()
    # Create File (transactions.txt), if not exist.
    create_transactions_txt_file()

    accounts = load_accounts_data()
    while True:
        print("-" * 50)
        print(f"Welcome to the {BANK_NAME}".center(50))
        print("\n")
        print("\t\tOperations:")
        print("\t\t1. Login")
        print("\t\t2. Exit")

        try:
            choice = input("\n\nEnter your choice: ")
        except KeyboardInterrupt:
            print("Operation cancelled by the user.")
        else:
            if choice not in {"1", "2"}:
                print("Invalid choice. Please select a valid option.(1-2)")
            elif choice == "2":
                print("Exit from operation.")
                break
            elif choice == "1":
                atm_login(accounts=accounts)

        print("-" * 50)


def get_withdrawal_amount(prompt: str, account_record: list[str]) -> float:
    """Return a withdrawal amount from user."""
    while True:
        try:
            withdrawal_amount = float(input(prompt))
            validate_withdrawal_amount(
                withdrawal_amount=withdrawal_amount,
                account_record=account_record
            )
        except ValueError as error:
            print(f"Error: {error}")
        else:
            return withdrawal_amount


def calculate_remaining_balance(
    available_balance: float,
    withdrawal_amount: float
) -> float:
    """Calculate and return the remining balance."""
    return available_balance - withdrawal_amount


def is_account_status_active(account_record: list[str]) -> bool:
    """Check whether a bank account status is active or not."""
    account_status = account_record[6]
    if account_status == ACCOUNT_STATUS_ACTIVE:
        return True
    return False


def validate_withdrawal_amount(
    withdrawal_amount: float,
    account_record: list[str]
) -> None:
    """Validate the withdrawal amount."""
    if not is_account_status_active(account_record=account_record):
        raise ValueError("Account is not an active.")
    if withdrawal_amount < 0:
        raise ValueError("Amount must be greater than zero.")
    if withdrawal_amount < MIN_WITHDRAW_AMOUNT:
        raise ValueError(
            f"Minimum withdrawal amount is {MIN_WITHDRAW_AMOUNT}.")
    if withdrawal_amount > MAX_WITHDRAW_AMOUNT:
        raise ValueError(
            f"Maximum withdrawal amount is {MAX_WITHDRAW_AMOUNT}.")
    if not withdrawal_amount % 100 == 0:
        raise ValueError(f"Amount must be a multiple of {WITHDRAW_MULTIPLE}.")

    # Get the current account balance.
    current_account_balance = float(account_record[4])
    # Get the remaining account balance.
    remaining_balance = calculate_remaining_balance(
        available_balance=current_account_balance,
        withdrawal_amount=withdrawal_amount
    )

    if withdrawal_amount > current_account_balance:
        raise ValueError("Insufficient account balance.")

    if remaining_balance < MIN_ACCOUNT_BALANCE:
        raise ValueError(
            f"Minimum balance of {MIN_ACCOUNT_BALANCE} must be maintained.")
    if current_account_balance <= 0:
        raise ValueError("No balance available for withdrawal.")


def get_transaction_records(transactions: list[str]) -> list[str]:
    """Return the transactions record"""
    return tuple(record.split(",") for record in transactions)


def auto_generate_transaction_id(transactions: list[str]) -> str:
    """Return the auto generated transaction ID."""
    if not transactions:
        return "TXN" + str(1).zfill(10)
    last_transaction = max({int(record[0].split("TXN")[1])
                            for record in get_transaction_records(
                                transactions=transactions)}) + 1
    return "TXN" + str(last_transaction).zfill(10)


def atm_withdrawal_cash(
    atm_number: int,
    accounts: list[str],
    transactions: list[str]
) -> None:
    """Withdrawal cash amount from ATM."""
    index, account_record = get_account_record(
        atm_card_num=atm_number,
        accounts=accounts
    )

    print("-" * 50)
    print(f"{BANK_NAME}".center(50))
    print("-" * 50)
    print("Withdraw Cash\n".center(50))
    print(f"Account Number     : {account_record[1]}")
    print(f"Customer Name      : {account_record[2]}")
    available_balance = float(account_record[4])
    print(f"Available Balnce   : {available_balance:.2f}")
    print("-" * 50)
    print("\n")
    try:
        withdrawal_amount = get_withdrawal_amount(
            prompt="Enter the withdrawal amount: ",
            account_record=account_record,
        )
    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
    else:
        print(f"Withdrawal amount: {withdrawal_amount}")
        new_trasaction_id = auto_generate_transaction_id(
            transactions=transactions)
        remaining_balance = calculate_remaining_balance(
            available_balance=available_balance,
            withdrawal_amount=withdrawal_amount
        )
        new_transaction_record = build_transactions_record(
            transaction_id=new_trasaction_id,
            account_number=account_record[1],
            card_number=str(atm_number),
            transaction_type=TRANSACTION_TYPE_WITHDRAW,
            transaction_amount=str(withdrawal_amount),
            available_balance=str(remaining_balance),
            transaction_status=SUCCESS,
            transaction_date=str(datetime.today())
        )
        transactions.append(new_transaction_record)
        save_transactions_data(transactions=transactions)

        update_account_record = build_accounts_record(
            account_id=account_record[0],
            account_number=account_record[1],
            customer_name=account_record[2],
            atm_card_number=str(atm_number),
            balance=str(remaining_balance),
            atm_pin=account_record[5],
            status=account_record[6],
            created_date=account_record[7],
            expiry_date=account_record[8]
        )
        accounts[index] = update_account_record
        save_accounts_data(accounts=accounts)
        print(f"Successfully withdraw {withdrawal_amount}.")
    print("-" * 50)
    print("\n")
    print("Note:")
    print(f"\u25fe Minimum withdrawal : {float(MIN_WITHDRAW_AMOUNT):.2f}")
    print(
        f"\u25fe MAximum withdrawal : "
        f"{float(MAX_WITHDRAW_AMOUNT):.2f} per transaction")
    print(f"\u25fe Amount must be multiple of {float(WITHDRAW_MULTIPLE):.2f}")
    print(
        f"\u25fe Minimum balance after withdrawal: "
        f"{float(MIN_ACCOUNT_BALANCE):.2f}")


def update_available_balance(
    current_balance: float,
    deposit_balance: float
) -> float:
    """Return a available balance."""
    return current_balance + deposit_balance


def atm_deposit_cash(atm_number: int, accounts: list[str]) -> None:
    """Deposit cash amount to the ATM"""
    index, account_record = get_account_record(
        atm_card_num=atm_number,
        accounts=accounts
    )
    print("-" * 50)
    print(f"{BANK_NAME}".center(50))
    print("-" * 50)
    print("Deposit Cash\n".center(50))
    print(f"Account Number     : {account_record[1]}")
    print(f"Customer Name      : {account_record[2]}")
    current_balance = float(account_record[4])
    print(f"Current Balance   : {current_balance:.2f}")
    print("-" * 50)
    print("\n")
    try:
        deposit_amount = float(input("Enter the deposit amount: "))
    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
    else:
        print(f"Deposit amount: {deposit_amount}")
        updated_balance = update_available_balance(
            current_balance=current_balance,
            deposit_balance=deposit_amount
        )
        update_record = build_accounts_record(
            account_id=account_record[0],
            account_number=account_record[1],
            customer_name=account_record[2],
            atm_card_number=str(atm_number),
            balance=str(updated_balance),
            atm_pin=account_record[5],
            status=account_record[6],
            created_date=account_record[7],
            expiry_date=account_record[8]
        )
        accounts[index] = update_record
        save_accounts_data(accounts=accounts)

    print("-" * 50)
    print("\n")
    print("Note:")
    print(f"\u25fe Minimum deposit : {float(MIN_DEPOSIT_AMOUNT):.2f}")
    print(
        f"\u25fe Maximum deposit : "
        f"{float(MAX_DEPOSIT_AMOUNT):.2f} per transaction")
    print(f"\u25fe Amount must be multiple of {float(DEPOSIT_MULTIPLE):.2f}")
    print("-" * 50)
    print("\nStatus :\n")
    print("Deposit successful!")
    print(f"Updated Balance: {updated_balance}")


def atm_balance_enquiry(atm_number: int, accounts: list[str]) -> None:
    """Check the balance in your account."""
    _, account_record = get_account_record(
        atm_card_num=atm_number,
        accounts=accounts
    )
    print("-" * 50)
    print(f"{BANK_NAME}.".center(50))
    print("-" * 50)
    print("Balance Enquiry".center(50))
    print("\n")
    print(f"Account Number: {account_record[1]}")
    print(f"Customer Name: {account_record[2]}")
    print("\n")
    print("-" * 50)
    print("\n")
    print(f"Available Balance: {float(account_record[4]):.2f}")
    print("\n")
    print("-" * 50)
    print("\nStatus:")
    print("\nBalance Displayed successfully.")
    print("-" * 50)


def atm_bank_statement(
    atm_number: int,
    accounts: list[str],
    transactions: list[str]
) -> None:
    """Displayed the ATM bank statement."""
    _, account_record = get_account_record(atm_card_num=atm_number, accounts=accounts)
    transaction_records = get_transaction_records(transactions=transactions)
    filtered_records = [record for record in transaction_records
                        if str(atm_number) == record[2]]
    if not filtered_records:
        print("Not available entries.")
        return
    print("-" * 100)
    print(f"{BANK_NAME}".center(100))
    print("-" * 100)
    print(f"Account Number: {account_record[1]}")
    print(f"Customer Name: {account_record[2]}")
    print(f"ATM Number: {atm_number}")
    print("-" * 100)
    print(
        f"{'Txn ID':<20}  {'Type':<10}  {'Amount':>20}  {'Status':<10} "
        f" {'Date & Time:':<20}")
    print("-" * 100)
    for record in filtered_records[:5]:
        print(
            f"{record[0]:<20}  {record[3]:<10}  {record[4]:>20}  "
            f"{record[6]:<10}  {record[7]:<20}")
    print("-" * 100)


def validate_atm_pin(atm_pin: str) -> str:
    """Validate the ATM pin."""
    if len(atm_pin) != 4:
        raise ValueError("An ATM pin should be 4 digits.")
    if not atm_pin.isdigit():
        raise ValueError("An ATM PIN should be in digits.")


def atm_change_pin(atm_number: int, accounts: list[str]) -> None:
    """Changing to the ATM PIN from user."""
    index, account_record = get_account_record(
        atm_card_num=atm_number,
        accounts=accounts
    )
    atm_pin = get_atm_pin(
        prompt="Enter the new ATM pin: ",
        atm_number=atm_number,
        accounts=accounts
    ).strip()
    update_record = build_accounts_record(
        account_id=account_record[0],
        account_number=account_record[1],
        customer_name=account_record[2],
        atm_card_number=str(atm_number),
        balance=account_record[4],
        atm_pin=atm_pin,
        status=account_record[6],
        created_date=account_record[7],
        expiry_date=account_record[8]
    )
    accounts[index] = update_record
    save_accounts_data(accounts=accounts)
    print("Successfully changed the ATM PIN.")


def get_account_record_by_account_number(
    atm_number: int,
    account_number: str,
    accounts: list[str]
) -> str:
    """Get the account record by account number."""
    for record in accounts:
        record = record.split(",")
        if record[3] == str(atm_number) or record[1] == account_number:
            return record


def search_account(atm_number: int, accounts: list[str]) -> None:
    """Search the account details by ATM number."""
    print("-" * 100)
    print(f"{BANK_NAME}".center(100))
    print("-" * 100)
    print("Search Account".center(100))
    print("\n")
    print("Search By :")
    print("\n\t\u2714 Account Number")
    print("\n")
    account_number = input("Enter the bank account number: ").strip()
    account_record = get_account_record_by_account_number(
        atm_number=atm_number,
        account_number=account_number,
        accounts=accounts
    )

    print("-" * 100)
    print("Search Result".center(100))
    print("-" * 100)
    print(f"Account Number: {account_record[1]}")
    print(f"Customer Name: {account_record[2]}")
    print(f"Account Status: {account_record[6]}")
    print(f"Current Balance: {float(account_record[4]):.2f}")
    print("\n")
    print("-" * 100)


def main_main(atm_number: int) -> None:
    """Run the ATM Withdraw Validation."""
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
                atm_withdrawal_cash(
                    atm_number=atm_number,
                    accounts=accounts,
                    transactions=transactions
                )

            elif choice == "4":
                atm_deposit_cash(
                    atm_number=atm_number,
                    accounts=accounts
                )

            elif choice == "5":
                atm_balance_enquiry(atm_number=atm_number, accounts=accounts)

            elif choice == "6":
                atm_bank_statement(
                    atm_number=atm_number,
                    accounts=accounts,
                    transactions=transactions
                )

            elif choice == "7":
                atm_change_pin(atm_number=atm_number, accounts=accounts)

            elif choice == "8":
                search_account(atm_number=atm_number, accounts=accounts)

        print("-" * 50)


if __name__ == "__main__":
    atm_login_menu()
