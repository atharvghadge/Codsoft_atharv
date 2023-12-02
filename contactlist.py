class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"Name: {self.name}\nPhone: {self.phone}\nEmail: {self.email}\nAddress: {self.address}\n"


class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print(f"Contact '{contact.name}' added successfully!")

    def view_contacts(self):
        if self.contacts:
            for contact in self.contacts:
                print(contact)
        else:
            print("No contacts in the book.")

    def search_contact(self, search_term):
        found_contacts = [contact for contact in self.contacts if search_term.lower() in contact.name.lower() or search_term in contact.phone]
        if found_contacts:
            for contact in found_contacts:
                print(contact)
        else:
            print("Contact not found.")

    def update_contact(self, search_term):
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone:
                print("Current contact information:")
                print(contact)
                contact.name = input("Enter updated name: ")
                contact.phone = input("Enter updated phone: ")
                contact.email = input("Enter updated email: ")
                contact.address = input("Enter updated address: ")
                print("Contact updated successfully!")
                break
        else:
            print("Contact not found.")

    def delete_contact(self, search_term):
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone:
                self.contacts.remove(contact)
                print("Contact deleted successfully!")
                break
        else:
            print("Contact not found.")


def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact = Contact(name, phone, email, address)
            contact_book.add_contact(contact)
        elif choice == '2':
            contact_book.view_contacts()
        elif choice == '3':
            search_term = input("Enter a name or phone number to search: ")
            contact_book.search_contact(search_term)
        elif choice == '4':
            search_term = input("Enter a name or phone number to update: ")
            contact_book.update_contact(search_term)
        elif choice == '5':
            search_term = input("Enter a name or phone number to delete: ")
            contact_book.delete_contact(search_term)
        elif choice == '6':
            print("Exiting the Contact Book application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
