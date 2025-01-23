class Kirja:
    def __init__(self, nimi, tekija, laji, julkaisuvuosi):
        self.nimi = nimi
        self.tekija = tekija
        self.laji = laji
        self.julkaisuvuosi = julkaisuvuosi

def vanhempi_kirja(kirja1: Kirja, kirja2: Kirja):
    if kirja1.julkaisuvuosi < kirja2.julkaisuvuosi:
        return f"{kirja1.nimi} on vanhempi, se kirjoitettiin {kirja1.julkaisuvuosi}"
    elif kirja1.julkaisuvuosi > kirja2.julkaisuvuosi:
        return f"{kirja2.nimi} on vanhempi, se kirjoitettiin {kirja2.julkaisuvuosi}"
    else:
        return f"{kirja1.nimi} ja {kirja2.nimi} kirjoitettiin {kirja1.julkaisuvuosi}"

# Esimerkit
python = Kirja("Fluent Python", "Luciano Ramalho", "ohjelmointi", 2015)
everest = Kirja("Huipulta huipulle", "Carina Räihä", "elämänkerta", 2010)
norma = Kirja("Norma", "Sofi Oksanen", "rikos", 2015)

# Funktiokutsut
print(vanhempi_kirja(python, everest))  # Tulostaa: Huipulta huipulle on vanhempi, se kirjoitettiin 2010
print(vanhempi_kirja(python, norma))  # Tulostaa: Fluent Python ja Norma kirjoitettiin 2015
