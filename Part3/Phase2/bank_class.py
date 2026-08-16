"""
Bank Name

Create multiple bank accounts where all accounts share a common bank name.
"""


class Bank:
    """Represent a bank."""
    bank_name = "Canara"

    def __init__(self, branch_name: str):
        self.branch_name = branch_name

    def display_bank_info(self) -> None:
        """Display bank information."""
        print("-" * 40)
        print("Bank Information: ")
        print("-" * 40)
        print(f"Name   : {Bank.bank_name}")
        print(f"Branch : {self.branch_name}")
        print("-" * 40)


def main() -> None:
    """Run the main program."""
    bank_object1 = Bank(branch_name="Kothrud")
    bank_object1.display_bank_info()
    bank_object2 = Bank(branch_name="Haveli")
    bank_object2.display_bank_info()


if __name__ == "__main__":
    main()
