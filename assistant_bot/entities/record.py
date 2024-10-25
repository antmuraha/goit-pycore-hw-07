from assistant_bot.entities.field_name import FieldName
from assistant_bot.entities.field_phone import FieldPhone


class Record:
    '''
    A class to store information about a contact, including name and phone list.
    '''

    def __init__(self, name):
        self.name = FieldName(name)
        self.phones: list[FieldPhone] = []

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

    def __repr__(self):
        return f"Record: \"{self}\""

    def add_phone(self, phone: str):
        if not self.find_phone(phone):
            self.phones.append(FieldPhone(phone))
        else:
            raise RecordPhoneAlreadyExistError

    def remove_phone(self, phone: str):
        self.phones = list(filter(lambda p: p.value != phone, self.phones))

    def edit_phone(self, phone: str, new_phone: str):
        record = next(
            (x for x in self.phones if x.value == phone), None)

        if record:
            record.value = new_phone

    def find_phone(self, phone: str) -> FieldPhone | None:
        record = next(
            (x for x in self.phones if x.value == phone), None)

        return record


class RecordPhoneAlreadyExistError(Exception):
    def __init__(self, *args):
        super().__init__(*args)
