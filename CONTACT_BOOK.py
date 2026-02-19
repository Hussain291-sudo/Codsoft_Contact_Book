import json
import os

CONTACTS_FILE = 'contacts.json'


def load_contacts():
    """Load contacts from file if it exists."""
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as f:
            return json.load(f)
    return {}


def save_contacts(contacts):
    """Save contacts to file."""
    with open(CONTACTS_FILE, 'w') as f:
        json.dump(contacts, f, indent=4)


def add_contact(contacts):
    """Add a new contact."""
    name = input("Enter name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return
    if name in contacts:
        print("Contact already exists. Use update to modify.")
        return

    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()
    address = input("Enter address: ").strip()

    contacts[name] = {
        'phone': phone,
        'email': email,
        'address': address
    }
    save_contacts(contacts)
    print("Contact added successfully.")


def view_contacts(contacts):
    """Display list of all contacts with names and phone numbers."""
    if not contacts:
        print("No contacts found.")
        return
    print("\nContact List:")
    for name, details in contacts.items():
        print(f"Name: {name}, Phone: {details['phone']}")


def search_contact(contacts):
    """Search for a contact by name or phone number."""
    query = input("Enter name or phone number to search: ").strip().lower()
    if not query:
        print("Search query cannot be empty.")
        return

    found = False
    for name, details in contacts.items():
        if query in name.lower() or query in details['phone']:
            print(f"\nName: {name}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}")
            print(f"Address: {details['address']}")
            found = True

    if not found:
        print("No matching contact found.")


def update_contact(contacts):
    """Update an existing  contact."""
    name = input("Enter the name of the contact to update: ").strip()
    if name not in contacts:
        print("Contact not found.")
        return
    print("Leave field blank to keep current values.")

    phone = input(f"New phone (current:{contacts[name]['phone']}): ").strip()
    email = input(f"New email (current:{contacts[name]['email']}): ").strip()
    address = input(f" Enter New address ( current:{contacts[name]['address']}): ").strip()

    if phone:
        contacts[name]['phone'] = phone
    if email:
        contacts[name]['email'] = email
    if address:
        contacts[name]['address'] = address

    save_contacts(contacts)
    print("Contact updated successfully.")


def delete_contact(contacts):
    """Delete a content"""
    name = input("Enter the name of the contact to delete: ").strip()
    if name not in contacts:
        print("Contact not found.")
        return

    confirm = input(f" Are you sure you want to Delete {name}? (yes/no): ").strip().lower()
    if confirm == 'yes':
        del contacts[name]
        save_contacts(contacts)
        print("Contact deleted successfully.")
    else:
        print("Deletion cancelled.")


def main():
    """Main menu for the Contact Book"""
    contacts = load_contacts()
    while True:
        print("\n--- Contact Book ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose the option (1-6): ").strip()

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            print(" Exiting Contact Book.Goodbye!")
            break
        else:
            print("Invalid choice. please try again")


if __name__ == "__main__":
    main()




                   