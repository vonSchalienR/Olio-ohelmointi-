
import random

class Item:
    """Edustaa esinettä, jonka voi ostaa, myydä tai vaihtaa uhkapelissä."""
    def __init__(self, name: str, value: int):
        self.name = name
        self.value = value
    
    def __str__(self):
        return f"{self.name} (Arvo: {self.value})"

class Player:
    """Edustaa pelaajahahmoa, jolla on reppu ja kultaa."""
    def __init__(self, name: str, gold: int):
        self.name = name
        self.gold = gold
        self.backpack = []
    
    def add_item(self, item: Item):
        """Lisää esineen pelaajan reppuun."""
        self.backpack.append(item)
    
    def remove_item(self, item: Item):
        """Poistaa esineen pelaajan repusta."""
        if item in self.backpack:
            self.backpack.remove(item)
            return True
        return False
    
    def __str__(self):
        backpack_contents = ', '.join(str(item) for item in self.backpack) if self.backpack else "Tyhjä"
        return f"Pelaaja: {self.name}, Kulta: {self.gold}, Reppu: [{backpack_contents}]"

class Shopkeeper(Player):
    """Edustaa NPC-kauppiasta, joka hoitaa kaupankäynnin."""
    def __init__(self, name: str, gold: int, shop):
        super().__init__(name, gold)
        self.shop = shop
    
    def interact(self, player: Player):
        """Mahdollistaa pelaajan vuorovaikutuksen kauppiaan kanssa."""
        print(f"Hei, {player.name}! Tervetuloa kauppaan {self.shop.name}.")
        self.shop.display_items()

class Shop:
    """Edustaa kauppaa, jossa voi ostaa, myydä ja uhkapelata esineitä."""
    def __init__(self, name: str):
        self.name = name
        self.items_for_sale = []
    
    def add_item(self, item: Item):
        """Lisää esineen kaupan valikoimaan."""
        self.items_for_sale.append(item)
    
    def display_items(self):
        """Näyttää kaupassa myynnissä olevat esineet."""
        print(f"Tervetuloa kauppaan {self.name}! Myynnissä olevat esineet:")
        if not self.items_for_sale:
            print("Ei saatavilla olevia esineitä.")
        for item in self.items_for_sale:
            print(item)
    
    def buy_item(self, player: Player, item_name: str):
        """Mahdollistaa esineen ostamisen, jos pelaajalla on tarpeeksi kultaa."""
        for item in self.items_for_sale:
            if item.name == item_name and player.gold >= item.value:
                player.gold -= item.value
                player.add_item(item)
                self.items_for_sale.remove(item)
                print(f"{player.name} osti {item_name} {item.value} kullan hinnalla.")
                return
        print("Osto epäonnistui: Ei tarpeeksi kultaa tai esinettä ei ole saatavilla.")
    
    def sell_item(self, player: Player, item_name: str):
        """Mahdollistaa esineen myymisen pelaajan repusta."""
        for item in player.backpack:
            if item.name == item_name:
                player.gold += item.value // 2  # Kauppa ostaa esineet puolella hinnalla
                player.remove_item(item)
                self.items_for_sale.append(item)
                print(f"{player.name} myi {item_name} {item.value // 2} kullalla.")
                return
        print("Myynti epäonnistui: Esinettä ei ole repussa.")
    
    def gamble(self, player: Player, desired_item_name: str):
        """Mahdollistaa esineen vaihtamisen satunnaisesti uhkapelissä."""
        if not player.backpack or not self.items_for_sale:
            print("Uhkapeli epäonnistui: Ei esineitä vaihdettavaksi.")
            return
        
        desired_item = next((item for item in self.items_for_sale if item.name == desired_item_name), None)
        if desired_item is None:
            print("Uhkapeli epäonnistui: Haluttua esinettä ei ole kaupassa.")
            return
        
        if random.random() > 0.5:
            lost_item = random.choice(player.backpack)
            player.remove_item(lost_item)
            player.add_item(desired_item)
            self.items_for_sale.remove(desired_item)
            self.items_for_sale.append(lost_item)
            print(f"Uhkapeli onnistui! {player.name} voitti {desired_item_name}, mutta menetti {lost_item.name}.")
        else:
            print("Uhkapeli epäonnistui: Parempi onni ensi kerralla!")
