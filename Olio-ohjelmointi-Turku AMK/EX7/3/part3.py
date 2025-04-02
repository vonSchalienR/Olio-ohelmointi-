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
        return self._address if self._address else "address unknown"
    
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
    
    def search(self, name):
        person = self.get_entry(name)
        if person:
            numbers = person.numbers() if person.numbers() else ["number unknown"]
            return f"{name}\n" + "\n".join(numbers) + f"\n{person.address()}"
        return "address unknown\nnumber unknown"
    
    def list_people(self):
        return list(self._persons.keys())

# Example usage
phonebook = PhoneBook()
phonebook.add_number("Eric", "02-123456")
phonebook.add_address("Emily", "Viherlaaksontie 7, Espoo")
print(phonebook.search("Eric"))
print(phonebook.search("Emily"))
print(phonebook.search("Wilhelm"))
phonebook.add_address("Eric", "Linnankatu 75, Turku")
print(phonebook.search("Eric"))
