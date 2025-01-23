class Lemmikki:
    def __init__(self, nimi: str, laji: str, syntymavuosi: int):
        self.nimi = nimi
        self.laji = laji
        self.syntymavuosi = syntymavuosi

def uusi_lemmikki(nimi: str, laji: str, syntymavuosi: int):
    return Lemmikki(nimi, laji, syntymavuosi)

# Esimerkki
def main():
    musti = uusi_lemmikki("Musti", "koira", 2017)
    print(musti.nimi)  # Tulostaa "Musti"
    print(musti.laji)  # Tulostaa "koira"
    print(musti.syntymavuosi)  # Tulostaa 2017

if __name__ == "__main__":
    main()
