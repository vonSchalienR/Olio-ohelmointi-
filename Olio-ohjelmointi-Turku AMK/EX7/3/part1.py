class Person:
    def __init__(self, name):
        self._name = name
        self._numbers = []
        self._address = None

    def name(self):
        return self._name
    
    def numbers(self):
        return self._numbers
    
    def address(self):
        return self._address
    
    def add_number(self, number):
        self._numbers.append(number)
    
    def add_address(self, address):
        self._address = address

class PhoneBook:
    def __init__(self):
        self._entries = {}
    
    def add_person(self, name):
        if name not in self._entries:
            self._entries[name] = Person(name)
    
    def add_number(self, name, number):
        if name in self._entries:
            self._entries[name].add_number(number)
    
    def add_address(self, name, address):
        if name in self._entries:
            self._entries[name].add_address(address)
    
    def get_person(self, name):
        return self._entries.get(name, None)
    
    def list_people(self):
        return list(self._entries.keys())

# Example usage
phonebook = PhoneBook()
phonebook.add_person("Eric")

person = phonebook.get_person("Eric")
print(person.name())
print(person.numbers())
print(person.address())

phonebook.add_number("Eric", "040-123456")
phonebook.add_address("Eric", "Mannerheimintie 10 Helsinki")

print(person.numbers())
print(person.address())
