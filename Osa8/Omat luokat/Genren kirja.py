class Kirja:
    def __init__(self, nimi, tekija, laji, julkaisuvuosi):
        self.nimi = nimi
        self.tekija = tekija
        self.laji = laji
        self.julkaisuvuosi = julkaisuvuosi

def genren_kirjat(kirjat: list, genre: str):
    # Suodatetaan listasta ne kirjat, joiden genre vastaa annettua genreä
    return [kirja for kirja in kirjat if kirja.laji == genre]

# Esimerkit
python = Kirja("Fluent Python", "Luciano Ramalho", "ohjelmointi", 2015)
everest = Kirja("Huipulta huipulle", "Carina Räihä", "elämänkerta", 2010)
norma = Kirja("Norma", "Sofi Oksanen", "rikos", 2015)
lumiukko = Kirja("Lumiukko", "Jo Nesbø", "rikos", 2007)

kirjat = [python, everest, norma, lumiukko]

# Funktiokutsut
print("rikoskirjoja ovat")
for kirja in genren_kirjat(kirjat, "rikos"):
    print(f"{kirja.tekija}: {kirja.nimi}")
