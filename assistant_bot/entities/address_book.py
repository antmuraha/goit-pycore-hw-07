from collections import UserDict
from assistant_bot.entities.record import Record


class AddressBook(UserDict):
    '''
    A class for storing and managing records.
    '''

    def __init__(self):
        self.data = {"records": []}

    def __str__(self):
        count = len(self.data["records"])
        return f"Address Book with {count} records"

    def add_record(self, record: Record):
        self.data["records"].append(record)

    def find(self, name: str) -> Record | None:
        record = next(
            (x for x in self.data["records"] if x.name.value == name), None)
        return record

    def delete(self, name: str) -> Record | None:
        self.data["records"] = list(
            filter(lambda item: item.name.value != name, self.data["records"]))
