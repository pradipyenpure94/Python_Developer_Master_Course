"""Create contact book application."""

contact_book = {}

while True:
    print("Contact book Application: ")
    print("1. Add contact.")
    print("2. View contacts.")
    print("3. Exit")

    choice = input("Enter your choice? ")

    if choice not in {"1", "2", "3"}:
        print("Please enter a valid choice (1-3)")
        continue

    elif choice == "1":
        name = input("Enter contact name: ")
        if not name:
            print("Please enter name..!")
            continue
        if name.casefold() in contact_book:
            print("Contact already exists..!")
            continue
        mobile_no = input("Enter contact number: ")
        if not mobile_no.isdigit():
            print("Mobile number should be digit..!")
            continue
        if len(mobile_no) != 10:
            print("Mobile number should be 10 digit..!")
            continue
        contact_book[name] = mobile_no
        print("Contact added successfully..!")

    elif choice == "2":
        if not contact_book:
            print("Contacts empty..!")
        else:
            print("Contacts: ")
            print("-"*40)
            print(f"{'Name':<20} | {'Mobile No.':<11}")
            print("-"*40)
            for name, mobile_no in contact_book.items():
                print(f"{name:<20} | {mobile_no:<11}")
            print("-"*40)

    elif choice == "3":
        print("Exit..!")
        break
