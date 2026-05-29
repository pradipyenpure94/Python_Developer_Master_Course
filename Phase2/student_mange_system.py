"""Student management system."""

students = {}

while True:
    print("1. Add student record")
    print("2. View student record")
    print("3. Search student record")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice not in {"1", "2", "3", "4"}:
        print("Invalid input! Please enter valid choice(1-4)")    
        continue

    if choice == "1":
        try:
            stud_id = str(len(students) + 1)
            name = input("Enter student name: ")
            if not name:
                print("Name cannot be empty!")
                continue
            marks = float(input("Enter student marks: "))
            if marks < 0:
                print("Marks cannot be negative.")
                continue
            if any(student['name'].casefold() == name.casefold()
                   for student in students.values()):
                print("Student name already exists!")
                continue
        except ValueError:
            print("Invalid input! Please enter a valid input.")
            continue

        students[stud_id] = {
            "name": name,
            "marks": marks
            }
        print("Student record added successfully!")
    elif choice == "2":
        if not students:
            print("Students record entry not available.")
        else:
            print("Students information:")
            print("-"*60)
            print(f"{'Student Id':<10} | {'Name':<30} | {'Marks':<10}")
            print("-"*60)
            for stud_id, details in students.items():
                print(f"{stud_id:<10} | {details['name']:<30} | {details['marks']:<10.2f}")
                print("-"*60)

    elif choice == "3":
        stud_id = input("Enter student Id to search: ")
        if stud_id in students:
            print(f"{stud_id} record found!")
        else:
            print(f"{stud_id} record not found!")

    elif choice == "4":
        print("Exit.")
        break
