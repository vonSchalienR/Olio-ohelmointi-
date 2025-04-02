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
        self._persons = {}
    
    def add_number(self, name, number):
        if name not in self._persons:
            self._persons[name] = Person(name)
        self._persons[name].add_number(number)
    
    def add_address(self, name, address):
        if name not in self._persons:
            self._persons[name] = Person(name)
        self._persons[name].add_address(address)
    
    def get_entry(self, name):
        return self._persons.get(name, None)
    
    def list_people(self):
        return list(self._persons.keys())

# Example usage
phonebook = PhoneBook()
phonebook.add_number("Eric", "02-123456")
print(phonebook.get_entry("Eric"))
print(phonebook.get_entry("Emily"))
