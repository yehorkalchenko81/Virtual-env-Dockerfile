from collections import UserDict
from datetime import datetime
from upcoming_birthdays import get_upcoming_birthdays


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, name):
        if not name:
            raise ValueError
        Field.__init__(self, name)


class Phone(Field):
    def __init__(self, number):
        if len(number) != 10 or not number.isdigit():
            raise ValueError
        Field.__init__(self, number)


class Birthday(Field):
    def __init__(self, value):
        Field.__init__(self, datetime.strptime(value, "%d.%m.%Y").date())


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def find_phone(self, phone):
        return self.__find_phone(phone)

    def edit_phone(self, old_phone, new_phone):
        self.phones[self.phones.index(self.__find_phone(old_phone))] = Phone(new_phone)

    def remove_phone(self, phone):
        self.phones.remove(self.__find_phone(phone))

    def __find_phone(self, phone):
        for number in self.phones:
            if number.value == phone:
                return number
        raise ValueError

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record):
        if type(record) != Record:
            raise ValueError
        self.data[record.name.value] = record

    def find(self, name):
        return self.__find(name)

    def delete(self, name):
        if self.__find(name):
            del self.data[name]

    def __find(self, name):
        result = self.data.get(name, None)
        if result is None:
            raise ValueError
        return result

    def get_upcoming_birthdays(self):
        print(*get_upcoming_birthdays([{key: value.birthday} for key, value in self.data.items()]))
