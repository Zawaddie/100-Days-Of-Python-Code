phonebook = {}

def add_contact():
    name = input("Enter contact name: ")
    if name in phonebook:
        print("Contact already exists.")
    else:
        number = input("Enter phone number: ")
        phonebook[name] = number
        print("Contact added successfully!")

def search_contact():
    name = input("Enter contact name: ")
    if name in phonebook:
        print("Phone number:", phonebook[name])
    else:
        print("Contact not found in the phonebook.")

def remove_contact():
    name = input("Enter contact name: ")
    if name in phonebook:
        del phonebook[name]
        print("Contact removed successfully!")
    else:
        print("Contact not found in the phonebook.")

def view_contacts():
    print("Phonebook Contacts:")
    for name, number in phonebook.items():
        print(f"- {name}: {number}")

while True:
    print("My Phonebook")
    print("-----------------")
    print("1. Add a contact")
    print("2. Search for a contact")
    print("3. Remove a contact")
    print("4. View all contacts")
    print("5. Exit")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        search_contact()
    elif choice == "3":
        remove_contact()
    elif choice == "4":
        view_contacts()
    elif choice == "5":
        print("Exiting the program...")
        break
    else:
        print("Invalid choice. Please try again.")
