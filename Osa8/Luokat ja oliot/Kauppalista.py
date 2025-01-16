class Kauppalista:
    def __init__(self):
        self.tuotteet_lista = []

    def lisaa(self, tuote, maara):
        self.tuotteet_lista.append((tuote, maara))

    def tuotteita(self):
        return len(self.tuotteet_lista)

    def tuote(self, indeksi):
        return self.tuotteet_lista[indeksi - 1][0]

    def maara(self, indeksi):
        return self.tuotteet_lista[indeksi - 1][1]

def tuotteita_yhteensa(lista: Kauppalista):
    yhteensa = 0
    for i in range(1, lista.tuotteita() + 1):
        yhteensa += lista.maara(i)
    return yhteensa

# Testataan ohjelma
if __name__ == "__main__":
    lista = Kauppalista()
    lista.lisaa("banaanit", 10)
    lista.lisaa("omenat", 5)
    lista.lisaa("ananas", 1)

    print(tuotteita_yhteensa(lista))
