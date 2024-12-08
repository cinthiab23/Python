def main_menu():
    print("Menu:")
    while True:
        try:
            print("\nWelcome! You can create new email entries, change email addresses, delete entries, or display entries.")
            print("1. Create a new entry")
            print("2. Display all entries")
            print("3. Update an existing entry")
            print("4. Remove an entry")
            print("5. Quit")
            choice = int(input("Please enter the number of your selection: "))
            if 1 <= choice <= 5:
                return choice
            else:
                print("That is not a valid number. Try again.")
        except ValueError:
            print("That is not a valid number. Try again.")


def check():
    try:
        with open("customer_list.txt", 'r') as file:
            lines = file.readlines()
        return lines
    except FileNotFoundError:
        print("Customer list does not exist. Creating a new file...")
        return []


def save(output):
    with open("customer_list.txt", 'w') as file:
        for line in output:
            file.write(line)
    print("File updated.")


def create():
    customer = check()
    fname = input("Please enter the customer's first name: ")
    lname = input("Please enter the customer's last name: ")
    phone = input("Please enter the customer's phone number: ")
    email = input("Please enter the customer's email: ")
    entry = f"{fname}, {lname}, {phone}, {email}\n"
    customer.append(entry)
    save(customer)


def read():
    customer = check()
    if customer:
        print("Customer List:")
        for index, entry in enumerate(customer, start=1):
            print(f"{index}. {entry.strip()}")
    else:
        print("No entries found.")


def update():
    customer = check()
    read()
    try:
        index = int(
            input("Enter the number of the entry you want to update: ")) - 1
        if 0 <= index < len(customer):
            fname = input(
                "Enter new first name (or press Enter to keep current): ")
            lname = input(
                "Enter new last name (or press Enter to keep current): ")
            phone = input("Enter new phone (or press Enter to keep current): ")
            email = input("Enter new email (or press Enter to keep current): ")

            entry = customer[index].strip().split(", ")
            customer[index] = f"{fname or entry[0]}, {lname or entry[1]}, {
                phone or entry[2]}, {email or entry[3]}\n"
            save(customer)
        else:
            print("Invalid entry number.")
    except ValueError:
        print("Invalid input. Please enter a number.")


def delete():
    customer = check()
    read()
    try:
        index = int(
            input("Enter the number of the entry you want to delete: ")) - 1
        if 0 <= index < len(customer):
            del customer[index]
            save(customer)
            print("Entry deleted.")
        else:
            print("Invalid entry number.")
    except ValueError:
        print("Invalid input. Please enter a number.")


# Main execution
while True:
    choice = main_menu()
    if choice == 1:
        create()
    elif choice == 2:
        read()
    elif choice == 3:
        update()
    elif choice == 4:
        delete()
    elif choice == 5:
        print("Exiting program.")
        break
