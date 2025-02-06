class Pet:
    def __init__(self, name, species, year_of_birth):
        self.name = name
        self.species = species
        self.year_of_birth = year_of_birth

    def __str__(self):
        return f"Pet: {self.name}, Species: {self.species}, Year of Birth: {self.year_of_birth}"


def new_pet(name: str, species: str, year_of_birth: int) -> Pet:
    return Pet(name, species, year_of_birth)


# Example usage:
my_pet = new_pet("Buddy", "Dog", 2018)
print(my_pet)
