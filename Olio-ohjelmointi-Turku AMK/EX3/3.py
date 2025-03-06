
class Grid:
    """
    Edustaa ruudukkopohjaista maailmaa, jossa pelaajat ja esineet voivat olla.
    """
    def __init__(self, width: int, height: int):
        """
        Alustaa ruudukon annetuilla mitoilla.
        :param width: Ruudukon leveys.
        :param height: Ruudukon korkeus.
        """
        assert width > 0 and height > 0, "Ruudukon mittojen on oltava positiivisia."
        self.width = width
        self.height = height
        self.cells = [[[] for _ in range(width)] for _ in range(height)]

    def add_entity(self, x: int, y: int, entity):
        """
        Lisää entiteetin (pelaaja tai esine) ruudukkoon annetuilla koordinaateilla.
        :param x: X-koordinaatti.
        :param y: Y-koordinaatti.
        :param entity: Lisättävä entiteetti (Pelaaja tai Esine).
        """
        assert 0 <= x < self.width and 0 <= y < self.height, "Koordinaatit ovat rajojen ulkopuolella."
        self.cells[y][x].append(entity)
        entity.position = (x, y)

    def move_entity(self, entity, new_x: int, new_y: int):
        """
        Siirtää entiteetin uuteen sijaintiin, jos se on sallituissa rajoissa.
        :param entity: Siirrettävä entiteetti.
        :param new_x: Uusi X-koordinaatti.
        :param new_y: Uusi Y-koordinaatti.
        """
        assert 0 <= new_x < self.width and 0 <= new_y < self.height, "Uusi sijainti on rajojen ulkopuolella."
        x, y = entity.position
        self.cells[y][x].remove(entity)
        self.cells[new_y][new_x].append(entity)
        entity.position = (new_x, new_y)

class Item:
    """
    Edustaa esinettä StoneAge-maailmassa.
    """
    def __init__(self, name: str):
        """
        Alustaa esineen nimellä.
        :param name: Esineen nimi.
        """
        self.name = name
        self.position = None

class Player:
    """
    Edustaa pelaajaa StoneAge-maailmassa.
    """
    def __init__(self, name: str, grid: Grid):
        """
        Alustaa pelaajan nimellä ja tyhjällä varastolla.
        :param name: Pelaajan nimi.
        :param grid: Peliruudukko, jossa pelaaja on.
        """
        self.name = name
        self.grid = grid
        self.position = None
        self.inventory = []

    def move(self, dx: int, dy: int):
        """
        Siirtää pelaajaa annetuilla delta-arvoilla.
        :param dx: Muutos x-suunnassa.
        :param dy: Muutos y-suunnassa.
        """
        x, y = self.position
        new_x, new_y = x + dx, y + dy
        self.grid.move_entity(self, new_x, new_y)

    def pick_up_item(self):
        """
        Poimii esineen nykyiseltä ruudulta.
        """
        x, y = self.position
        cell = self.grid.cells[y][x]
        items = [e for e in cell if isinstance(e, Item)]
        if items:
            item = items[0]
            cell.remove(item)
            self.inventory.append(item)
            print(f"{self.name} poimi esineen: {item.name}!")
        else:
            print("Ei poimittavia esineitä.")

# Esimerkkikäyttö
grid = Grid(5, 5)
player1 = Player("Luolamies", grid)
item1 = Item("Kivi")

grid.add_entity(2, 2, player1)
grid.add_entity(2, 2, item1)

player1.pick_up_item()
player1.move(1, 0)
