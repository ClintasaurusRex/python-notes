print("--------------------------Contact Book App-------------------------")
contact_book = {}
print("Contact Book Menu:")
def display_menu():
   menu_lst = ["Add Contact", "View Contact", "Edit Contact", "Delete Contact", "List All Contacts", "Exit"]
   for index, item in enumerate(menu_lst):
    print(f"{index + 1}. {item}")

def add_contact(contact_book):
  name = input("Enter contact name: ")
  phone = input("Enter phone number: ")
  email = input("Enter email address: ")
  address = input("Enter address: ")

  if name in contact_book:
    print("Contact already exists!")
  else: 
    contact_book[name] = {
      "phone": phone,
      "email": email,
      "address": address
    }
    print("Contact added successfully")
display_menu()
add_contact(contact_book)
print(contact_book)