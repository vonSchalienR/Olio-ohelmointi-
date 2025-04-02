class MagicPotion:
    def __init__(self, name: str):
        self.name = name
        self.ingredients = {}
    
    def add_ingredient(self, ingredient: str, amount: float):
        self.ingredients[ingredient] = self.ingredients.get(ingredient, 0) + amount
    
    def print_recipe(self):
        print(f"{self.name}:")
        for ingredient, amount in self.ingredients.items():
            print(f"{ingredient} {amount} grams")

class SecretMagicPotion(MagicPotion):
    def __init__(self, name: str, password: str):
        super().__init__(name)
        self.__password = password
    
    def add_ingredient(self, ingredient: str, amount: float, password: str):
        if password != self.__password:
            raise ValueError("Wrong password!")
        super().add_ingredient(ingredient, amount)
    
    def print_recipe(self, password: str):
        if password != self.__password:
            raise ValueError("Wrong password!")
        super().print_recipe()


diminuendo = SecretMagicPotion("Diminuendo maximus", "hocuspocus")
diminuendo.add_ingredient("Toadstool", 1.5, "hocuspocus")
diminuendo.add_ingredient("Magic sand", 3.0, "hocuspocus")
diminuendo.add_ingredient("Frogspawn", 4.0, "hocuspocus")
diminuendo.print_recipe("hocuspocus")


diminuendo.print_recipe("pocushocus")
