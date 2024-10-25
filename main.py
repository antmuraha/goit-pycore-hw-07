from assistant_bot.entities.address_book import AddressBook
from assistant_bot.entities.record import Record


book = AddressBook()

print("BOOK_1", book)

# empty = Record("") # FieldNameValueError

# Create a record for "John"
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

print("john_record", john_record)

# Add a record "John" to address book
book.add_record(john_record)

# Create and add new record for "Jane"
jane_record = Record("Jane")
jane_record.add_phone("9876543210")

# Testing adding and removing a phone "1111111111"
jane_record.add_phone("1111111111")
# jane_record.add_phone("1111111111") # RecordPhoneAlreadyExistError
print(jane_record)
jane_record.remove_phone("1111111111")
print(jane_record)

book.add_record(jane_record)

print("BOOK_2", book)

# Display all entries in the book
for name, record in book.data.items():
    print("RECORD", record)

# Find and edit the phone for "John"
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Display: Contact name: John, phones: 1112223333; 5555555555

# Search for a specific phone in a "John" record
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Display: 5555555555

# Remove a record "Jane"
book.delete("Jane")

print("BOOK_3", book)
