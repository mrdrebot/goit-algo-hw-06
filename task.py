from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, name):
        if name:
            super().__init__(name)
        else:
            raise ValueError("You have not enterd name!")

class Phone(Field):
    def __init__(self, phone):
        if len(phone) >= 10 and phone.isdigit():
            super().__init__(phone)
        else:
            raise ValueError("You have enterd less than 10 digitals!")

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone_number):
        new_phone = Phone(phone_number)
        self.phones.append(new_phone)

    def remove_phone(self, remove_phone):
        for phone in self.phones:
            if phone.value == remove_phone:
                self.phones.remove(phone)

    def edit_phone(self, old_phone, new_phone):
        old_p = Phone(old_phone)
        new_p = Phone(new_phone)

        for phone in self.phones:
            if phone.value == old_p.value:
                phone.value = new_p.value

    def search_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                return phone
            
        return None


    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    # реалізація класу
    # def __init__(self, user_record):
    #     print(user_record)
    #     self.user_record = user_record

    def add_record(self, user_record):
        #   print(user_record)
        #   print(user_record.name)
        #   print(user_record.phones)

          self.data[user_record.name.value] = user_record

    def search_contact(self, contact_name):
        return self.data.get(contact_name)

    def __str__(self):
        # return str(self.data)
        return f"Contacts:\n{'\n'.join(self.data.keys())}"

book = AddressBook()
# print(book)
maks_record = Record("Maks")
miha_record = Record("Miha")
alex_record = Record("Alex")
# maks_record = Record("")
# print(maks_record)
maks_record.add_phone("1234567890")
maks_record.add_phone("5555555555")
maks_record.add_phone("5555555556")
miha_record.add_phone("5555555556")
alex_record.add_phone("5555555556")
# print(maks_record)
maks_record.remove_phone("5555555556")
# print(maks_record)
maks_record.edit_phone("5555555555", "7777777777")
# print(maks_record)
# print(maks_record.search_phone("7777777777"))
print(maks_record.search_phone("7777777779"))

book.add_record(maks_record)
book.add_record(miha_record)
book.add_record(alex_record)
print(book)

print(book.search_contact("Maks"))
print(book.search_contact("Maks1"))