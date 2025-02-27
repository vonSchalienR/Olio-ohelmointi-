class Person:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def __str__(self):
        return f"{self.name} ({self.height} cm)"

class Room:
    def __init__(self):
        self.persons = []
    
    def add(self, person):
        self.persons.append(person)
    
    def is_empty(self):
        return len(self.persons) == 0
    
    def print_contents(self):
        if self.is_empty():
            print("The room is empty.")
        else:
            total_height = sum(person.height for person in self.persons)
            num_people = len(self.persons)
            print(f"There are {num_people} persons in the room, and their combined height is {total_height} cm.")
            for person in self.persons:
                print(person)
    
    def shortest(self):
        if self.is_empty():
            return None
        return min(self.persons, key=lambda person: person.height)
    
    def remove_shortest(self):
        if self.is_empty():
            return None
        shortest_person = self.shortest()
        self.persons.remove(shortest_person)  
        return shortest_person

room = Room()

room.add(Person("Lea", 183))
room.add(Person("Kenya", 172))
room.add(Person("Ally", 166))
room.add(Person("Nina", 162))
room.add(Person("Dorothy", 175))
print("Is the room empty?", room.is_empty())

removed = room.remove_shortest()
print(f"Removed from room: {removed.name}")
print()
room.print_contents()
